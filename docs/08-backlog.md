# 작업 목록 (백로그)

실행 가능한 작업을 한 곳에 모은다. 항목마다 **ID, 우선순위(P0~P2), 난이도(S/M/L), 상태, 해야 할 일, 완료 기준, 검증 방법, 관련 문서**를 적었다. **사용자 결정이 필요한 항목은 질문 문장까지** 써 두었다.

- **작성 시점은 2026-11-27이다.** 코드는 이후 바뀌었을 수 있으니, 작업 전에 `git log`(저장소가 git으로 올라간 뒤)와 코드로 현재 상태를 확인한다. 줄 번호는 쓰지 않고 선택자·함수 이름으로 가리킨다.
- **상태 값**: `완료` / `진행 중` / `대기` / `사용자 결정 필요` / `보류` / `미채택`(검토했으나 채택하지 않음, P 구역).
- **보류**는 사용자가 "과하다·이름이 크다·밝은 게 좋다"고 한 뒤 화려한 제안을 멈춘 상태다. 사용자 승인 없이 시작하지 않는다([01-context-and-decisions.md](01-context-and-decisions.md)).
- 인터랙션 제안은 **장식이 아니라 증거(OK/NG, 전/후, 값과 한계)를 보여 주는 것만** 후보로 둔다.
- 검증 명령의 기본형: `python tools/check_site.py`, `python tools/lint_site.py --theme light`(모바일은 `--w 390`, 한국어는 `--lang ko`), `python tools/shot_site.py --full --theme light`, 푸시 전 `python tools/scan_public.py`([AGENTS.md](../AGENTS.md) 5절).

## 한눈에 보기

| ID | 제목 | 우선 | 난이도 | 상태 |
|---|---|---|---|---|
| A1 | 글꼴 스택 순서 바로잡기 | P0 | S | 완료(2026-11-27 검증) |
| A2 | `.sk` 전환 충돌 수정 | P0 | S | 완료(2026-11-27 검증) |
| A3 | 내비 Principles 링크 | P0 | S | 완료(2026-11-27 검증) |
| A4 | 모션 일시정지 토글 | P0 | S | 완료(2026-11-27 검증) |
| A5 | 구성도 점선 모션 정지 | P1 | S | 완료(2026-11-27 검증) |
| A6 | 영상 poster·빈 포스터 교체 | P0 | S | 완료(2026-11-27 검증) |
| A7 | 미디어 틸트 제거 | P1 | S | 완료(2026-11-27 검증) |
| B1 | 경력 블록·이력서 링크 | P0 | M | 사용자 결정 필요 |
| B2 | 이미지 출처 확인(와셔·기포·RBV 기판) | P0 | S | 사용자 결정 필요 |
| B3 | 한국어 번역 94건 검토 | P0 | M | 사용자 결정 필요 |
| B4 | 용어 통일 | P1 | S | 사용자 결정 필요 |
| B5 | Raw Buffer Visualizer 라이선스 표기 확인 | P0 | S | 사용자 결정 필요 |
| B6 | Labeling Studio YOLO 계열 라이선스 안내 | P1 | S | 사용자 결정 필요 |
| B7 | Credits & Notices 상시 표시 | P0 | M | 대기(B2 이후) |
| B8 | `Usable` 칩 정의 | P1 | S | 사용자 결정 필요 |
| B9 | "Releases" 제목 불일치 | P2 | S | 사용자 결정 필요 |
| B10 | 히어로 주 버튼과 첫 화면 경력 한 줄 | P1 | S | 사용자 결정 필요 |
| B11 | 한국어 모드 번역 누락 요소 | P1 | S | 사용자 결정 필요 |
| B12 | 반복 문구("장비가 준비되기 전에") 정리 | P2 | S | 사용자 결정 필요 |
| C0 | 새 촬영 가능 여부 | P0 | S | 사용자 결정 필요 |
| C1 | GIF → mp4 규격 적용 | P0 | S | 대기 |
| C2 | 빈 시작 구간 컷 | P0 | S | 대기 |
| C3~C8 | 프로젝트별 새 클립·정지 화면, 데모 릴 | P1~P2 | S~L | 대기(C0 이후) |
| D1~D8 | 디자인·구조(방향 선택, 웹폰트, 구조 개편, 확대 보기, 마스코트 등) | P1~P2 | S~L | 보류 / 사용자 결정 필요 |
| E1~E8 | 증거형 인터랙션 | P0~P2 | S~M | 대기 / 보류 |
| F1~F7 | 운영(수치 갱신, 동기화, 배포, 호환성) | P1~P2 | S | F1 취소(수치 미표시, 2026-11-27), 나머지 대기 |
| P1~P6 | 성능 잔여 선택지(`content-visibility`, GIF→mp4, 긴 mp4 단축, `srcset`, 로드 레이아웃 긴 작업, 첫 언어 전환) | P2 | S~M | 미채택 / 보류 |

---

## A. 버그 수정 (완료, 2026-11-27 검증)

> **상태: A1~A7 모두 완료(2026-11-27 검증).** 같은 시기에 추가 2건도 처리했다(항목 내용은 이 저장소에 기록되지 않았다). **검증 근거**: 동적 시험 dyn_motion 41/41 통과, dyn_a11y 20/20 통과(시험 스크립트는 저장소에 없고 작업 세션에서 실행했다), `python tools/check_site.py` 위반 0건, `lint_site.py` 5회 실행 모두 이슈 0건, `python tools/scan_public.py` 0건. 아래 각 항목의 "할 일"과 "완료 기준"은 작성 시점의 원문이며, 실제 적용 결과(예: A1의 최종 `--font` 스택)는 [03-site-architecture.md](03-site-architecture.md)가 기준이다. 이후 성능 작업은 [09-performance.md](09-performance.md)에 있다. 배경 상세: [04-design-evaluation.md](04-design-evaluation.md) 진단 7, [05-expert-reports/interaction-motion.md](05-expert-reports/interaction-motion.md) 권고 1~3·9.
>
> 이전 기록(작성 말미 스냅샷): 2026-11-27 오후 3시 20분경에는 A1~A5·A7이 코드에 반영돼 있었고 A6은 3D PCB 포스터까지만 확인했었다. 그 시점에는 완료 기준을 통과했는지 검증하지 않았다.

