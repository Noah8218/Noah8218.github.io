# AGENTS.md: 이 저장소의 작업 지침 (AI·사람 공용, 첫 진입점)

> 이 문서의 "사용자"는 저장소 주인(사이트의 주인공)이다. 사용자가 한 말과 결정은 [docs/01-context-and-decisions.md](docs/01-context-and-decisions.md)에 시간순으로 있다. 사실은 2026-11-27 작성 시점 기준이니 코드와 `git log`로 현재 상태를 먼저 확인한다.

## 1. 이 저장소는 무엇인가

- 개인 포트폴리오 **정적 웹사이트**다(HTML/CSS/JS, 빌드 없음, 외부 의존성 없음). 공개 주소는 https://noah8218.github.io 이고 GitHub Pages로 배포한다.
- **스크롤형 한 페이지**이며 영어 기본 + 한국어(KO) 전환, 라이트 기본 + 다크 토글이다. **슬라이드/PPT 방식이 아니다**(슬라이드 덱으로 잘못 만들다 폐기한 이력이 있다).
- 내용은 사용자가 이미 공개한 OpenVisionLab 저장소 6개와 프로필 README에서만 가져온다. **이 저장소는 공개다.** 비공개 경력 포트폴리오는 이 저장소와 별개이며 포함하지 않는다.

## 2. 작업 전에 반드시 지킬 규칙

**공개 안전** (자세히: [docs/02-content-policy.md](docs/02-content-policy.md))
- 회사·고객사·전 직장·전화번호·학교·팀원 이름, 로컬 경로·계정명을 어떤 파일에도 쓰지 않는다. 연락 이메일은 사이트에 이미 공개된 한 곳 외에 문서에 쓰지 않는다.
- 제3자 자료(다른 사람 사이트, 발표 자료)의 캡처를 저장소에 넣지 않는다. 취향 레퍼런스는 글로만 설명한다.
- 푸시 전에 `python tools/scan_public.py`가 통과해야 한다.

**문구 출처** (사이트의 모든 문장은 다음 셋 중 하나여야 한다)
1. `docs/sources/`의 README 원문 문장 그대로(영어 기준), 한국어는 `README.ko.md` 계열 문장 우선.
2. 사용자가 직접 지정한 문구(영어를 바꾼 요소에 `data-ed`).
3. AI 번역 한국어(`data-ko-src="tr"`로 표시).
- **새 사실·경력·수치·성능 주장을 만들지 않는다.** 한계를 밝히는 문장("생산 정확도의 근거가 아님", "생산 장비 제어용으로 검증되지 않음", OpenCV 재배포 단서)을 약하게 만들지 않는다. Star·팔로워는 2026-11-27 고정값이며 기준일 표기를 지우지 않는다.

**이 사이트에서 하지 말 것** (사용자 피드백에서 나온 금지, 7절 참고)
- 새 장식 효과 금지: 글로우, 블러 등장, 캔버스 연출, 큰 글자(히어로 이름은 `clamp(2.6rem,6vw,4.5rem)`를 넘기지 않는다). 한 마디 피드백을 사이트 전체 개편으로 과잉 해석하지 않는다.
- 회사 정보, 새 사실 추가 금지. 승인 없이 [보류 제안](docs/04-design-evaluation.md)(일러스트 히어로, 시안 B/D, 마스코트) 적용 금지.
- **의존성·웹폰트·라이브러리(GSAP 등)를 사용자 승인 없이 넣지 않는다.** 이 제약은 작업자(AI)가 정한 것이고 사용자 요구가 아니므로, 도입하려면 먼저 사용자에게 묻는다.
- **성능을 해치는 구조를 다시 넣지 않는다**: 매 프레임 전체 캔버스를 지우고 다시 그리는 히어로, 스크롤 중 GIF·영상 즉시 재생, 테마 전환 중 전체 transition 등([docs/09-performance.md](docs/09-performance.md) 7절). 무거운 효과·미디어를 넣은 뒤에는 같은 문서 6절로 재측정한다.

## 3. 저장소 지도

