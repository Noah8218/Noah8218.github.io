#!/usr/bin/env python3
"""사이트의 ?lint=1 레이아웃 검사 결과(JSON)를 헤드리스 브라우저로 읽어 출력한다.

용도: 저장소 루트의 index.html 을 헤드리스 Edge/Chrome 으로 열고, js/main.js 의 runLint 가 DOM 에 남긴
      검사 결과를 읽는다. 검사 항목: 가로 넘침, 뷰포트 오른쪽 밖 요소, 14px 미만 글자, alt 누락.
사용: python tools/lint_site.py [--w 1440|390] [--h 높이] [--lang ko] [--theme light] [--profile 이름] [--json]
      (저장소 루트에서 실행하는 것을 기준으로 하지만, 경로는 스크립트 위치로 계산하므로 어디서든 된다.)
종료 코드: 0 이슈 0건 / 1 이슈 있음 / 2 브라우저를 찾지 못했거나 결과를 읽지 못함.
필요: Python 3.9+, Edge 또는 Chrome(환경 변수 BROWSER 에 실행 파일 경로를 줄 수 있다). Pillow 는 필요 없다.

- 폭 600 이상: 브라우저 헤드리스 --dump-dom 으로 읽는다.
- 폭 600 미만: 헤드리스 창은 약 492px 아래로 줄어들지 않는다(실측: --window-size=390 이 뷰포트 492px 로 열림).
  그래서 이 경우에만 DevTools 프로토콜(표준 라이브러리 소켓)로 같은 브라우저를 띄워 뷰포트를 390x844 로 에뮬레이션한다.
  shot_site.py 도 이 모듈의 narrow_session 을 쓴다.
- 브라우저 프로필 폴더는 tools/.browser-profile-<--profile 이름>/ (DevTools 쪽은 뒤에 -cdp)이며 지우지 않는다.
"""
import argparse
import base64
import contextlib
import html
import json
import os
import re
import shutil
import socket
import struct
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

T = Path(__file__).resolve().parent   # tools/
ROOT = T.parent                       # 저장소 루트 = 사이트
OUT = T / "out"                       # 기본 출력 폴더(.gitignore 대상)
NARROW = 600


def _win_dir(var, default_name):
    """윈도 환경 변수가 없으면 시스템 드라이브 기준 기본 폴더로 대신한다."""
    return os.environ.get(var) or (os.environ.get("SystemDrive", "") + os.sep + default_name)