### A1. 글꼴 스택 순서 바로잡기 (P0, S, 완료 2026-11-27)
- **배경**: `css/style.css`의 `--font`에서 `system-ui`가 `"Pretendard"`보다 먼저 매칭되어, 한국어 Windows에서 영문 제목까지 맑은 고딕으로 렌더된다. Pretendard는 이 PC·대부분의 방문자에 설치돼 있지 않다.
- **할 일**: `--font` 스택을 `"Pretendard Variable","Pretendard","Segoe UI Variable Text","Segoe UI",-apple-system,BlinkMacSystemFont,"Noto Sans KR","Malgun Gothic","Apple SD Gothic Neo",system-ui,sans-serif` 순서로 고친다(**웹폰트 파일은 추가하지 않는다**). 한국어 모드에서 `.ttl`, `.name`, `.pull p`, `.pr li`, `.big`의 음수 자간(`letter-spacing`)이 한글에 걸리는지 확인하고 `html[lang=ko]` 리셋 범위를 맞춘다.
- **완료 기준**: 한국어 Windows에서 영문 제목이 Segoe UI 계열로 렌더된다. 줄바꿈 위치가 바뀌어도 가로 넘침·잘림이 없다. 웹폰트 파일이 늘지 않았다.
- **검증**: `lint_site.py`(1440, 390, `--lang ko`), `shot_site.py --lang ko --hash projects` 캡처를 눈으로 비교. 렌더 글꼴은 브라우저 개발자 도구의 "Rendered fonts"로 확인.
- **위험**: Segoe UI는 라틴 폭이 맑은 고딕과 달라 줄바꿈이 바뀐다. macOS·Android 렌더는 **미확인**.
- **관련**: [art-direction.md](05-expert-reports/art-direction.md) 권고 1.

### A2. `.sk` 전환 충돌 수정 (P0, S, 완료 2026-11-27)
- **배경**: `.sk`의 `transition: transform .25s`가 `.reveal`의 전환을 덮어써 Skills 카드 4장이 페이드·스태거 없이 뜬다(다른 카드와 동작이 다르다).
- **할 일**: `.sk.reveal`의 `transition`에 opacity·transform·filter 전환을 합친다. 호버용 짧은 transform 전환은 입장이 끝난 뒤에만 쓰거나 틸트를 없앤다(A7과 함께 처리하면 단순해진다).
- **완료 기준**: Skills 카드 4장이 스크롤 진입 때 다른 카드와 같은 페이드와 0.1초 간격 스태거로 나타난다. 계산된 `transition`에 opacity가 있다.
- **검증**: 브라우저 개발자 도구에서 `.sk.reveal`의 computed transition 확인, 라이브(비 `still`) 화면에서 스크롤 진입 확인.
- **관련**: [interaction-motion.md](05-expert-reports/interaction-motion.md) 권고 1.

### A3. 내비 Principles 링크 (P0, S, 완료 2026-11-27)
- **배경**: `#principles` 구간(스크롤 약 3,600px)에서 내비 활성 항목이 0개다. `main.js`의 `secs`에는 `principles`가 있지만 `#menu`에 링크가 없다.
- **할 일**: (가) `onScroll()`에서 `principles`를 직전 섹션(`skills`) 활성으로 매핑하거나, (나) 내비에 Principles 링크를 추가한다. 내비 폭이 이미 빠듯하므로(가)가 단순하다.
- **완료 기준**: 원칙 구간의 10·50·90% 지점에서 활성 항목이 정확히 하나다. (나)를 택하면 모바일 메뉴와 `max-width:1000px` 구간의 링크 여백이 깨지지 않는다.
- **검증**: `shot_site.py --hash principles --pp 0.1`/`0.5`/`0.9`로 캡처, 라이브에서 스크롤 확인.

### A4. 모션 일시정지 토글 (P0, S, 완료 2026-11-27)
- **배경**: 자동 재생 영상·GIF·히어로 캔버스를 멈출 수단이 없다(WCAG 2.2.2). `prefers-reduced-motion`은 로드 시점에만 판단하고 이후 변경을 구독하지 않는다.
- **할 일**: 내비에 모션 토글(또는 뷰어별 Play/Pause)을 두고, 켜면 `html.still`과 같은 상태로 만든다(영상 pause, GIF는 포스터, 캔버스 정지). `matchMedia('(prefers-reduced-motion: reduce)')`의 `change`를 구독한다. `data-aria` 라벨은 `ARIA` 객체에 EN·KO로 추가한다. still 판정 분기(`main.js`, `hero.js`)를 한 헬퍼로 모은다.
- **완료 기준**: 토글 후 자동 재생과 반복 모션이 0이다(`document.getAnimations()`에 실행 중인 항목 없음). 토글 상태가 새로고침 뒤에도 유지된다(저장한다면 `localStorage` 키 하나 추가, 막힌 환경 대비 예외 처리 유지). 키보드로 조작되고 `aria-pressed`가 갱신된다.
- **검증**: 라이브 화면에서 토글 전후 비교, `lint_site.py`.
- **위험**: 중간(분기가 여러 곳). **새 장식이 아니라 접근성 요구**다.
- **관련**: [interaction-motion.md](05-expert-reports/interaction-motion.md) 권고 3.

### A5. 구성도 점선 모션 정지 (P1, S, 완료 2026-11-27)
- **배경**: 구성도의 점선 화살표는 "아직 개발 중"인 연동인데 `flow` 키프레임으로 흘러 "작동 중"으로 읽힌다. 화면 밖에서도 계속 돈다.
- **할 일**: `.eco.in .e.x`의 흐름 애니메이션을 없애고 점선은 정지한다. 실선(작동 중)에만 의미 있는 모션을 둔다면 보일 때만 돌린다.
- **완료 기준**: 점선이 움직이지 않는다. 범례 문구("Dashed arrows mark direct cross-project integration still in development.")와 어긋나지 않는다. 선 그리기 등장은 1회만 유지된다.
- **검증**: 구성도 구간 라이브 확인, `shot_site.py --hash ecosystem`.
- **관련**: [interaction-motion.md](05-expert-reports/interaction-motion.md) 권고 9.

