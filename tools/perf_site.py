#!/usr/bin/env python3
"""사이트 성능 1회 측정(분석용): 헤드리스 Edge/Chrome + DevTools 프로토콜.

목적: 사이트가 느리거나 끊기는지 수치로 본다. 무거운 효과·미디어를 넣거나 구조를 크게 바꾼 뒤, 같은 조건으로 다시 재서 전후를 비교한다.
      측정 결과의 해석과 이전 측정값은 docs/09-performance.md 에 있다.
사용: python tools/perf_site.py --case desktop|desktop_slow|mobile_slow [--gpu on|off] [--out 경로.json]
      --case desktop       1440x900, CPU 스로틀 없음
      --case desktop_slow  1440x900, CPU 4배 스로틀(느린 노트북 가정)
      --case mobile_slow   390x844 모바일 에뮬레이션, CPU 4배 스로틀(느린 휴대폰 가정)
      --gpu on|off         off 면 --disable-gpu 로 띄운다(기본 on)
      --out                JSON 저장 경로. 기본은 tools/out/perf_<케이스>_<gpu>.json (tools/out 은 .gitignore 대상, 없으면 만든다)
      한 케이스에 약 1분이 걸린다. 브라우저 프로필 폴더는 tools/.browser-profile-perf-<케이스>[-gpu]-cdp/ 이고 지우지 않는다.
측정 항목(JSON 키):
  load                  DCL, load, FCP, LCP(와 LCP 요소), CLS, 로드 중 긴 작업(시작 ms, 길이 ms), 노드 수
  resources_at_load     로드 시점에 요청한 에셋 이름
  idle_top_5s           맨 위에 5초 머물 때 메인 스레드 점유율(%): 전체·스크립트·레이아웃·스타일 (히어로 캔버스 비용)
  scroll_all            맨 위에서 끝까지 휠 스크롤하는 동안 프레임 시간: 평균 fps, p50·p95·p99, 최대, 17·34·50ms 초과 프레임 수
  scroll_by_section     같은 값을 섹션별로
  after_scroll          힙(MB), 노드 수, CLS, 긴 작업 수·합계
  media_rows_5s         GIF·영상이 있는 프로젝트 행 4개(t-ovl t-lab t-3d t-rbv)를 가운데로 스크롤하고 5초간 점유율과 프레임 시간
  interaction           테마 전환·언어 전환·썸네일 클릭의 반응 시간(클릭부터 두 프레임 뒤까지, ms). 언어 전환의 첫 값이 첫 전환 비용이다
  motion_still          측정 시작 시점에 html.still(모션 정지)이 켜져 있었는지. true 면 히어로 캔버스·등장 전환·원칙 구간 고정이 꺼진
                        상태라 다른 측정과 비교할 수 없다(프로필 폴더가 실행 사이에 남으므로 저장된 설정이 이어질 수 있다)
  files                 index.html, css/style.css, js/main.js, js/hero.js 의 SHA-256 앞 12자리(어떤 코드를 쟀는지 구분용)
한계:
  - file:// 로 열어서 네트워크 지연·압축·캐시가 들어가지 않는다. 전송량은 perf_profile.py 가 로컬 http 서버로 따로 본다.
  - 헤드리스 브라우저라 실제 화면 합성(GPU)과 다르다. 이 PC 의 주사율(프레임 시간 p50 약 8.3ms = 약 120Hz)에 fps 절댓값이 묶인다.
  - Edge(Chromium)만 쟀다. Safari·Firefox·실제 터치 기기는 측정하지 않았다.
  - 측정 중에 다른 작업(브라우저 탭, 빌드, 영상 재생)이 겹치면 프레임이 500~650ms 튄다. 두 번 이상 재고, 원인 분리는 perf_ab.py 로 한다.
종료 코드: 0 저장됨 / 2 브라우저를 못 찾음(lint_site.get_browser) / 그 밖의 예외는 파이썬 오류로 종료.
필요: Python 3.9+, Edge 또는 Chrome(환경 변수 BROWSER 로 지정 가능, tools/lint_site.py 와 같은 탐색 규칙).
"""
import argparse
import contextlib
import hashlib
import json
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

