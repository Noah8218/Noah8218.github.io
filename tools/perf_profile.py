#!/usr/bin/env python3
"""성능 원인 추적(분석용): 로드·유휴 구간의 CPU 프로파일과, 로컬 http 서버에서 본 전송량.

목적: perf_site.py 가 "느리다"고 보이면, 시간이 어느 함수·파일에 쓰이는지와 어떤 파일이 얼마나 내려받아지는지를 본다.
      해석과 이전 측정값은 docs/09-performance.md 에 있다.
사용: python tools/perf_profile.py [--cpu 4] [--out 경로.txt]
      --cpu   CPU 스로틀 배수(기본 4). 1 이면 스로틀 없음
      --out   표준 출력과 같은 내용을 저장할 텍스트 경로. 기본은 tools/out/perf_profile_cpu<배수>.txt (tools/out 은 .gitignore 대상, 없으면 만든다)
출력:
  1) CPU 프로파일 [load]  페이지 로드(navigate부터 완료 2초 뒤까지) 표본. 파일·구분별 합계(ms)와 자기 시간(self time) 상위 함수
  2) CPU 프로파일 [idle]  로드 3.5초 뒤 맨 위에서 5초간 가만히 둔 표본(히어로 캔버스 등 유휴 비용). (idle) 은 쉰 시간이다
  3) 전송량 [at_load]·[after_scroll]  로컬 http 서버(표준 라이브러리, 압축·캐시 없음)로 열어 로드 직후와 끝까지 스크롤한 뒤의 요청 수·합계(KB)·확장자별(KB),
     로드 시점 요청 목록, 스크롤 중 추가로 요청된 큰 파일 20개
  프로파일 표본 간격은 250us 이고 (program) 은 브라우저 내부(레이아웃·페인트·합성 등) 시간이다.
한계:
  - 전송량의 스크롤은 120px 씩 약 30ms 간격으로 끝까지 빠르게 내리는 것이다. 행에 머무르며 보는 사용자와 다르다(머무르면 그 행의 GIF·영상을 추가로 받는다).
  - 로컬 서버라 네트워크 지연·압축·캐시가 없다. 실제 호스팅의 전송량과 다를 수 있다.
  - 헤드리스 Edge(Chromium) 한 번의 측정이다. 반복 변동이 있으니 비교는 같은 조건으로 두 번 이상 잰다.
  - 이 도구는 perf_site.py 와 같은 프로필 폴더를 쓴다. 동시에 두 개를 실행하지 않는다.
종료 코드: 0 끝남 / 2 브라우저를 못 찾음(lint_site.get_browser).
필요: Python 3.9+, Edge 또는 Chrome(환경 변수 BROWSER 로 지정 가능).
"""
import argparse
import collections
import http.server
import socketserver
import sys
import threading
import time
from pathlib import Path

T = Path(__file__).resolve().parent
sys.path.insert(0, str(T))
import perf_site as ps  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
SITE = ps.P
LINES = []


def emit(s=""):
    """표준 출력에 찍고 저장용 목록에도 모은다."""
    print(s)
    LINES.append(s)


def top_self(prof, n=14):
    nodes = {x["id"]: x for x in prof["nodes"]}
    acc = collections.defaultdict(float)
    byurl = collections.defaultdict(float)
    total = 0.0
    for s, d in zip(prof["samples"], prof["timeDeltas"]):
        cf = nodes[s]["callFrame"]
        k = f"{cf['functionName'] or '(anon)'} @ {cf['url'].split('/')[-1] or '-'}:{cf['lineNumber']}"
        acc[k] += d / 1000.0
        byurl[cf["url"].split("/")[-1] or cf["functionName"]] += d / 1000.0
        total += d / 1000.0
    return total, sorted(acc.items(), key=lambda x: -x[1])[:n], sorted(byurl.items(), key=lambda x: -x[1])[:8]