### A6. 영상 poster·빈 포스터 교체 (P0, S, 완료 2026-11-27)
- **배경**: 2D Workbench 영상 두 개에는 포스터(`assets/ovl-inspection-stages.webp`)가 이미 들어갔다(작성 시점 코드). 반면 3D Studio·Raw Buffer Visualizer·Labeling Studio·Machine Studio의 첫 포스터는 결과 없는 빈 화면이다(3D: `Untested 8`, RBV: `No image selected`, Labeling: 주석 없는 이미지, Machine Studio: `PAUSED, RUNNING 0/2`).
- **할 일**: 각 프로젝트의 첫 미디어 포스터를 **결과가 채워진 프레임**으로 바꾼다(기존 GIF에서 프레임 추출, 새 촬영 없음). 파일 이름은 `.poster.webp` 규칙을 따르고 출처를 `assets-provenance.md`에 갱신한다.
- **완료 기준**: 6개 프로젝트의 첫 화면(재생 전)에 결과(검출 박스, OK/NG, 값)가 보인다. 빈 앱 화면·재생 아이콘만 있는 썸네일이 없다.
- **검증**: `shot_site.py --full`로 정지 화면 확인, `lint_site.py`(alt 누락 없음).
- **관련**: [project-showcase.md](05-expert-reports/project-showcase.md) 우선순위 1, [02-content-policy.md](02-content-policy.md) 4절.

### A7. 미디어 틸트 제거 (P1, S, 완료 2026-11-27)
- **배경**: 마우스를 올리면 `.frame`(과 `.sk`)이 `perspective` 기울기로 최대 약 4도 기울어 UI 글자를 읽기 어렵다.
- **할 일**: `main.js`의 포인터 이벤트에서 `transform` 기울기를 제거한다. 스포트라이트(`--mx/--my`)는 유지할지 지울지 작업자가 판단하되, **새 효과를 더하지 않는다.**
- **완료 기준**: `.frame` 호버 시 `transform`이 바뀌지 않는다. 스크린샷이 정지 상태로 보인다.
- **검증**: 라이브에서 마우스 호버 확인.
- **관련**: [interaction-motion.md](05-expert-reports/interaction-motion.md) 권고 7.

---

## B. 콘텐츠

### B1. 경력 블록·이력서 링크 (P0, M, **사용자 결정 필요**)
- **배경**: 평가자 8명 중 다수가 "딱 하나 바꾼다면"으로 지적했다. 사이트에 경력 근거가 문장 하나뿐이라 개인 오픈소스 소개로 읽힌다([06-persona-evaluation.md](06-persona-evaluation.md)).
- **질문**: "About 바로 아래에 실무 경력 블록(기간 · 회사 유형 · 장비/공정 · 내 역할 · 숫자 1개를 3~4줄)과 이력서 PDF 링크를 넣을까요? 회사·고객사 이름은 공개 사이트에 어디까지 쓸 수 있습니까(정하기 전에는 회사 유형으로만 씁니다)? 공개해도 되는 이력서 파일이 있습니까? 구직 중인지, 협업·외주 문의를 받는지도 문구로 밝힐까요?"
- **할 일**: 답을 받은 뒤 사용자가 제공한 문장·수치만 `.xp` 블록(기간, 역할, 회사 유형, 본문, 기술 칩, 선택 링크)으로 넣는다. EN·KO `data-ko`를 쓰고 새 수치를 만들지 않는다.
- **완료 기준**: 사용자가 준 문장만 들어갔다. 회사명은 사용자가 승인한 형태만. `scan_public.py`와 `check_site.py`(사용자 지정 문구는 `data-ed`와 `allowed_labels.txt` 등록)가 통과한다.
- **검증**: 영어·한국어·모바일 캡처.
- **관련**: [ux-benchmark.md](05-expert-reports/ux-benchmark.md)의 경력 블록 자리, [02-content-policy.md](02-content-policy.md) 1절.

### B2. 이미지 출처 확인: 와셔·기포·Raw Buffer Visualizer 기판 사진 (P0, S, **사용자 결정 필요, 공개 전 필수**)
- **배경**: 합성(3D)·생성(육각형 예제)·공개 데이터(VisA)는 출처가 밝혀져 있다. 그러나 `lab-detection-washer`, `lab-segmentation-bubble`, `lab-hero-smart-mask`(기포), `rbv-manual-stride-before/after`, `rbv-debugger-memory-image`의 기판 사진은 출처가 사이트와 공개 README 어디에도 없다. 업무 자료에서 온 것이라면 비밀유지 문제가 되는 가장 직접적인 경로다.
- **질문**: "와셔 이미지, 기포 필름 이미지, Raw Buffer Visualizer의 기판 사진은 (a)직접 만든 샘플입니까, (b)라이선스가 있는 공개 데이터입니까, (c)업무에서 얻은 자료입니까? (c)이면 사이트와 저장소에서 내리고 합성·공개 데이터로 바꿔야 합니다."
- **할 일**: 답을 `docs/assets-provenance.md`에 파일별로 기록한다. (c)이면 파일 교체(공개 저장소 6개의 README에 같은 이미지가 이미 공개돼 있는지도 확인).
- **완료 기준**: 모든 `assets/` 파일에 출처 구분(직접 생성 / 공개 데이터와 라이선스 / 합성)이 있다. 출처 불명 파일이 0이다.
- **검증**: `scan_public.py`의 바이너리 경고 확인, 사람 검토.
- **관련**: [06-persona-evaluation.md](06-persona-evaluation.md) 공개 리스크 검토자, [02-content-policy.md](02-content-policy.md) 4절.

### B3. 한국어 번역 94건 검토 (P0, M, **사용자 검토 필요**)
- **배경**: README에 한국어 원문이 없어 AI가 번역한 문장(`data-ko-src="tr"`) 94건(중복 제외, 당시 요소 117개)이 사용자 검토를 기다린다. 작성 말미에 내비에 추가된 `Principles`→`원칙`이 1건 더 있어 07 문서의 목록은 95건이고, `tools/check_site.py`는 번역 요소 118개를 센다.
- **추가(2026-11-27)**: 원칙 구간 한국어 8건(줄 6 + 문단 2) 추가, AI 번역(`data-ko-src="tr"`), 검토 전. 위 94건·95건·118개 숫자에는 넣지 않았다([01-context-and-decisions.md](01-context-and-decisions.md) 16번).
- **질문**: "[07-copy-audit.md](07-copy-audit.md)의 번역 목록 94건을 읽고, 어색하거나 틀린 곳을 알려 주세요(수정 문구를 주시면 `data-ko`에 반영합니다). 용어 통일 결정(B4)도 같이 부탁드립니다."
- **할 일**: 검토 결과를 `index.html`의 `data-ko`에 반영하고, 사용자가 고친 문장은 `data-ko-src`를 정리(`tr` 제거 또는 `ed`)한다. 07 문서의 목록을 갱신한다.
- **완료 기준**: 목록의 모든 행이 "확인함" 또는 수정됨. `check_site.py` 통과.
- **검증**: `check_site.py`, 한국어 모드 캡처(`--lang ko`).