```
index.html            한 페이지 전체(구조·문구·EN/KO 쌍). 섹션: top about projects ecosystem skills principles releases contact
css/style.css         스타일 전부. 맨 위 :root·[data-theme] 토큰, 맨 아래 html.still·반응형
js/main.js            i18n, 테마, 내비·scroll-spy, reveal, 카운터, 미디어 뷰어, 구성도 SVG, 스크롤 연동, ?lint
js/hero.js            히어로 캔버스(점 격자, 스캔 빔, 검출 괄호)
assets/               스크린샷(.webp)·GIF·mp4·favicon. 출처는 docs/assets-provenance.md. manifest.json은 .gitignore 대상
tools/                검사 도구(Python 표준 라이브러리): check_site, lint_site, shot_site, scan_public, fetch_sources, 성능 측정 perf_site·perf_profile·perf_ab
docs/                 문서(00-index.md부터). sources/는 README 원문 사본, design-proposals/는 시안·프로토타입, 09-performance.md는 성능 측정·원인·남은 한계
AGENTS.md CLAUDE.md   에이전트 지침. README.md는 사람용 소개
```

## 4. 고치는 방법

**문구**: `index.html` 안에서 직접 고친다. 영어는 요소 텍스트, 한국어는 같은 요소의 `data-ko` 속성이다. 고친 뒤 `python tools/check_site.py`로 출처 대조.

| 속성 | 뜻 | 규칙 |
|---|---|---|
| `data-ko="…"` | 한국어 문구. 있으면 KO 전환 때 텍스트로 바뀐다 | 영어(요소 텍스트)와 한국어는 같은 의미여야 한다 |
| `data-ko-src="tr"` | **AI가 번역**한 한국어(README 한국어 원문 없음) | 번역을 새로 쓰면 반드시 붙인다. 사용자 검토 대상([07](docs/07-copy-audit.md)) |
| `data-ko-src="ed"` | README 한국어 원문을 **고쳐 쓴** 한국어 | 고친 한국어에 붙인다 |
| `data-ko-src` 없음 | README 한국어 원문 **그대로** | 한 글자도 바꾸지 않는다 |
| `data-ed` | 영어를 README에서 고쳐 쓴 요소 | 사용자가 지정한 문구에만. `data-ko`와 함께 쓴다 |

- 새 라벨(문장이 아닌 UI 단어)은 `tools/allowed_labels.txt`에 등록한다.
- 한국어 전환은 `main.js`의 `setLang()`가 `data-ko` ↔ 원래 영어(`data-en`)를 바꾼다. 영어가 바뀌는 요소는 반드시 `data-ko`를 가져야 한다.

**새 프로젝트·미디어 추가** (상세: [docs/03-site-architecture.md](docs/03-site-architecture.md))
1. 파일은 공개 저장소 파일만 쓴다. `assets/<약어>-<내용>.webp`(스크린샷), `.mp4`(영상), GIF는 `.poster.webp`(결과가 보이는 첫 프레임)와 함께. 출처 URL과 라이선스를 `docs/assets-provenance.md`에 적는다.
2. 기존 `article.row`를 복제해 `.vw[data-vw]` 안에 `.stage > .m`(미디어), `.caps > p`(캡션), `.thumbs > button`(썸네일)을 **같은 개수·같은 순서**로 맞춘다. GIF는 `<img src=poster data-gif=GIF>`.
3. 접근성 연결: 캡션 `p`에 `id`(예: `c-ovl1`), 썸네일 `button`은 `aria-labelledby`로 그 id를 가리키고, `article.row`는 제목 `h3`의 id를 `aria-labelledby`로 가리킨다. 이미지 `alt`는 캡션과 같은 문장이고(`setLang`이 현재 언어 캡션으로 동기화), 캡션에도 `data-ko`를 붙인다. 합성·공개 데이터는 캡션에 밝힌다.
4. 행은 짝수번째마다 좌우가 교대된다(`.row:nth-of-type(even)`). 행을 추가·삭제하면 번호(`p.no`), 통계(`오픈소스 프로젝트 6`), Overview, 메뉴를 함께 확인한다.

**스타일**: 색·글꼴 토큰은 `css/style.css` 맨 위 `:root`(`--font --pad --wrap`)와 `[data-theme=dark]`·`[data-theme=light]`(`--bg --fg --accent …`)에만 둔다. 컴포넌트에 색 값을 직접 쓰지 않는다.

