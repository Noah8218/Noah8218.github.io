#!/usr/bin/env python3
"""스크롤 끊김 원인 가르기(분석용 A/B): 기능을 하나씩 꺼서 전체 스크롤 프레임 시간을 비교한다.

목적: perf_site.py 로 스크롤 중 프레임이 튀는 것이 보일 때, 히어로 캔버스나 블러(backdrop-filter·filter) 같은 후보를 끄고 다시 재서
      그 후보가 원인인지 가른다. 해석과 이전 측정값은 docs/09-performance.md 에 있다.
사용: python tools/perf_ab.py [CPU배수] [--out 경로.json]
      CPU배수  CPU 스로틀 배수(기본 1). 예: python tools/perf_ab.py 4
      --out    JSON 저장 경로. 기본은 tools/out/ab_cpu<배수>.json (tools/out 은 .gitignore 대상, 없으면 만든다)
모드(모드마다 같은 조건으로 2회씩, 데스크톱 1440x900 케이스):
  base      아무것도 끄지 않음
  noblur    모든 요소의 backdrop-filter 와 .reveal 의 filter 를 !important 로 제거
  nocanvas  js/hero.js 요청을 막아 히어로 캔버스를 없앰
  none      noblur 와 nocanvas 를 함께 적용
  참고: 현재 사이트에는 등장 블러(.reveal 의 filter)가 없다(성능 작업에서 제거했다). 그래서 noblur 모드는 지금 코드에서는
        backdrop-filter 를 끄는 효과만 있어 의미가 약하다. 기능은 이전 측정과 같은 조건을 유지하려고 그대로 둔다.
출력: 모드·회차별로 평균 fps, p95, p99, 최대, 34·50ms 초과 프레임 수, 가장 나쁜 프레임 5개([프레임 ms, 스크롤 Y px]), 로드 중 긴 작업 수.
      가장 나쁜 프레임의 스크롤 Y 가 모드와 무관하게 같은 위치에서 반복되면, 꺼 본 기능이 아니라 그 위치의 다른 요소가 원인이라는 단서다.
한계: 헤드리스 Edge(Chromium), file:// 로 열어 네트워크 지연이 없고 실제 GPU 합성과 다르다. 모드당 2회뿐이라 통계적 결론이 아니라 단서다.
      측정 중 다른 작업이 겹치면 500~650ms 가 튄다(출력의 max 에 한 번만 큰 값이 나오면 잡음일 가능성이 크다). 브라우저를 8번 띄우므로 몇 분이 걸린다.
종료 코드: 0 끝남 / 2 브라우저를 못 찾음(lint_site.get_browser).
필요: Python 3.9+, Edge 또는 Chrome(환경 변수 BROWSER 로 지정 가능).
"""
import argparse
import json
import sys
import time
from pathlib import Path

T = Path(__file__).resolve().parent
sys.path.insert(0, str(T))
import perf_site as ps  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
NOBLUR = "(function(){var s=document.createElement('style');s.textContent='*{backdrop-filter:none!important;-webkit-backdrop-filter:none!important}.reveal,.reveal.in{filter:none!important}';document.addEventListener('DOMContentLoaded',function(){document.head.appendChild(s)});})();"


def run(mode, cpu, gpu=True, case="desktop"):
    with ps.session(case, gpu) as (cdp, c):
        for m in ("Page.enable", "Runtime.enable", "Performance.enable", "Network.enable"):
            cdp.call(m)
        cdp.call("Emulation.setDeviceMetricsOverride", width=c["w"], height=c["h"], deviceScaleFactor=1, mobile=c["mobile"])
        if cpu > 1:
            cdp.call("Emulation.setCPUThrottlingRate", rate=cpu)
        if mode in ("nocanvas", "none"):
            cdp.call("Network.setBlockedURLs", urls=["*hero.js"])
        cdp.call("Page.addScriptToEvaluateOnNewDocument", source=ps.INSTR)
        if mode in ("noblur", "none"):
            cdp.call("Page.addScriptToEvaluateOnNewDocument", source=NOBLUR)
        cdp.call("Page.navigate", url=(ps.P / "index.html").as_uri())
        for _ in range(100):
            if cdp.eval("document.readyState") == "complete":
                break
            time.sleep(0.2)
        time.sleep(3)
        lt_load = cdp.eval("__perf.longtasks.length")
        H = cdp.eval("document.documentElement.scrollHeight")
        cdp.eval("window.__start()")
        ps.wheel(cdp, H, 40, c["w"], c["h"])
        time.sleep(0.5)
        fr = cdp.eval("window.__stop()") or []
        st = ps.fstats(fr)
        big = sorted([f for f in fr if f[0] > 50], key=lambda f: -f[0])[:5]
        st["worst_5"] = [[round(d), y] for d, y in big]
        st["longtasks_load"] = lt_load
        return st


def main():
    ap = argparse.ArgumentParser(description="스크롤 끊김 원인 가르기 A/B(자세한 설명은 파일 맨 위 docstring)")
    ap.add_argument("cpu", type=int, nargs="?", default=1, help="CPU 스로틀 배수(기본 1)")
    ap.add_argument("--out", default="", help="JSON 저장 경로(기본 tools/out/ab_cpu<배수>.json)")
    a = ap.parse_args()
    cpu = a.cpu
    out = {}
    for mode in ("base", "noblur", "nocanvas", "none"):
        rs = [run(mode, cpu) for _ in range(2)]
        out[mode] = rs
        for i, r in enumerate(rs):
            print(f"[cpu x{cpu}] {mode:9} run{i+1}: fps={r['avg_fps']} p95={r['p95']} p99={r['p99']} max={r['max']} >34ms={r['over_34']} >50ms={r['over_50']} worst={r['worst_5']} loadLongTasks={r['longtasks_load']}")
    dest = Path(a.out).resolve() if a.out else ps.OUT / f"ab_cpu{cpu}.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("saved", dest)


if __name__ == "__main__":
    main()