### B4. 용어 통일 (P1, S, **사용자 결정 필요**)
- **배경**: `Recipe`/`recipe`/`레시피`, `툴`/`도구`/`Tool`, pass/fail↔OK/NG, 영상/이미지, 획득/수집/촬영, 장비/설비가 섞여 있다. 원인은 공개 README 한국어판이 저장소마다 다른 용어를 쓰는 것이다. 목록: [07-copy-audit.md](07-copy-audit.md) "용어 불일치".
- **질문**: "(1) `Recipe`로 통일할까요, `레시피`로 통일할까요? 앱 화면의 실제 UI 라벨은 무엇입니까? (2) `툴`·`도구`·`Tool`은 `도구`로 통일하고 UI 이름만 `Tool`로 둘까요? (3) 영어 캡션의 pass/fail을 OK/NG로 통일할까요(README 원문과 달라집니다)? (4) 영상/이미지, 획득/수집, 장비/설비는 어느 쪽으로 할까요?"
- **할 일**: 결정을 `docs/02-content-policy.md` 번역 정책에 용어표로 적고 `index.html`에 일괄 반영한다. README 원문과 달라지는 문구는 `data-ed`/`data-ko-src="ed"`로 표시한다.
- **완료 기준**: 한 화면 안에서 같은 개념이 한 가지로만 불린다. `check_site.py` 통과.

### B5. Raw Buffer Visualizer 라이선스 표기 확인 (P0, S, **사용자 확인 필요**)
- **배경**: 사이트 칩은 MIT인데 GitHub의 라이선스 판정은 `NOASSERTION`이다(`docs/sources/meta_RawBufferVisualizer.json`).
- **질문**: "Raw Buffer Visualizer 저장소에 `LICENSE` 파일이 있습니까? MIT가 맞다면 GitHub이 인식하도록 파일을 정리할 수 있습니까?"
- **할 일**: 확인 결과에 따라 칩 문구를 유지·수정한다(저장소 쪽 수정은 사용자 몫이며 공개 저장소 변경이라 별도 승인).
- **완료 기준**: 사이트 칩과 저장소의 라이선스 사실이 일치한다.

### B6. Labeling Studio YOLO 계열 라이선스 안내 (P1, S, **사용자 결정 필요**)
- **질문**: "Labeling Studio는 YOLOv8n·YOLO11n 같은 YOLO 계열 모델을 학습·추론에 씁니다. 사용자에게 모델 라이선스 안내를 사이트에 넣을까요? README에 이미 안내 문장이 있으면 그 문장 그대로 쓰겠습니다."
- **완료 기준**: 결정과 반영 여부가 기록된다. 문구는 README 원문 그대로.

### B7. Credits & Notices 상시 표시 (P0, M, 대기, B2 이후)
- **배경**: VisA CC BY 4.0 표기가 6번째 썸네일을 눌러야 보이는 한 줄(`.vnote`)과 푸터 한 줄뿐이고, 변경 표시(검출 박스를 그려 넣고 webp로 재압축한 개작본)와 원본 링크 구성이 부족하다. 푸터의 `Copyright (c) 2026 Noah Choi`는 모든 이미지를 작성자 것으로 읽히게 한다. Vision SDK의 OpenCV 재배포 단서는 칩(MIT) 때문에 가려진다.
- **할 일**: 푸터 위에 항상 보이는 크레딧 블록을 만든다: VisA 표기(링크·변경 표시), 출처가 다른 이미지 구분(B2 결과), Vision SDK의 OpenCV 재배포 단서(문장 그대로), 상표 문구. 문구는 README 문장 그대로 쓰고 새 문장은 사용자 지정으로 `data-ed`.
- **완료 기준**: 스크롤 끝에서 별도 클릭 없이 모든 출처가 보인다. VisA 표기에 원본 링크와 변경 표시가 있다. 접더라도 OpenCV 단서 한 줄은 항상 보인다. 모바일에서 가로 넘침 없음.
- **검증**: `check_site.py`, `lint_site.py`, 모바일 캡처.
- **관련**: [02-content-policy.md](02-content-policy.md) 7절.

### B8. `Usable` 칩 정의 (P1, S, **사용자 결정 필요**)
- **배경**: `Usable`은 정의가 없고 칩 분류가 섞여 있다(`Usable`=상태, `Source available`=배포 형태, `Active development`=개발 단계, `VS Marketplace`=채널). 2D Workbench는 게시된 ZIP이 소스 워크플로보다 오래돼도 `Usable`이다.
- **질문**: "`Usable`을 어떤 상태로 정의할까요? 아니면 칩을 '받는 방식'(`ZIP + source`, `Source only`, `VS Marketplace`)으로 바꿀까요?"
- **완료 기준**: 칩 의미가 한 가지 기준으로 정리되고 README 사실과 어긋나지 않는다.

### B9. "Releases" 제목 불일치 (P2, S, **사용자 결정 필요**)
- **배경**: 섹션 제목은 "Releases"인데 항목은 README·CHANGELOG의 소스 버전 기록이다. 조회한 저장소들의 GitHub `releases/latest` 응답이 모두 404였다(이 API는 prerelease를 돌려주지 않아 prerelease 게시 여부는 확인하지 못했다. 방문자가 GitHub에서 Releases를 눌렀을 때 비어 보일 수 있다).
- **질문**: "섹션 제목을 'Version history' 같은 말로 바꿀까요, 아니면 GitHub Releases를 게시할까요?"
- **완료 기준**: 제목과 실제 내용이 일치한다.

### B10. 히어로 주 버튼과 첫 화면 경력 한 줄 (P1, S, **사용자 결정 필요**)
- **배경**: 히어로 주 버튼이 GitHub이고 Email은 보조다. 첫 화면에 경력 정보가 없다(8년·20+는 About에 있다). 3명 이상의 평가자가 지적했다.
- **질문**: "히어로의 주 버튼을 Email(또는 이력서)로 바꾸고, 이름 아래에 '경력 8년 · 장비 프로젝트 20+ · 반도체/디스플레이/배터리/자동차' 한 줄을 올릴까요?"(두 번째는 이미 공개된 문장을 재배치하는 것이다)
- **완료 기준**: 결정이 반영되고 이름 글자 크기는 키우지 않는다.

