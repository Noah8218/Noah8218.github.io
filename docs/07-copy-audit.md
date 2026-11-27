# 문구 점검(AI 티 제거) 기록

사이트 문구의 AI 티, 번역투, 영어·한국어 불일치를 점검하고 고친 기록이다. 사용자가 "한글 영어 둘 다 현업에 맞는 AI스러운 어휘·용어를 전부 찾아 고쳐 달라"고 요청했고, 두 차례 수정했다(1차 29건 + 제목 줄표 1건, 2차는 평가자 8명의 공통 지적 A~I). 이 문서는 **무엇을 어떻게 고쳤고, 무엇이 아직 사용자 확인 대기인지**를 남긴다. 되돌리거나 같은 기준으로 새 문구를 검사할 때 쓴다.

## 방법

| 구분 | 기준 |
|---|---|
| 영어 | 홍보·과장 어휘(ecosystem, seamless, robust, leverage 등), 줄표(em dash), "not X, but Y" 부정 병렬, 추상명사 나열, 같은 문단 안의 동의어 순환(right/correct), 빈 틀 표현("I prefer engineering that ...") |
| 한국어 | humanizer-ko의 **AI 티 37개 패턴**을 기준으로 삼았다(번역투, 불필요한 피동·명사형, 상투적 연결어, 영어 직역 등). 도구 이름과 현업 용어는 고치지 않는다 |
| 과교정 방지 | 사람이 쓴 문장을 일부러 어색하게 바꾸지 않는다. 장비 현업어(티칭, 양산 샘플, 광학계, 척 기준 영역 등)는 그대로 둔다. 한계를 밝히는 문장(예: "생산 정확도의 근거는 아닙니다")은 **약하게 만들지 않는다** |
| 수치·확신도 보존 | 수치, 제품명, 주장의 세기는 바꾸지 않았다. 평가자가 제안한 대체 문장 중 README에 없는 경험이 들어간 것은 쓰지 않았다 |
| 출처 규칙 | 사이트의 모든 문장은 (1) README 문장 그대로, (2) 사용자가 문구를 직접 지정한 것(`data-ed`), (3) 한국어 번역(`data-ko-src="tr"`) 중 하나다. 규칙 상세는 [02-content-policy.md](02-content-policy.md) |
| 표시 | 영어를 고친 요소는 `data-ed`, README 한국어 원문을 고친 요소는 `data-ko-src="ed"`, AI 번역은 `data-ko-src="tr"`. `tools/check_site.py`가 이 표시를 기준으로 말뭉치(`docs/sources/`)와 대조한다 |

- 되돌리려면 해당 행의 '전' 문구로 영어(요소 텍스트)와 한국어(`data-ko` 속성)를 함께 바꾸고 위 속성을 지운다. 표에서 `-`는 바꾸지 않은 칸이다. 삭제한 문장은 '전' 칸에 **원문을 그대로** 남겼다.
- 표의 `#` 열 번호(`n=…`)는 1차 점검 당시 문구 목록의 번호다. 지금은 쓰지 않는다.
- 표에 나오는 `README_*.md`, `README_ko_*.md`는 `docs/sources/` 아래의 원문 사본이다.
- 이 기록은 점검 시점의 사이트 기준이다. 이후 버그 수정·디자인 변경으로 요소 위치가 달라졌을 수 있다.

## 1차 수정

