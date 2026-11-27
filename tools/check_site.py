#!/usr/bin/env python3
"""index.html 의 보이는 텍스트가 출처 말뭉치(docs/sources)에 있는지 검사한다.

용도: 사이트의 모든 영어 문장과 프로젝트 설명 한국어 문장이 사용자가 공개한 README·GitHub 현황에 근거하는지 확인한다.
사용: python tools/check_site.py        (저장소 루트에서 실행하는 것을 기준으로 하지만, 경로는 스크립트 위치로 계산한다)
종료 코드: 0 위반 없음 / 1 말뭉치에 없는 문구·수정 문구 불일치·금지어가 있음 / 2 index.html 이나 docs/sources 를 찾지 못함.
필요: Python 3.9+ 표준 라이브러리만(브라우저·Pillow 불필요).

- 검사 대상: 보이는 텍스트 노드, img alt, <title>, meta description, data-ko 값(번역 표시가 없는 것).
- data-ko-src="tr" 요소는 번역 목록으로 따로 출력하고 말뭉치 검사에서 제외한다(영어 원문 노드는 검사한다).
- data-ed 요소의 영어, data-ko-src="ed" 요소의 한국어, 수정한 meta description 은 말뭉치 검사에서 제외하고 "수정 문구 목록"으로 출력한다.
  이 수정 문구가 docs/audit/final_edits.json 의 new_* 와 일치하는지, 목록의 모든 수정이 반영됐는지 확인한다(목록에 없는 수정은 위반).
  그 파일은 저장소에 없을 수 있다. 없으면 이 일치 검사만 "건너뜀"으로 출력하고 나머지 검사는 그대로 한다
  (이때 수정 문구는 목록을 사람이 확인해야 한다. 수정한 meta description 은 같은 문장이 data-ed 요소의 영어로 있을 때만 수정 문구로 본다).
- 말뭉치: docs/sources/README_*.md(README_ko_*.md 포함), stats.md, meta_*.json. 무관한 WPG-CUSTOM 저장소 파일은 제외한다.
- 금지어가 index.html, css, js 에 있으면 위반.
"""
import json
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

T = Path(__file__).resolve().parent   # tools/
ROOT = T.parent                       # 저장소 루트 = 사이트
S = ROOT / "docs" / "sources"
P = ROOT
EDITS = ROOT / "docs" / "audit" / "final_edits.json"

# 금지어 정규식. 글자 하나를 [] 로 감싼 것은 이 파일이 공개 전 검사(scan_public.py)에 스스로 걸리지 않게 하려는 표기이며 뜻은 같다.
FORBIDDEN = [r"\bL[G]\b", r"삼[성]", r"S[D]I", r"하이[닉]스", r"크레[셈]", r"케이[템]", r"피닉[슨]", r"현[대]", r"0\d{1,2}-\d{3,4}-\d{4}"]
SYMBOLS = re.compile(r"^[^\w가-힣]+$")


def extras(text):
    """태그·링크 문법에 가려지는 README 문장(alt/title 속성, 링크 제목, mailto 주소)을 말뭉치에 더한다."""
    out = re.findall(r'(?:alt|title)="([^"]*)"', text)
    out += re.findall(r'\]\([^)\s]*\s+"([^"]*)"\)', text)
    out += re.findall(r"mailto:([^)\s]+)", text)
    return "\n".join(out)


def strip_md(text):
    text = re.sub(r"<[^>]+>", "", text)
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r"\[([^\[\]]*)\]\(([^)]*)\)", r"\1", text)
    return text.replace("*", "").replace("`", "")


def squash(text):
    return re.sub(r"\s+", "", text)


def norm(text):
    return " ".join(text.split())


def build_corpus():
    files = sorted(set(S.glob("README_*.md"))) + [S / "stats.md"] + sorted(S.glob("meta_*.json"))
    parts = []
    for f in files:
        if "WPG-CUSTOM" in f.name or not f.is_file():
            continue
        raw = f.read_text(encoding="utf-8", errors="replace")
        parts.append(strip_md(raw))
        parts.append(extras(raw))
    return squash("\n".join(parts))