### B11. 한국어 모드 번역 누락 요소 (P1, S, **사용자 결정 필요**)
- **배경**: 한국어 모드에서도 `<title>`·meta description, 타임라인 Raw Buffer Visualizer 2.0.9·2.0.8 항목, 푸터 저작권 줄은 영어다. 2.0.9·2.0.8은 뜻을 확신할 수 없어 번역하지 않았다.
- **질문**: "Raw Buffer Visualizer 2.0.9의 `final-row ROI spans`, `pinned-view`와 2.0.8의 `bounded incremental inspection`은 어떤 뜻입니까? 알려 주시면 번역합니다."
- **할 일**: 뜻을 받아 번역하고 `lang="en"`이 필요한 영어 문장에 `lang` 속성을 붙일지 검토한다. `<title>`은 언어 전환 때 바뀌게 할지 결정한다.

### B12. 반복 문구 정리 (P2, S, **사용자 결정 필요**)
- **배경**: "장비가 준비되기 전에 개발한다"는 전제가 히어로, About 인용문, Overview 목적 문단에 반복된다(원칙 1번은 README 문장으로 이미 교체됨. 2026-11-27부터는 프로필 README의 `Build earlier.`).
- **질문**: "같은 메시지가 세 곳에 나옵니다. 하나로 줄일까요, 그대로 둘까요?"

---

## C. 미디어

### C0. 새 촬영 가능 여부 (P0, S, **사용자 결정 필요**)
- **질문**: "새 화면을 직접 촬영할 수 있습니까? 필요한 것: 합성 PCB·웨이퍼 샘플(3D Studio), VisA 모델 2종(YOLOv8n, YOLO11n)과 MobileSAM 가중치(Labeling Studio), 공개 샘플 Good/Bad 쌍(2D Workbench), 앱 실행 환경(Machine Studio), 사용자 이름·경로가 보이지 않는 깨끗한 Windows 환경."
- **영향**: C3~C8은 이 답이 정해진 뒤에만 시작한다. 새 촬영 없이 되는 개선(C1, C2, A6, E1)을 먼저 한다.

### C1. GIF → mp4 규격 적용 (P0, S, 대기)
- **배경**: GIF 5개 합계 4,852,368 B. 같은 해상도 H.264 mp4(crf 30, 무음)로 바꾸면 1,263,580 B로 실측됐다(PCB 1,169,935→278,903, 웨이퍼 1,472,101→526,899, Smart Mask 730,212→87,664, 멀티모델 993,467→184,636, RBV 486,653→185,478). **화질은 눈으로 검수하지 않았다.** 사이트 `assets/` 합계는 9,354,962 B다.
- **할 일**: 변환(`ffmpeg`, `-an -movflags +faststart`)한 mp4를 `<video class="m" muted loop playsinline preload="none" poster=…>`로 교체한다(뷰어는 이미 `<video>` 경로가 있다). GIF는 포스터 추출용으로만 쓰고 배포하지 않는다. 카드·히어로는 6~12초, 1280×720, 15 fps, 1MB 이하.
- **완료 기준**: 5개 GIF가 mp4 + `poster.webp`로 바뀌고 총 용량이 줄었다. 화질을 사람이 확인했다. reduced-motion·모션 토글(A4)에서 정지 포스터가 보인다. 출처 표에 반영됐다.
- **검증**: `du`로 용량, `shot_site.py` 캡처, 라이브 재생 확인, `check_site.py`.
- **관련**: [04-design-evaluation.md](04-design-evaluation.md) 4-5, [project-showcase.md](05-expert-reports/project-showcase.md).

### C2. 빈 시작 구간 컷 (P0, S, 대기)
- **배경**: 3D Studio GIF 앞 1~2초, Raw Buffer Visualizer GIF 앞 약 2초가 빈 화면이다.
- **완료 기준**: 재생 시작 첫 프레임부터 내용이 보인다(C1과 같은 변환 때 처리).

### C3. 2D Workbench 새 클립 (P1, M, 대기, C0 이후)
- **할 일**: [project-showcase.md](05-expert-reports/project-showcase.md)의 "2D Workbench > 촬영 목록(대본)"을 따라 (1) Shape Count 12초(검출 5→OK, 검출 2→NG), (2) 공개 ZIP으로 첫 결과까지 9초, (3) Good/Bad 정지 이미지 3장을 찍는다. 기존 mp4 두 개(약 36초)는 앞 12초 클립이나 Tool 챕터 탭으로 쪼갠다.
- **완료 기준**: 대본의 길이·해상도·용량 목표를 지키고, 화면에 개인 경로·계정이 없다. 소스 빌드(v2.2.0-dev.12)와 공개 ZIP(v2.1.0-rc.3)을 캡션에서 구분한다.
- **검증**: `scan_public.py`(바이너리 경고), 눈 확인.

### C4. Machine Studio 클립·정지 화면 (P1, M, 대기, C0 이후)
- **할 일**: 시뮬레이션 실행 12초, 고장 주입 10초(알람 표시는 촬영 때 확인), 6탭 정지 화면 재촬영. 현재 미디어에 움직이는 자료가 0개다. 2D/3D/Labeling과의 직접 연동 장면은 README가 "개발 중"이라 **만들지 않는다.**
- **관련**: [project-showcase.md](05-expert-reports/project-showcase.md) "Machine Studio".

### C5. 3D Studio 로트·웨이퍼 클립과 히어로 대표 클립 (P1, M, 대기, C0 이후)
- **할 일**: 합성 PCB 8장 로트 12초, 웨이퍼 9지점 12초. 합성 데이터 배지 필수. **히어로에 어떤 클립을 쓸지는 사용자 결정**이다(UX 제안은 3D Studio 로트).
- **질문**: "히어로에 클립을 넣는다면 어느 프로젝트로 할까요? (제안: 3D Studio 로트)"

### C6. Labeling Studio 클립 (P1, M, 대기, C0 이후)
- **할 일**: Smart Mask 고해상도 10초, 비교→지정→추론 12초, 같은 이미지의 YOLO11n 결과 1장. 기포 샘플은 B2 확인 뒤에만 사용한다.

### C7. Vision SDK 코드 실행 (P2, S, 대기, C0 이후)
- **할 일**: 코드 실행→콘솔 `16x16` 8초, FirstInspection 실제 출력(텍스트가 더 낫다). 네이티브 의존성 구성이 촬영 PC에서 되는지 먼저 확인.

### C8. Raw Buffer Visualizer 보조 클립 (P2, S, 대기)
- **할 일**: README가 링크한 `manual-stride.gif`, `pixel-neighborhood.gif`의 존재·용량·최신 UI 반영 여부를 먼저 확인한다(**미확인**). 있으면 mp4로 변환.

