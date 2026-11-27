#!/usr/bin/env python3
"""공개 GitHub 저장소의 README 와 메타 정보를 다시 받아 docs/sources/ 를 갱신한다.

용도: docs/sources/ 는 사이트 문장의 근거가 되는 README 스냅샷이다. 원본 저장소가 바뀌었을 때 이 스크립트로 새로 받는다.
사용: python tools/fetch_sources.py [--dry-run]
- --dry-run: 받을 URL 과 저장할 파일 이름만 출력하고 네트워크 요청도 파일 쓰기도 하지 않는다.
- 대상(모두 Noah8218 소유 공개 저장소): OpenVisionLab, OpenVisionLab-Labeling-Studio, OpenVisionLab-3D-Studio,
  OpenVisionLab-Machine-Studio, OpenVisionLab-Vision-SDK, RawBufferVisualizer, Noah8218(프로필).
- 저장 이름: README_<저장소>.md(영어), README_ko_<저장소>.md(한국어, 없으면 건너뜀), meta_<저장소>.json.
  추가 한 건: README_ko_RawBufferVisualizer_overview.md (RawBufferVisualizer 의 한국어 소개 문서. 파일명에 버전이 들어 있어
  새 버전이 나오면 EXTRA 의 주소를 고쳐야 한다).
- stats.md 는 손으로 쓴 문서라 덮어쓰지 않는다(갱신 방법은 docs/sources/README.md).
- 토큰을 쓰지 않는 비인증 공개 API 를 쓴다. GitHub API 는 비인증 요청이 IP 당 시간당 60회로 제한된다.
  이 스크립트는 API 요청 14회(저장소 7개 x README, 메타)를 쓴다. 제한에 걸리면(403/429) 안내를 출력하고 끝낸다.
- 영어 README·메타를 못 받거나(404 포함), 선택 파일이 404 가 아닌 오류로 실패하면 기존 파일을 하나도 덮어쓰지 않는다(날짜가 섞인 스냅샷 방지).
- 저장 형식: BOM 없는 UTF-8, 줄 끝 LF(원본의 CRLF 는 LF 로 바꾼다).
종료 코드: 0 성공(또는 --dry-run) / 1 받지 못한 파일이 있음(아무것도 쓰지 않음).
필요: Python 3.9+ 표준 라이브러리만. 인터넷 연결.
"""
import argparse
import sys
import urllib.error
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT / "docs" / "sources"
OWNER = "Noah8218"
REPOS = ["OpenVisionLab", "OpenVisionLab-Labeling-Studio", "OpenVisionLab-3D-Studio", "OpenVisionLab-Machine-Studio",
         "OpenVisionLab-Vision-SDK", "RawBufferVisualizer", "Noah8218"]
EXTRA = [("README_ko_RawBufferVisualizer_overview.md",
          f"https://raw.githubusercontent.com/{OWNER}/RawBufferVisualizer/main/docs/marketplace-overview-2.2.5.ko.md")]
UA = "portfolio-site-fetch-sources/1.0"
TIMEOUT = 30


def plan():
    """(저장 파일명, URL, Accept 헤더, 필수 여부) 목록."""
    items = []
    for r in REPOS:
        items.append((f"README_{r}.md", f"https://api.github.com/repos/{OWNER}/{r}/readme", "application/vnd.github.raw", True))
        items.append((f"README_ko_{r}.md", f"https://raw.githubusercontent.com/{OWNER}/{r}/main/README.ko.md", "*/*", False))
        items.append((f"meta_{r}.json", f"https://api.github.com/repos/{OWNER}/{r}", "application/vnd.github+json", True))
    items += [(name, url, "*/*", False) for name, url in EXTRA]
    return items


def get(url, accept):
    """(본문 bytes, None) 또는 (None, 사유). 404 는 사유 '404' 로 구분한다."""
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            return r.read(), None
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None, "404"
        if e.code in (403, 429):
            left, reset = e.headers.get("X-RateLimit-Remaining"), e.headers.get("X-RateLimit-Reset")
            return None, (f"HTTP {e.code}: GitHub API 속도 제한(비인증은 시간당 60회)에 걸렸을 수 있다. "
                          f"남은 횟수 {left}, 초기화 시각(epoch 초) {reset}. 한 시간쯤 뒤에 다시 실행한다.")
        return None, f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001 - 네트워크 오류는 사유로만 보고한다
        return None, f"{type(e).__name__}: {e}"


def to_lf(data):
    """BOM 을 떼고 줄 끝을 LF 로 통일한다."""
    return data.decode("utf-8-sig").replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def main():
    ap = argparse.ArgumentParser(description="공개 README·메타를 받아 docs/sources/ 를 갱신한다.")
    ap.add_argument("--dry-run", action="store_true", help="받을 URL 목록만 출력한다(요청·쓰기 없음)")
    a = ap.parse_args()

    items = plan()
    if a.dry_run:
        for name, url, _, required in items:
            print(f"{'필수' if required else '선택'}  {url}  ->  docs/sources/{name}")
        print(f"\n{len(items)}건(--dry-run: 요청하지 않았고 파일도 쓰지 않았다). stats.md 는 받지 않는다.")
        return 0

    got, failed = {}, []
    for name, url, accept, required in items:
        body, why = get(url, accept)
        if body is None:
            if why == "404" and not required:
                print(f"건너뜀(404): {name}")
                continue
            failed.append((name, url, why))
            print(f"실패: {name} <- {url} ({why})", file=sys.stderr)
            continue
        if not body.strip():
            failed.append((name, url, "빈 응답"))
            print(f"실패: {name} <- {url} (빈 응답)", file=sys.stderr)
            continue
        got[name] = to_lf(body)
        print(f"받음: {name} ({len(body)} bytes)")
    if failed:
        print(f"\n{len(failed)}개를 받지 못해 아무것도 쓰지 않았다. 기존 docs/sources/ 는 그대로다.", file=sys.stderr)
        return 1
    DEST.mkdir(parents=True, exist_ok=True)
    for name, data in got.items():
        (DEST / name).write_bytes(data)
    print(f"\n{len(got)}개를 {DEST} 에 썼다.")
    print("다음 할 일: docs/sources/README.md 의 스냅샷 날짜와 stats.md(별 수·팔로워·라이선스)를 새 값으로 손으로 고친 뒤 "
          "python tools/check_site.py 로 사이트 문구가 여전히 근거를 갖는지 확인한다.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