**모션 규칙**: 새 모션은 `html.still`(reduced-motion, 내비의 `#motion` 정지 토글, `?shot`, `?lint`) 상태에서 **최종 상태로 풀려야** 한다. `style.css` 맨 아래 `html.still` 블록에 풀림 규칙을 같이 추가한다. 자동 재생·반복 모션은 정지할 수단을 둔다. 모션은 장식이 아니라 증거(OK/NG, 전/후)를 보여 줄 때만 쓴다.

## 5. 검증 방법 (저장소 루트에서, 순서대로)

```
python tools/check_site.py                       # 문구 출처·금지어. 종료 0 = 통과
python tools/lint_site.py --theme light          # 레이아웃 린트(가로 넘침, 14px 미만 글자, alt 누락). 모바일은 --w 390
python tools/shot_site.py --full --theme light   # 전체 캡처 -> tools/out/ (한국어 --lang ko, 섹션 --hash projects)
python tools/scan_public.py                      # 푸시 전 유출 검사. 종료 0 = 통과
python tools/perf_site.py --case desktop         # 성능 재측정(선택): 코드를 크게 바꾼 뒤에만, 다른 작업을 모두 끄고. docs/09-performance.md 6절
```

- 도구는 Edge 또는 Chrome이 필요하다(없으면 환경 변수 `BROWSER`에 실행 파일 경로). **`lint_site`·`shot_site`는 `--theme` 기본값이 `dark`다**: 기본 화면은 라이트이므로 `--theme light`를 직접 준다. 영어·한국어, 데스크톱(1440)·모바일(390)을 모두 본다.
- **사람이 직접 볼 것**: (1) 라이트·다크 두 테마와 EN·KO 전환, (2) 모바일 메뉴(햄버거)와 가로 스크롤 없음, (3) 프로젝트 6개의 썸네일 클릭·방향키 이동과 영상·GIF 재생, (4) 구성도 선과 범례, (5) 원칙 구간 스크롤, (6) 키보드 Tab 이동과 포커스 표시. Safari·Firefox·실제 터치·스크린리더는 **미검증**이다.
- 로컬 서버: `python -m http.server 8000` 후 http://localhost:8000/ . `index.html`을 `file://`로 열어도 동작하지만(도구가 이 방식을 쓴다) 브라우저가 `localStorage`를 막으면 테마·언어 저장이 되지 않고(코드는 예외를 삼키고 메모리 상태만 유지), 영상 로딩 동작이 서버 환경과 다를 수 있다. 최종 확인은 서버로 한다.
- 개발용 쿼리: `?lang=ko|en`, `?theme=dark|light`, `?shot=1`(정지 모드), `?lint=1`, `?pp=0~1`(원칙 구간 진행도 고정). 상세는 [docs/03-site-architecture.md](docs/03-site-architecture.md).

**작업 흐름**: (1) `AGENTS.md`와 관련 문서를 읽고 [08-backlog.md](docs/08-backlog.md)에서 항목과 완료 기준을 확인한다. (2) `git status`로 다른 사람의 진행 중 변경을 확인하고 건드리지 않는다. (3) 고친다. (4) 위 검증 명령을 순서대로 실행하고 화면을 직접 본다. (5) 결과와 미검증 항목을 [08-backlog.md](docs/08-backlog.md)에 반영한다.

**사용자에게 먼저 묻는다**: 새 시각 요소·효과, 웹폰트·라이브러리, 경력·이력서·연락 방식 문구, 새 클립 촬영, 사용자 README와 문구 동기화(공개 저장소 변경), 이미지·영상의 출처가 불확실한 파일 추가. 답을 기다리는 동안 무관한 작업은 계속한다.

## 6. 배포와 커밋

- 저장소 이름은 `Noah8218.github.io`이고 `main` 푸시가 곧 배포다(Pages 소스는 `main` 루트이고 legacy 빌드다. 2026-11-27 저장소 생성 때 자동으로 켜졌고 `gh api repos/Noah8218/Noah8218.github.io/pages`로 확인했다). 첫 배포 확인: 주소 200 응답, 페이지가 참조하는 파일 35개 모두 200, 콘솔 오류 없음, EN↔KO·라이트↔다크 전환 동작. 푸시 후 빌드에 1분 안팎 걸리고 그동안 404가 나올 수 있다. 푸시 후 사이트를 열어 EN·KO·라이트·다크를 확인한다.
- **공개 저장소이므로 커밋 이메일이 노출된다.** `git config user.email "<숫자ID>+<GitHub 사용자명>@users.noreply.github.com"` 형식의 GitHub noreply 주소를 쓴다(실제 주소는 GitHub 설정의 이메일 화면에서 확인). 이미 푸시한 커밋의 이메일은 되돌리기 어렵다.
- 커밋 전에 `python tools/scan_public.py`와 `check_site.py`를 통과시킨다. 한 커밋에는 한 목적만 둔다.