T = Path(__file__).resolve().parent   # tools/
sys.path.insert(0, str(T))
from lint_site import CDP, OUT, WS, get_browser, profile_dir  # noqa: E402  (기존 최소 CDP 클라이언트·브라우저 탐색 재사용)

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
P = T.parent  # 사이트 루트(저장소 루트)

CASES = {
    "desktop": dict(w=1440, h=900, mobile=False, cpu=1),
    "desktop_slow": dict(w=1440, h=900, mobile=False, cpu=4),
    "mobile_slow": dict(w=390, h=844, mobile=True, cpu=4),
}

INSTR = r"""
(function(){
  var P = window.__perf = {frames:[], longtasks:[], cls:0, lcp:0, lcpEl:'', rec:false};
  try{ new PerformanceObserver(function(l){l.getEntries().forEach(function(e){P.longtasks.push([Math.round(e.startTime),Math.round(e.duration)])})}).observe({type:'longtask',buffered:true}); }catch(e){}
  try{ new PerformanceObserver(function(l){l.getEntries().forEach(function(e){if(!e.hadRecentInput)P.cls+=e.value})}).observe({type:'layout-shift',buffered:true}); }catch(e){}
  try{ new PerformanceObserver(function(l){l.getEntries().forEach(function(e){P.lcp=Math.round(e.startTime);P.lcpEl=(e.element&&(e.element.tagName+'.'+(e.element.className||'')))||''})}).observe({type:'largest-contentful-paint',buffered:true}); }catch(e){}
  window.__start = function(){ P.frames=[]; P.rec=true; var last=performance.now(); (function f(t){ if(!P.rec) return; P.frames.push([+(t-last).toFixed(1), Math.round(window.scrollY)]); last=t; requestAnimationFrame(f); })(last); };
  window.__stop = function(){ P.rec=false; return P.frames; };
})();
"""


def pct(a, p):
    if not a:
        return None
    a = sorted(a)
    return round(a[min(len(a) - 1, int(len(a) * p))], 1)


def fstats(frames):
    dts = [f[0] for f in frames if f[0] < 1000]  # 처음 프레임의 큰 값 제외
    if not dts:
        return {}
    return dict(frames=len(dts), p50=pct(dts, .5), p95=pct(dts, .95), p99=pct(dts, .99), max=round(max(dts), 1),
                over_17=sum(1 for d in dts if d > 17.5), over_34=sum(1 for d in dts if d > 34), over_50=sum(1 for d in dts if d > 50),
                avg_fps=round(1000 / (sum(dts) / len(dts)), 1))


@contextlib.contextmanager
def session(case, gpu):
    """케이스별 헤드리스 브라우저를 띄우고 (CDP 핸들, 케이스 설정)을 돌려준다. lint_site.narrow_session 과 같은 방식(프로필 규칙 포함)."""
    c = CASES[case]
    browser = get_browser()
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    cmd = [browser, "--headless=new"] + ([] if gpu else ["--disable-gpu"]) + ["--hide-scrollbars", f"--remote-debugging-port={port}",
           "--remote-allow-origins=*", "--no-first-run",
           f"--user-data-dir={profile_dir('perf-' + case + ('-gpu' if gpu else ''), '-cdp')}", "about:blank"]
    proc = subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        ws_url = None
        for _ in range(60):
            try:
                tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=2))
                pages = [t for t in tabs if t.get("type") == "page"]
                if pages:
                    ws_url = pages[0]["webSocketDebuggerUrl"]
                    break
            except Exception:  # noqa: BLE001
                time.sleep(0.5)
        if not ws_url:
            raise RuntimeError("브라우저 DevTools 에 연결하지 못했다")
        cdp = CDP(WS(ws_url))
        yield cdp, c
        with contextlib.suppress(Exception):
            cdp.call("Browser.close")
    finally:
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.terminate()


def metrics(cdp):
    return {m["name"]: m["value"] for m in cdp.call("Performance.getMetrics")["metrics"]}