공개 포트폴리오 사이트의 AI 티 나는 표현, 번역투, 영어와 한국어가 서로 다른 문구 29건(# 열)과 제목의 줄표 1건을 고쳤다. 목록에 없는 문구는 바꾸지 않았다. 원칙 1·2번 영어 문구가 길어져 1440px 화면에서 줄이 넘쳐 `.pr li` 글자 크기만 줄였다(`6.1vw`를 `5.7vw`로, `5.6rem`을 `4.8rem`으로). 이후 2차 수정에서 원칙 문구를 다시 바꿨다.

### 수정한 문구

| # | 위치(섹션) | 영어 전 | 영어 후 | 한국어 전 | 한국어 후 | 이유 |
|---|---|---|---|---|---|---|
| 2 | 페이지 메타(description) | Building OpenVisionLab — open-source C#/.NET tools for 2D/3D inspection, labeling, and debugging. | OpenVisionLab: open-source C#/.NET tools for 2D/3D inspection, labeling, and debugging. | - | - | meta description. n=20과 같은 문구, 줄표 제거. |
| 8 | 내비게이션(Overview 메뉴) | Ecosystem | Overview | 생태계 | 구성도 | Ecosystem은 마케팅 어휘. 이 섹션은 프로젝트가 서로 어떻게 이어지는지 보여 주는 구성도라 Overview/구성도로 한다. |
| 11 | 내비게이션(Contact 메뉴) | - | - | 연락 | 연락처 | 메뉴 이름으로 쓴 '연락'은 영어를 그대로 옮긴 번역투. 명사 '연락처'가 자연스럽다. n=389와 같이 적용(영어는 그대로). |
| 20 | 히어로(소개 문장) | Building OpenVisionLab — open-source C#/.NET tools for 2D/3D inspection, labeling, and debugging. | OpenVisionLab: open-source C#/.NET tools for 2D/3D inspection, labeling, and debugging. | OpenVisionLab을 만들고 있습니다 — 2D/3D 검사, 라벨링, 디버깅을 위한 오픈소스 C#/.NET 도구. | OpenVisionLab: 2D/3D 검사, 라벨링, 디버깅용 오픈소스 C#/.NET 도구. | 줄표 제거. 바로 위 tagline과 'Building'으로 시작하는 반복도 없앴다. |
| 30 | About(둘째 문단) | OpenVisionLab is my personal open-source R&D ecosystem for C# machine-vision developers. | OpenVisionLab is my personal open-source R&D project for C# machine-vision developers. | OpenVisionLab은 C# 머신비전 개발자를 위한 저의 개인 오픈소스 R&D 생태계입니다. | OpenVisionLab은 C# 머신비전 개발자를 위한 제 개인 오픈소스 R&D 프로젝트입니다. | ecosystem을 project로. 한국어 '저의'를 '제'로. |
| 31 | About(셋째 문단) | - | - | 가상 장비, 이미지 데이터, 검사 소프트웨어, 재사용 가능한 알고리즘, 검증 워크플로를 연결하기 위해 이 생태계를 만들고 있습니다. | 가상 장비, 이미지 데이터, 검사 소프트웨어, 재사용 가능한 알고리즘, 검증 워크플로를 연결하기 위해 만들고 있습니다. | 영어는 유지(아직 만드는 중이라는 상태와 연결 대상 5개를 담은 문장이라 패턴 8로 보지 않았다). 한국어만 '이 생태계'를 빼서 n=30 변경과 맞췄다. |
| 59 | 프로젝트 > 2D Workbench(기능 목록) | - | - | 같은 Recipe로 Good/Bad 샘플을 Batch inspection하고 결과를 확인합니다. | 같은 Recipe로 Good/Bad 샘플에 Batch inspection을 실행하고 결과를 확인합니다. | UI 이름 Batch inspection을 동사처럼 붙인 '~하고'를 명사 + 실행으로 풀었다. README 본문의 'Batch inspection을 실행합니다'와 같은 표현이다. |
| 135 | 프로젝트 > Machine Studio(설명) | Configure a virtual machine, write its control sequence, and check machine behavior before hardware commissioning. | Configure virtual equipment, write its control sequence, and check machine behavior before hardware commissioning. | - | - | 'virtual machine'은 C# 개발자에게 VM(가상 머신)으로 읽힌다. 같은 페이지의 virtual equipment와 한국어 '가상 장비'에 맞췄다. |
| 149 | 프로젝트 > Machine Studio(기능 목록) | Author sequences with explicit targets, waiting conditions and applied step settings. | Write sequences with explicit targets, waiting conditions and applied step settings. | - | - | 같은 카드 설명(n=135)은 write인데 여기만 Author로 바꿔 불렀다. write로 통일했다. Author는 격식체 어휘다. |
| 194 | 프로젝트 > Vision SDK(기능 목록) | - | - | 2D는 Tool을 설정하고 Execute(Mat)을 호출합니다. | 2D는 Tool을 설정하고 Execute(Mat)를 호출합니다. | 조사 오류. 'Mat'은 모음으로 끝나게 읽는다. |
| 208 | 프로젝트 > Raw Buffer Visualizer(설명) | - | - | C# 머신 비전용 Image Watch 방식 디버깅 | C# 머신비전용 Image Watch 방식 디버깅 | AI 티가 아니라 표기 통일이다. 같은 사이트의 다른 문구(산업용 머신비전, 머신비전 개발자 등)는 모두 붙여 쓴다. |
| 216 | 프로젝트 > Raw Buffer Visualizer(영상 안내) | - | - | 실제 처리 성능을 측정한 영상은 아닙니다. | 편집한 시연 영상입니다. 처리 시간을 측정한 영상은 아닙니다. | 영어 'Edited demonstration; not a processing-time measurement.'와 맞춤. 한국어에서 빠진 '편집한 시연'을 복원. |
| 232 | Overview(섹션 제목) | Ecosystem | Overview | 생태계 | 구성도 | n=8과 같은 이유(섹션 제목). |
| 252 | Overview(목적 문단 앞부분) | The purpose is not to replace real equipment validation. It is to | OpenVisionLab does not replace real equipment validation. Its purpose is to | 목적은 실제 장비 검증을 대체하는 것이 아니라 | OpenVisionLab은 실제 장비 검증을 대체하지 않습니다. 목적은 | 'not X. It is to Y' 부정 병렬을 '대체하지 않는다'(한계 고지는 유지)와 '목적은 Y'로 나눴다. 한국어 '~하는 것이 아니라 ~하는 것' 대구도 같이 풀었다. 원문의 끝 공백은 HTML에서 유지. |
| 254 | Overview(목적 문단 뒷부분) | , so physical-machine time can be used for the things that truly require hardware, optics and production samples. | , so physical-machine time can be used for work that requires hardware, optics and production samples. | 입니다. 그래서 실제 장비 시간은 하드웨어, 광학계, 양산 샘플이 꼭 필요한 일에 쓸 수 있습니다. | 입니다. 그래서 실제 장비 시간은 하드웨어, 광학계, 양산 샘플이 필요한 일에 쓸 수 있습니다. | 'the things that truly require'를 'work that requires'로 줄였다(군더더기, 강조어 truly 제거). 한국어 '꼭'도 뺐다. n=253(strong)은 그대로 둔다. |
| 256 | Skills(부제) | - | - | 프로젝트 뒤의 경험 | 프로젝트의 바탕이 된 경험 | 영어는 유지. 한국어 '뒤의'는 behind의 직역이라 어색해서 '바탕이 된'으로 바꿨다. |
| 294 | 원칙(1번) | Build earlier. | Build before the machine is ready. | 더 일찍 만든다. | 장비가 준비되기 전에 만든다. | 무엇을 일찍 만드는지 없는 슬로건이라 같은 페이지 tagline(n=19)의 구체 표현으로 풀었다. 길이는 늘어난다. |
| 295 | 원칙(2번) | Validate explicitly. | Validate against explicit criteria. | 명시적으로 검증한다. | 명시한 기준으로 검증한다. | 부사만 있는 슬로건에 대상(기준)을 붙여 explicit의 뜻을 남겼다. 사용자가 뜻한 것이 '기준 명시'인지 확인 필요. 길이는 늘어난다. |
| 296 | 원칙(3번) | - | - | 상태를 결정적으로 유지한다. | 상태를 결정론적으로 유지한다. | 영어는 유지(공학 관용 표현). 한국어 '결정적으로'는 decisive로 읽히므로 deterministic의 표준 번역 '결정론적으로'로 바꿨다. |
| 298 | 원칙(5번) | - | - | 증거를 보존한다. | 근거를 보존한다. | 영어는 유지. 같은 evidence를 n=303은 '근거', README 원문(n=192)은 '결과 근거'로 옮겼는데 여기만 '증거'라 '근거'로 통일했다. |
| 300 | 원칙 아래 본문(첫 문단 앞부분) | I prefer engineering that improves | I would rather improve | - | - | 'I prefer engineering that improves'의 빈 틀을 줄였다. n=302와 한 문장이다: I would rather improve ... than add complexity just for novelty. 한국어 앞부분은 그대로. 이 문장은 바로 아래 문단과 내용이 겹쳐서, 통째로 지울지는 사용자 판단. |
| 302 | 원칙 아래 본문(첫 문단 뒷부분) | over adding complexity only for novelty. | than add complexity just for novelty. | 을 높이는 엔지니어링을 선호합니다. | 을 높이는 쪽을 선호합니다. | n=300과 짝. '엔지니어링을 선호'의 빈 명사를 뺐다. 원문의 앞 공백은 HTML에서 유지. |
| 303 | 원칙 아래 본문(둘째 문단) | For machine-vision software, an algorithm producing the right result once is not enough. The complete system must acquire the correct image, execute the correct inspection at the correct time, preserve the result, recover from failure, and provide enough evidence to explain what happened later. | For machine-vision software, an algorithm producing the right result once is not enough. The complete system must acquire the right image, run the right inspection at the right time, preserve the result, recover from failure, and provide enough evidence to explain what happened later. | - | - | 같은 문단에서 right와 correct를 섞어 썼다(동의어 순환). right로 통일하고 execute를 run으로 바꿨다. 한국어는 이미 '올바른'으로 통일돼 있어 그대로. |
| 319 | 릴리스 > 변경 이력(Vision SDK 3.3.0-rc.3) | - | - | Matching 탐색 grid를 제한하고 Host 종료·촬영 deadline·terminal 결과를 보강했습니다. Caliper 품질을 선택형 Pipeline acceptance에 연결하고 고정 패키지 소비 검사를 추가했습니다. | Matching 탐색 grid를 제한하고 Host 종료·촬영 deadline·terminal 결과를 보강했습니다. Caliper 품질을 선택형 Pipeline acceptance에 연결하고 고정 패키지를 사용하는 앱 검증을 추가했습니다. | consumer를 직역한 '소비 검사'가 무엇을 검사하는지 읽히지 않아 '패키지를 사용하는 앱 검증'으로 풀었다. |
| 331 | 릴리스 > 변경 이력(Vision SDK 3.3.0-rc.1) | - | - | 9점 표면 보정, 물리 엣지 gap/flush와 협력 취소를 추가했습니다. | 9점 표면 보정, 물리 엣지 gap/flush와 3D 협력 취소를 추가했습니다. | 영어 'cooperative 3D cancellation'에서 빠진 3D를 복원. |
| 339 | 릴리스 > 변경 이력(Vision SDK 3.2.0-rc.5) | - | - | CI에서 패키지 검증 오류를 보존하도록 개선했습니다. | CI에서 패키지 검증 진단 정보를 보존하도록 했습니다. | 영어 'diagnostics'를 '오류'로 옮긴 것을 바로잡음. |
| 343 | 릴리스 > 변경 이력(Vision SDK 3.2.0-rc.4) | - | - | QR 판독, 선택형 3D CUDA 연산과 소비자 안내를 추가했습니다. | QR 판독, 선택형 3D CUDA 연산과 패키지 사용 안내를 추가했습니다. | consumer guidance를 직역한 '소비자 안내'는 고객 안내로 읽힌다. 패키지를 쓰는 쪽을 위한 안내라는 뜻이 보이게 '패키지 사용 안내'로 바꿨다. |
| 347 | 릴리스 > 변경 이력(Vision SDK 3.1.0) | - | - | 선택형 CUDA 엣지 점수 계산과 표면 측정을 개선했습니다. | 선택형 CUDA 엣지 점수 계산을 추가하고 표면 측정을 개선했습니다. | 영어 'Add optional CUDA edge scoring and improve surface measurements'와 맞춤. 한국어는 둘 다 '개선'으로 읽혔다. |
| 389 | Contact(섹션 제목) | - | - | 연락 | 연락처 | n=11과 같은 이유(섹션 제목). 영어는 그대로. |
| 줄표 | 페이지 제목(브라우저 탭 `<title>`) | Noah Choi — Industrial Machine Vision Software Engineer | Noah Choi \| Industrial Machine Vision Software Engineer | - | - | 줄표 일괄 점검 규칙에 따라 제목의 ` — `를 ` \| `로 바꿨다. 수정 목록(#)에는 없는 항목이다. `og:*` 메타는 이 사이트에 없다. |

### 1차 시점에 수정하지 않고 사용자 확인이 필요했던 것

- 엔지니어링 원칙 6줄 중 4줄(3~6번)은 공학 관용 표현이라 그대로 두었다. 6줄 슬로건 형식 자체가 AI 티로 읽힐 수 있으니 풀어 쓸지는 사용자 결정.
- "장비가 준비되기 전에 개발한다"는 전제가 히어로, About 인용문, Overview 목적 문단, 원칙 1번에서 4번 반복된다.
- 3D Studio 설명에 `recipe`(소문자)와 `Recipe`(대문자)가 섞여 있다. UI 용어면 `Recipe`로 통일하는 쪽이 맞다.
- 영어 캡션은 pass/fail, 한국어와 2D Workbench 설명은 OK/NG를 쓴다.
- 3D Studio의 `compatible files`가 무엇과 호환인지 영어에 없다(한국어 README는 '같은 형식(C3D)').
- 코드 예제 캡션 `A small inspection`이 코드라는 말이 없어 모호하다.
- 변경 이력 영어 문장 형식(명령형/과거형/명사구)과 `harden`, `Bound`, `terminal results` 같은 내부 용어는 저장소 CHANGELOG 문구와 맞춰 두었다.
- 한국어 모드에서 한국어 원문이 없는 영어 문구가 224곳이다(주로 RBV, 최신 변경 요약, 기술 카드, 타임라인).
- 같은 문구가 사용자의 GitHub README에도 있다. 사이트만 고치면 README와 문구가 달라진다. README까지 고칠지는 사용자 결정(공개 저장소 변경이라 별도 승인 필요).

## 2차 수정 (평가 8명 반영)

평가자 8명(시니어 머신비전 엔지니어, 장비 업체 개발팀장, 리크루터, C#/.NET 오픈소스 사용자, 모션 디자이너, 한국어 편집자, 영어 편집자, 공개 리스크 검토자)이 공통으로 지적한 항목(A~I)만 고쳤다. 새 사실·수치·경험을 만들지 않았다. 사이트의 모든 문장은 README 문장 그대로이거나, 사용자가 문구를 지정한 것(A2, B, E1)이거나, 한국어 번역(`data-ko-src="tr"`)이다.
`index.html`, `css/style.css`에 반영했고 `js/main.js`는 바꾸지 않았다. 영어를 바꾼 요소에는 `data-ed`를 붙였다. 영어를 바꾸지 않은 행은 '영어 후'를 `-`로 두었고, 한국어가 영어 그대로였던 행의 '한국어 전'은 '(번역 없음, 영어 그대로 표시)'로 적었다. 삭제한 문장은 '전' 칸에 원문을 그대로 남겼으니 그 문장을 해당 요소에 되돌리면 복구된다.

### 수정한 문구

| # | 위치 | 영어 전 | 영어 후 | 한국어 전 | 한국어 후 | 이유 |
|---|---|---|---|---|---|---|
| A1 | About(셋째 문단) | I am building it to connect virtual equipment, image data, inspection software, reusable algorithms and validation workflows. | (삭제) | 가상 장비, 이미지 데이터, 검사 소프트웨어, 재사용 가능한 알고리즘, 검증 워크플로를 연결하기 위해 만들고 있습니다. | (삭제) | Overview 다이어그램이 같은 내용을 보여 주고, About 인용문과 Overview 목적 문단과도 겹친다는 평가 공통 지적. 문단 전체를 지워 문장 사이 공백·구두점은 그대로다. |
| A2 | About(인용문) | When software development starts only after the machine and samples are ready, validation risk is concentrated near the end of the schedule. | If software development only starts once the machine and samples are ready, validation and its risk end up at the end of the schedule. | 소프트웨어 개발이 장비와 샘플이 준비된 뒤에야 시작되면, 검증 위험이 일정 막바지에 집중됩니다. | 장비와 샘플이 준비된 뒤에야 소프트웨어 개발을 시작하면, 검증과 그 위험이 일정 막바지에 몰립니다. | 사용자 지정 문구(`data-ed`, 한국어 `tr`). 형광펜 구간은 `validation and its risk end up at the end of the schedule` / `검증과 그 위험이 일정 막바지에 몰립니다`. |
| B | Overview(목적 문단) | OpenVisionLab does not replace real equipment validation. Its purpose is to move architecture, sequence, inspection, failure-mode and integration verification earlier, so physical-machine time can be used for work that requires hardware, optics and production samples. | OpenVisionLab does not replace testing on the real machine. It lets you check architecture, sequence, inspection, failure modes and integration before the machine arrives, so time on the real machine goes to work that needs hardware, optics and production samples. | OpenVisionLab은 실제 장비 검증을 대체하지 않습니다. 목적은 아키텍처, 시퀀스, 검사, 고장 모드, 통합 검증을 앞당기는 것입니다. 그래서 실제 장비 시간은 하드웨어, 광학계, 양산 샘플이 필요한 일에 쓸 수 있습니다. | OpenVisionLab은 실제 장비 시험을 대체하지 않습니다. 아키텍처, 시퀀스, 검사, 고장 모드, 통합을 장비가 들어오기 전에 확인할 수 있게 해서, 실제 장비 시간은 하드웨어, 광학계, 양산 샘플이 필요한 일에 쓸 수 있게 합니다. | 사용자 지정 문구(`data-ed`, 한국어 `tr`). 강조(`strong`) 구간은 `architecture, sequence, inspection, failure modes and integration` / `아키텍처, 시퀀스, 검사, 고장 모드, 통합`. 마크업은 span 3조각(강조 span 포함) 그대로다. |
| C1-1 | Engineering Principles(1번 줄) | Build before the machine is ready. | Loading a Recipe restores its settings without running the inspection. | 장비가 준비되기 전에 만든다. | Recipe를 불러올 때는 검사 실행 없이 설정만 복원합니다. | README_OpenVisionLab.md / README_ko_OpenVisionLab.md 문장 그대로. 슬로건 6줄을 README 문장 6개로 교체. `data-ed`·`data-ko-src` 없음(말뭉치 검사 통과). |
| C1-2 | Engineering Principles(2번 줄) | Validate against explicit criteria. | Saving and running are separate actions. | 명시한 기준으로 검증한다. | 저장과 실행은 별도 동작입니다. | README_OpenVisionLab.md / README_ko_OpenVisionLab.md 문장 그대로. 슬로건 6줄을 README 문장 6개로 교체. `data-ed`·`data-ko-src` 없음(말뭉치 검사 통과). |
| C1-3 | Engineering Principles(3번 줄) | Keep state deterministic. | Loading a project, selecting a device or browsing results does not run the machine. | 상태를 결정론적으로 유지한다. | 프로젝트 열기, 장치 선택, 결과 탐색만으로 장비가 실행되지는 않습니다. | README_OpenVisionLab-Machine-Studio.md / README_ko_OpenVisionLab-Machine-Studio.md 문장 그대로. 슬로건 6줄을 README 문장 6개로 교체. `data-ed`·`data-ko-src` 없음(말뭉치 검사 통과). |
| C1-4 | Engineering Principles(4번 줄) | Fail safely. | Execution errors are reported separately from NG. | 안전하게 실패한다. | 실행 오류는 NG와 구분합니다. | README_OpenVisionLab.md / README_ko_OpenVisionLab.md 문장 그대로. 슬로건 6줄을 README 문장 6개로 교체. `data-ed`·`data-ko-src` 없음(말뭉치 검사 통과). |
| C1-5 | Engineering Principles(5번 줄) | Preserve evidence. | After input or parameter changes, retained results are marked as previous results; run again to update them. | 근거를 보존한다. | 입력이나 파라미터가 바뀌면 보관된 결과는 이전 결과로 표시합니다. 현재 설정의 결과를 보려면 다시 실행합니다. | README_OpenVisionLab.md 문장 그대로. 한국어는 README_ko_OpenVisionLab.md의 대응 두 문장을 이어 붙였다(영어는 세미콜론 한 문장). 슬로건 6줄을 README 문장 6개로 교체. `data-ed`·`data-ko-src` 없음(말뭉치 검사 통과). |
| C1-6 | Engineering Principles(6번 줄) | Make problems reproducible. | AI results are candidates for review. | 문제를 재현 가능하게 만든다. | AI 결과는 검토할 후보입니다. | README_OpenVisionLab-Labeling-Studio.md / README_ko_OpenVisionLab-Labeling-Studio.md 문장 그대로. 슬로건 6줄을 README 문장 6개로 교체. `data-ed`·`data-ko-src` 없음(말뭉치 검사 통과). |
| C2 | Engineering Principles(글꼴·대비) | - | - | - | - | `.pr li` 글자를 `clamp(1.3rem, min(3.1vw, vh*.05), 2.7rem)`(모바일 `clamp(1.3rem, 5.8vw, 2.1rem)`), 굵기 700, 줄 간격 1.25로 줄여 1440·1366·1024·390에서 잘림 없음. 비활성 줄 불투명도 하한 .16을 .5로 올려 대비 검정 배경 4.72:1, 흰 배경 3.47:1(이전 약 1.5:1). |
| C3-1 | Engineering Principles 아래 본문(첫 문단) | I would rather improve stability, traceability, recovery and reproducibility than add complexity just for novelty. | (삭제) | 저는 단지 새로움을 위해 복잡도를 더하기보다 안정성, 추적성, 복구, 재현성을 높이는 쪽을 선호합니다. | (삭제) | 요청에 따라 삭제. 구간 부제(Engineering Principles)는 유지. 복구하려면 원문을 `<div class="wrap pr-copy" data-stagger>` 안 `<p class="reveal">`에 되돌리고 `.pr-copy` CSS를 복원한다. |
| C3-2 | Engineering Principles 아래 본문(둘째 문단) | For machine-vision software, an algorithm producing the right result once is not enough. The complete system must acquire the right image, run the right inspection at the right time, preserve the result, recover from failure, and provide enough evidence to explain what happened later. | (삭제) | 머신비전 소프트웨어에서는 알고리즘이 한 번 올바른 결과를 내는 것만으로는 충분하지 않습니다. 시스템 전체가 올바른 이미지를 획득하고, 올바른 시점에 올바른 검사를 실행하며, 결과를 보존하고, 실패에서 복구하고, 나중에 무슨 일이 있었는지 설명할 근거를 충분히 제공해야 합니다. | (삭제) | 요청에 따라 삭제. `.pr-copy` CSS 3줄은 쓰는 곳이 없어져 함께 지웠다. |
| D | Releases > Latest(3D Studio 카드) | Adds an optional reference-surface RMS limit to Thickness, bulk expected results and named failure causes in Validation, and faster workspace tab switching. Reports validation with no expected decisions separately from matched results, clarifies Tool Lab displays, and uses neutral gray surfaces with plainer wording. | Adds an optional reference-surface RMS limit to Thickness, bulk expected results and named failure causes in Validation, and faster workspace tab switching. | (번역 없음, 영어 그대로 표시) | Thickness에 선택형 기준면 RMS 한계를 추가하고, Validation에 일괄 기대 결과와 이름 붙은 실패 원인을 더했으며, 작업 영역 탭 전환을 더 빠르게 했습니다. | 두 번째 문장(`Reports validation ... plainer wording.`)이 정보가 없다는 평가 공통 지적으로 삭제. 남은 첫 문장은 README_Noah8218.md 그대로. 한국어는 H3에서 새로 번역(`tr`). |
| E1 | Contact(큰 문구) | If a project saves you time, a star or follow helps other vision developers find it. | Questions about the tools, bug reports, or equipment software work: email is the fastest way to reach me. | 프로젝트가 시간을 아껴 주었다면, 스타나 팔로우가 다른 비전 개발자들이 프로젝트를 찾는 데 도움이 됩니다. | 도구 관련 질문, 버그 제보, 장비 소프트웨어 관련 문의는 이메일이 가장 빠릅니다. | 사용자 지정 UI 문구(`data-ed`, 한국어 `tr`). `tools/allowed_labels.txt`에 등록. `.big`에 `text-wrap: balance`를 더해 한국어 줄바꿈의 외톨이 낱말을 줄였다. |
| E2 | Contact(버튼 아래 보조 문구) | If a project saves you time, a star or follow helps other vision developers find it. | (문구 그대로, 위치만 이동) | 프로젝트가 시간을 아껴 주었다면, 스타나 팔로우가 다른 비전 개발자들이 프로젝트를 찾는 데 도움이 됩니다. | (문구 그대로, 위치만 이동) | 큰 문구에서 이메일 주소 아래의 작은 muted 문구(`.aside`, .9rem)로 옮겼다. 삭제하지 않았다. |
| F0 | 프로젝트 6행(라벨) | - | Get it | - | 받는 법 | 칩 줄 아래의 한 줄 라벨. `tools/allowed_labels.txt`에 등록, 한국어는 `tr`. |
| F1 | 프로젝트 > 2D Workbench(Get it 줄) | - | Download the win-x64 ZIP from Releases. It requires the .NET 8 Desktop Runtime (x64). The published ZIP is v2.1.0-rc.3; it predates the source workflow shown here. | - | Releases에서 win-x64 ZIP을 받습니다. .NET 8 Desktop Runtime (x64)가 필요합니다. 공개 ZIP은 v2.1.0-rc.3이며, 이 문서에서 보여 주는 소스의 작업 흐름보다 이전 버전입니다. | README_OpenVisionLab.md 'Try it in 3 steps' 1번과 그 아래 문단 / README_ko_OpenVisionLab.md 같은 위치. 문장 그대로. 3문장이라 '1~2문장' 지침보다 길지만 필수 문장 때문이다. |
| F2 | 프로젝트 > Labeling Studio(Get it 줄) | - | Windows 10/11 x64; .NET 8 and WPF; one local operator. Windows 10/11 x64, .NET SDK 8.0.421, and PowerShell are required. | - | Windows 10/11 x64, .NET 8과 WPF 기반이며, 작업자 한 명이 한 PC에서 쓰는 환경입니다. Windows 10/11 x64, .NET SDK 8.0.421, PowerShell이 필요합니다. | README_OpenVisionLab-Labeling-Studio.md 'Installation and requirements' 첫 항목과 'Build from source' 첫 문장 / README_ko_OpenVisionLab-Labeling-Studio.md. 문장 그대로. 'Windows 10/11 x64'가 두 번 나온다. |
| F3 | 프로젝트 > 3D Studio(Get it 줄) | - | Use Windows 10 build 19041 or later, or Windows 11, on x64, with Git, PowerShell 5.1 or later, and the SDK selected by global.json (10.0.300, latestFeature). If you already have a self-contained Windows package, extract it and run OpenVisionLab.ThreeD.Shell.exe. Its .NET runtime is included. | - | Windows 10 build 19041 이상 또는 Windows 11 x64, Git, PowerShell 5.1 이상과 global.json이 선택하는 SDK(10.0.300, latestFeature)가 필요합니다. 자체 실행형 Windows 패키지가 있다면 압축을 풀고 OpenVisionLab.ThreeD.Shell.exe를 실행합니다. .NET 런타임이 포함되어 있습니다. | README_OpenVisionLab-3D-Studio.md 'Build from source' 첫 문장과 'Try it in 3 steps' 아래 패키지 문단 / README_ko_OpenVisionLab-3D-Studio.md. 문장 그대로. 'Build and run the Shell.'(링크 문구)은 빼고 같은 내용을 담은 빌드 요구 문장을 썼다. README 본문에 '.NET 10' 글자는 없고 SDK 10.0.300(배지는 .NET-10)으로만 나온다. |
| F4 | 프로젝트 > Machine Studio(Get it 줄) | - | Requirements: Windows 10 or later, the .NET 8 SDK, and Git. Visual Studio users can open OpenVisionLab.MachineStudio.sln and select OpenVisionLab.MachineStudio as the startup project. | - | Windows 10 이상, .NET 8 SDK와 Git이 필요합니다. Visual Studio에서는 OpenVisionLab.MachineStudio.sln을 열고 시작 프로젝트를 OpenVisionLab.MachineStudio로 지정합니다. | README_OpenVisionLab-Machine-Studio.md 'Build from source' / README_ko_OpenVisionLab-Machine-Studio.md. 문장 그대로. |
| F5 | 프로젝트 > Vision SDK(Get it 줄) | - | The 3.3.0-rc.2 GitHub prerelease contains six SDK .nupkg files and a SHA-256 list. OpenVisionLab-authored portions use the MIT License, with copyright and attribution preserved as required by NOTICE. Commercial redistribution of Core's bundled OpenCvSharp/OpenCV binaries remains blocked pending distribution/legal-owner approval of the final notice bundle, Intel notice conditions and distribution workflow. | - | 3.3.0-rc.2 GitHub 사전 릴리스에는 SDK .nupkg 6개와 SHA-256 목록이 있습니다. OpenVisionLab이 작성한 부분은 MIT License를 따르며 NOTICE에 따라 필요한 저작권·기여 고지를 보존해야 합니다. Core에 번들된 OpenCvSharp/OpenCV 바이너리의 상업적 재배포는 최종 고지 묶음, Intel 고지 조건과 배포 절차에 대한 배포·법무 책임자의 승인 전까지 차단 상태입니다. | README_OpenVisionLab-Vision-SDK.md 'Package files and offline use'와 'License and redistribution' / README_ko_OpenVisionLab-Vision-SDK.md. 문장 그대로. 세 번째 문장은 README처럼 굵게(`strong`) 둔다. README의 다음 문장('Those files remain rc.2; the rc.3 source update does not replace them ...')은 넣지 않았다. |
| F6 | 프로젝트 > Raw Buffer Visualizer(Get it 줄) | - | Supported extension targets are Visual Studio 2022 17.9+ x64 and stable Visual Studio 2026 18.x. Source version is distinct from the version currently available on Marketplace. | - | 지원하는 확장 대상은 Visual Studio 2022 17.9+ x64와 안정판 Visual Studio 2026 18.x입니다. 소스 버전은 현재 Marketplace에서 받을 수 있는 버전과 별개입니다. | README_RawBufferVisualizer.md 'Supported Workflow' 마지막 문단과 'Source Version' 첫 문단. 영어 문장 그대로. 한국어 README(README_ko_RawBufferVisualizer.md)는 404라 한국어는 `tr`. README에 'Marketplace에서 설치한다'는 문장은 없어 그 부분은 건너뛰고, 가장 가까운 두 번째 문장을 썼다. |
| G | 푸터 위(출처 줄) | - | Image source: VisA (Zou et al., ECCV 2022), CC BY 4.0. | - | 이미지 출처: VisA (Zou et al., ECCV 2022), CC BY 4.0. | README_OpenVisionLab-Labeling-Studio.md 'Results on real PCB images' 마지막 문장 / README_ko_OpenVisionLab-Labeling-Studio.md. `CC BY 4.0`은 README와 같은 `https://github.com/amazon-science/spot-diff`로 링크(`target="_blank" rel="noopener"`). 항상 보이는 푸터에 두었다. 6번째 썸네일의 기존 캡션(`data-for="5"`)은 그대로. |
| H1 | 히어로(인사) | Hello, I'm | - | 안녕하세요, 저는 | 안녕하세요, | 사용자 지정(한국어 모드 정리). `tr` 유지. |
| H2 | 한국어 모드(자간) | - | - | - | - | `html[lang=ko]`에서만 `.cue`, `.ttl.sm`, `.sub`, `.road dt`, `.get .gl`의 `letter-spacing`을 0으로 덮어썼다(원래 .14em·.1em). 한국어 캡처로 확인. 영문 모드는 그대로. |
| H3-1 | Skills > 머신비전 | 2D: Edge, Blob, Contour, Pattern Matching, Line Gauge and measurement | - | (번역 없음, 영어 그대로 표시) | 2D: Edge, Blob, Contour, Pattern Matching, Line Gauge, 측정 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. 알고리즘 이름은 영어 그대로. |
| H3-2 | Skills > 머신비전 | 3D: Height Map, Full XYZ, Thickness and Warpage | - | (번역 없음, 영어 그대로 표시) | 3D: 높이 맵, 전체 XYZ, Thickness, Warpage | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. 사이트의 기존 한국어(높이 맵 / 전체 XYZ)와 맞춤. Thickness·Warpage는 측정 도구 이름. |
| H3-3 | Skills > 머신비전 | Image coordinate conversion, defect merging and inspection-result processing | - | (번역 없음, 영어 그대로 표시) | 이미지 좌표 변환, 결함 병합, 검사 결과 처리 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-4 | Skills > 머신비전 | Area Scan and Line Scan camera workflows | - | (번역 없음, 영어 그대로 표시) | Area Scan, Line Scan 카메라 워크플로 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. '워크플로'는 사이트의 기존 한국어 표기. |
| H3-5 | Skills > 장비 소프트웨어 | Camera, lighting, I/O, sensor, PLC and motion integration | - | (번역 없음, 영어 그대로 표시) | 카메라, 조명, I/O, 센서, PLC, 모션 연동 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. '연동'은 카드 제목 '성능 및 연동'과 맞춤. |
| H3-6 | Skills > 장비 소프트웨어 | Inspection Sequence and Recipe architecture | - | (번역 없음, 영어 그대로 표시) | 검사 시퀀스와 레시피 아키텍처 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. 지시한 용어 기준(레시피). 기존 한국어 README는 `Recipe`를 영어로 쓴다(충돌, 아래 확인 사항). |
| H3-7 | Skills > 장비 소프트웨어 | TOP / BTM independent processing and multi-worker execution | - | (번역 없음, 영어 그대로 표시) | TOP / BTM 독립 처리와 멀티 워커 실행 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-8 | Skills > 장비 소프트웨어 | Timeout, recovery and delayed-callback isolation | - | (번역 없음, 영어 그대로 표시) | 타임아웃, 복구, 지연 콜백 격리 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-9 | Skills > 장비 소프트웨어 | Long-running equipment-state and error-handling design | - | (번역 없음, 영어 그대로 표시) | 장시간 가동 장비의 상태·오류 처리 설계 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-10 | Skills > 성능 및 연동 | C++ DLL / C++/CLI / C# interoperability | - | (번역 없음, 영어 그대로 표시) | C++ DLL / C++/CLI / C# 연동 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-11 | Skills > 성능 및 연동 | Large unmanaged image buffers | - | (번역 없음, 영어 그대로 표시) | 대용량 비관리 이미지 버퍼 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-12 | Skills > 성능 및 연동 | Multi-threaded inspection queues | - | (번역 없음, 영어 그대로 표시) | 멀티스레드 검사 큐 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-13 | Skills > 성능 및 연동 | Rule / AI inspection-module integration | - | (번역 없음, 영어 그대로 표시) | 규칙 기반 / AI 검사 모듈 연동 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-14 | Skills > 성능 및 연동 | Native / managed boundary design | - | (번역 없음, 영어 그대로 표시) | 네이티브 / 관리 코드 경계 설계 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-15 | 프로젝트 > Raw Buffer Visualizer(기능 1) | Open Bitmap, OpenCvSharp Mat, Emgu CV Mat, RawBufferView, RawBufferSnapshot and supported collections through debugger visualizers. | - | (번역 없음, 영어 그대로 표시) | 디버거 시각화 도구로 Bitmap, OpenCvSharp Mat, Emgu CV Mat, RawBufferView, RawBufferSnapshot과 지원되는 컬렉션을 엽니다. | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. README_ko_RawBufferVisualizer_overview.md의 '지원되는 컬렉션', '시각화 도구' 용어를 따랐다. |
| H3-16 | 프로젝트 > Raw Buffer Visualizer(기능 2) | Inspect dimensions, format, stride, byte order, valid bits, pixel values, source/pixel addresses and source lifetime. | - | (번역 없음, 영어 그대로 표시) | 크기, 형식, 스트라이드, 바이트 순서, 유효 비트, 픽셀 값, 소스/픽셀 주소, 소스 수명을 확인합니다. | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. 같은 overview 문서의 용어(스트라이드, 유효 비트, 바이트 순서, 수명). |
| H3-17 | 프로젝트 > Raw Buffer Visualizer(기능 3) | Compare retained images, diagnose buffer interpretation, inspect raw-value histograms and save snapshots. | - | (번역 없음, 영어 그대로 표시) | 보관한 이미지를 비교하고 버퍼 해석을 진단합니다. 원시 값 히스토그램을 확인하고 스냅샷을 저장합니다. | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. 한 문장을 둘로 나눠 연결어미 쉼표를 줄였다. |
| H3-18 | Releases > Latest(Labeling Studio 0.4.4) | Ran the full workflow on real PCB images (VisA PCB4): labels imported, YOLOv8n and YOLO11n trained and compared in the app, and TensorRT engines built with the edge runtime. Label import now keeps the chosen split. | - | (번역 없음, 영어 그대로 표시) | 실제 PCB 이미지(VisA PCB4)로 전체 워크플로를 실행했습니다. 라벨을 가져온 뒤 앱에서 YOLOv8n과 YOLO11n을 학습해 비교했고, 엣지 실행 구성으로 TensorRT 엔진을 만들었습니다. 라벨 가져오기가 이제 고른 분할을 유지합니다. | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. '엣지 실행 구성'은 README_ko_OpenVisionLab-Labeling-Studio.md의 표기, '고른 분할'은 같은 README 0.4.4 항목의 표기. |
| H3-19 | Releases > Latest(2D Workbench 2.2.0-dev.12) | Learn windows follow the selected theme, more editors are localized, and threshold settings stay consistent across text, sliders and saved Recipes. | - | (번역 없음, 영어 그대로 표시) | Learn 창이 선택한 테마를 따르고, 더 많은 편집기를 현지화했으며, 임계값 설정이 텍스트, 슬라이더, 저장한 레시피에서 일관되게 유지됩니다. | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. Learn은 README의 Learn Mode 이름. |
| H3-20 | Releases > Latest(3D Studio 0.8.2-dev) | Adds an optional reference-surface RMS limit to Thickness, bulk expected results and named failure causes in Validation, and faster workspace tab switching. | - | (번역 없음, 영어 그대로 표시) | Thickness에 선택형 기준면 RMS 한계를 추가하고, Validation에 일괄 기대 결과와 이름 붙은 실패 원인을 더했으며, 작업 영역 탭 전환을 더 빠르게 했습니다. | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. 행 D와 같은 문장. 'bulk expected results'와 'named failure causes'는 직역에 가깝다. |
| H3-21 | Releases > 타임라인(RBV 2.2.5) | Nested image discovery, pointer-frame matching and debugger registration package checks | - | (번역 없음, 영어 그대로 표시) | 중첩된 이미지 탐색, 포인터 프레임 매칭, 디버거 등록 패키지 검사 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. 영어가 명사구라 한국어도 명사구로 맞췄다. README_ko_RawBufferVisualizer_overview.md의 2.2.5 항목은 더 긴 별도 설명이라 가져오지 않았다. |
| H3-22 | Releases > 타임라인(RBV 2.2.4) | Inspector state persistence, layout and session recovery, compact readouts and JSON stream capacity | - | (번역 없음, 영어 그대로 표시) | 검사 패널 상태 유지, 레이아웃·세션 복구, 간결한 판독값 표시, JSON 스트림 용량 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. overview의 '검사 패널' 표기. |
| H3-23 | Releases > 타임라인(RBV 2.2.3) | Cleared Preview metadata while preserving the supported installation range | - | (번역 없음, 영어 그대로 표시) | 지원하는 설치 범위를 유지한 채 Preview 메타데이터를 해제했습니다. | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. overview 2.2.3의 '해제', '설치 범위'. |
| H3-24 | Releases > 타임라인(RBV 2.2.2) | Preserved user-selected docking, floating and document-tab placement | - | (번역 없음, 영어 그대로 표시) | 사용자가 선택한 도킹, 부동 창, 문서 탭 위치를 유지했습니다. | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. overview 2.2.2의 '도킹', '부동 창', '문서 탭'. |
| H3-25 | Releases > 타임라인(RBV 2.2.1) | Corrected Classic visualizer loading and package registration checks | - | (번역 없음, 영어 그대로 표시) | Classic 시각화 도구 로딩과 패키지 등록 검사를 수정했습니다. | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-26 | Releases > 타임라인(RBV 2.2.0) | Dialog-free image opening, image-only collection routing and pixel measurement | - | (번역 없음, 영어 그대로 표시) | 대화 상자 없는 이미지 열기, 이미지 전용 컬렉션 라우팅, 픽셀 측정 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-27 | Releases > 타임라인(RBV 2.1.0) | Inspection status, discovery responsiveness, pixel/histogram behavior and safer saves | - | (번역 없음, 영어 그대로 표시) | 검사 상태, 탐색 응답성, 픽셀/히스토그램 동작, 더 안전한 저장 | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다.  |
| H3-28 | Releases > 타임라인(RBV 2.0.7) | Signed Int32 image support; package superseded by 2.0.8 | - | (번역 없음, 영어 그대로 표시) | 부호 있는 Int32 이미지 지원. 이 패키지는 2.0.8이 대체했습니다. | 한국어 모드에서 영어로 남던 본문을 번역(`data-ko-src="tr"`). 영어는 바꾸지 않았다. overview의 '부호 있는 32비트 정수'. |
| I1 | 프로젝트 > 2D Workbench(영상 1, `ovl-tool-settings.mp4`) | - | - | - | - | `<video>`에 `poster="assets/ovl-inspection-stages.webp"`를 더했다. 영상 첫 프레임과 같은 앱 메인 창이고 16:9라서 고른 정지 이미지다(영상 첫 프레임 자체는 아니다). `preload="none"`, `?shot`, reduced-motion 동작은 그대로. |
| I2 | 프로젝트 > 2D Workbench(영상 2, `ovl-preprocessing-chains.mp4`) | - | - | - | - | 같은 `poster="assets/ovl-inspection-stages.webp"`. 4분할 Layer 비교 화면이라 이 영상(전처리 연결)과 가장 가깝다. `ovl-sample-catalog.webp`는 4:3 대화 상자라 영상 화면과 달라 쓰지 않았다. |

건너뛴 번역(한국어 모드에서 영어로 남음): 타임라인 Raw Buffer Visualizer 2.0.9 `Checked live transfer for medium native images, final-row ROI spans and pinned-view stability`와 2.0.8 `Correct debugger payload packaging and bounded incremental inspection`. `final-row ROI spans`, `pinned-view`, `bounded incremental inspection`의 뜻을 확신할 수 없어 번역하지 않았다. 뜻을 알려 주면 번역한다.

### 새로 추가한 문구와 근거

| 문구 | 근거 |
|---|---|
| Get it 줄 6개(프로젝트별 위 표 F1~F6) | 각 행의 README_*.md(영어)와 README_ko_*.md(한국어). 위 표의 '이유' 칸에 절 이름을 적었다. Raw Buffer Visualizer의 한국어만 `tr`(README_ko_RawBufferVisualizer.md가 404) |
| `Get it` / `받는 법` | 라벨(문장 아님). `tools/allowed_labels.txt`에 등록, 한국어 `tr` |
| `Image source: VisA (Zou et al., ECCV 2022), CC BY 4.0.` / `이미지 출처: VisA (Zou et al., ECCV 2022), CC BY 4.0.` | README_OpenVisionLab-Labeling-Studio.md 'Results on real PCB images', README_ko_OpenVisionLab-Labeling-Studio.md '실제 PCB 이미지 결과' |
| Contact 큰 문구 `Questions about the tools, ...` | 사용자 지정(README에 없음). `data-ed`, `tools/allowed_labels.txt` 등록, 한국어 `tr` |
| Engineering Principles 6줄 | README_OpenVisionLab.md(1, 2, 4, 5번), README_OpenVisionLab-Machine-Studio.md(3번), README_OpenVisionLab-Labeling-Studio.md(6번)와 각 README_ko_*.md |
| 한국어 번역 28개(H3) | 영어 원문의 번역(`tr`). 용어는 README_ko_RawBufferVisualizer_overview.md와 다른 README_ko_*.md를 따랐다 |

### 코드를 고친 곳

- `css/style.css`: `.pr li` 글자·굵기·줄 간격·불투명도 하한(.5), `.pr li+li` 간격, 모바일 `.pr li` 글자, `.pr-copy` 규칙 3줄 삭제, `.get`·`.get .gl`·`.get strong` 추가, `.aside` 추가, `.big`에 `text-wrap:balance`, `.foot` 보조 규칙(`p+p`, `a`), `html[lang=ko]` 자간 0 덮어쓰기 1줄.
- `js/main.js`: 바꾸지 않았다(SHA-256 동일).
- `index.html`의 `<video>` 두 개에 `poster` 속성만 더했다.

### 사용자가 정해야 하는 것

- 경력 블록과 이력서 링크를 추가할지(평가자 4명이 첫째로 지적했다).
- 와셔, 기포 필름, HDD 기판 이미지가 직접 만든 것인지 공개 데이터인지 확인(출처가 화면에 없다).
- 업무와의 관계(비밀유지·겸업·직무발명 규정)를 확인했는지, 그 결과를 사이트에 표기할지(사용자 개인 확인 사항, 이 저장소에는 상세를 쓰지 않는다).
- `Usable` 칩의 정의(어떤 상태를 뜻하는지).
- Raw Buffer Visualizer의 MIT 표기와 GitHub의 라이선스 판정 불일치(NOASSERTION), LICENSE 파일 확인.
- Labeling Studio의 YOLO 계열 라이선스 안내를 넣을지.
- 'Releases' 제목과 GitHub Releases 미게시의 불일치.
- 영상과 GIF의 일시정지 수단.
- Overview를 Projects 앞으로 옮길지.
- 스크린샷 확대(lightbox) 기능을 넣을지.
- `Recipe`/`recipe` 표기, pass/fail과 OK/NG 용어.
- 툴/도구 용어 통일.
- 타임라인 문장 형식(명령형/과거형/명사구).
- Star·팔로워 수치가 2026-11-27 고정값인 점.

작업 중 확인한 추가 사항(사용자 판단 필요):

- 한국어 용어 충돌: 지시한 번역 기준은 `Recipe`를 `레시피`로 쓰지만, README_ko_OpenVisionLab.md와 사이트의 기존 한국어(2D Workbench 설명, 원칙 1번 `Recipe를 불러올 때는...`)는 `Recipe`를 영어로 쓴다. 새 번역(Skills, Latest)만 `레시피`로 썼고, README 문장 그대로인 곳은 `Recipe`로 남아 한 화면에 섞인다. `Tool`(2D의 기존 `툴`)과 `도구`도 같은 상태다.
- Raw Buffer Visualizer Get it: README에 'Marketplace에서 설치한다'는 문장이 없어 그 부분은 건너뛰었다. 대신 'Source version is distinct from the version currently available on Marketplace.'를 썼다. 필요 없으면 이 문장만 지우면 된다.
- 3D Studio Get it: README 본문에는 `.NET 10`이라는 글자가 없고 SDK `10.0.300`(배지는 .NET-10)만 있어 그 문장을 그대로 썼다.
- Vision SDK Get it: rc.2 사전 릴리스 문장 바로 뒤의 'Those files remain rc.2; the rc.3 source update does not replace them or announce a new package publication.'는 넣지 않았다. 소스 버전 rc.3 칩과 함께 보면 혼동할 수 있어 넣을지 결정이 필요하다.
- Labeling Studio Get it: README의 'There is no installer, code-signing package, or completed clean-PC install/upgrade/uninstall validation.'(Known Limitations)는 넣지 않았다. 받는 방법과 직접 관련된 한계 문장이라 넣을지 결정이 필요하다.
- Get it 줄에서 `Releases` 같은 낱말은 링크로 만들지 않았다(언어 전환이 요소 전체 텍스트를 바꾸는 구조라 링크를 넣으면 한국어 전환에서 사라진다). 아래의 저장소 버튼이 링크다.
- Get it 줄이 'Windows 10/11 x64'를 두 번 말하는 곳(Labeling Studio)이 있고, 2D Workbench와 Vision SDK, 3D Studio는 문장이 길다. 지침의 '1~2문장'을 넘지만 필수 문장 때문이다.


## 한국어 번역 검토 목록 (사용자 검토 필요)

사이트의 한국어 전환(KO)에서 **README에 한국어 원문이 없어서 AI가 번역한 문장**(`data-ko-src="tr"`)이다. **사용자 검토가 필요하다.** 공개 전에 어색하거나 틀린 곳을 고친다. 수정은 `index.html`의 해당 요소 `data-ko="..."` 값을 바꾸면 된다(번역 문장이 바뀌면 `data-ko-src`는 `tr`이 아니라 `ed`나 표시 없음으로 정리한다. [03-site-architecture.md](03-site-architecture.md)의 속성 표 참고). README 한국어 원문을 그대로 쓴 문장은 이 목록에 없다.

2차 수정에서 번역을 추가해 1차 목록(73건)보다 늘었다. 같은 개념이 `Recipe`(README 한국어 원문)와 `레시피`(새 번역)로 섞여 있으니 통일 여부를 정해야 한다(아래 용어 불일치 절).

중복 제외 94건 (사이트 안 번역 요소는 총 117개)

| # | 영어 | 한국어 |
|---|---|---|
| 1 | Skip to content | 본문으로 건너뛰기 |
| 2 | About | 소개 |
| 3 | Projects | 프로젝트 |
| 4 | Overview | 구성도 |
| 5 | Skills | 기술 |
| 6 | Releases | 릴리스 |
| 7 | Contact | 연락처 |
| 8 | Hello, I'm | 안녕하세요, |
| 9 | Industrial Machine Vision Software Engineer | 산업용 머신비전 소프트웨어 엔지니어 |
| 10 | Building open-source tools for machine-vision development before the physical machine is ready. | 실물 장비가 준비되기 전에 머신비전 개발을 위한 오픈소스 도구를 만듭니다. |
| 11 | OpenVisionLab: open-source C#/.NET tools for 2D/3D inspection, labeling, and debugging. | OpenVisionLab: 2D/3D 검사, 라벨링, 디버깅용 오픈소스 C#/.NET 도구. |
| 12 | Email | 이메일 |
| 13 | Scroll | 스크롤 |
| 14 | If software development only starts once the machine and samples are ready, | 장비와 샘플이 준비된 뒤에야 소프트웨어 개발을 시작하면, |
| 15 | validation and its risk end up at the end of the schedule | 검증과 그 위험이 일정 막바지에 몰립니다 |
| 16 | I am an industrial machine-vision software engineer with 8 years of experience across 20+ equipment projects in semiconductor, display, battery, and automotive manufacturing. | 저는 반도체, 디스플레이, 배터리, 자동차 제조 분야에서 20개 이상의 장비 프로젝트를 8년간 수행한 산업용 머신비전 소프트웨어 엔지니어입니다. |
| 17 | OpenVisionLab is my personal open-source R&D project for C# machine-vision developers. | OpenVisionLab은 C# 머신비전 개발자를 위한 제 개인 오픈소스 R&D 프로젝트입니다. |
| 18 | years of experience | 년 경력 |
| 19 | equipment projects | 장비 프로젝트 |
| 20 | open-source projects | 오픈소스 프로젝트 |
| 21 | GitHub stars | GitHub 스타 |
| 22 | followers | 팔로워 |
| 23 | as of | 기준일 |
| 24 | GitHub stars as of | GitHub 스타 기준일 |
| 25 | Usable | 사용 가능 |
| 26 | Source version | 소스 버전 |
| 27 | Get it | 받는 법 |
| 28 | Repository | 저장소 |
| 29 | Version | 버전 |
| 30 | Active development | 개발 중 |
| 31 | Template-matching results | 템플릿 매칭 결과 |
| 32 | Source available | 소스 공개 |
| 33 | Open Bitmap, OpenCvSharp Mat, Emgu CV Mat, RawBufferView, RawBufferSnapshot and supported collections through debugger visualizers. | 디버거 시각화 도구로 Bitmap, OpenCvSharp Mat, Emgu CV Mat, RawBufferView, RawBufferSnapshot과 지원되는 컬렉션을 엽니다. |
| 34 | Inspect dimensions, format, stride, byte order, valid bits, pixel values, source/pixel addresses and source lifetime. | 크기, 형식, 스트라이드, 바이트 순서, 유효 비트, 픽셀 값, 소스/픽셀 주소, 소스 수명을 확인합니다. |
| 35 | Compare retained images, diagnose buffer interpretation, inspect raw-value histograms and save snapshots. | 보관한 이미지를 비교하고 버퍼 해석을 진단합니다. 원시 값 히스토그램을 확인하고 스냅샷을 저장합니다. |
| 36 | Source version is distinct from the version currently available on Marketplace. | 소스 버전은 현재 Marketplace에서 받을 수 있는 버전과 별개입니다. |
| 37 | Supported extension targets are Visual Studio 2022 17.9+ x64 and stable Visual Studio 2026 18.x. | 지원하는 확장 대상은 Visual Studio 2022 17.9+ x64와 안정판 Visual Studio 2026 18.x입니다. |
| 38 | OpenVisionLab Direction | OpenVisionLab 방향 |
| 39 | Equipment concept | 장비 개념 |
| 40 | and process design | 및 공정 설계 |
| 41 | Sequence, axis, I/O, fault | 시퀀스, 축, I/O, 고장 |
| 42 | Virtual camera | 가상 카메라 |
| 43 | and image inputs | 및 이미지 입력 |
| 44 | Shared inspection algorithms | 공통 검사 알고리즘 |
| 45 | Data, training, inference | 데이터, 학습, 추론 |
| 46 | Inspection results | 검사 결과 |
| 47 | and metrics | 및 지표 |
| 48 | Machine sequence | 장비 시퀀스 |
| 49 | decision and replay | 판정 및 재생 |
| 50 | Solid arrows show available workflows or SDK reuse. | 실선 화살표는 사용 가능한 워크플로나 SDK 재사용을 나타냅니다. |
| 51 | Dashed arrows mark direct cross-project integration still in development. | 점선 화살표는 아직 개발 중인 프로젝트 간 직접 연동을 나타냅니다. |
| 52 | before the machine arrives, so time on the real machine goes to work that needs hardware, optics and production samples. | 을 장비가 들어오기 전에 확인할 수 있게 해서, 실제 장비 시간은 하드웨어, 광학계, 양산 샘플이 필요한 일에 쓸 수 있게 합니다. |
| 53 | OpenVisionLab does not replace testing on the real machine. It lets you check | OpenVisionLab은 실제 장비 시험을 대체하지 않습니다. |
| 54 | architecture, sequence, inspection, failure modes and integration | 아키텍처, 시퀀스, 검사, 고장 모드, 통합 |
| 55 | Experience Behind the Projects | 프로젝트의 바탕이 된 경험 |
| 56 | Machine Vision | 머신비전 |
| 57 | 2D: Edge, Blob, Contour, Pattern Matching, Line Gauge and measurement | 2D: Edge, Blob, Contour, Pattern Matching, Line Gauge, 측정 |
| 58 | 3D: Height Map, Full XYZ, Thickness and Warpage | 3D: 높이 맵, 전체 XYZ, Thickness, Warpage |
| 59 | Area Scan and Line Scan camera workflows | Area Scan, Line Scan 카메라 워크플로 |
| 60 | Image coordinate conversion, defect merging and inspection-result processing | 이미지 좌표 변환, 결함 병합, 검사 결과 처리 |
| 61 | Equipment Software | 장비 소프트웨어 |
| 62 | Camera, lighting, I/O, sensor, PLC and motion integration | 카메라, 조명, I/O, 센서, PLC, 모션 연동 |
| 63 | Inspection Sequence and Recipe architecture | 검사 시퀀스와 레시피 아키텍처 |
| 64 | Long-running equipment-state and error-handling design | 장시간 가동 장비의 상태·오류 처리 설계 |
| 65 | TOP / BTM independent processing and multi-worker execution | TOP / BTM 독립 처리와 멀티 워커 실행 |
| 66 | Timeout, recovery and delayed-callback isolation | 타임아웃, 복구, 지연 콜백 격리 |
| 67 | Performance & Interop | 성능 및 연동 |
| 68 | C++ DLL / C++/CLI / C# interoperability | C++ DLL / C++/CLI / C# 연동 |
| 69 | Large unmanaged image buffers | 대용량 비관리 이미지 버퍼 |
| 70 | Multi-threaded inspection queues | 멀티스레드 검사 큐 |
| 71 | Native / managed boundary design | 네이티브 / 관리 코드 경계 설계 |
| 72 | Rule / AI inspection-module integration | 규칙 기반 / AI 검사 모듈 연동 |
| 73 | Desktop & Tooling | 데스크톱 및 도구 |
| 74 | Technologies | 사용 기술 |
| 75 | Engineering Principles | 엔지니어링 원칙 |
| 76 | Latest | 최신 |
| 77 | Ran the full workflow on real PCB images (VisA PCB4): labels imported, YOLOv8n and YOLO11n trained and compared in the app, and TensorRT engines built with the edge runtime. Label import now keeps the chosen split. | 실제 PCB 이미지(VisA PCB4)로 전체 워크플로를 실행했습니다. 라벨을 가져온 뒤 앱에서 YOLOv8n과 YOLO11n을 학습해 비교했고, 엣지 실행 구성으로 TensorRT 엔진을 만들었습니다. 라벨 가져오기가 이제 고른 분할을 유지합니다. |
| 78 | Learn windows follow the selected theme, more editors are localized, and threshold settings stay consistent across text, sliders and saved Recipes. | Learn 창이 선택한 테마를 따르고, 더 많은 편집기를 현지화했으며, 임계값 설정이 텍스트, 슬라이더, 저장한 레시피에서 일관되게 유지됩니다. |
| 79 | Adds an optional reference-surface RMS limit to Thickness, bulk expected results and named failure causes in Validation, and faster workspace tab switching. | Thickness에 선택형 기준면 RMS 한계를 추가하고, Validation에 일괄 기대 결과와 이름 붙은 실패 원인을 더했으며, 작업 영역 탭 전환을 더 빠르게 했습니다. |
| 80 | Nested image discovery, pointer-frame matching and debugger registration package checks | 중첩된 이미지 탐색, 포인터 프레임 매칭, 디버거 등록 패키지 검사 |
| 81 | Inspector state persistence, layout and session recovery, compact readouts and JSON stream capacity | 검사 패널 상태 유지, 레이아웃·세션 복구, 간결한 판독값 표시, JSON 스트림 용량 |
| 82 | Cleared Preview metadata while preserving the supported installation range | 지원하는 설치 범위를 유지한 채 Preview 메타데이터를 해제했습니다. |
| 83 | Preserved user-selected docking, floating and document-tab placement | 사용자가 선택한 도킹, 부동 창, 문서 탭 위치를 유지했습니다. |
| 84 | Corrected Classic visualizer loading and package registration checks | Classic 시각화 도구 로딩과 패키지 등록 검사를 수정했습니다. |
| 85 | Dialog-free image opening, image-only collection routing and pixel measurement | 대화 상자 없는 이미지 열기, 이미지 전용 컬렉션 라우팅, 픽셀 측정 |
| 86 | Inspection status, discovery responsiveness, pixel/histogram behavior and safer saves | 검사 상태, 탐색 응답성, 픽셀/히스토그램 동작, 더 안전한 저장 |
| 87 | Signed Int32 image support; package superseded by 2.0.8 | 부호 있는 Int32 이미지 지원. 이 패키지는 2.0.8이 대체했습니다. |
| 88 | Roadmap | 로드맵 |
| 89 | Connect Machine Studio acquisition to 2D, 3D and Labeling inspection workflows. | Machine Studio의 영상 획득을 2D, 3D, Labeling 검사 워크플로에 연결합니다. |
| 90 | Next | 다음 |
| 91 | Generative AI-based validation image data. | 생성형 AI 기반 검증 이미지 데이터. |
| 92 | Planned | 계획 |
| 93 | Questions about the tools, bug reports, or equipment software work: email is the fastest way to reach me. | 도구 관련 질문, 버그 제보, 장비 소프트웨어 관련 문의는 이메일이 가장 빠릅니다. |
| 94 | If a project saves you time, a star or follow helps other vision developers find it. | 프로젝트가 시간을 아껴 주었다면, 스타나 팔로우가 다른 비전 개발자들이 프로젝트를 찾는 데 도움이 됩니다. |
| 95 | Principles | 원칙 |

> 95번은 이 기록을 쓰는 동안 내비에 Principles 링크가 추가되며 생긴 번역이다(`data-ko-src="tr"`). 위 94건은 그 전 목록이고, `tools/check_site.py`는 작성 말미 코드에서 번역 요소 118개를 센다(중복 제외 후 95건).


## 사용자 확인이 필요한 용어 불일치

점검 중 확인했지만 사용자 판단 없이 바꾸지 않은 것이다. 질문 문장은 [08-backlog.md](08-backlog.md) B 구역에 있다.

| 항목 | 현재 상태 | 원인 | 선택지 |
|---|---|---|---|
| `Recipe` / `recipe` / `레시피` | 영어: 2D는 `Recipe`, 3D 설명·캡션은 `recipe`, 3D 기능은 `Recipe`. 한국어: README 문장은 `Recipe`, 새 번역(Skills, Latest)은 `레시피` | 공개 README 한국어판이 저장소마다 다른 용어를 쓴다(2D는 `Recipe`, 3D는 `레시피`) | UI 라벨이 `Recipe`이면 영어·한국어 모두 `Recipe`로 통일. 앱 화면의 실제 라벨은 **미확인** |
| `툴` / `도구` / `Tool` | 2D 설명 `툴`, 3D·Labeling·SDK `도구`, SDK 2D 불릿 `Tool` | 저장소별 README 용어 차이 | `도구`로 통일하되 UI 이름 `Tool`은 영어 유지 |
| pass/fail ↔ OK/NG | 영어 3D 캡션은 pass/fail, 한국어 캡션과 2D 설명은 OK/NG | README 문장 차이 | 영어도 OK/NG로 통일할지(README 원문은 그대로 두는 쪽이 출처 규칙에 맞음) |
| 영상 / 이미지 / 획득·수집·촬영 | 2D·Machine Studio `영상`, Labeling·히어로·구성도 `이미지`, 획득(Machine Studio)·수집(SDK)·촬영(타임아웃 문장) | 저장소별 README 용어 차이 | 한 벌로 통일 |
| 장비 / 설비 | SDK `설비 판정`, 나머지 `장비` | README 원문 | 통일 여부 |
| `Version` / `Source version` | 칩 라벨이 섞여 있고 차이를 설명하지 않는다. `v` 접두사도 일관되지 않다 | 소스 버전과 게시본 버전이 다른 저장소가 있다 | 라벨 정의를 정하거나 한 가지로 통일 |
| `Usable` 칩 | 정의가 없다. 2D Workbench는 게시된 ZIP이 소스 워크플로보다 오래돼도 `Usable` | 칩 분류가 상태·배포 형태·개발 단계·채널로 섞임 | 정의를 쓰거나 칩을 받는 방식(`ZIP + source` 등)으로 교체 |
| `Source available` + `MIT` | 한 줄에 같이 있어 오픈소스 표기와 충돌해 보인다 | 칩 문구 | 문구 교체 |
| `Releases` 제목 | GitHub Releases가 비어 있는데 섹션 제목은 Releases | 항목이 README·CHANGELOG의 소스 버전 기록 | 제목을 바꾸거나 GitHub Releases를 게시 |
| `Learn windows`, `edge runtime`, `compatible files` | 사이트 안에 정의가 없다 | README 용어를 줄임 | 정의 추가 또는 풀어 쓰기 |
| 변경 이력 문장 형식 | 명령형 / 과거형 / 명사구가 섞임. `harden`, `Bound`, `terminal results` 같은 내부 용어 | 저장소 CHANGELOG 문구와 맞춰 둠 | 형식 통일 여부(CHANGELOG와 어긋나게 됨) |
| 코드 예제 캡션 `A small inspection` | 코드라는 말이 없다 | README 원문 | 캡션 보강 |
| "장비가 준비되기 전에 개발한다" 반복 | 히어로, About 인용문, Overview 목적 문단에 반복 | 핵심 메시지 | 줄일지 |

## 사용자 README와의 동기화

같은 문구가 사용자의 GitHub README에도 있다. 사이트만 고치면 README와 문구가 달라진다. README까지 고칠지는 사용자 결정이며, 공개 저장소 변경이라 별도 승인이 필요하다.

## 검사 도구

문구를 바꾼 뒤에는 `python tools/check_site.py`로 출처 말뭉치 대조와 금지어를 확인한다(사용법은 [AGENTS.md](../AGENTS.md)의 검증 절).