## 7. 사용자 피드백 이력 (같은 실수를 하지 않는다)

- 처음 화면을 보고 "너무 AI스럽다, 과하게 화려해서 반감이 든다"고 했고, 원인을 묻자 "그냥 **이름이 너무 크게 나와서** 거부감이 들었다"고 답했다. 이름 글자를 최대 약 216px에서 약 72px로 줄였다. 이어서 "**밝은 게 더 좋아 보인다**"고 해서 기본 테마를 라이트로 바꿨다.
- **교훈**: 한 마디를 사이트 전체 개편으로 과잉 해석하지 않는다. 절제된 방향이 취향이다. 새 효과를 더하기 전에 사용자에게 묻는다.
- 공개 안전: "깃허브에 올라가는 공개인 걸 알지? 가능하면 현재 내가 GitHub에 공개한 프로젝트만 써라."
- 취향 레퍼런스(https://www.nazmussayad.com/ 등)의 공통점은 "색이 의미를 갖는 체계"와 "다이어그램·일러스트로 설명하는 언어"다. 단 위 피드백이 우선이다. 시안 B/D는 사용자가 아직 보지 못했고 **보류**다.

## 8. 지금 할 일 Top 5 ([docs/08-backlog.md](docs/08-backlog.md)에 완료 기준 포함)

**완료(2026-11-27)**: 버그 수정 A1~A7(글꼴 스택, `.sk` 전환 충돌, 내비 Principles 링크, 모션 일시정지 토글, 구성도 점선 모션, 영상 poster·빈 포스터, 미디어 틸트)과 추가 2건(항목 내용은 이 저장소에 기록되지 않았다), 성능 작업(히어로 캔버스, 테마 전환, 등장 전환, 미디어 재생 시점, 구성도 레이아웃). 검증: 동적 시험 dyn_motion 41/41·dyn_a11y 20/20 통과(시험 스크립트는 저장소에 없고 작업 세션에서 실행), `check_site.py` 위반 0건, `lint_site.py` 5회 실행 모두 이슈 0건, `scan_public.py` 0건. 성능은 유휴 CPU·테마 전환이 줄었고 스크롤 끊김·로드 직후 긴 작업은 개선을 확정하지 못했다. 수치와 한계는 [docs/09-performance.md](docs/09-performance.md). 상세 항목은 [08-backlog.md](docs/08-backlog.md) A 구역.

1. **B2. 이미지 출처 확인**(공개 전 필수): 와셔·기포·RBV 기판 사진이 직접 만든 것인지 공개 데이터인지. 사용자만 답할 수 있다.
2. **B1. 경력 블록·이력서 링크**: 평가자 다수가 첫째로 지적했다. 사용자 결정이 필요하다.
3. **B3·B4. 한국어 번역 94건 검토와 용어 통일**(Recipe/레시피, OK/NG 등).
4. **B7. Credits & Notices 상시 표시**: VisA CC BY 4.0, Vision SDK의 OpenCV 재배포 단서, RBV 라이선스 확인.
5. **성능 잔여 선택지**(P1~P6, 모두 미채택·보류): [docs/09-performance.md](docs/09-performance.md) 5절 참조.

## 9. 문서 지도

[docs/00-index.md](docs/00-index.md)가 전체 문서와 "언제 읽는가"를 정리한다. 사이트 구조는 [03](docs/03-site-architecture.md), 문구·공개 규칙은 [02](docs/02-content-policy.md), 결정 이력은 [01](docs/01-context-and-decisions.md), 작업 목록은 [08](docs/08-backlog.md), 성능 측정·한계는 [09](docs/09-performance.md)이다. 평가·시안 문서(04~06, `design-proposals/`)는 AI 평가자의 것이고 참고용이다.