def busy(m0, m1):
    wall = m1["Timestamp"] - m0["Timestamp"]
    d = lambda k: (m1.get(k, 0) - m0.get(k, 0))  # noqa: E731
    return dict(wall_s=round(wall, 2), main_thread_busy_pct=round(100 * d("TaskDuration") / wall, 1),
                script_pct=round(100 * d("ScriptDuration") / wall, 1), layout_pct=round(100 * d("LayoutDuration") / wall, 1),
                style_pct=round(100 * d("RecalcStyleDuration") / wall, 1))


def wheel(cdp, total, step, w, h, delay=0.016):
    y = 0
    while y < total:
        cdp.call("Input.dispatchMouseEvent", type="mouseWheel", x=w // 2, y=h // 2, deltaX=0, deltaY=step)
        time.sleep(delay)
        y += step


def main():
    ap = argparse.ArgumentParser(description="사이트 성능 1회 측정(자세한 설명은 파일 맨 위 docstring)")
    ap.add_argument("--case", default="desktop", choices=list(CASES))
    ap.add_argument("--gpu", default="on", choices=["on", "off"])
    ap.add_argument("--out", default="", help="JSON 저장 경로(기본 tools/out/perf_<케이스>_<gpu>.json)")
    a = ap.parse_args()
    out = {"case": a.case, "gpu": a.gpu, "when": time.strftime("%Y-%m-%d %H:%M:%S"), "files": {}}
    for f in ("index.html", "css/style.css", "js/main.js", "js/hero.js"):
        out["files"][f] = hashlib.sha256((P / f).read_bytes()).hexdigest()[:12]
    with session(a.case, a.gpu == "on") as (cdp, c):
        for m in ("Page.enable", "Runtime.enable", "Performance.enable"):
            cdp.call(m)
        cdp.call("Emulation.setDeviceMetricsOverride", width=c["w"], height=c["h"], deviceScaleFactor=1, mobile=c["mobile"])
        if c["cpu"] > 1:
            cdp.call("Emulation.setCPUThrottlingRate", rate=c["cpu"])
        cdp.call("Page.addScriptToEvaluateOnNewDocument", source=INSTR)
        url = (P / "index.html").as_uri()
        t0 = time.time()
        cdp.call("Page.navigate", url=url)
        for _ in range(100):
            if cdp.eval("document.readyState") == "complete":
                break
            time.sleep(0.2)
        out["load_wall_s"] = round(time.time() - t0, 2)
        time.sleep(2.5)  # 안정화
        out["motion_still"] = bool(cdp.eval("document.documentElement.classList.contains('still')"))
        if out["motion_still"]:
            print("경고: html.still(모션 정지)이 켜진 상태로 측정한다. 히어로 캔버스·등장 전환이 꺼져 있어 다른 측정과 비교할 수 없다.", file=sys.stderr)
        nav = cdp.eval("(function(){var n=performance.getEntriesByType('navigation')[0];var p=performance.getEntriesByType('paint');var o={};p.forEach(function(e){o[e.name]=Math.round(e.startTime)});return {dcl:Math.round(n.domContentLoadedEventEnd),load:Math.round(n.loadEventEnd),fcp:o['first-contentful-paint']||null,lcp:__perf.lcp,lcpEl:__perf.lcpEl,cls:+__perf.cls.toFixed(4),longtasks:__perf.longtasks,nodes:document.getElementsByTagName('*').length}})()")
        out["load"] = nav
        res = cdp.eval("performance.getEntriesByType('resource').map(function(e){return e.name})") or []
        out["resources_at_load"] = sorted({r.split("/")[-1].split("?")[0] for r in res})
        # 유휴 CPU (히어로 캔버스 등)
        cdp.eval("window.scrollTo(0,0)")
        m0 = metrics(cdp)
        time.sleep(5)
        m1 = metrics(cdp)
        out["idle_top_5s"] = busy(m0, m1)
        # 구간 오프셋
        secs = cdp.eval("['top','about','projects','ecosystem','skills','principles','releases','contact'].map(function(i){var e=document.getElementById(i);return [i, e?Math.round(e.getBoundingClientRect().top+scrollY):null]})")
        H = cdp.eval("document.documentElement.scrollHeight")
        out["doc_height"] = H
        # 전체 스크롤
        cdp.eval("window.__start()")
        step = 40 if not c["mobile"] else 30
        wheel(cdp, H, step, c["w"], c["h"])
        time.sleep(0.5)
        frames = cdp.eval("window.__stop()") or []
        out["scroll_all"] = fstats(frames)
        seg = {}
        offs = [s for s in secs if s[1] is not None] + [["end", H]]
        for i in range(len(offs) - 1):
            part = [f for f in frames if offs[i][1] <= f[1] < offs[i + 1][1]]
            seg[offs[i][0]] = fstats(part)
        out["scroll_by_section"] = seg
        m = cdp.eval("({heap_mb:+((performance.memory&&performance.memory.usedJSHeapSize||0)/1048576).toFixed(1),nodes:document.getElementsByTagName('*').length,cls:+__perf.cls.toFixed(4),longtasks:__perf.longtasks.length,longtask_ms:__perf.longtasks.reduce(function(s,x){return s+x[1]},0)})")
        out["after_scroll"] = m
        res2 = cdp.eval("performance.getEntriesByType('resource').map(function(e){return e.name})") or []
        out["resources_after_scroll"] = sorted({r.split("/")[-1].split("?")[0] for r in res2})
        # 미디어 행 재생 비용(5초씩)
        media = {}
        for rid in ("t-ovl", "t-lab", "t-3d", "t-rbv"):
            cdp.eval(f"document.getElementById('{rid}').scrollIntoView({{block:'center'}})")
            time.sleep(1.5)
            cdp.eval("window.__start()")
            m0 = metrics(cdp)
            time.sleep(5)
            m1 = metrics(cdp)
            fr = cdp.eval("window.__stop()") or []
            media[rid] = dict(busy(m0, m1), frames=fstats(fr))
        out["media_rows_5s"] = media
        # 상호작용 반응 시간: 클릭부터 두 프레임 뒤까지
        cdp.eval("window.scrollTo(0,0)")
        time.sleep(0.5)
        inter = {}
        inter["theme_toggle_ms"] = [cdp.call("Runtime.evaluate", expression="(function(){return new Promise(function(r){var t=performance.now();document.getElementById('theme').click();requestAnimationFrame(function(){requestAnimationFrame(function(){r(Math.round(performance.now()-t))})})})})()", awaitPromise=True, returnByValue=True)["result"]["value"] for _ in range(3)]
        inter["lang_toggle_ms"] = [cdp.call("Runtime.evaluate", expression="(function(){return new Promise(function(r){var b=[].slice.call(document.querySelectorAll('button')).filter(function(x){return /^(EN|KO)$/i.test(x.textContent.trim())});var t=performance.now();(b[(window.__i=(window.__i||0)^1)]||b[0]).click();requestAnimationFrame(function(){requestAnimationFrame(function(){r(Math.round(performance.now()-t))})})})})()", awaitPromise=True, returnByValue=True)["result"]["value"] for _ in range(4)]
        inter["thumb_click_ms"] = [cdp.call("Runtime.evaluate", expression="(function(){return new Promise(function(r){var th=document.querySelectorAll('#projects [role=tablist] button, #projects .thumbs button');if(!th.length){r(-1);return}var t=performance.now();th[(window.__j=((window.__j||0)+1)%th.length)].click();requestAnimationFrame(function(){requestAnimationFrame(function(){r(Math.round(performance.now()-t))})})})})()", awaitPromise=True, returnByValue=True)["result"]["value"] for _ in range(6)]
        out["interaction"] = inter
        mm = metrics(cdp)
        out["totals"] = {k: round(mm[k], 3) for k in ("TaskDuration", "ScriptDuration", "LayoutDuration", "RecalcStyleDuration", "LayoutCount", "RecalcStyleCount") if k in mm}
    dest = Path(a.out).resolve() if a.out else OUT / f"perf_{a.case}_{a.gpu}.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("saved", a.case, a.gpu, dest)


if __name__ == "__main__":
    main()