def find_browser():
    """BROWSER 환경 변수 -> Edge 2곳 -> Chrome -> macOS -> PATH(Linux 일반 이름) 순으로 실행 파일을 찾는다. 없으면 None."""
    env = os.environ.get("BROWSER")
    if env:
        return env if Path(env).is_file() else shutil.which(env)
    pf86 = _win_dir("ProgramFiles(x86)", "Program Files (x86)")
    pf = _win_dir("ProgramFiles", "Program Files")
    cands = [
        Path(pf86) / "Microsoft" / "Edge" / "Application" / "msedge.exe",
        Path(pf) / "Microsoft" / "Edge" / "Application" / "msedge.exe",
        Path(pf) / "Google" / "Chrome" / "Application" / "chrome.exe",
        Path(pf86) / "Google" / "Chrome" / "Application" / "chrome.exe",
    ]
    cands += [
        Path("/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge"),
        Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
    ]
    for c in cands:
        if c.is_file():
            return str(c)
    for name in ("microsoft-edge", "microsoft-edge-stable", "msedge", "google-chrome", "google-chrome-stable",
                 "chromium", "chromium-browser", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    return None


_BROWSER = None


def get_browser():
    """브라우저 경로를 돌려준다. 못 찾으면 한국어 안내를 출력하고 종료 코드 2 로 끝낸다."""
    global _BROWSER
    if _BROWSER is None:
        _BROWSER = find_browser()
    if not _BROWSER:
        env = os.environ.get("BROWSER")
        why = f"환경 변수 BROWSER 가 가리키는 실행 파일이 없다: {env}" if env else "Edge 또는 Chrome 실행 파일을 찾지 못했다."
        print(why + "\n"
              "설정 방법: 환경 변수 BROWSER 에 Edge 또는 Chrome 실행 파일의 전체 경로를 지정한 뒤 다시 실행한다.\n"
              "  PowerShell: $env:BROWSER = '<msedge.exe 또는 chrome.exe 의 전체 경로>'\n"
              "  bash/zsh  : export BROWSER='<실행 파일 경로>'\n"
              "탐색 순서: BROWSER -> Edge(Program Files (x86), Program Files) -> Chrome -> macOS 앱 -> PATH 의 chromium 계열.",
              file=sys.stderr)
        sys.exit(2)
    return _BROWSER


def profile_dir(profile, suffix=""):
    """프로필 폴더: tools/.browser-profile-<이름><suffix>. 이름의 경로 구분자 등은 _ 로 바꾼다."""
    return T / (".browser-profile-" + re.sub(r"[^\w.-]", "_", profile) + suffix)


def site_url(query, h=""):
    return (ROOT / "index.html").as_uri() + query + (f"#{h}" if h else "")


class WS:
    """클라이언트 쪽 최소 WebSocket (텍스트 프레임만)."""

    def __init__(self, url):
        m = re.match(r"ws://([^:/]+):(\d+)(/.*)", url)
        host, port, path = m.group(1), int(m.group(2)), m.group(3)
        self.s = socket.create_connection((host, port), timeout=30)
        key = base64.b64encode(os.urandom(16)).decode()
        self.s.sendall((f"GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\nUpgrade: websocket\r\nConnection: Upgrade\r\n"
                        f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.s.recv(4096)
        if b" 101 " not in buf.split(b"\r\n")[0]:
            raise RuntimeError("WebSocket 핸드셰이크 실패: " + buf[:200].decode(errors="replace"))
        self.rest = buf.split(b"\r\n\r\n", 1)[1]

    def _read(self, n):
        while len(self.rest) < n:
            chunk = self.s.recv(65536)
            if not chunk:
                raise ConnectionError("연결 종료")
            self.rest += chunk
        out, self.rest = self.rest[:n], self.rest[n:]
        return out

    def send(self, text):
        data = text.encode()
        n = len(data)
        head = b"\x81" + (bytes([0x80 | n]) if n < 126 else b"\xfe" + struct.pack(">H", n) if n < 65536 else b"\xff" + struct.pack(">Q", n))
        mask = os.urandom(4)
        self.s.sendall(head + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(data)))

    def recv(self):
        msg = b""
        while True:
            b0, b1 = self._read(2)
            n = b1 & 0x7F
            if n == 126:
                n = struct.unpack(">H", self._read(2))[0]
            elif n == 127:
                n = struct.unpack(">Q", self._read(8))[0]
            payload = self._read(n)
            op = b0 & 0x0F
            if op == 8:
                raise ConnectionError("서버가 연결을 닫음")
            if op in (1, 0, 2):
                msg += payload
                if b0 & 0x80:
                    return msg.decode("utf-8", errors="replace")


class CDP:
    def __init__(self, ws):
        self.ws, self.n = ws, 0

    def call(self, method, **params):
        self.n += 1
        self.ws.send(json.dumps({"id": self.n, "method": method, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.n:
                if "error" in msg:
                    raise RuntimeError(f"{method}: {msg['error']}")
                return msg.get("result", {})

    def eval(self, expr):
        r = self.call("Runtime.evaluate", expression=expr, returnByValue=True)
        return r.get("result", {}).get("value")


@contextlib.contextmanager
def narrow_session(w, h, profile="site"):
    """폭 w x 높이 h 로 에뮬레이션한 브라우저 페이지의 CDP 핸들을 돌려준다(768 미만이면 모바일 에뮬레이션)."""
    browser = get_browser()
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    cmd = [browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--remote-debugging-port={port}",
           "--remote-allow-origins=*", "--no-first-run", f"--user-data-dir={profile_dir(profile, '-cdp')}", "about:blank"]
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
        cdp.call("Page.enable")
        cdp.call("Emulation.setDeviceMetricsOverride", width=w, height=h, deviceScaleFactor=1, mobile=w < 768)
        yield cdp
        with contextlib.suppress(Exception):
            cdp.call("Browser.close")
    finally:
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.terminate()


def wait_for(cdp, expr, timeout=20):
    t0 = time.time()
    while time.time() - t0 < timeout:
        v = cdp.eval(expr)
        if v:
            return v
        time.sleep(0.3)
    return None


def run_lint(w, h, lang="en", theme="dark", profile="site"):
    """lint JSON(dict)을 돌려준다. 실패하면 None."""
    url = site_url(f"?lint=1&lang={lang}&theme={theme}&vh={h}")
    if w < NARROW:
        with narrow_session(w, h, profile) as cdp:
            cdp.call("Page.navigate", url=url)
            txt = wait_for(cdp, "document.getElementById('lintout') && document.getElementById('lintout').textContent")
        return json.loads(txt) if txt else None
    cmd = [
        get_browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}",
        "--force-device-scale-factor=1", "--virtual-time-budget=6000", "--no-first-run",
        f"--user-data-dir={profile_dir(profile)}", "--dump-dom", url,
    ]
    try:
        r = subprocess.run(cmd, capture_output=True, timeout=120)
    except subprocess.TimeoutExpired:
        print("브라우저 시간 초과", file=sys.stderr)
        return None
    dom = r.stdout.decode("utf-8", errors="replace")
    m = re.search(r'<pre id="lintout"[^>]*>(.*?)</pre>', dom, re.S)
    if not m:
        print("lintout 을 찾지 못했다(스크립트 오류 가능). stderr 앞부분:", file=sys.stderr)
        print(r.stderr.decode("utf-8", errors="replace")[:600], file=sys.stderr)
        return None
    return json.loads(html.unescape(m.group(1)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--w", type=int, default=1440)
    ap.add_argument("--h", type=int)
    ap.add_argument("--lang", default="en")
    ap.add_argument("--theme", default="dark")
    ap.add_argument("--profile", default="site")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    h = a.h or (844 if a.w <= 600 else 900)
    data = run_lint(a.w, h, a.lang, a.theme, a.profile)
    if data is None:
        return 2
    if a.json:
        print(json.dumps(data, ensure_ascii=False))
    issues = data["issues"]
    head = (f"폭 {data['w']} scrollWidth {data['scrollWidth']} clientWidth {data['clientWidth']} 문서 높이 {data['height']} "
            f"data-ko {data['dataKo']}개(번역 {data['dataKoTr']}개)")
    if not issues:
        print(f"OK  {head}  이슈 0건")
        return 0
    for it in issues:
        print(f"[{it['kind']}] {it['sel']} | {it['text']} | {it['detail']}")
    print(f"\n이슈 {len(issues)}건  {head}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
