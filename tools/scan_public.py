#!/usr/bin/env python3
"""공개(push) 전에 저장소 전체에서 회사 자료·개인정보·로컬 경로·비밀값 흔적을 찾는다.

용도: 이 저장소는 공개 GitHub Pages 용이다. 회사·고객사 이름, 전화번호, 내 PC 경로와 계정, 학교·팀원 정보,
      내부 작업 흔적, 허용 목록 밖의 이메일, 비밀값 흔적이 어디에도 없는지 push 전에 확인한다.
사용: python tools/scan_public.py [--report-only]
- 저장소 루트 아래 텍스트 파일 전부(.md .html .css .js .py .json .txt .svg .gitignore 등)를 줄 단위로 검사한다.
  제외: .git, tools/out, tools/.browser-profile-*, node_modules, __pycache__.
- 위반은 `파일:줄 | 매치 [분류]` 로 출력한다. 분류: 회사·고객사·전 직장 / 전화번호 / 로컬 경로·계정 / 개인·학교·팀원 /
  내부 작업 흔적 / 이메일 / 비밀값 흔적. 이메일은 공개 프로필에 이미 있는 주소 한 개를 index.html 과
  docs/sources/README_Noah8218.md 에서만 허용하고, noreply 주소와 git@github.com(SSH 주소 표기)은 어디서나 허용한다.
- docs/sources/ 의 사본(README_*.md, meta_*.json, stats.md)은 사용자의 공개 README 원문이라, 일반 단어 기반의 비밀값 검사
  (비밀값 흔적 분류의 두 번째 묶음)만 건너뛰고 나머지(회사·고객사 포함)는 똑같이 검사한다.
  사이트 자신의 문서에서 약칭 규칙(회사 정규식의 마지막 항목)에 걸리면 허용 목록에 넣지 말고 사람이 판단한다
  (--report-only 로 목록만 본다).
- 바이너리(이미지·영상 등)는 존재만 확인하고, 바이트에서 ASCII 5자 이상 문자열을 뽑아(strings 방식, Pillow 불사용) 위 패턴과
  Author/Artist/Copyright/GPS 가 있으면 "바이너리 경고"로 따로 목록만 출력한다(차단하지 않는다). 압축된 영상·이미지 데이터에서
  우연히 맞는 3글자 이하 일치(영문 약칭, 드라이브 문자)와 느슨한 이메일 모양은 잡음이라 버린다. 처음 보는 바이너리 형식도
  경고한다(회사 문서 형식이 섞여 들어오지 않았는지 보려는 용도).
- --report-only: 위반이 있어도 목록만 출력하고 종료 코드 0 으로 끝낸다.
종료 코드: 0 위반 없음(또는 --report-only) / 1 위반 있음. 바이너리 경고는 종료 코드에 영향을 주지 않는다.
필요: Python 3.9+ 표준 라이브러리만.

표기 주의: 아래 정규식에서 글자 하나를 [] 로 감싼 것(예: 삼[성])은 이 파일이 자기 자신의 검사에 걸리지 않게 하려는 것이며
정규식 뜻은 같다. 허용 이메일도 같은 이유로 조각을 이어 붙여 만든다.
"""
import argparse
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent

A = re.ASCII  # \b 를 ASCII 기준으로 써서 영문 약칭 바로 뒤에 한글이 붙은 표기도 잡는다
# (분류, [정규식], 플래그, docs/sources 사본에도 적용할지)
RULES = [
    ("회사·고객사·전 직장",
     [r"\bL[G]\b", r"삼[성]", r"S[D]I", r"하이[닉]스", r"크레[셈]", r"케이[템]", r"피닉[슨]", r"현[대]", r"\bS[K]\b"], A, True),
    ("전화번호", [r"0\d{1,2}-\d{3,4}-\d{4}"], A, True),
    ("로컬 경로·계정",
     [r"[A-Za-z]:\\", r"/[U]sers/", r"/[h]ome/", r"App[D]ata", r"scratch[p]ad", r"(?i:nach[o])", r"모[두]의 창업", r"포트폴리오_PP[T]",
      r"file:[/]//"], A, True),
    ("개인·학교·팀원", [r"인천[대]", r"정보기술대학[원]", r"석[사]", r"김일[웅]", r"정태[우]"], A, True),
    ("내부 작업 흔적", [r"v10\d|v11\d", r"(?i:PPT[X])", r"(?i:[.]ppt[x])"], A, True),
    ("비밀값 흔적", [r"gh[p]_", r"github_pa[t]_", r"-----BEGI[N]"], A, True),
    ("비밀값 흔적", [r"ap[i][_-]?key", r"secre[t]", r"passwor[d]", r"toke[n]\s*[:=]"], A | re.I, False),
]
RULES = [(cat, [re.compile(x, fl) for x in rxs], in_src) for cat, rxs, fl, in_src in RULES]
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+", A)
EMAIL_BIN = re.compile(r"[\w.+-]{3,}@[\w-]{2,}\.[A-Za-z]{2,}[\w.]*", A)
OWN_EMAIL = "dhqtlzm12" + "@" + "naver.com"
OWN_EMAIL_FILES = ("index.html", "docs/sources/README_Noah8218.md")
EMAIL_OK_ANYWHERE = ("@users.noreply.github.com", "git@github.com")
BIN_WORDS = re.compile(r"Author|Artist|Copyright|GPS")