### C9. 14초 데모 릴 (P2, L, 대기, C3~C7 이후)
- **할 일**: [project-showcase.md](05-expert-reports/project-showcase.md)의 "데모 릴 구성안"(컷 6개 + 끝 카드). v0은 기존 재료(컷 3·4·6 + SDK 코드 정지 화면, 약 9초), v1은 신규 클립 합성.
- **주의**: 모든 컷에 편집본·합성·시뮬레이션 표기. 용량 1MB 이하 목표(미측정).

---

## D. 디자인·구조 (보류, 사용자 결정 후 진행)

> 이 구역의 제안은 AI 평가자의 것이며 **사용자가 시안을 아직 보지 못했다.** 사용자가 "과하다·이름이 크다·밝은 게 좋다"고 했으므로 화려한 쪽은 보류다. 근거와 시안: [04-design-evaluation.md](04-design-evaluation.md), [design-proposals/README.md](design-proposals/README.md).

### D1. 비주얼 방향 선택 (P1, L, **사용자 결정 필요, 보류**)
- **질문**: "시안 3장([concept-b-hero-cream.png](design-proposals/concept-b-hero-cream.png) 크림·남색, [concept-d-industrial-dark.png](design-proposals/concept-d-industrial-dark.png) 산업 모니터 다크, [concept-b-in-d-tokens.png](design-proposals/concept-b-in-d-tokens.png) 이중 테마 확인용)을 보고 방향을 고르시겠습니까? 아니면 지금의 절제된 라이트 사이트를 유지하고 시안은 참고로만 둘까요?"
- **완료 기준**: 결정이 `01-context-and-decisions.md`에 기록된다. 선택이 없으면 현재 방향을 유지한다.
- **주의**: B와 D에 공통인 기반(의미 색 토큰, 글꼴 스택, 상태 칩 색 구분, 모노 kicker와 단계 탭, 미디어 프레임 테두리)부터 하자는 것이 아트 디렉터 추천이었으나 이것도 사용자 승인 후에 한다.

### D2. 웹폰트·GSAP 허용 (P1, S, **사용자 결정 필요**)
- **질문**: "Pretendard·JetBrains Mono 서브셋(OFL, 약 390KB 추정)을 `assets/`에 내장해도 됩니까? GSAP 같은 라이브러리는 쓰지 않아도(`pathLength`와 `dashoffset`으로 충분) 되는데 허용하시겠습니까? 허용하지 않으면 시스템 글꼴 스택과 순수 CSS/JS로 갑니다."
- **배경**: "의존성·웹폰트 금지"는 AI가 정한 제약이다. 사용자의 모션 덱에는 웹폰트 내장과 GSAP 사용 이력이 있다.

### D3. 구조 개편: 6카드 요약 그리드·상세 `<dialog>`·길이 줄이기 (P1, L, **보류**)
- **배경**: 페이지가 길고(정지 모드 약 15,000px, 라이브는 더 길다) 첫 제품 화면이 스크롤 약 2.7화면 뒤에 나온다. 제안 목표 길이는 약 8,500~9,000px(설계 목표, 구현 후 재측정 필요).
- **할 일(승인 시)**: 6카드 요약 그리드 추가(기존 행 유지) → 행을 `<dialog>`로 이동, 원칙 구간 고정 길이 축소, 릴리스 접기. 단계적으로 한다.
- **완료 기준**: 목표 길이 재측정, 모든 기존 정보가 상세로 옮겨져 손실 없음.
- **관련**: [ux-benchmark.md](05-expert-reports/ux-benchmark.md).

### D4. Overview를 Projects 앞으로, Overview에 Raw Buffer Visualizer 포함 여부 (P2, S, **사용자 결정 필요**)
- **질문**: "구성도를 프로젝트 6개 앞으로 옮길까요? 현재 구성도에는 Raw Buffer Visualizer가 없는데 넣을까요(README의 흐름도에는 없습니다)?"

### D5. 스크린샷 확대 보기 (P1, M, **사용자 결정 필요**)
- **배경**: 1600px 원본 스크린샷이 약 656px 프레임에 줄어 UI 글자가 읽히지 않고 확대 수단이 없다. 장식이 아니라 증거 가독성 기능이다.
- **질문**: "스크린샷을 눌러 크게 보는 기능(`<dialog>` 확대)을 넣을까요?"
- **완료 기준**: 클릭·Esc·포커스 복귀가 되고 영상 항목은 포스터만 확대한다. 키보드로 조작된다.

### D6. 마스코트·프로필 사진 (P2, M, **사용자 결정 필요**)
- **질문**: "프로필 사진이나 마스코트(캐릭터) 같은 그림 요소를 쓰시겠습니까? 쓰지 않으면 숙련도 배지·퍼센트도 만들지 않습니다(근거 없는 자기평가는 새 주장이 됩니다)."

### D7. 색 의미 매핑 (P2, S, **사용자 결정 필요**)
- **질문**: "초록=OK·사용 가능, 주황=NG·주의, 호박=ROI·측정 같은 색 의미 매핑에 동의하십니까? (현재는 포인트색 청록 1색입니다.)"

### D8. 링크 미리보기(OG) 메타 (P2, S, 대기)
- **배경**: OG 메타가 없어 링크 미리보기에 그림이 없다. 새 이미지 제작이 필요하다.
- **할 일**: 사용자가 이미지(`assets/og.png` 등)를 정하면 `og:*`와 `twitter:*` 메타를 추가한다. 이미지는 새 장식이 아니라 기존 스크린샷 활용을 우선한다.

---

## E. 인터랙션 (증거를 보여 주는 것만)

> 프로토타입은 [design-proposals/README.md](design-proposals/README.md)에 있다. **Edge(Chromium) 헤드리스로만 검증**했고 Safari·Firefox·실제 터치·스크린리더는 **미검증**이다. 프로토타입의 판독값(Threshold 170, 960×720, 3.2 ms 등)은 캡처 화면에서 읽은 값이라 공개 전에 확인한다.

### E1. Raw Buffer Visualizer stride 전/후 슬라이더 (P0, S, 대기)
- **배경**: 기존 전/후 두 장(3,840→3,920바이트 스트라이드)으로 "깨진 이미지가 숫자 하나로 정상이 된다"를 조작해서 보여 준다. 새 촬영 없음.
- **할 일**: [proto-stride-compare.html](design-proposals/proto-stride-compare.html)의 CSS와 스크립트를 `.vw` 안 `.m` 레이어로 이식한다(전/후 썸네일 2개를 "비교" 1개로 합침). `data-ko`로 EN/KO 라벨.
- **완료 기준**: 마우스 드래그, 방향키·Home, 버튼으로 조작되고 `aria-valuenow`가 갱신된다. 모바일 390 폭에서 동작한다.
- **검증**: `lint_site.py`, 라이브 조작, 키보드 확인.