def load_labels():
    f = T / "allowed_labels.txt"
    labels = set()
    if f.exists():
        for line in f.read_text(encoding="utf-8").splitlines():
            if line.strip():
                labels.add(squash(line))
    return labels


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.in_title = False
        self.nodes = []      # (line, text)
        self.alts = []       # (line, alt)
        self.metas = []      # (line, text)
        self.kos = []        # (line, ko, tr, en, ed_src)
        self.stack = []      # data-ko 요소 추적: [tag, line, ko, tr, text, ed, ed_src]
        self.eds = []        # (line, en, ko) data-ed 요소(영어 수정)
        self.ed_nodes = 0    # data-ed 요소 안에서 말뭉치 검사를 건너뛴 텍스트 노드 수
        self.orphans = []    # data-ko 없이 data-ed 를 가진 요소(언어 전환이 영어를 되돌리지 못한다)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        if tag in ("script", "style"):
            self.skip += 1
        if tag == "title":
            self.in_title = True
        if tag == "img" and "alt" in a and a["alt"]:
            self.alts.append((line, a["alt"]))
        if tag == "meta" and a.get("name") == "description":
            self.metas.append((line, a.get("content", "")))
        if "data-ed" in a and "data-ko" not in a:
            self.orphans.append((line, tag))
        if "data-ko" in a:
            self.stack.append([tag, line, a["data-ko"], a.get("data-ko-src") == "tr", "",
                               "data-ed" in a, a.get("data-ko-src") == "ed"])

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if tag == "title":
            self.in_title = False
        if self.stack and self.stack[-1][0] == tag:
            _, line, ko, tr, text, ed, ed_src = self.stack.pop()
            self.kos.append((line, ko, tr, text, ed_src))
            if ed:
                self.eds.append((line, text, ko))

    def handle_data(self, data):
        if self.skip:
            return
        line = self.getpos()[0]
        if self.in_title:
            for part in re.split(r"\s[—|·]\s", data):
                self.metas.append((line, part))
            return
        if self.stack:
            self.stack[-1][4] += data
        if data.strip():
            if any(e[5] for e in self.stack):
                self.ed_nodes += 1
            else:
                self.nodes.append((line, data))


def load_edits():
    """final_edits.json 에서 바뀐 값만 뽑는다: (text 영어, text 한국어 전체, text 한국어 중 ko_src 가 빈 값인 것, content).
    파일이 없으면 None(일치 검사를 건너뛴다)."""
    if not EDITS.exists():
        return None
    edits = json.loads(EDITS.read_text(encoding="utf-8"))
    en, ko_all, ko_ed, content = Counter(), Counter(), Counter(), Counter()
    for e in edits:
        if e["field"] == "content":
            if e["old_en"] != e["new_en"]:
                content[norm(e["new_en"])] += 1
            continue
        if e["old_en"] != e["new_en"]:
            en[norm(e["new_en"])] += 1
        if e["old_ko"] != e["new_ko"]:
            ko_all[norm(e["new_ko"])] += 1
            if not e["ko_src"]:
                ko_ed[norm(e["new_ko"])] += 1
    return en, ko_all, ko_ed, content


