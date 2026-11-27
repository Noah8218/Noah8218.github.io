#!/usr/bin/env python3
"""헤드리스 Edge/Chrome 으로 사이트(index.html?shot=1)를 PNG 로 저장한다.

용도: 폭·높이·언어·테마·섹션을 지정해 화면을 찍어 눈으로 확인한다.
사용: python tools/shot_site.py [--w 1440] [--h 900] [--hash 섹션id] [--full] [--lang ko] [--theme light]
                                [--pp 0.5] [--profile 이름] [--out 경로]
- 기본 출력: tools/out/site-<폭>x<높이>-<해시|top>-<언어>-<테마>[-full][-pp값].png (tools/out 은 .gitignore 대상)
- --out: 저장 경로(상대 경로는 현재 폴더 기준). 폴더가 없으면 만든다.
- --full: ?lint=1 로 문서 높이를 읽어 창 높이를 그 값(최대 16000)으로 키워 한 장으로 찍는다. 이때 vh=H 를 사이트에 넘겨
  100vh 기반 높이(히어로·원칙 구간)가 문서 높이로 부풀지 않게 한다.
- --pp: 원칙 구간을 스크롤 진행도(0~1)로 고정해 sticky 상태를 확인한다.
- 폭 600 미만은 헤드리스 창이 492px 아래로 줄지 않고, --screenshot 은 스크롤된(해시 이동한) 페이지를 어긋나게 찍는다.
  그래서 이 두 경우는 lint_site.narrow_session(DevTools 에뮬레이션 + Page.captureScreenshot)으로 찍는다.
- 프로필 폴더는 tools/.browser-profile-<이름>/ 고정이며 지우지 않는다.
종료 코드: 0 저장 성공 / 1 스크린샷 파일이 만들어지지 않음 / 2 브라우저를 못 찾았거나 문서 높이를 읽지 못함.
필요: Python 3.9+, Edge 또는 Chrome(환경 변수 BROWSER 로 지정 가능). Pillow 는 선택(있으면 저장 후 이미지 크기를 출력한다).
"""
import argparse
import base64
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_site import NARROW, OUT, get_browser, narrow_session, profile_dir, run_lint, site_url, wait_for  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--w", type=int, default=1440)
    ap.add_argument("--h", type=int, default=900)
    ap.add_argument("--hash", default="")
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--theme", default="dark")
    ap.add_argument("--pp")
    ap.add_argument("--profile", default="site")
    ap.add_argument("--out")
    a = ap.parse_args()

    height = a.h
    if a.full:
        data = run_lint(a.w, a.h, a.lang, a.theme, a.profile)
        if data is None:
            print("문서 높이를 읽지 못했다", file=sys.stderr)
            return 2
        height = min(int(data["height"]), 16000)
    q = f"?shot=1&lang={a.lang}&theme={a.theme}&vh={a.h}" + (f"&pp={a.pp}" if a.pp else "")
    url = site_url(q, a.hash)
    OUT.mkdir(parents=True, exist_ok=True)
    tag = f"site-{a.w}x{a.h}-{a.hash or 'top'}-{a.lang}-{a.theme}" + ("-full" if a.full else "") + (f"-pp{a.pp}" if a.pp else "")
    out = Path(a.out).resolve() if a.out else OUT / f"{tag}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    before = out.stat().st_mtime if out.exists() else 0
    t0 = time.time()
    # --screenshot 플래그는 스크롤된 페이지(해시 이동)를 어긋나게 찍으므로, 해시 지정 시에는 DevTools 로 찍는다.
    if a.w < NARROW or (a.hash and not a.full):
        with narrow_session(a.w, a.h, a.profile) as cdp:
            cdp.call("Page.navigate", url=url)
            wait_for(cdp, "document.readyState === 'complete'")
            time.sleep(2.0)
            if a.full:
                cdp.call("Emulation.setDeviceMetricsOverride", width=a.w, height=height, deviceScaleFactor=1, mobile=a.w < 768)
                time.sleep(0.8)
            else:
                cdp.eval("(function(){var h=location.hash.slice(1),t=h&&document.getElementById(h);if(t)t.scrollIntoView()})()")
                time.sleep(0.5)
            png = cdp.call("Page.captureScreenshot", format="png")["data"]
        out.write_bytes(base64.b64decode(png))
    else:
        cmd = [
            get_browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={a.w},{height}",
            "--force-device-scale-factor=1", "--virtual-time-budget=4000", "--no-first-run",
            f"--user-data-dir={profile_dir(a.profile)}", f"--screenshot={out}", url,
        ]
        try:
            subprocess.run(cmd, capture_output=True, timeout=180)
        except subprocess.TimeoutExpired:
            print("브라우저 시간 초과", file=sys.stderr)
    if not out.exists() or out.stat().st_mtime <= before:
        print(f"스크린샷 실패: {out}", file=sys.stderr)
        return 1
    try:
        from PIL import Image
        w, h = Image.open(out).size
        print(f"{out} ({w}x{h}, {time.time() - t0:.1f}s)")
    except Exception:  # noqa: BLE001 - Pillow 가 없거나 읽지 못해도 저장은 끝났다
        print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