def profile_phase(case, gpu, cpu, phase):
    with ps.session(case, gpu) as (cdp, c):
        for m in ("Page.enable", "Runtime.enable", "Performance.enable", "Profiler.enable"):
            cdp.call(m)
        cdp.call("Emulation.setDeviceMetricsOverride", width=c["w"], height=c["h"], deviceScaleFactor=1, mobile=c["mobile"])
        cdp.call("Emulation.setCPUThrottlingRate", rate=cpu)
        cdp.call("Profiler.setSamplingInterval", interval=250)
        url = (SITE / "index.html").as_uri()
        if phase == "load":
            cdp.call("Profiler.start")
            cdp.call("Page.navigate", url=url)
            for _ in range(100):
                if cdp.eval("document.readyState") == "complete":
                    break
                time.sleep(0.2)
            time.sleep(2.0)
        else:
            cdp.call("Page.navigate", url=url)
            for _ in range(100):
                if cdp.eval("document.readyState") == "complete":
                    break
                time.sleep(0.2)
            time.sleep(3.5)
            cdp.eval("window.scrollTo(0,0)")
            cdp.call("Profiler.start")
            time.sleep(5)
        prof = cdp.call("Profiler.stop")["profile"]
        return top_self(prof)


def serve_weights():
    class Q(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *a, **k):
            super().__init__(*a, directory=str(SITE), **k)

        def log_message(self, *a):
            pass
    srv = socketserver.TCPServer(("127.0.0.1", 0), Q)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    out = {}
    with ps.session("desktop", True) as (cdp, c):
        for m in ("Page.enable", "Runtime.enable"):
            cdp.call(m)
        cdp.call("Emulation.setDeviceMetricsOverride", width=c["w"], height=c["h"], deviceScaleFactor=1, mobile=False)
        cdp.call("Page.navigate", url=f"http://127.0.0.1:{port}/index.html")
        for _ in range(100):
            if cdp.eval("document.readyState") == "complete":
                break
            time.sleep(0.2)
        time.sleep(2.5)
        get = "performance.getEntriesByType('resource').map(function(e){return [e.name.split('/').pop().split('?')[0], e.initiatorType, e.encodedBodySize||e.transferSize||0]})"
        r1 = cdp.eval(get) or []
        out["at_load"] = r1
        H = cdp.eval("document.documentElement.scrollHeight")
        y = 0
        while y < H:
            cdp.call("Input.dispatchMouseEvent", type="mouseWheel", x=720, y=450, deltaX=0, deltaY=120)
            time.sleep(0.03)
            y += 120
        time.sleep(3)
        out["after_scroll"] = cdp.eval(get) or []
    srv.shutdown()
    return out


def fmt(rows):
    tot = sum(r[2] for r in rows)
    kinds = collections.defaultdict(int)
    for n, t, s in rows:
        ext = n.rsplit(".", 1)[-1].lower() if "." in n else "?"
        kinds[ext] += s
    return tot, dict(sorted(kinds.items(), key=lambda x: -x[1]))


def main():
    ap = argparse.ArgumentParser(description="CPU 프로파일과 전송량(자세한 설명은 파일 맨 위 docstring)")
    ap.add_argument("--cpu", type=int, default=4, help="CPU 스로틀 배수(기본 4)")
    ap.add_argument("--out", default="", help="결과 텍스트 저장 경로(기본 tools/out/perf_profile_cpu<배수>.txt)")
    a = ap.parse_args()
    for phase in ("load", "idle"):
        total, top, byurl = profile_phase("desktop", True, a.cpu, phase)
        emit(f"\n===== CPU 프로파일 [{phase}] (CPU x{a.cpu} 스로틀) 표본 합 {total:.0f}ms")
        emit("파일/구분별: " + ", ".join(f"{k} {v:.0f}ms" for k, v in byurl))
        for k, v in top:
            emit(f"  {v:7.1f}ms  {k}")
    w = serve_weights()
    for k in ("at_load", "after_scroll"):
        tot, kinds = fmt(w[k])
        emit(f"\n===== 전송량 [{k}] 요청 {len(w[k])}개, 합계 {tot/1024:.0f} KB, 확장자별(KB): " + ", ".join(f"{e} {v/1024:.0f}" for e, v in kinds.items()))
    emit("\n로드 시점 요청 목록: " + ", ".join(f"{n}({s//1024}KB)" for n, t, s in w["at_load"]))
    late = [r for r in w["after_scroll"] if r[0] not in {x[0] for x in w["at_load"]}]
    emit("스크롤 중 추가 요청: " + ", ".join(f"{n}({s//1024}KB)" for n, t, s in sorted(late, key=lambda r: -r[2])[:20]))
    dest = Path(a.out).resolve() if a.out else ps.OUT / f"perf_profile_cpu{a.cpu}.txt"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(LINES) + "\n", encoding="utf-8")
    print("saved", dest)


if __name__ == "__main__":
    main()