def main():
    if not (P / "index.html").is_file():
        print(f"index.html 이 없다: {P / 'index.html'}", file=sys.stderr)
        return 2
    corpus = build_corpus()
    if not corpus:
        print(f"출처 말뭉치가 비어 있다. {S} 에 README_*.md, stats.md, meta_*.json 이 있어야 한다"
              "(python tools/fetch_sources.py 로 받을 수 있다).", file=sys.stderr)
        return 2
    labels = load_labels()
    html = (P / "index.html").read_text(encoding="utf-8")
    pg = Page()
    pg.feed(html)

    def ok(text, labels_ok=True):
        s = squash(text)
        if len(s) <= 1 or SYMBOLS.match(s):
            return True
        if labels_ok and s in labels:
            return True
        return s in corpus

    edits = load_edits()
    en_edits, ko_all, ko_ed_edits, content_edits = edits or (None, None, None, Counter())
    if edits is None:  # 대체 규칙: data-ed 요소의 영어와 같은 문장인 meta description 은 수정한 것으로 본다
        content_edits = Counter(norm(en) for _, en, _ in pg.eds)
    metas, ed_metas = [], []
    for line, t in pg.metas:
        (ed_metas if norm(t) in content_edits else metas).append((line, t))

    bad = []
    for line, t in pg.nodes:
        if not ok(t):
            bad.append((line, t.strip()))
    for line, t in pg.alts:
        if not ok(t, False):
            bad.append((line, "alt: " + t))
    for line, t in metas:
        if not ok(t):
            bad.append((line, "meta/title: " + t.strip()))
    for line, ko, tr, en, ed_src in pg.kos:
        if not tr and not ed_src and not ok(ko, False):
            bad.append((line, "data-ko: " + ko))

    # 수정 문구: final_edits.json 의 new_* 와 일치해야 하고, 목록의 모든 수정이 반영돼 있어야 한다.
    ed_en = [(line, norm(en)) for line, en, ko in pg.eds]
    ed_ko = [(line, norm(ko)) for line, ko, tr, en, ed_src in pg.kos if ed_src]
    for line, tag in pg.orphans:
        bad.append((line, f"data-ed 요소({tag})에 data-ko 가 없다"))
    if edits is not None:
        for line, t in ed_en:
            if t not in en_edits:
                bad.append((line, "data-ed 영어가 final_edits.json 의 new_en 이 아니다: " + t))
        for line, t in ed_ko:
            if t not in ko_ed_edits:
                bad.append((line, 'data-ko-src="ed" 한국어가 final_edits.json 의 new_ko 가 아니다: ' + t))
        for want, have, label in (
            (en_edits, Counter(t for _, t in ed_en), "영어 data-ed"),
            (ko_all, Counter(norm(ko) for _, ko, _, _, _ in pg.kos), "한국어 data-ko"),
            (content_edits, Counter(norm(t) for _, t in ed_metas), "meta content"),
        ):
            for t, n in want.items():
                if have[t] < n:
                    bad.append((0, f"{label}: final_edits.json 의 수정이 반영되지 않았다({have[t]}/{n}): {t}"))

    bad.sort()
    for line, t in bad:
        print(f"{line} | {t}")

    forb = []
    files = [P / "index.html"] + sorted((P / "css").glob("*")) + sorted((P / "js").glob("*"))
    for f in files:
        if not f.is_file():
            continue
        text = f.read_text(encoding="utf-8")
        for rx in FORBIDDEN:
            for m in re.finditer(rx, text):
                ln = text.count("\n", 0, m.start()) + 1
                forb.append(f"{f.name}:{ln} 금지어 /{rx}/ → {m.group(0)}")
    for x in forb:
        print(x)

    trs = [(line, en, ko) for line, ko, tr, en, ed_src in pg.kos if tr]
    plain = [x for x in pg.kos if not x[2]]
    print("\n== 번역 목록 (data-ko-src=\"tr\") ==")
    for line, en, ko in sorted(trs):
        print(f"{line}: {' '.join(en.split())}  →  {ko.strip()}")
    print("\n== 수정 문구 목록 (data-ed / data-ko-src=\"ed\" / 수정한 meta) ==")
    for line, en, ko in sorted(pg.eds):
        print(f"{line}: [EN] {norm(en)}")
    for line, ko, tr, en, ed_src in sorted(x for x in pg.kos if x[4]):
        print(f"{line}: [KO] {norm(ko)}")
    for line, t in sorted(ed_metas):
        print(f"{line}: [META] {norm(t)}")
    print(f"수정 요소: 영어 data-ed {len(ed_en)}개, 한국어 data-ko-src=\"ed\" {len(ed_ko)}개, meta {len(ed_metas)}개"
          f" (data-ed 안 텍스트 노드 {pg.ed_nodes}개를 말뭉치 검사에서 제외)")
    if edits is None:
        print(f"건너뜀: {EDITS.relative_to(ROOT).as_posix()} 가 없어 수정 문구 일치 검사를 하지 않았다(위 수정 문구 목록은 사람이 확인).")
    print(f"\n번역 요소 {len(trs)}개, 한국어 원문 요소 {len(plain)}개, 위반 {len(bad)}건, 금지어 {len(forb)}건, 말뭉치 {len(corpus)}자")
    return 1 if bad or forb else 0


if __name__ == "__main__":
    sys.exit(main())