### E2. 2D Workbench 파이프라인 단계 워커 (P1, M, 대기)
- **배경**: 스크린샷 위에서 원본→Filter→Threshold→Morphology→Blob→Contour→판정을 단계별로 비춘다. 화면 속 수치만 쓰므로 새 사실이 없다.
- **할 일**: [proto-pipeline-walker.html](design-proposals/proto-pipeline-walker.html)의 좌표·판독값 상수를 `data-steps`로 분리해 프로젝트 01 뷰어의 새 항목으로 넣는다. 영역 좌표는 캡처 해상도(1600×900)에 종속이라 캡처가 바뀌면 다시 측정한다.
- **완료 기준**: 단계 이동(클릭·방향키)이 되고 유휴 시 애니메이션이 멈춘다. `html.still`에서 정적 7단계로 풀린다.
- **관련**: [interaction-motion.md](05-expert-reports/interaction-motion.md) 권고 6.

### E3. Labeling Studio VisA 실측 카드·모델 A/B 토글 (P1, S~M, 사용자 승인 후)
- **배경**: 가장 강한 증거(VisA PCB4 실측 표: YOLOv8n mAP50 0.747, 놓친 불량 3/40, 정상 오검 4/402 / YOLO11n 0.723, 8/40, 1/402)가 6번째 썸네일에 묻혀 있고 숫자가 화면에 없다.
- **주의**: 지금 사이트에는 성능 수치를 싣지 않는 것이 과장을 줄인다는 평가가 있었다. 싣는다면 **README 표를 그대로** 옮기고 "한 데이터셋의 결과이고 생산 정확도의 근거가 아님" 문장과 VisA 출처를 같은 카드에 둔다.
- **질문**: "Labeling Studio 카드에 VisA PCB4 실측 표(README 숫자 그대로)를 넣을까요?"

### E4. 3D Studio 로트 8칸 타일·값-한계 게이지 (P2, M, 대기)
- **할 일**: 합성 PCB 로트 8장의 Pass 5 / Fail 3을 타일로, 2079.53 vs 허용 1502–1913을 게이지로. **합성 데이터 배지 필수.** 1차는 기존 GIF에서 3타일을 추출, 2차는 8타일 재촬영(C5).

### E5. Machine Studio 6탭 워크플로 플레이어 (P2, M, 대기)
- **할 일**: 기존 정지 화면 6장에 번호 핫스팟을 얹는다. 2D/3D/Labeling 직접 연동은 만들지 않는다.

### E6. Vision SDK 경계 스테퍼 (P2, S, 대기)
- **할 일**: "SDK가 하는 일 / 내 앱이 하는 일" 경계를 코드와 함께 단계로 보여 준다. 라이선스 문단을 접더라도 **OpenCV 재배포 단서 한 줄은 항상 보이게** 한다(B7).

### E7. 구성도 노드를 링크로 (P1, S, 대기)
- **할 일**: `.nd`를 링크로 바꿔 프로젝트로 스크롤하게 하고, 호버·포커스 시 연결선을 강조한다. 점선은 정지 상태 유지(A5), 실선(작동 중)에만 진행 점을 허용한다.
- **완료 기준**: 키보드 포커스 순서가 노드 순서와 맞는다.

### E8. 보류(장식에 가까운 제안)
다음은 사용자 취향상 **하지 않는다**: Customize 패널(Ctrl+.), Ctrl+K 이동, Vision mode 이스터에그, 스캔 빔 reveal로 `.scan` 대체, Principles 상태 그림 6개, 히어로 괄호 의미 고정과 캔버스 연출 변경, reveal 동사 다양화(pop·grow·pulse), 프로젝트 인덱스 레일(점선 진행 막대). 사용자가 명시적으로 원할 때만 다시 검토한다.

---

## F. 운영

### F1. Star·팔로워 수치 갱신 (P1, S, 취소)
- **상태**: 취소(사용자 결정으로 수치 미표시, 2026-11-27). 사이트에서 Star·팔로워 수치와 기준일을 삭제했다([01-context-and-decisions.md](01-context-and-decisions.md) 15번).
- **배경**: 41 stars(15+6+5+1+10+4), 팔로워 90은 2026-11-27 고정값이었다.
- **할 일/완료 기준**: 해당 없음.

### F2. 사이트·README 문구 동기화 (P2, S, **사용자 승인 필요**)
- **배경**: 같은 문구가 사용자의 GitHub README에도 있다. 사이트만 고치면 달라진다. README 수정은 공개 저장소 변경이다.
- **질문**: "사이트에서 고친 문구(예: Overview, 목적 문단)를 GitHub 프로필 README에도 반영할까요?"

### F3. 릴리스 타임라인·Latest 갱신 (P2, S, 대기)
- **할 일**: 새 버전이 나오면 `fetch_sources.py`로 README 사본을 갱신하고, 사이트의 문구는 README 문장 그대로 옮긴다. 누락 프로젝트(2D·3D·Labeling·Machine Studio 이력은 타임라인에 없다)를 넣을지는 사용자 결정.

### F4. Pages 설정과 Jekyll 처리 확인 (P1, S, 대기)
- **할 일**: 저장소 Settings > Pages의 소스(`main` 루트)를 확인한다. 루트에 `.nojekyll`이 없으면 GitHub Pages가 Jekyll로 `docs/*.md`를 처리할 수 있으니 필요 여부를 확인한다(**미확인**).
- **완료 기준**: https://noah8218.github.io 에서 `index.html`이 열리고 EN·KO·라이트·다크가 동작한다.

### F5. 커밋 신원 확인 (P0, S, 대기)
- **할 일**: 첫 커밋 전에 `git config user.email`이 GitHub noreply 주소인지 확인한다([AGENTS.md](../AGENTS.md) 6절). 푸시 전 `scan_public.py`.

### F6. 에셋 출처 표 유지 (P1, S, 대기)
- **할 일**: `assets/`에 파일을 추가·교체할 때마다 `docs/assets-provenance.md`에 원본 URL과 라이선스를 적는다. 원본 매니페스트 `assets/manifest.json`은 `.gitignore` 대상이다.

### F7. 브라우저·보조기술 검증 (P2, M, 대기)
- **할 일**: Safari, Firefox, 실제 터치, 스크린리더(NVDA 등)로 검증한다. `.vw:has(.code)`, `backdrop-filter`, `IntersectionObserver` 동작을 본다. 결과를 이 문서와 [03-site-architecture.md](03-site-architecture.md) 한계 표에 반영한다.

