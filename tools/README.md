# tools: 사이트 검사 도구

이 저장소(공개 GitHub Pages 사이트)를 고치고 검증하는 파이썬 스크립트 모음이다. 저장소만 받으면 어디서든 같은 방식으로 돌릴 수 있도록 모든 경로를 스크립트 위치 기준 상대 경로로 계산한다(`tools/` 의 부모 폴더가 저장소 루트이자 사이트 루트).
아래 명령은 저장소 루트에서 실행하는 것을 기준으로 쓴다(PowerShell 에서는 `/` 대신 `\` 도 된다).

## 도구

| 도구 | 용도 | 예시 명령 | 종료 코드 |
| --- | --- | --- | --- |
| `check_site.py` | `index.html` 의 보이는 문장이 `docs/sources/` 의 공개 README 에 근거하는지 검사하고, 번역·수정 문구 목록과 금지어를 출력한다 | `python tools/check_site.py` | 0 위반 없음 / 1 위반 있음 / 2 `index.html` 이나 `docs/sources/` 가 없음 |
| `lint_site.py` | 헤드리스 브라우저로 `?lint=1` 레이아웃 검사를 읽는다(가로 넘침, 오른쪽으로 삐져나간 요소, 14px 미만 글자, alt 누락) | `python tools/lint_site.py --w 1440 --profile t1` | 0 이슈 없음 / 1 이슈 있음 / 2 브라우저를 못 찾았거나 결과를 읽지 못함 |
| `shot_site.py` | 헤드리스 브라우저로 사이트를 PNG 로 저장한다 | `python tools/shot_site.py --w 1440 --h 900 --hash top --theme light --profile t1 --out tools/out/top.png` | 0 저장됨 / 1 파일이 안 만들어짐 / 2 브라우저를 못 찾았거나 문서 높이를 못 읽음 |
| `fetch_sources.py` | 공개 README·메타를 다시 받아 `docs/sources/` 를 갱신한다 | `python tools/fetch_sources.py --dry-run` | 0 성공 / 1 받지 못한 파일이 있음(아무것도 쓰지 않음) |
| `scan_public.py` | 공개 전 유출 검사: 저장소 전체의 텍스트와 바이너리 메타데이터에서 회사·개인·로컬 경로·비밀값 흔적을 찾는다 | `python tools/scan_public.py` | 0 위반 없음(`--report-only` 면 항상 0) / 1 위반 있음 |
| `perf_site.py` | 헤드리스 브라우저로 성능을 1회 잰다: 로드(LCP 등), 유휴 CPU, 스크롤 프레임 시간, 미디어 행 CPU, 테마·언어 전환 반응 시간(아래 "성능 측정 도구") | `python tools/perf_site.py --case desktop` | 0 저장됨 / 2 브라우저를 못 찾음 |
| `perf_profile.py` | CPU 프로파일(로드·유휴)과 로컬 http 서버에서의 전송량을 텍스트로 출력한다 | `python tools/perf_profile.py --cpu 4` | 0 끝남 / 2 브라우저를 못 찾음 |
| `perf_ab.py` | 히어로 캔버스·블러를 하나씩 꺼서 스크롤 끊김 원인을 가르는 A/B | `python tools/perf_ab.py 1` | 0 끝남 / 2 브라우저를 못 찾음 |
| `allowed_labels.txt` | `check_site.py` 가 말뭉치에 없어도 허용하는 UI 라벨 목록(아래 "수정 문구 표시 규칙") | (실행 파일이 아님) | 해당 없음 |

각 스크립트 맨 위 docstring 에 용도·사용법·종료 코드·필요 환경이 있다. `lint_site.py` 와 `shot_site.py` 는 브라우저 탐색과 DevTools 에뮬레이션 코드를 공유한다(`shot_site.py` 가 `lint_site.py` 를 가져다 쓴다).

`fetch_sources.py` 는 인터넷으로 `docs/sources/` 의 파일을 덮어쓴다. 먼저 `--dry-run` 으로 주소를 확인하고, 덮어쓰기 전에 작업을 커밋해 둔다. 자세한 내용은 `docs/sources/README.md`.

## 환경

- Python 3.9 이상. 실제로 실행해 본 것은 3.11.9 뿐이다(3.9, 3.10 은 문법상 가능하다고 보지만 미검증).
- 표준 라이브러리만 쓴다. Pillow 는 어느 도구에도 필수가 아니다. `lint_site.py`, `check_site.py`, `fetch_sources.py`, `scan_public.py` 는 가져오지 않고, `shot_site.py` 는 있으면 저장한 이미지 크기를 출력할 뿐이다(Pillow 를 막고 실행해 확인했다).
- `lint_site.py`, `shot_site.py`, `perf_site.py`, `perf_profile.py`, `perf_ab.py` 는 Edge 또는 Chrome 이 필요하다. 탐색 순서: 환경 변수 `BROWSER`(실행 파일 경로) → Edge(Program Files (x86), Program Files) → Chrome → macOS 앱 경로 → PATH 의 `microsoft-edge`, `google-chrome`, `chromium` 계열. 못 찾으면 한국어 안내를 출력하고 종료 코드 2 로 끝난다.
- 검증한 환경: Windows 11, Edge(Program Files (x86) 설치). Chrome, macOS, Linux 는 경로 탐색 코드만 있고 실행해 보지 못했다.
- 브라우저 프로필 폴더는 `tools/.browser-profile-<--profile 이름>/`(DevTools 를 쓰는 경우 뒤에 `-cdp`)이며 `.gitignore` 대상이다. 도구가 지우지 않는다.
- 기본 출력 폴더는 `tools/out/` 이며 `.gitignore` 대상이다. 없으면 만든다.

## 공통 옵션 (`lint_site.py`, `shot_site.py`)

| 옵션 | 뜻 | 기본값 |
| --- | --- | --- |
| `--w` | 브라우저 폭(px) | 1440 |
| `--h` | 브라우저 높이(px) | `lint_site.py`: 폭 600 이하 844, 그보다 크면 900 / `shot_site.py`: 900 |
| `--lang en\|ko` | 사이트 언어 | `en` |
| `--theme dark\|light` | 사이트 테마 | `dark` (사이트 자체의 기본은 light 이므로 도구가 항상 값을 넘긴다) |
| `--profile 이름` | 브라우저 프로필 폴더 이름. 동시에 여러 개를 돌릴 때 서로 다르게 준다 | `site` |

`lint_site.py` 전용: `--json`(검사 결과 JSON 을 먼저 출력).
`shot_site.py` 전용:

- `--hash 섹션id`: 해당 섹션으로 스크롤해서 찍는다(예: `top`, `projects`).
- `--full`: 문서 전체 높이(최대 16000px)로 한 장을 찍는다.
- `--pp 0~1`: 원칙 구간(sticky)의 스크롤 진행도를 고정한다.
- `--out 경로`: 저장 경로. 없으면 `tools/out/site-<폭>x<높이>-<해시>-<언어>-<테마>[-full][-pp값].png`.

`check_site.py`, `scan_public.py`, `fetch_sources.py` 에는 위 옵션이 없다. 각각 `--report-only`(scan), `--dry-run`(fetch) 이 있다.

폭이 600 미만이면 DevTools 프로토콜(표준 라이브러리 소켓)로 같은 브라우저를 띄워 뷰포트를 에뮬레이션한다. 이유는 아래 "흔한 문제".

## 성능 측정 도구 (`perf_site.py`, `perf_profile.py`, `perf_ab.py`)

사이트가 느리거나 끊기는지 수치로 보는 분석용 도구다. 검사 도구(위 5개)와 달리 통과·실패 기준이 없고 JSON·텍스트를 남긴다. 수치의 해석, 이전 측정값, 남은 한계는 [docs/09-performance.md](../docs/09-performance.md) 에 있다. 세 파일 맨 위 docstring 에 측정 항목과 한계가 있다. `perf_profile.py`, `perf_ab.py` 는 `perf_site.py` 를 가져다 쓰고(`import perf_site as ps`), `perf_site.py` 는 `lint_site.py` 의 `get_browser`, `profile_dir`, `CDP`, `WS` 를 쓴다.

| 도구 | 목적 | 사용 | 출력(기본 `tools/out/`, `--out` 으로 변경) | 한계 |
| --- | --- | --- | --- | --- |
| `perf_site.py` | 한 케이스를 1회 측정: 로드(DCL, load, FCP, LCP, CLS, 긴 작업), 유휴 CPU 5초, 전체 스크롤 프레임 시간(섹션별 포함), 미디어 행 4개의 5초 점유, 테마·언어·썸네일 전환 반응 시간 | `python tools/perf_site.py --case desktop\|desktop_slow\|mobile_slow [--gpu on\|off] [--out 경로.json]` | `perf_<케이스>_<gpu>.json`. `motion_still` 이 `true` 면 모션 정지 상태로 잰 것이라 비교하지 않는다 | `file://` 라 네트워크 지연 없음, 헤드리스라 실제 GPU 합성과 다름, Edge(Chromium)만 측정. 한 케이스 약 1분 |
| `perf_profile.py` | 로드·유휴 구간의 CPU 프로파일(자기 시간 상위 함수)과 로컬 http 서버에서 본 전송량(로드 직후, 끝까지 스크롤한 뒤) | `python tools/perf_profile.py [--cpu 4] [--out 경로.txt]` | `perf_profile_cpu<배수>.txt` | 전송량의 스크롤은 빠르게 지나가는 것이라 행에 머무는 사용자와 다름. 압축·캐시 없음 |
| `perf_ab.py` | 스크롤 끊김 원인 분리: base, noblur, nocanvas, none 을 2회씩 비교 | `python tools/perf_ab.py [CPU배수] [--out 경로.json]` | `ab_cpu<배수>.json` | 모드당 2회뿐이라 단서일 뿐 결론이 아님. 현재 사이트에는 등장 블러가 없어 `noblur` 는 의미가 약함 |

- `--case`: `desktop`(1440x900, 스로틀 없음), `desktop_slow`(같은 크기, CPU 4배 스로틀), `mobile_slow`(390x844 모바일 에뮬레이션, CPU 4배 스로틀).
- **코드를 크게 바꾼 뒤에만, 다른 작업(브라우저 탭, 빌드, 영상 재생, 다른 측정)을 모두 끄고** 실행한다. 겹치면 프레임이 500~650ms 튄다. 같은 케이스를 2회 이상 잰다.
- 브라우저 프로필 폴더는 `tools/.browser-profile-perf-<케이스>[-gpu]-cdp/` 이고 `.gitignore` 대상이다. 도구가 지우지 않으므로 저장된 설정(모션 정지 등)이 실행 사이에 이어질 수 있다. 같은 프로필을 쓰는 측정을 동시에 돌리지 않는다.
- **검증 범위**: 측정에 쓴 원본 스크립트는 2026-11-27 에 Windows 11 + Edge 에서 실행했다. 이 저장소로 옮긴 버전은 `perf_site.py --case desktop` 을 2회 전체 실행해 JSON 이 생기는 것을 확인했다(새 프로필 첫 실행은 로드가 15초까지 느려져 버리고 다시 쟀다, [docs/09-performance.md](../docs/09-performance.md) 3-7절). `perf_profile.py` 와 `perf_ab.py` 는 `py_compile` 과 `--help` 만 확인했고 브라우저를 띄우는 전체 실행은 하지 않았다(옮기면서 경로·프로필 규칙·출력 위치를 `lint_site.py` 에 맞췄고 `motion_still` 기록을 더했다. 측정 로직은 같다). 이 둘은 처음 쓸 때 한 번 돌려 결과가 생기는지 확인한다. Chrome, macOS, Linux 는 `lint_site.py` 의 탐색 코드를 재사용할 뿐 실행해 보지 못했다.

## 개발 보조 쿼리

`index.html` 의 인라인 스크립트와 `js/main.js` 가 읽는 값이다(작성 시점 소스를 읽어 확인한 것이므로, 소스가 바뀌었으면 거기서 다시 확인한다). 도구가 자동으로 붙이니 손으로 브라우저에서 확인할 때만 직접 쓴다.

| 쿼리 | 동작 |
| --- | --- |
| `?shot=1` | 정지 모드(애니메이션·전환 끔, 모든 요소를 보이게), 지연 로딩 이미지를 즉시 로드, 비디오 컨트롤을 켜지 않음, 로드 뒤 `#해시` 섹션으로 스크롤 |
| `?lint=1` | `?shot=1` 과 같은 정지 모드·즉시 로드·해시 스크롤에 더해, 로드 300ms 뒤 레이아웃 검사 결과를 숨겨진 `<pre id="lintout">` 에 JSON 으로 넣는다(`lint_site.py` 가 읽음) |
| `?lang=ko` 또는 `en` | 시작 언어. 저장된 언어보다 우선 |
| `?theme=light` 또는 `dark` | 시작 테마. `dark` 가 아닌 값은 light. 저장된 테마보다 우선 |
| `?pp=0.5` | 원칙 구간을 이 진행도(0~1)로 고정하고 sticky 레이아웃을 유지한다(정지 모드에서도 적용) |
| `?vh=900` | `--vh` 와 스크롤 계산에 쓰는 뷰포트 높이를 이 값(px)으로 고정한다. 전체 높이로 캡처할 때 100vh 기반 구간이 문서 높이로 부푸는 것을 막는다 |

쿼리는 아니지만 브라우저 `localStorage` 의 `motion` 값이 `off` 면 정지 모드, `on` 이면 OS 의 "동작 줄이기" 설정이 있어도 애니메이션을 켠다. `lang`, `theme` 도 `localStorage` 에 저장된다.

## 수정 문구 표시 규칙

사이트의 문장은 `docs/sources/` 의 공개 README 에 있는 문장이 원칙이다. 번역하거나 고친 문장은 HTML 속성으로 표시하고, `check_site.py` 가 그 표시를 읽어 검사 대상과 목록을 가른다.

| 표시 | 뜻 | `check_site.py` 의 처리 |
| --- | --- | --- |
| `data-ko="한국어"` | 영어 요소에 짝지은 한국어 문장(언어 전환 때 바뀐다) | 아래 `data-ko-src` 가 없으면 README 한국어 원문이어야 한다. 말뭉치에 없으면 위반 |
| `data-ko-src="tr"` | 그 한국어는 영어 원문을 번역한 것(README 에 한국어 원문이 없다) | 말뭉치 검사에서 제외하고 "번역 목록"으로 출력. 영어 원문 텍스트는 그대로 검사 |
| `data-ko-src="ed"` | 그 한국어는 README 한국어를 고쳐 쓴 문장 | 말뭉치 검사에서 제외하고 "수정 문구 목록"에 `[KO]` 로 출력 |
| `data-ed` | 영어 문장을 README 에서 고쳐 쓴 요소. 반드시 `data-ko` 와 같이 쓴다 | 말뭉치 검사에서 제외하고 목록에 `[EN]` 으로 출력. `data-ko` 없이 쓰면 위반 |

- `<title>`, `<meta name="description">`, `img alt` 도 검사 대상이다. `alt` 는 라벨 허용 목록이 적용되지 않는다.
- 비교는 공백을 모두 지운 뒤 부분 문자열로 한다. 말뭉치는 마크다운 태그·링크 문법을 벗겨 만든다.
- `allowed_labels.txt`: 말뭉치에 없어도 허용할 "UI 라벨"을 한 줄에 하나씩 적는다(예: 건너뛰기 링크, 언어 버튼). 보이는 텍스트 노드와 `<title>`/`meta` 에만 적용되고, `data-ko` 값과 `alt` 에는 적용되지 않는다. 근거가 필요한 문장을 여기에 넣어 검사를 피하지 않는다.
- `docs/audit/final_edits.json`(선택): 수정 문구의 최종 목록 파일이다. 있으면 `data-ed`/`data-ko-src="ed"` 문구가 이 목록의 `new_en`/`new_ko` 와 일치하는지, 목록의 모든 수정이 사이트에 반영됐는지 검사한다. 각 항목은 `field`("content" 면 meta description), `old_en`, `new_en`, `old_ko`, `new_ko`, `ko_src` 를 가진다. **이 저장소에는 이 파일이 없어서 그 일치 검사는 "건너뜀"으로 출력된다.** 그때는 "수정 문구 목록" 출력을 사람이 확인한다. 이 파일이 없을 때 meta description 은 같은 문장이 `data-ed` 요소의 영어로 있을 때만 수정 문구로 본다.
- 금지어(회사·고객사 이름과 전화번호 모양)가 `index.html`, `css/`, `js/` 에 있으면 위반이다. 저장소 전체 검사는 `scan_public.py` 가 한다.

## 공개 전 점검 순서

1. `python tools/check_site.py`
2. `python tools/lint_site.py --w 1440 --profile t1`, `--w 390`, `--lang ko` 조합
3. `python tools/shot_site.py ...` 로 눈으로 확인(`tools/out/` 의 PNG 를 연다)
4. `python tools/scan_public.py` (종료 코드 1 이면 push 하지 않는다)

`scan_public.py` 의 검사 분류는 회사·고객사·전 직장, 전화번호, 로컬 경로·계정, 개인·학교·팀원 정보, 내부 작업 흔적, 이메일, 비밀값 흔적이다. 이메일은 사용자가 공개 프로필에 이미 올린 주소 한 개를 정해진 파일에서만 허용한다. `docs/sources/` 사본에는 일반 단어 기반 비밀값 검사만 적용하지 않는다. 이미지·영상은 바이트에서 ASCII 문자열을 뽑아 메타데이터 단어와 위 패턴을 찾아 "바이너리 경고"로 목록만 출력한다(종료 코드에 영향 없음). 검사 패턴에서 글자 하나를 `[]` 로 감싼 것(예: `삼[성]`)은 스크립트가 자기 자신에게 걸리지 않게 하려는 표기이며 뜻은 같다. 약칭 규칙에 걸린 곳이 사이트 자신의 문서에 있으면 허용 목록에 넣지 말고 사람이 판단한다(`--report-only` 로 목록만 본다).

## 흔한 문제

- **브라우저를 못 찾는다(종료 코드 2).** Edge 나 Chrome 을 설치하거나, 환경 변수 `BROWSER` 에 실행 파일의 전체 경로를 지정한다. PowerShell: `$env:BROWSER = '<msedge.exe 또는 chrome.exe 전체 경로>'`, bash: `export BROWSER='<경로>'`.
- **폭 600 미만을 찍는데 폭이 안 맞는다.** 헤드리스 브라우저 창은 약 492px 아래로 줄어들지 않는다(`--window-size=390` 이 뷰포트 492px 로 열린다는 기존 실측 기록을 따른 것이다). 그래서 폭 600 미만과, 해시(`--hash`)를 줄 때의 스크린샷은 DevTools 프로토콜로 뷰포트를 에뮬레이션해서 찍는다(폭 768 미만이면 모바일 에뮬레이션). 이 경로는 로컬 임시 포트(127.0.0.1)를 열고 브라우저를 하나 더 띄운다.
- **`--hash` 로 찍은 화면이 어긋난다.** 브라우저의 `--screenshot` 옵션은 스크롤된(해시로 이동한) 페이지를 어긋나게 찍는다. `shot_site.py` 는 해시를 줄 때(`--full` 이 아닐 때) 자동으로 DevTools 경로를 쓴다.
- **경로에 한글이 있다.** 도구는 `Path.as_uri()` 로 `file://` 주소를 만들기 때문에 한글 폴더 이름은 자동으로 퍼센트 인코딩된다. 브라우저 주소창에 직접 쓸 때는 주소를 손으로 적지 말고 `index.html` 파일을 끌어다 놓는다.
- **한 번 실행에 20~30초 걸린다.** 측정값: 이 환경에서 `lint_site.py --w 1440` 약 31초, `shot_site.py --hash top` 약 22초(새 `--profile` 이름으로 처음 돌린 값). 느린 원인은 확인하지 않았다. 시간 초과는 `lint_site.py` 120초, `shot_site.py` 180초다.
- **같은 프로필로 동시에 두 개를 돌렸더니 실패한다.** 같은 프로필 폴더를 두 브라우저가 동시에 쓰는 것이 원인일 수 있다(추정). 동시에 돌릴 때는 `--profile` 이름을 다르게 준다.
- **`lint_site.py` 의 폭이 `--w` 보다 작게 나온다(예: 1440 → 1416).** 이 환경에서 측정한 값이다. 폭 600 이상 경로가 헤드리스 창 크기(`--window-size`)를 쓰기 때문으로 보이며(추정) 이슈로 보지 않는다.
- **`check_site.py` 가 "말뭉치가 비어 있다"고 한다.** `docs/sources/` 의 파일이 없다. `python tools/fetch_sources.py` 로 받는다.