TEXT_EXT = {".md", ".html", ".htm", ".css", ".js", ".mjs", ".py", ".json", ".txt", ".svg", ".yml", ".yaml", ".xml", ".csv", ".toml"}
TEXT_NAMES = {".gitignore", ".gitattributes", ".nojekyll", "CNAME", "LICENSE"}
MEDIA_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".mp4", ".webm", ".ico", ".avif"}
SKIP_DIRS = {".git", "node_modules", "__pycache__"}


def is_source_copy(rel):
    return rel.startswith("docs/sources/") and rel != "docs/sources/README.md"


def email_ok(addr, rel):
    addr = addr.rstrip(".")
    low = addr.lower()
    if low.endswith(EMAIL_OK_ANYWHERE[0]) or low == EMAIL_OK_ANYWHERE[1]:
        return True
    return low == OWN_EMAIL and rel in OWN_EMAIL_FILES


def scan_line(line, rel, src_copy, binary=False):
    """한 줄의 위반 [(분류, 매치)]. binary=True 는 압축 데이터에서 우연히 맞는 짧은 일치를 버린다(3글자 이하 매치, 느슨한 이메일)."""
    hits = []
    for cat, rxs, in_src in RULES:
        if src_copy and not in_src:
            continue
        for rx in rxs:
            hits += [(cat, m.group(0)) for m in rx.finditer(line) if not binary or len(m.group(0)) >= 4]
    for m in (EMAIL_BIN if binary else EMAIL).finditer(line):
        if not email_ok(m.group(0), rel):
            hits.append(("이메일", m.group(0)))
    return hits


def walk():
    """(상대 경로 posix, 절대 경로)를 정렬해서 돌려준다."""
    out = []
    for dp, dns, fns in os.walk(ROOT):
        rel_dir = Path(dp).relative_to(ROOT).as_posix()
        dns[:] = sorted(d for d in dns if d not in SKIP_DIRS and not d.startswith(".browser-profile-")
                        and (rel_dir + "/" + d).lstrip("./") != "tools/out")
        for fn in sorted(fns):
            p = Path(dp) / fn
            out.append((p.relative_to(ROOT).as_posix(), p))
    return out


def is_text(p):
    if p.suffix.lower() in TEXT_EXT or p.name in TEXT_NAMES:
        return True
    if p.suffix.lower() in MEDIA_EXT:
        return False
    with open(p, "rb") as f:
        return b"\x00" not in f.read(4096)


def scan_binary(rel, p):
    """바이너리의 경고 [(분류, 문자열)]. 파일당 최대 5건."""
    warns, seen = [], set()
    if p.suffix.lower() not in MEDIA_EXT:
        warns.append(("처음 보는 바이너리 형식", p.suffix or p.name))
    for s in re.findall(rb"[\x20-\x7e]{5,}", p.read_bytes()):
        t = s.decode("ascii")
        found = scan_line(t, rel, False, True) + [("메타데이터 단어", m.group(0)) for m in BIN_WORDS.finditer(t)]
        for cat, h in found:
            if (cat, h) not in seen:
                seen.add((cat, h))
                warns.append((cat, f"{h}  (문자열: {t[:60]})"))
    return warns[:5]


def main():
    ap = argparse.ArgumentParser(description="공개 전 유출 검사")
    ap.add_argument("--report-only", action="store_true", help="위반이 있어도 목록만 출력하고 종료 코드 0")
    a = ap.parse_args()

    viol, bwarn, n_text, n_bin = [], [], 0, 0
    for rel, p in walk():
        if is_text(p):
            n_text += 1
            src = is_source_copy(rel)
            for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").split("\n"), 1):
                for cat, m in scan_line(line, rel, src):
                    viol.append(f"{rel}:{i} | {m}  [{cat}]")
        else:
            n_bin += 1
            for cat, m in scan_binary(rel, p):
                bwarn.append(f"{rel} | {m}  [{cat}]")
    for v in viol:
        print(v)
    if bwarn:
        print("\n== 바이너리 경고 (차단하지 않음, 사람이 확인) ==")
        for w in bwarn:
            print(w)
    print(f"\n텍스트 {n_text}개·바이너리 {n_bin}개 검사, 위반 {len(viol)}건, 바이너리 경고 {len(bwarn)}건"
          + (" (--report-only: 종료 코드 0)" if a.report_only and viol else ""))
    return 1 if viol and not a.report_only else 0


if __name__ == "__main__":
    sys.exit(main())