---

## P. 성능 잔여 선택지 (2026-11-27 성능 작업 뒤에 남은 것, 모두 미채택·보류)

> 여기의 **ID P1~P6은 항목 번호**이고 우선순위 P0~P2와 다르다. 수치·근거·측정 방법은 [09-performance.md](09-performance.md)(3절 수치, 5절 선택지, 6절 재측정)다. **효과가 측정된 항목은 없다**(전송량·파일 크기만 측정). 아래 "완료 기준"의 비교 값은 09 문서 3절의 `base2`(전)·`after_final`(후)이고, 코드를 고친 뒤 같은 케이스를 2회 이상 재서 비교한다(`python tools/perf_site.py --case desktop|desktop_slow|mobile_slow`, 다른 작업을 모두 끄고).

### P1. `content-visibility:auto` (P2, S, 미채택)
- **배경**: 화면 밖 섹션의 렌더 비용을 줄이는 선택지다. 채택하지 않았고 효과는 측정하지 않았다.
- **할 일**: 긴 섹션(`.sec` 등)에 `content-visibility:auto`와 `contain-intrinsic-size`를 시험한다.
- **완료 기준**: 3케이스에서 `scroll_all.over_50`과 `load.longtasks` 최장이 09 문서 3절의 전·후 범위보다 낮다. 문서 높이, scroll-spy(`#menu` 활성 항목), 원칙 구간(`.pr-wrap`) 위치, 해시 이동이 달라지지 않는다(`lint_site.py`, `shot_site.py --full`로 비교).
- **위험**(추정): 화면 밖 요소의 높이가 확정되지 않아 문서 높이가 변하면 스크롤 위치와 scroll-spy 계산이 어긋날 수 있다.

### P2. GIF를 mp4로 교체 (P2, S~M, 미채택, C1과 같은 작업을 성능 관점에서 본 항목)
- **배경**: 성능 작업 전 코드에서 끝까지 빠르게 스크롤했을 때 전송량 5691KB 중 GIF가 2331KB(약 41%)였다(`3d-pcb-lot-inspection.gif` 1142KB, `lab-hero-smart-mask.gif` 713KB, `rbv-debugger-memory-image.gif` 475KB가 확인됨). 현재 코드는 스크롤로 지나가기만 하면 GIF를 받지 않으므로(2020KB) 이득은 행에 머무는 방문자로 한정될 것이다(추정). 파일 크기 감소는 C1에 측정된 값이 있고(GIF 5개 4,852,368B → mp4 1,263,580B) 재생 CPU 감소는 측정하지 않았다.
- **할 일/완료 기준**: C1의 기준을 따른다. 더해서 `perf_site.py`의 `media_rows_5s` 점유율(GIF 행: 4배 스로틀 24~52%)이 mp4일 때 낮아지는지 재서 확인한다. 화질은 사람이 눈으로 본다.

### P3. 약 36초 mp4 단축 (P2, M, 미채택, **사용자 승인 필요**)
- **배경**: `ovl-tool-settings.mp4`가 전송량에서 가장 큰 단일 파일(1343KB)이었다. 2D Workbench mp4 두 개는 합쳐 약 36초다(C3의 기록). 단축 효과(전송량·재생 CPU)는 측정하지 않았다.
- **할 일/완료 기준**: C3의 앞 12초 클립·Tool 챕터 분할을 따른다. 새 편집본은 콘텐츠 변경이므로 사용자 승인 후 진행한다. 완료 시 `perf_profile.py`의 전송량으로 `ovl-*.mp4` 용량 감소를 확인한다.

### P4. `srcset` 이미지 (P2, M, 미채택)
- **배경**: 끝까지 스크롤한 뒤 전송량 2020KB 중 webp가 1971KB(98%)다. 작은 화면용 이미지를 따로 주면 줄 수 있다는 것은 추정이며 측정하지 않았다.
- **할 일**: 이미지별 작은 버전을 만들고 `srcset`·`sizes`를 붙인다.
- **완료 기준**: 390px 폭에서 `perf_profile.py` 방식의 전송량이 줄었다(측정). 새 파일의 출처가 `docs/assets-provenance.md`에 있다. `syncAlt`·캡션 동기화, `check_site.py`, `lint_site.py`가 통과한다.
- **비용**: 저장소 용량 증가, 출처 표 갱신.

### P5. 첫 로드의 레이아웃 긴 작업 (P2, M, 보류)
- **배경**: 데스크톱 최장 0~297ms, CPU 4배 스로틀에서 10회 중 8회가 최장 0.88~1.68초다. 후 로드 프로파일에서 `layoutEco()`의 자기 시간이 1062.7ms로, 첫 `offsetWidth` 읽기가 문서 전체 레이아웃을 치르는 것으로 보인다(추정, 호출 그래프 미확인).
- **할 일**: 먼저 `Profiler`로 긴 작업의 실제 호출 위치를 확인한다. 그다음 구성도 선 계산 시점을 늦추거나 레이아웃 비용을 쪼개는 방안을 비교한다.
- **완료 기준**: 같은 조건 2회 이상에서 `load.longtasks` 최장이 09 문서 3절의 전·후 범위보다 낮다. 구성도 선·화살촉 위치가 이전과 같다(`lint_site.py`, `shot_site.py --hash ecosystem` 비교). 접근성·`html.still` 동작이 같다.

### P6. 첫 언어 전환의 글꼴·레이아웃 비용 (P2, M, 보류)
- **배경**: CPU 4배 스로틀에서 첫 언어 전환이 약 1.0~1.5초(`interaction.lang_toggle_ms` 첫 값), 이후는 146~867ms다. 전 코드 프로파일(스로틀 없음)에서 첫 전환 270ms 중 레이아웃이 213ms였다. 글꼴 미캐시(한글 글꼴로 바뀌며 재레이아웃)가 원인일 것으로 추정하지만 확인하지 않았다.
- **할 일**: 언어 전환 구간 CPU 프로파일로 글꼴 전환인지 레이아웃인지 먼저 가른다. 웹폰트는 사용자 승인 없이 넣지 않는다([AGENTS.md](../AGENTS.md) 2절, D2).
- **완료 기준**: 4배 스로틀 첫 전환이 09 문서 3절의 전·후 범위(990~1521ms)보다 낮고 웹폰트가 늘지 않았다. 글꼴 스택을 바꾸면 줄바꿈·가로 넘침을 `lint_site.py`(1440, 390, `--lang ko`)로 확인한다.
