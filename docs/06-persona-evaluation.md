# 입장별 평가 결과 (AI 평가자 8명)

> **한계를 먼저 밝힌다.**
>
> - 평가자 8명은 모두 **AI 에이전트**다. 서로 다른 입장(시니어 머신비전 엔지니어, 장비 업체 개발팀장, 비기술 리크루터, C#/.NET 오픈소스 사용자, 프론트엔드·모션 디자이너, 한국어 윤문 편집자, 영어 기술문서 편집자, 공개 리스크 검토자)을 맡겨 사이트의 영어·한국어·라이트·모바일 캡처와 소스를 보게 했다. **실제 사람의 의견을 대신하지 않는다.**
> - **평가자에게는 "AI 티 수정을 이미 했다"는 사실을 알려 주지 않았다.** 그래서 지적 중 일부(예: 문구의 AI 티, 번역 미완성 영어 잔존)는 평가 당시 상태 기준이며, 이후 2차 수정이 일부를 반영했다([07-copy-audit.md](07-copy-audit.md)).
> - 점수는 1~10(10이 최고). 평가 대상은 2026-11-27 시점(2차 문구 수정 직후, 다크 기본)의 사이트이고 캡처는 Edge(Chromium) 헤드리스로 만들었다. 캡처 파일은 제3자 자료가 섞일 수 있어 저장소에 싣지 않았고, 원문의 캡처 파일명은 "스크린샷 캡처"로 바꿨다.
> - 본문의 `index.html:525-531`, `main.js:161` 같은 줄 번호는 평가 시점 파일 기준이다. 지금과 어긋나므로 선택자·함수 이름으로 찾는다.
> - 평가자 다수가 첫째로 지적한 **경력 블록·이력서 링크**는 사용자 결정이 필요한 항목으로 [08-backlog.md](08-backlog.md)에 올라 있다.
> - 8명 모두 행동은 `maybe`(연락·채용·설치를 바로 하지는 않지만 이력서나 저장소를 더 볼 의향)였다.


## 점수

| 입장 | 명확성 | 신뢰도 | 완성도 | 언어 자연스러움 | 종합 | 행동 |
|---|---|---|---|---|---|---|
| 시니어 머신비전 엔지니어 | 6 | 6 | 7 | 5 | 6 | maybe |
| 장비 업체 개발팀장 | 6 | 6 | 8 | 5 | 6 | maybe |
| 비기술 리크루터 | 4 | 6 | 8 | 5 | 5 | maybe |
| C#/.NET 오픈소스 사용자 | 6 | 7 | 7 | 4 | 6 | maybe |
| 프론트엔드·모션 디자이너 | 6 | 8 | 7 | 5 | 6 | maybe |
| 한국어 윤문 편집자 | 6 | 7 | 5 | 5 | 5 | maybe |
| 영어 기술문서 편집자 | 6 | 7 | 6 | 6 | 6 | maybe |
| 공개 리스크 검토자 | 7 | 7 | 8 | 5 | 6 | maybe |
| **평균** | **5.9** | **6.8** | **7.0** | **5.0** | **5.8** | |

8명 모두 행동은 `maybe`(연락·채용·설치를 바로 하지는 않지만 이력서나 저장소를 더 볼 의향)였습니다.

## 시니어 머신비전 엔지니어

**첫인상**: 큰 이름 밑에 'C#/OpenCV 도구를 만들고, 장비가 나오기 전에 시뮬레이터로 먼저 돌려 본다'는 한 줄이 바로 읽혀서 뭘 하는 사람인지는 10초 안에 안다. 그런데 8년·20+ 프로젝트라는 숫자 말고는 현장 이야기가 한 줄도 없다. 어떤 장비였는지, 택타임이 얼마였는지, 본인이 뭘 맡았는지가 없고 데모는 전부 합성 스캔·공개 데이터셋·mock 입력이다. 글은 README를 번역·요약한 티가 나고(원칙 6줄 슬로건, 'explicit', 'evidence', 'validation workflows'), 사실 오류는 못 찾았지만 사람이 쓴 문장이라는 느낌은 약하다.

**행동(maybe)**: Raw Buffer Visualizer는 VS Marketplace에서 5분이면 설치·검증할 수 있고 stride 3840→3920 예시가 실제로 겪어 본 사람의 것이라 설치해 보고 별을 줄 용의가 있다. 연락·면접 제안은 보류한다. 20+ 프로젝트 중 본인이 뭘 책임졌는지 사이트로는 알 수 없고, 6개 프로젝트 전부 실장비·실센서 없이 합성 데이터로 시연되기 때문이다. 이력서나 면접에서 사례가 나오면 만날 의향은 있다. 면접에서 캐묻고 싶은 것: (1) 20+개 중 하나를 골라 카메라·조명·트리거 구성, 택타임 목표와 실측, 본인 담당 모듈. (2) Skills의 'delayed-callback isolation'은 어떤 사고에서 나왔고 어떻게 분리했나(타임아웃 뒤에 늦게 온 결과가 다음 제품에 붙는 문제인가). (3) 라인스캔에서 엔코더 동기와 스티칭 경계의 defect merging은 어떻게 했나. (4) 단면 높이맵으로 척 기준면 대비 웨이퍼 두께를 잴 때 웨이퍼 휨·척 오염·캘리브레이션 불확도를 어떻게 다루나. (5) 시뮬레이터에서 검증한 시퀀스가 실제 PLC 로직과 어떻게 이어지고, 시뮬과 실장비 차이로 놓친 버그가 있었나. (6) 저장소에 AGENTS.md가 있고 릴리스 속도가 빠른데, 코드에서 직접 설계·리뷰한 부분과 AI 도구로 생성한 부분을 어떻게 나누나.

**핵심 지적**

- (high) About / Skills (스크린샷 캡처): 현장 경력의 근거가 이 문장과 Skills 불릿이 전부다. 프로젝트 6개의 데모는 합성 PCB/웨이퍼 스캔(3d-*), 공개 데이터셋 VisA, 생성한 육각형 이미지(lab-anomaly-grid-disk), mock 입력(ms-capture-and-inspection.webp의 'Numerical mock input')이고, 실제 카메라·3D 센서·PLC를 붙인 흔적이 없다. Skills의 'Area Scan and Line Scan camera workflows'도 라인스캔을 보여 주는 프로젝트가 없다. 현업자는 '20+'라는 개수가 아니라 사례 하나의 구체성으로 판단하는데 그게 없어서 숫자가 장식으로 읽힌다.
- (high) Projects 02 Labeling Studio (lab-visa-pcb4-test-result.webp 캡션, 스크린샷 캡처): 면책 문장만 있고 숫자가 없다. 공개 README(Labeling Studio)에는 미검 3/40(YOLOv8n), 8/40(YOLO11n), 정상 이미지 오검(과검) 4/402, 1/402, TensorRT FP16 GPU 시간 0.76/0.82 ms(RTX 4070 SUPER, 입력 960 px, confidence 0.25)가 있는데 사이트에는 빠져 있다. 현업자가 제일 먼저 묻는 미검/과검/택타임에 답이 없다. 2D Workbench도 스크린샷에는 62 ms, 242 ms 같은 시간이 찍혀 있는데 본문에는 처리 시간이 한 번도 안 나온다.
- (high) Projects 03 3D Studio (3d-wafer-teach.webp, 3d-pcb-result-ng.webp): (1) 'compatible files'가 무엇인지 EN에는 없다(KO는 '같은 형식(C3D)'). 공개 README 기준으로 레시피 입력은 C3D뿐이고 TIFF/RAW는 일반 import 대상이 아니다. 즉 상용 3D 센서의 실데이터를 쓰려면 C3D로 변환해야 하는데 사이트에는 그 말이 없다. (2) 값의 단위가 안 보인다. 웨이퍼 화면의 '698.83 / 661 – 732'는 µm로 읽히는데 README상 단위는 미보정 'raw-height'이고 합성 스캔이다. (3) 'Thickness'는 양면 두께가 아니라 기준면 대비 높이차다(README: 'it does not measure a paired upper and lower surface'). 웨이퍼 쪽은 Warp/Bow/TTV라고 부르고 'Warpage'는 PCB·패키지 용어라서, 웨이퍼 장비 경험자는 이 값을 웨이퍼 두께로 오해하거나 이름 때문에 신뢰를 깎는다.
- (med) Projects 04 Machine Studio (ms-capture-and-inspection.webp, ms-simulation.webp): 시뮬레이터가 무엇을 하고 안 하는지가 사이트에 없다. 공개 README에는 'The fixed 5 ms tick is simulation time, not a hard real-time scheduling guarantee', 'Real PLC, robot and camera control ... are outside the current supported scope'가 있는데 사이트는 'It is not qualified for production equipment control or safety functions.'만 말한다. 이 문장만 보면 PLC 연결은 되는데 안전 검증이 안 됐을 뿐이라고 읽히고, Skills의 'PLC' 칩과 붙어서 더 그렇다. 캡처 화면(ms-capture-and-inspection.webp)은 검은 바탕에 회색 사각형이고 UI에 'Mock · deterministic model (not a real inspection)'이라고 적혀 있는데 사이트 캡션은 'main image and camera settings'다. 또 'inspect faults'는 의미가 틀린다. 시뮬레이터에서는 고장을 주입(activate/clear)하는 것이다. 마지막으로 여기서 쓴 시퀀스가 설계 검토용인지, 실장비로 내보낼 수 있는지가 안 나와서 현업자는 용도를 못 정한다.
- (med) Projects 칩 (Usable / Source version / MIT) - 스크린샷 캡처, 2D·3D·SDK 행: 'Usable' 칩과 실제 상태가 어긋난다. 2D Workbench는 공개 README 기준 배포 ZIP이 v2.1.0-rc.3이고 스크린샷이 보여 주는 워크플로는 v2.2.0-dev.12 소스 빌드에서만 된다. 3D Studio README에는 'The latest hosted Workbench checks fail in docking/render cleanup ... this snapshot is not fully CI-qualified'와 'Tool selection can still pause the interface'가 있는데 칩은 'Usable'이다. Vision SDK 칩은 'MIT'인데 README에는 'Commercial redistribution of Core's bundled OpenCvSharp/OpenCV binaries remains blocked pending distribution/legal-owner approval'이 있다. 사내 도입을 검토하는 사람은 저장소를 열어 이 문장을 바로 발견하고, 사이트의 나머지 문구도 낮춰 읽게 된다.

**잘한 점**

- Projects 06 Raw Buffer Visualizer (rbv-manual-stride-before.webp, rbv-manual-stride-after.webp): 'known 3920-byte row stride' 예시는 1280×3 = 3840 바이트 행에 80 바이트 패딩이 붙은 BGR24 버퍼를 잘못 해석하면 이미지가 기운다는, 카메라 SDK 버퍼를 직접 다뤄 본 사람만 아는 문제다. 화면에 Stride, Min Stride 3840, padding 80 B/row, Valid bits, Byte order가 그대로 보인다. Marketplace에 올라가 있어서 6개 중 유일하게 내가 5분 안에 직접 검증할 수 있는 결과물이다.
- Skills 중 현장 문장 (스크린샷 캡처): 'TOP / BTM independent processing and multi-worker execution', 'Timeout, recovery and delayed-callback isolation', 'Image coordinate conversion, defect merging'은 양면 검사와 타임아웃 뒤 늦게 도착한 콜백, 타일 경계 불량 병합을 겪은 사람이 쓰는 말이다. 생성형 문장이 만들어 내는 단어가 아니다. 같은 이유로 SDK 설명 'Your application owns acquisition, display, ROI editing, recipe storage and the final equipment decision.'도 최종 판정은 호스트가 한다는 책임 경계를 맞게 잡았다.
- 2D Workbench 화면 (ovl-inspection-stages.webp, ovl-tool-settings.mp4): 4분할 레이어 비교(Original / Binary / Clean / Filtered), 스텝별 ms, 'Final verdict 2/2 judged steps OK', Acceptance의 Lower/Upper 개수 한계와 'Time limit 1000 ms', 'Resolution (mm/px) 0.006', Pattern Matching 점수 93.1/86.2/80.1이 보인다. 레시피 티칭할 때 실제로 쓰는 요소(중간 이미지 비교, 판정 한계, 시간 제한)가 빠짐없이 있어서 장난감 UI가 아니라는 것이 화면으로 전달된다.
- 3D Studio 결과 표 (3d-pcb-result-ng.webp): Value / Allowable range / Margin / Verdict / Cause 열이 있고 NG 이유가 'One or more measured H-axis separations from the fitted reference surface exceed the limits.'처럼 문장으로 나온다. 'Margin'(한계까지 남은 여유)과 Mean/Min/Max 행별 Pass/Fail 분리는 양산 중 경계값 제품을 분석할 때 필요한 정보이고, 그런 표를 만든 사람은 NG 분석을 해 본 사람이다.

**딱 하나 바꾼다면**: About 바로 아래에 '현장 경력' 블록을 하나 넣는다. 장비 분류, 본인 담당, 택타임 같은 실제 수치를 3~4줄로 쓴다(고객명은 가려도 된다). 20+ 프로젝트와 8년이라는 숫자에 근거가 한 번이라도 붙으면 나머지 6개 프로젝트가 '현업 경험에서 나온 도구'로 읽히고, 지금 합성 데이터와 면책 문장만으로 낮아진 신뢰가 가장 크게 회복된다.

## 장비 업체 개발팀장

**첫인상**: 화면은 깔끔하고 이름·직함·C#/.NET 오픈소스까지는 10초 안에 읽힌다. 그런데 어느 회사에서 무슨 장비를 맡았는지는 안 보이고, 오픈소스 메인테이너 소개 같아서 지원자 링크로는 어색하다. 8년/20+ 프로젝트 한 줄 말고는 전부 2026년에 만든 개인 프로젝트와 릴리스 노트라서, 이 링크만으로는 경력을 판단할 수 없다. 글은 구호형 문장과 번역투가 군데군데 있어 사람이 쓴 건지 의심이 든다(아래 ai_sounding 10건).

**행동(maybe)**: 이력서를 열어 보고 30분 전화 면접까지는 부른다. C#/OpenCvSharp, 높이맵 Thickness/Warpage, 버퍼 stride 디버깅은 우리 장비 SW 스택과 맞고, 한계를 스스로 적는 태도가 좋다. 다만 8년 경력의 근거가 이 링크에는 없어서 이 링크만 보고 면접 확정은 하지 않는다. 면접에서 물을 것: (1) 20+ 프로젝트 중 본인이 설계·구현을 맡은 3건의 장비 종류, 카메라/조명/모션/PLC 구성, 택타임, 과검·미검 수치. (2) 'TOP / BTM independent processing'과 'delayed-callback isolation'이 실제로 터진 사례와 재현·수정 과정. (3) C++/CLI 경계에서 대용량 unmanaged 버퍼 수명 문제를 겪은 사례(Raw Buffer Visualizer가 거기서 나왔는지). (4) 실제 PLC 프로토콜, 고객사 셋업·시운전·야간 대응 경험(Machine Studio는 실 PLC·카메라 제어가 범위 밖이라 이 링크로는 확인 불가). (5) 6개 제품과 SDK를 약 6개월에 혼자 낸 방식. AI 도구를 어떻게 썼고, 코드 한 곳을 골라 즉석에서 설명할 수 있는지.

**핵심 지적**

- (high) About (스크린샷 캡처), 통계 카드: 경력을 말하는 유일한 문장인데 회사 유형(장비 제조사/SI/수요기업), 기간, 담당 역할, 대표 장비가 없다. 그 아래는 전부 개인 오픈소스이고, 공개 저장소 메타 기준 6개 중 4개가 2026-05~08에 생성됐다. 그래서 8년은 이 페이지 어디에서도 확인되지 않는다. 4개 업종에서 20건 이상이라 넓게 얕게 했는지, 주 개발자였는지도 구분이 안 된다. 통계 카드도 검증 불가한 8, 20+ 옆에 검증 가능한 41 stars, 90 followers를 같은 크기로 늘어놓아 무게가 뒤집혀 있다.
- (high) Contact (스크린샷 캡처): 내가 연락하려고 내려온 섹션의 가장 큰 글씨가 별·팔로우 요청이다. 이 페이지가 구직용인지 오픈소스 홍보용인지 여기서 갈린다. 근무 지역, 입사 가능 시기, 희망 역할, 이력서 링크가 없고 채널도 개인 네이버 메일 하나다. 히어로에서도 주 버튼이 Email이 아니라 GitHub(teal)이어서 연락 우선순위가 뒤바뀌어 있다.
- (med) Skills (스크린샷 캡처, 칩 목록): 우리 장비와 맞는지 가르는 정보가 전부 빠져 있다. 어떤 카메라(GigE/CoaXPress/CameraLink, 제조사), 프레임 그래버, 조명 컨트롤러, 모션 보드, PLC 모델과 프로토콜인지 없고 칩은 'PLC' 한 단어다. 'TOP / BTM independent processing'은 설명이 없다. 부제 'Experience Behind the Projects'는 증거 없이 목록만 나열한다. 공개 프로젝트(Machine Studio)는 README에서 실제 PLC·로봇·카메라 제어를 지원 범위 밖으로 적고 있어서, 현장 연동 경험을 보여 줄 곳이 사이트에 없다.
- (med) Hero (스크린샷 캡처), Overview (스크린샷 캡처), Roadmap: 히어로와 원칙 1번은 '장비가 준비되기 전에 만든다'를 이미 하는 일처럼 말한다. 그런데 구성도에서 Machine Studio와 2D/3D/Labeling을 잇는 선은 전부 점선(미완)이고 로드맵 Next가 'Connect Machine Studio acquisition to 2D, 3D and Labeling inspection workflows.'다. 핵심 아이디어의 연결부가 아직 없다는 뜻이다. 한계를 적은 건 좋지만 히어로 문장이 현재 되는 것보다 크게 읽힌다. 구성도는 점선이 실선과 교차해 30초 안에 읽기 어렵다.
- (med) Releases (스크린샷 캡처): 16줄 버전 이력은 채용 담당자에게 소음이고, 읽히는 부분은 오히려 감점 요인이다. Raw Buffer Visualizer 2.2.1, 2.2.2, 2.2.3이 모두 2026-10-01이고, 'Corrected Classic visualizer loading and package registration checks', 'package superseded by 2.0.8'이 같이 보인다. Vision SDK는 rc.4/rc.5(10-12), rc.2/rc.3(11-16)이 같은 날 연달아 나온다. 릴리스 위생이 불안하거나 자동 생성처럼 보인다. 'Latest' 카드는 비전 SDK 사용자가 아니면 읽을 수 없다.

**잘한 점**

- Projects > Labeling Studio (스크린샷 캡처, 캡션과 vnote): 'These results come from one dataset with 40 defective test images and are not evidence of production accuracy.'와 'three defects found, one small defect missed' 캡션이다. 놓친 불량 1건을 그대로 보여 준다. 양산 정확도 근거가 아니라고 먼저 선을 긋는 사람의 데이터는 믿고 읽을 수 있다. 이게 이 사이트에서 가장 신뢰가 가는 문장이다.
- Projects > Raw Buffer Visualizer (캡션 rbv-manual-stride-before/after): '잘못된 3,840바이트 스트라이드로 해석한 PCB 스냅샷'과 '3,920바이트를 직접 적용한 같은 스냅샷' 비교다. 라인 스캔·프레임 그래버 버퍼에서 row padding 때문에 이미지가 기울어 보이는 문제를 겪어 본 사람이 아니면 고를 수 없는 예다. 8년이라는 말 없이도 경력이 보이는 유일한 곳이고, Visual Studio Marketplace에 게시돼 있어 검증할 수 있다.
- Projects > 3D Studio 캡션: 'five pass, three fail with the failing value and limit'이다. NG 판정과 함께 실제 값과 한계를 같이 보여 주는 결과 표다. 장비 SW에서 고객 대응이 가능하려면 이게 있어야 한다. 합성 데이터임을 'synthetic'으로 밝히고 'development source snapshot, not a production qualification'이라고 적은 것도 과장이 없다.
- Projects > Vision SDK 불릿: 'Your application owns acquisition, display, ROI editing, recipe storage and the final equipment decision.' SDK와 장비 앱의 책임 경계를 한 줄로 그었다. 라이브러리를 팀에 넘겨 본 사람의 구분이고, 최종 설비 판정을 앱에 남기는 설계도 안전 쪽이다.

**딱 하나 바꾼다면**: About 바로 아래에 실무 경력 블록(기간 · 회사 유형 · 장비/공정 · 내 역할 · 숫자 1개를 3~4줄)과 이력서 PDF 링크를 넣는다. 이게 없으면 이 링크는 지원자 소개가 아니라 개인 오픈소스 소개로 읽힌다.

## 비기술 리크루터

**첫인상**: 폰으로 열었더니 'Noah Choi, Industrial Machine Vision Software Engineer'까지는 바로 읽힌다. 그런데 그 밑 문장이 오픈소스 도구 이야기라서 이 사람이 일자리를 찾는 건지, 도구를 알리려는 건지 모르겠다. 경력 8년·장비 프로젝트 20개 이상이라는 내가 쓸 수 있는 정보는 두 번째 화면까지 내려가야 나오고, 그 뒤부터는 PropertyGrid, Recipe XML, TOP / BTM 같은 말이라 폰에서는 여기서 닫는다. 화면은 깔끔하고 믿음은 가지만, 글은 정돈된 슬로건 같아서 이 사람 목소리로 들리지 않는다.

**행동(maybe)**: 맡고 있는 머신비전/장비 SW 포지션이 있으면 이메일은 한 통 보낸다. 다만 내용은 '이력서(PDF)와 지금 재직·이직 상황, 희망 지역을 보내 달라'가 된다. 사이트만으로는 JD에 맞출 근거(회사별 경력 연도, 직무, 지역, 구직 상태)가 없어 후보 시트에 못 올린다. 포지션이 없으면 링크만 저장하고 닫는다. GitHub 스타·팔로우는 내가 할 일이 아니다.

**핵심 지적**

- (high) Contact 섹션 (스크린샷 캡처): 연락처 섹션의 가장 큰 글씨가 개발자에게 GitHub 스타를 부탁하는 문장이다. GitHub 프로필 README의 마지막 줄을 그대로 옮긴 것으로, 리크루터에게는 '이 페이지는 내게 하는 말이 아니다'라는 신호다. 구직 중인지, 외주를 받는지, 협업 제안을 받는지도 어디에도 없다. 기본 버튼 순서도 Email, GitHub, Visual Studio Marketplace인데, Marketplace는 개발 도구 스토어라 리크루터가 누르면 설치 페이지로 간다.
- (high) 히어로 (스크린샷 캡처): 첫 화면에 이름·직함은 있지만 '경력 몇 년, 어느 산업, 무슨 일을 하는 사람인지'가 없다. 8년/20+ 프로젝트/반도체·디스플레이·배터리·자동차는 About 섹션 본문(작은 글씨)에 있어서 폰에서는 한 화면을 더 내려가야 보인다. 대신 첫 화면은 'OpenVisionLab: open-source C#/.NET tools for 2D/3D inspection, labeling, and debugging.'처럼 개발자용 한 줄로 채워져 있다. 주 버튼(청록)은 GitHub이고 이메일은 보조 버튼이다.
- (high) About / Skills 섹션 (스크린샷 캡처): 8년 경력의 근거가 이 한 문장뿐이다. 회사·재직 기간·직책·지역·학력이 없고, 사이트 전체가 '개인 R&D 오픈소스'만 보여 준다. Skills 부제는 'Experience Behind the Projects'인데 아래는 연도·회사·성과 없는 키워드 묶음이다. 리크루터는 경력자를 후보로 올릴 때 '어디서 몇 년, 무슨 직무'가 최소 요건이라, 이 사이트로는 후보 등록이 안 된다.
- (high) Projects / Skills / Overview (스크린샷 캡처): 각 프로젝트의 설명이 전부 개발자 용어다. 같은 줄에 PropertyGrid, ROI, Recipe XML, MobileSAM, YOLOv8n, TensorRT, C3D가 나오고, 칩에는 'machine-vision opencvsharp4 blob-detection pattern-matching' 같은 GitHub 토픽이 그대로 붙어 있다. Skills는 'TOP / BTM independent processing and multi-worker execution', 'Timeout, recovery and delayed-callback isolation'처럼 명사구 나열이다. 'Overview' 메뉴를 누르면 요약이 아니라 'Sequence, axis, I/O, fault'가 들어간 아키텍처 도표가 나오고, 점선 화살표는 '아직 개발 중'이라는 뜻이라 절반이 미완성으로 보인다. 비전문가는 어디서부터가 아니라 첫 줄에서 막힌다.
- (med) Releases 섹션 (스크린샷 캡처) 및 모바일 메뉴 (스크린샷 캡처): Releases는 17개 항목의 변경 이력(RBV 10건, Vision SDK 7건)이라 리크루터에게 정보량이 0인데, Contact 바로 위에 길게 깔려 있다. 모바일 캡처 기준 페이지는 16,000px 이상(캡처 도구 결과, 상한일 수 있음)이고, 원칙 섹션은 CSS로 화면 4개 분량(.pr-wrap{height:calc(var(--vh)*4)})을 고정 스크롤시켜 6줄만 보여 준다. 폰에서는 상단 알약 메뉴에 이름·EN/KO·테마·햄버거만 있어 이메일/연락처가 안 보인다. 연락처를 찾으려면 햄버거를 열어 Contact를 눌러야 한다.

**잘한 점**

- 모바일 첫 화면 (스크린샷 캡처): 390px 폭에서 이름, 한글 이름(최노아), 직함, 설명 한 줄, GitHub/Email 버튼이 스크롤 없이 한 화면에 다 들어오고 가로 스크롤이 없다. 상단 알약 메뉴에 EN/KO 토글이 항상 보인다. 폰 첫 화면 기준으로 깨지거나 잘리는 곳이 없다.
- About의 숫자 카드 (스크린샷 캡처): '8 years of experience', '20+ equipment projects'를 큰 숫자로 따로 보여 준다. 사이트 전체에서 리크루터가 5초에 읽을 수 있는 몇 안 되는 정보다. 'as of 2026-11-27' 날짜를 붙였고, GitHub 별 합계 41(15+6+5+1+10+4)이 별도 자료(stats.md)와 맞는다. 다만 이 카드가 히어로가 아닌 두 번째 화면에 있는 게 아쉽다.
- 프로젝트 설명 속 범위 한정 문구 (스크린샷 캡처, 3D Studio·Machine Studio·Labeling Studio 노트): 'These results come from one dataset with 40 defective test images and are not evidence of production accuracy.', 'It is not qualified for production equipment control or safety functions.'처럼 과장을 스스로 막아 둔다. 기술을 모르는 나도 '숫자를 부풀리지 않는 사람'이라는 인상을 받는다. 채용 담당자가 기술 지인에게 물어볼 때도 안전하다.
- 3D Studio·Labeling Studio 데모 화면 (스크린샷 캡처, 프로젝트 3·2번 캡션): 'five pass, three fail with the failing value and limit', 'four washers and one defective washer'처럼 화면 캡션이 OK/NG 개수를 센 결과로 되어 있어, 용어를 몰라도 '불량을 골라내는 프로그램'이라는 것이 보인다. 실제 앱 화면이라 '이 사람이 만든 것이 실제로 돌아간다'는 증거로 읽힌다.

**딱 하나 바꾼다면**: 히어로의 이름·직함 바로 아래에 '경력 8년 · 장비 프로젝트 20+ · 반도체/디스플레이/배터리/자동차'를 한 줄로 올리고, 주 버튼을 GitHub에서 Email(또는 이력서 PDF)로 바꾼다. 리크루터가 10초 안에 묻는 '누구, 어느 분야, 몇 년차, 어떻게 연락'이 첫 화면 하나에서 끝나야 나머지 섹션이 읽힌다.

## C#/.NET 오픈소스 사용자

**첫인상**: 첫 화면은 포트폴리오 표지다. 제일 큰 건 이름이고, 이게 무슨 도구냐를 말해 주는 한 줄(OpenVisionLab: open-source C#/.NET tools for 2D/3D inspection, labeling, and debugging.)은 작은 회색 글씨라 두 번 읽었다. C#/.NET, OpenCvSharp, 디버깅 같은 단어가 걸려서 스크롤은 내렸고, 프로젝트마다 버전·라이선스·별이 붙은 건 오픈소스 페이지답게 보였다. 다만 받아서 5분 안에 돌려 보는 길은 Raw Buffer Visualizer 말고는 안 보였고, 이 사이트 글에는 AI가 쓴 티가 나는 문단이 여러 군데 있다(아래 ai_sounding).

**행동(maybe)**: 당장 하는 일은 Raw Buffer Visualizer 설치(hero 3번째 버튼 'Visual Studio Marketplace')와 Vision SDK 저장소 열어 보기까지다. 2D Workbench, 3D Studio, Labeling Studio는 사이트에 받는 경로가 없고(README를 열어야 ZIP이 있는지, 소스 빌드인지, .NET 8인지 10인지 나온다) 별도 안 누르고 북마크만 한다. 별 41개, 팔로워 90은 판단 근거가 못 되고, 유지보수는 Recent version history의 날짜(최근 2026-11-16, 작업일 2026-11-27 기준 11일 전)와 버전 간격으로만 짐작한다. 한 사람이 6개를 돌본다는 점이 보여서 사내 앱에 의존성으로 넣는 결정은 아직 못 한다.

**핵심 지적**

- (high) Projects 01~06 (스크린샷 캡처): 6개 중 5개는 사이트에서 받는 방법도, 요구 환경도 알 수 없다. 'Usable'은 정의가 없고 칩 분류도 섞여 있다('Usable'=상태, 'Source available'=배포 형태, 'Active development'=개발 단계, 'VS Marketplace'=채널). 공개 README 기준으로 2D Workbench에는 v2.1.0-rc.3 win-x64 ZIP(.NET 8 Desktop Runtime x64 필요)이 있고, README 스스로 그 ZIP이 소스 워크플로보다 오래됐다고 적었는데 사이트는 소스 버전 v2.2.0-dev.12만 보여 준다. 3D Studio는 .NET 10 소스 빌드, Vision SDK는 NuGet.org 미게시(rc.2 .nupkg 6개를 GitHub 프리릴리스에서 받아야 함)다. 데모 영상은 새 소스 빌드 기준이라, ZIP을 받은 사람은 영상에 나온 화면을 못 볼 수 있다.
- (high) Projects 05 Vision SDK (스크린샷 캡처): 내 상황(C#+OpenCvSharp 사내 앱)에 가장 직접 맞는 프로젝트인데 코드 예제가 '{}' 아이콘 뒤 두 번째 탭에 숨어 있고, 기본으로 보이는 건 'Matching Tool — template match result'라는 합성 이미지(전 매치 Score:1.000)다. 예제 코드도 16x16 단색 Mat에 Threshold를 걸고 크기만 출력해서 '16x16'이 나오는 스모크 테스트라 SDK 품질을 판단할 근거가 못 된다. 'in your own C# application'이라고 쓰면 dotnet add package를 기대하는데, 패키지 경로가 없다.
- (high) Releases (스크린샷 캡처): 릴리스가 아니라 소스 버전 나열이다. Latest 카드에는 날짜도 링크도 없고, 타임라인 17개 항목 중 Vision SDK와 Raw Buffer Visualizer만 있어 2D/3D/Labeling/Machine Studio 이력은 없다. 링크가 하나도 없어서 'v3.3.0-rc.3이 뭐가 바뀌었나'를 CHANGELOG에서 확인할 수도, 받을 수도 없다. 표기도 제각각이다: 'v2.2.0-dev.12', '0.4.4', 'v0.8.2-dev', '2.2.5'; 라벨도 'Source version'과 'Version'이 섞여 있다. 같은 칩 줄의 'Version 0.4.4'가 게시본인지 소스인지 알 수 없다.
- (med) Hero (스크린샷 캡처): 10초 안에 '이게 어떤 도구냐'를 말하는 문장이 화면에서 가장 약하다. 제일 큰 요소는 사람 이름이고 첫 화면에 스크린샷이 없다. 내가 찾던 키워드 'OpenCvSharp'와 'Windows 전용'은 hero에 없다. 또 브랜드 'OpenVisionLab'과 GitHub 저장소 'OpenVisionLab'(실제로는 2D Workbench) 이름이 같아서, 검색해 들어가면 우산 프로젝트가 아니라 2D 도구가 나온다. 카드 01 제목은 '2D Workbench'인데 저장소 이름과 exe 이름은 OpenVisionLab이다. 주 버튼도 프로젝트가 아니라 GitHub 프로필이다.
- (med) Projects 데모 영역 (스크린샷 캡처, js/main.js): '데모 화면이 믿을 만한가'를 직접 확인할 수가 없다. 1600px 원본 WebP를 650px 폭에 줄여 보여 주는데 확대 기능이 없어서 WPF UI 글자(Pipeline, PropertyGrid 값)가 읽히지 않는다. 마우스를 올리면 프레임 전체가 최대 약 4도 기울어서 더 읽기 어렵다. mp4와 GIF는 반복 재생에 컨트롤이 없다(controls는 reduced-motion일 때만 켜짐). 정지 상태 첫 화면도 약하다: 3D Studio 첫 슬롯 포스터는 'Untested / Waiting' 상태의 빈 뷰어이고, 2D Workbench 첫 슬롯은 poster 없는 video라 로딩 전 검은 사각형이다(스크린샷 캡처에서 확인). Machine Studio 스크린샷은 영어 UI인데 장치명이 한국어('검사 유닛 A', '이송 축 A')라 영어 페이지에서 어색하다.

**잘한 점**

- Labeling Studio 뷰어 6번째 슬라이드와 vnote (lab-visa-pcb4-test-result): 캡션 'YOLOv8n on a VisA PCB4 test image: three defects found, one small defect missed'처럼 놓친 결함을 숨기지 않고, 'These results come from one dataset with 40 defective test images and are not evidence of production accuracy.'와 VisA CC BY 4.0 출처까지 바로 옆에 적었다. 성능 과장이 없다는 가장 강한 신호다.
- Raw Buffer Visualizer 슬라이드 2, 3 (rbv-manual-stride-before/after): 잘못된 3840바이트 스트라이드와 실제 3920바이트 스트라이드를 같은 PCB 스냅샷으로 전후 비교해서 보여 준다. 행 패딩 때문에 이미지가 기울어 보이는 건 C# 비전 개발자가 한 번씩 겪는 버그라 이 도구가 내 문제를 푼다는 게 숫자 하나로 전달된다. 'Edited demonstration; not a processing-time measurement.'도 정직하다.
- Vision SDK 불릿 2번째: 'Your application owns acquisition, display, ROI editing, recipe storage and the final equipment decision.' 라이브러리가 어디까지 책임지는지 한 문장으로 경계를 긋는다. 내 앱에 넣을 때 무엇을 직접 만들어야 하는지 바로 알 수 있다.
- Projects 3D Studio, Machine Studio의 note, 3D 캡션: 'This version is a development source snapshot, not a production qualification.'와 'It is not qualified for production equipment control or safety functions.'를 칩 바로 아래 둔 점, 3D 캡션에 'synthetic' 합성 스캔임을 적은 점. 데모 데이터의 성격과 한계를 먼저 밝혀서 화면을 믿고 볼 수 있다.

**딱 하나 바꾼다면**: Projects 6개 행마다 '받는 법 + 요구 환경' 한 줄을 넣고 'Usable' 칩을 받는 방식('ZIP + source', 'Source only', 'VS Marketplace')으로 바꾼다. 예) 'Get it: win-x64 ZIP v2.1.0-rc.3 from GitHub Releases (needs .NET 8 Desktop Runtime x64). Newer features: build from source.'

## 프론트엔드·모션 디자이너

**첫인상**: 첫 화면은 생각보다 괜찮다. 점격자 위로 스캔 빔이 지나가고 모서리 브래킷 박스가 떴다 사라지는 게 '비전 엔지니어'라는 주제와 맞아서 흔한 다크 템플릿과는 결이 다르다. 그런데 스크롤하면 큰 제목 + 카드 + 글머리 구성이 20화면 가까이 이어지고, 끝까지 내려가도 나한테 뭘 해 달라는 사이트인지는 '스타나 팔로우'뿐이다. 영어 본문은 명사를 나열한 스펙 시트 문장이 많아서 사람이 쓴 글처럼 안 읽힌다.

**행동(maybe)**: 별은 줄 수 있다. Raw Buffer Visualizer처럼 실제 VS Marketplace에 올라간 도구가 있고, 'It is not qualified for production equipment control or safety functions.' 같은 한계 표기가 믿음을 준다. 연락·채용은 이 입장(프론트엔드)에서는 하지 않는다. 사이트가 구직·협업 여부를 말하지 않고 Contact가 '스타나 팔로우'만 요청하기 때문이다. 제작 방식(still 모드, 뷰어 접근성, 스크롤 연동 원칙 구간)은 레퍼런스로 저장해 둘 만하다.

**핵심 지적**

- (high) #contact .big (index.html:525-531), 히어로 .btns (index.html:60-64), 스크린샷 캡처: 사이트 전체에서 방문자에게 하는 유일한 요청이 스타·팔로우다. 채용·협업·질문을 받는지 어디에도 적혀 있지 않다. 버튼 위계도 어긋난다. 히어로에서는 GitHub가 class="btn pri"(61행)이고 Email은 보조(62행)인데, Contact에서는 Email이 class="btn pri"(527행)다. Marketplace 버튼은 제목 + <span class="bsub"> 2단 라벨이라 세 버튼 중 가장 길어 시선을 끈다.
- (high) 섹션 순서 index.html:96-423, .sec/.ttl css:104-106, .pr-wrap css:213, #tl index.html:492-510, 스크린샷 캡처: 페이지가 길고 증거가 늦게 나온다. still 모드 기준 문서 높이가 1440폭에서 15,355px, 390폭에서 20,603px이다(lint_site.run_lint로 측정). 실제 동작에서는 원칙 구간이 4×vh를 쓰므로 여기에 약 3화면이 더 붙는다. 섹션마다 5.5rem 제목 + 120px 패딩이 반복돼 Projects에 도착해도 첫 스크린샷은 y≈500에서 시작한다. 처음부터 세면 스크롤 약 3화면 뒤다(추정). 6개 프로젝트의 관계를 보여 주는 Overview 다이어그램(388행)은 프로젝트 6개 뒤에 있어서 지도 없이 상세부터 읽게 된다. 다이어그램도 y≈500-580 구간에서 Vision SDK 실선 3개와 Virtual camera 점선 3개가 교차하고, 820px에서는 행 간격이 줄어 화살표가 뭉친다(스크린샷 캡처). 타임라인 17건은 GitHub Releases와 겹친다.
- (med) index.html:105-106, main.js:147-158, main.js:174-177, assets/*.gif: 첫 프로젝트(2D Workbench)의 대표 매체가 poster 없는 preload="none" 영상이다. 실제 방문에서는 35% 이상 보일 때까지(main.js:174) 로드가 시작되지 않아, 검은 스테이지에 스캔선만 지나가고 1.3MB mp4를 기다린다. 제공된 캡처는 ?shot 모드라 preload=metadata가 걸려 첫 프레임이 보이므로 이 문제가 드러나지 않는다(코드로만 판단, 실제 로드 측정은 하지 않음). GIF 5개는 합계 약 4.85MB(파일 크기 합산)이고, 같은 내용을 mp4로 만들면 보통 5-10배 작다(경험치, 이 파일들로 측정하지 않음). 영상(2개)과 GIF(5개)가 서로 다른 코드 경로(main.js:154-158)를 타고, 스크롤로 벗어나면 src를 poster로 되돌려서 재진입마다 GIF가 처음부터 다시 돈다.
- (med) main.js:142, main.js:150, hero.js:95: 자동 재생되는 영상·GIF·히어로 캔버스 모두 일시정지 수단이 없다(WCAG 2.2.2: 5초 넘게 자동으로 움직이는 콘텐츠). prefers-reduced-motion이면 still이 켜져 영상에는 controls가 붙지만(142행), GIF는 run이 항상 false라(150행) 재생할 방법이 없다. 3D Studio·Labeling Studio·Raw Buffer Visualizer의 핵심 데모가 GIF인데 모션 줄이기 사용자는 poster 한 장만 본다.
- (med) index.html:370-372, 433-448, 486-488, 495·497·501-508, 7-8, 스크린샷 캡처(extra), 스크린샷 캡처: 한국어로 전환해도 영어가 그대로 남는 블록이 크다. Raw Buffer Visualizer 기능 3줄(370-372), Skills 불릿 전부(433-448, h3만 번역), Latest 카드 3개(486-488), 타임라인 중 Raw Buffer Visualizer 10건(495, 497, 501-508)에 data-ko가 없다. KO 릴리스 캡처에서는 Latest 카드 3개가 전부 영어다. 같은 타임라인 안에서 Vision SDK는 한국어, Raw Buffer Visualizer는 영어로 섞인다. <title>과 meta description도 전환되지 않는다(7-8행). html lang=ko인데 영어 문장에 lang="en"이 없어 스크린리더가 한국어 음성으로 읽는다.

**잘한 점**

- 히어로 캔버스 (hero.js:42-52 브래킷, 55-77 스캔 빔, 88-95 루프): '검사 화면'의 문법인 스캔 빔과 코너 브래킷 검출 박스를 배경 모션으로 옮겼다. 주제와 모션이 맞는 드문 경우다. 화면 밖이나 탭이 숨겨지면 루프를 멈추고(90행), 모바일·거친 포인터에서는 박스 수를 줄이고 포인터 반응을 끄는 등 비용도 챙겼다.
- html.still 한 클래스 (css:252-268, index.html:13-15): prefers-reduced-motion일 때 진입 모션·스캔선·다이어그램 드로잉·코드 줄 등장 상태를 전부 최종 상태로 풀고, 원칙 섹션은 정적 목록으로 접는 경로를 한 곳에 모았다. 모션을 끈 사용자도 내용 손실 없이 전체 페이지를 본다. 같은 경로를 캡처·린트 도구가 재사용한다.
- 미디어 뷰어 접근성 (index.html:117-122, main.js:23-25, 166-172): 썸네일이 aria-pressed 토글 버튼이고 aria-labelledby로 캡션을 이름으로 쓴다. ←/→/Home/End 키 이동이 구현돼 있고, 이미지 alt가 현재 언어의 캡션과 동기화된다(syncAlt). 포트폴리오 갤러리 중 이 수준을 지킨 곳은 드물다.
- 한계 표기 (index.html:168, 245, 296, 360, 418-419): 'These results come from one dataset with 40 defective test images and are not evidence of production accuracy.', 'It is not qualified for production equipment control or safety functions.', 점선 = 'still in development' 범례처럼 못 하는 것을 화면 안에서 먼저 말한다. 디자이너 입장에서도 이 사이트의 수치와 데모를 믿게 만드는 가장 강한 요소다.

**딱 하나 바꾼다면**: Overview 다이어그램을 About 바로 뒤(Projects 앞)로 옮기고, 히어로를 뺀 섹션의 제목 크기·패딩·원칙 구간 길이를 줄여서 첫 프로젝트 스크린샷이 스크롤 1.5화면 안에 나오게 한다. 지도를 먼저 보여 주고 증거를 앞당기는 한 번의 구조 변경이 명확성, 페이지 길이, 사이트의 가장 고유한 요소 노출을 한꺼번에 해결한다.

## 한국어 윤문 편집자

**첫인상**: KO를 켜자마자 제목은 한국어인데 본문이 영어로 남은 구간이 눈에 들어온다. 프로젝트 소개는 README에서 옮긴 개조식이라 현업 말투가 살아 있고 읽을 만한데, 소개와 원칙 단락은 번역기가 다듬은 매끈한 문장이라 두 목소리가 한 페이지에서 갈린다. 같은 사물을 툴/도구/Tool, 레시피/Recipe로 부르는 것도 한 사람이 쓴 글이 아니라 저장소별 README를 이어 붙인 글로 보이게 한다.

**행동(maybe)**: 지금 상태 그대로는 공개하지 않는다. data-ko 154개 중 오탈자나 격 파탄 같은 치명적인 오류는 적고 한계 고지 문장(데이터셋 1종과 테스트 불량 40장, 생산 장비 제어용으로 검증되지 않음)은 정직하게 쓰였다. 그러나 KO 모드에 번역 안 된 본문이 약 30개 남아 있고, 용어가 화면 안에서 갈리고, 소개·원칙 문단 몇 개가 번역투와 AI 상투를 보인다. 이 세 가지를 고치면 공개해도 된다.

**핵심 지적**

- (high) 스크린샷 캡처 / index.html Skills 카드 불릿, Raw Buffer Visualizer .feat, Releases .lat, #tl: KO 모드에서 카드 제목은 '장비 소프트웨어'로 바뀌는데 그 아래 불릿은 영어 그대로다. 소스에서 센 번역 필요 문자열은 약 30개다: Skills 불릿 14개(데스크톱 카드 5개는 고유명사 나열이라 제외), Raw Buffer Visualizer 불릿 3개, Latest 카드 3개, 타임라인 17개 중 Raw Buffer Visualizer 10개. 타임라인은 Vision SDK 항목(한국어)과 Raw Buffer Visualizer 항목(영어)이 번갈아 나와 항목마다 언어가 바뀐다(스크린샷 캡처). title, meta description, 푸터 'Copyright (c) 2026 Noah Choi'도 KO에서 안 바뀐다. 한국어 독자는 의도한 영문 유지가 아니라 번역 미완성으로 읽고, 채용 담당자가 가장 먼저 훑는 Skills가 영어로 남아 있다.
- (high) 프로젝트 섹션 01~05 (스크린샷 캡처, index.html data-ko 28~36, 56~65, 84~89, 70~79): 같은 개념을 부르는 이름이 한 페이지에서 갈린다. 도구: 툴(2D) / 도구(3D, Labeling, SDK) / Tool(SDK 2D 불릿). 레시피: Recipe(2D, Machine Studio) / 레시피(3D, SDK). 일괄 검사: Batch inspection(2D) / 일괄 검사(3D). 두께: Thickness(3D 불릿) / 두께(3D 캡션 '기판 두께'). 영상: 영상(2D, Machine Studio) / 이미지(Labeling, 히어로, 구성도). 장비: 설비 판정(SDK) / 장비(나머지). 영상 확보: 획득(Machine Studio) / 수집(SDK '영상 수집') / 촬영(타임아웃 '촬영 deadline'). 원인은 공개 README 한국어판이 저장소마다 다른 용어를 쓰기 때문이다(받아 둔 README 한국어판에서 센 값: 2D는 '툴' 15회, 'Recipe' 15회, '레시피' 0회, '영상' 27회, '이미지' 0회. 3D는 '도구' 19회, '레시피' 29회, 'Recipe' 0회. Labeling은 '이미지' 23회, '영상' 0회). 사이트가 이를 나란히 놓아 이음새가 드러난다. 앱 화면의 실제 UI 라벨이 'Recipe'인지 '레시피'인지는 확인하지 못했다.
- (med) 스크린샷 캡처 (엔지니어링 원칙 6줄, 화면에서 가장 크게 나오는 한국어): 영어 슬로건을 단어 대 단어로 옮겼다. '결정론적으로 유지한다'는 유지할 대상이 상태가 아니라 상태 전이·동작이 같은 입력에 같은 결과를 내는 성질이다. '안전하게 실패한다'는 실패하는 행위를 안전하게 하는 것으로 읽히는데 장비 현업 말로는 실패했을 때 안전한 상태로 간다는 뜻의 페일 세이프다. '근거를 보존한다'의 '근거'는 같은 페이지에서 'OK/NG 근거'(판정 이유)로도 쓰여 evidence(증거·기록)와 뜻이 섞인다. 6줄이 모두 '~한다.'로 같은 길이로 끝나는 연속 단문이라, 화면에서 가장 크게 읽히는 한국어가 가장 직역투다.
- (med) 릴리스 > 최근 버전 이력 (스크린샷 캡처, data-ko 140~145): 한국어 문장 속에 소문자 영어 명사(grid, deadline, terminal)를 그대로 끼워 어떤 뜻인지 한국어 독자가 풀 수 없다('terminal 결과'가 단말 결과로 읽힌다). '선택형'은 '선택형 문항'처럼 객관식을 뜻하는 말이라 optional·opt-in에는 맞지 않고 세 항목에 반복된다. '협력 취소'는 cooperative cancellation의 직역으로, .NET 쪽에서 쓰는 말은 '협조적 취소'로 알고 있다(확인 필요). 이 문구는 공개 README 변경 이력과 같은 사용자 원문이고, 사이트는 마지막 문장만 손봤다. 'pose grids'의 'pose'와 'frame Host'의 'frame'은 한국어에서 빠졌다.
- (med) 스크린샷 캡처, css/style.css 31행·106~111행: 영문 소제목용 자간(.sub, .ttl.sm, .cue, .road dt의 letter-spacing .14em)이 한글에도 그대로 걸려 '엔 지 니 어 링  원 칙', '최 신'처럼 글자가 벌어지고 띄어쓰기 경계가 안 보인다(스크린샷 캡처). html[lang=ko]로 덮어쓴 것은 .kname 하나뿐이다. 큰 제목에 쓴 -.045em(.ttl, .pr li)도 한글에는 빡빡하게 붙는다(스크린샷 캡처 '프로젝트'는 눈대중 판단). 히어로 문구는 마지막 줄에 '만듭니다.' 한 어절만 남는다(스크린샷 캡처). 칭찬할 부분: body의 word-break: keep-all은 한글 어절 단위 줄바꿈이라 맞다.

**잘한 점**

- Labeling Studio 캡션 (data-ko 47, 사용자 README 원문 계열): '데이터셋 1종과 테스트 불량 40장의 결과라 생산 정확도의 근거는 아닙니다.'는 한계를 수치로 못 박고 '다소', '어느 정도' 같은 완곡어가 없다. AI는 이렇게 쓰지 않는다. 사람이 숫자를 알고 쓴 문장이다.
- 현업어 선택 (data-ko 61, 70, 118): '실제 하드웨어 시운전 전에', '척 기준 영역', '양산 샘플', '광학계', '티칭'은 번역기가 고르지 않는 장비 현업어이고 문장에 제자리로 들어가 있다. 이 사이트에서 가장 사람이 쓴 흔적이 선명한 곳이다.
- Raw Buffer Visualizer 시연 영상 고지 (data-ko 98, ed)와 캡션 96~97: '편집한 시연 영상입니다. 처리 시간을 측정한 영상은 아닙니다.'는 짧고 단정한 합쇼체로 사실만 쓴다. '잘못된 3,840바이트 스트라이드로 해석한 PCB 스냅샷'은 수치가 들어가 있고 공개 README(3,840->3,920바이트)와 일치한다.
- Machine Studio 주의 문구 (data-ko 82): '생산 장비 제어나 안전 기능에 사용하도록 검증되지 않았습니다.'는 안전과 관련한 한계를 돌려 말하지 않고 그대로 쓴다. 문장도 짧다. 다만 3D Studio의 '운영 환경 검증 완료를 뜻하지 않습니다'는 IT 용어라 장비 독자에게는 손볼 곳이 있다(risk_flags 참고).

**딱 하나 바꾼다면**: KO 모드에서 영어로 남은 본문 약 30개(Skills, Latest 카드, 릴리스 타임라인, Raw Buffer Visualizer 불릿)를 번역한다. 번역하기 전에 용어 한 벌(도구, 레시피, 일괄 검사, 영상 획득)을 정하고 이미 번역된 문구도 같은 표로 맞춘다.

## 영어 기술문서 편집자

**첫인상**: ecosystem, seamless, robust, leverage 같은 홍보 어휘는 소스에서 이미 빠져 있고(전수 grep으로 확인), 줄표도 없고, 한계를 밝히는 문장이 곳곳에 있어서 첫인상은 믿을 만하다. 문법 오류도 거의 없다. 다만 AI 티는 단어가 아니라 구조에 남았다. Principles의 슬로건 6연타와 'I would rather...', 릴리스 노트의 'Adds X, clarifies Y, and uses Z' 나열, 추상명사 5개를 이어 붙인 문장이 그렇다. 채용 페이지로 읽으면 마지막 문장이 'star or follow'를 부탁하는 README 말투라서, 이 사람에게 무슨 일로 연락하면 되는지 영어 문구에서 가장 약하다.

**행동(maybe)**: 그대로 공개해도 사실 오류나 부끄러운 문법 오류는 없지만, 영어 원어민 편집자 눈에는 '현업 영어'와 '정리된 변경 이력 + 가치 선언'이 섞여 있다. 최소한 (1) 릴리스 노트 Latest 3건 문장, (2) Principles 구간의 슬로건과 'I would rather' 문단, (3) Contact 문구를 고치고 (4) 용어 표기(Recipe/recipe, OK/NG vs pass/fail, v 접두사, Source version/Version)를 통일한 뒤 공개하는 것이 맞다. 이 네 가지는 모두 문장 단위 수정이라 구조 변경 없이 가능하다.

**핵심 지적**

- (high) Contact (스크린샷 캡처): 연락처 섹션의 큰 글자 문장이 GitHub README 끝의 별 요청이다. 채용·협업 문의 페이지에서 방문자가 가장 알고 싶은 것은 '무슨 용건으로 메일을 보내도 되는가'인데 그 문장이 없다. About의 '41 GitHub stars' 타일과 겹쳐서 별 개수에 기대는 사람처럼 읽힌다. 영어 문법은 맞다.
- (high) Releases > Latest (스크린샷 캡처, 한국어 모드는 스크린샷 캡처): (1) 'Adds A to X, B and C in Y, and D'의 병렬이 깨졌다. 'faster workspace tab switching'은 추가하는 것이 아니고, 'bulk expected results'와 'named failure causes'가 Thickness에 붙는지 Validation에 붙는지 모호하다. (2) 같은 줄 안에서 Adds(현재 3인칭), Reports, clarifies, uses로 주어 없는 현재형이 이어져 자동 생성된 변경 목록처럼 읽힌다. (3) 'neutral gray surfaces with plainer wording'은 외부 독자에게 정보가 없다. (4) 같은 'Latest' 안에서 Labeling Studio는 과거형('Ran'), 2D Workbench는 수동 현재형('are localized'), 3D Studio는 현재형이라 시제가 세 가지다. (5) 'Learn windows'는 README의 'Learn Mode'를 줄인 말인데 사이트 어디에도 정의가 없고, 'edge runtime'도 마찬가지다. 한국어 모드에서는 이 세 카드가 전부 영어로 남는다.
- (high) Engineering Principles (스크린샷 캡처): 이 구간은 사이트에서 가장 큰 활자와 가장 긴 스크롤을 차지하는데 내용이 가장 일반적이다. 슬로건 6개(Fail safely. / Preserve evidence. ...)는 어떤 시스템에도 붙일 수 있고, 'I would rather X than Y just for novelty'는 전형적인 'I prefer' 가치 선언이며, 추상명사 4개 나열이다. 첫 줄 'Build before the machine is ready.'는 히어로 태그라인, About 인용문, Overview 목적 문단에 이어 네 번째로 같은 메시지다. 채용 담당자가 읽고 얻는 정보는 없다. 같은 구간에 이미 있는 실제 기능(3D Studio의 failing value와 limit 표시, Run Record 저장, SDK의 result evidence)이 근거로 쓰이지 않는다.
- (med) Releases > Recent version history (스크린샷 캡처): 한 목록 안에 문법 형태가 세 가지다: 명령형(Vision SDK 'Add...', 'Harden...'), 과거형(Raw Buffer Visualizer 2.2.1~2.2.3 'Cleared', 'Preserved', 'Corrected'), 동사 없는 명사구(2.1.0, 2.2.0, 2.2.4, 2.2.5 'Nested image discovery, pointer-frame matching and ...'). 'Bound'는 동사로 쓰였지만 'bind의 과거형'이나 명사로 읽히기 쉽고, 'harden ... terminal results', 'fixed package consumers'는 저장소를 모르는 사람이 의미를 짐작할 수 없다. 'Harden'은 같은 목록에서 두 번 쓰인다. 17건 중 11건이 Raw Buffer Visualizer 패치라 훑어보는 사람에게는 소음이 된다.
- (med) Projects 전반, Releases (스크린샷 캡처): 같은 개념의 표기가 흔들린다. (1) Recipe: 2D는 Recipe, 3D 설명과 캡션은 recipe('save a recipe', 'one recipe'), 3D 기능은 'in a Recipe'. (2) 판정어: 3D 캡션 'five pass, three fail'인데 같은 사이트의 다른 줄은 'OK/NG reasons'이고 한국어 캡션은 '5장 OK, 3장 NG'라서 영어만 다르다. (3) Batch inspection을 문장 중간에서 대문자로 쓴다. (4) 'operator'는 한국어 '사용자'와 다르고, 라벨링 도구의 사용자를 operator라고 부르면 장비 운용자로 읽힌다. (5) 'compatible'이 3D 카드에서 세 번 나오는데 무엇과 호환인지 영어에는 없다(한국어에는 'C3D'가 있다). (6) validation, verification, qualification을 섞어 쓴다. (7) 버전 표기: 칩은 v2.2.0-dev.12, Latest는 같은 릴리스를 2.2.0-dev.12로 쓰고, 칩 라벨도 'Source version'과 'Version'이 섞여 있으며 그 차이를 설명하지 않는다. (8) 'Source available' 칩이 'MIT' 칩 옆에 있다. source-available은 보통 OSI 오픈소스가 아닌 라이선스를 가리키는 용어라 'open-source tools'와 충돌해 보인다.

**잘한 점**

- Labeling Studio 여섯째 캡션과 vnote (lab-visa-pcb4-test-result): 'YOLOv8n on a VisA PCB4 test image: three defects found, one small defect missed'와 'are not evidence of production accuracy'는 성공 사례 옆에 놓친 결함을 적었다. 영어도 군더더기 없이 짧고, 개발자 사이트에서 거의 보기 힘든 종류의 문장이다. 사이트 전체의 신뢰도가 이 문장에 가장 크게 의존한다.
- Vision SDK 둘째 기능 줄: 'Your application owns acquisition, display, ROI editing, recipe storage and the final equipment decision.'은 API 문서에서 책임 경계를 쓰는 관용 표현(owns)을 정확하게 쓴 문장이다. 통합하려는 개발자가 무엇을 직접 해야 하는지 한 줄로 알 수 있다.
- Overview 범례와 첫 문장 (스크린샷 캡처): 'Dashed arrows mark direct cross-project integration still in development.'와 'OpenVisionLab does not replace real equipment validation.'은 한계를 범례와 도입 문장에 그대로 넣었다. 약하게 만들지 말고 유지할 문장이다.
- Raw Buffer Visualizer 타임라인 2.0.7, vnote: 'Signed Int32 image support; package superseded by 2.0.8'와 'Edited demonstration; not a processing-time measurement.'는 잘못된 릴리스와 편집된 영상을 숨기지 않는다. 릴리스 이력의 신뢰를 올리는 문장이다. 다만 후자는 'This is an edited demo, not a timing measurement.'처럼 주어를 넣으면 더 자연스럽다.

**딱 하나 바꾼다면**: Engineering Principles 구간의 영어를 전부 다시 쓴다. 슬로건 6줄과 두 문단(I would rather..., For machine-vision software, ...)을 지우고, Machine Studio 시뮬레이션, 3D Studio의 failing value와 limit 표시와 Run Record, Vision SDK의 result evidence 같은 실제 기능 세 줄로 바꾼다. 사이트에서 활자가 가장 크고 AI 티가 가장 진한 곳이며, 나머지 AI 흔적은 문장 몇 개를 고치는 수준이다.

## 공개 리스크 검토자

**첫인상**: 소스를 열어 보니 외부 요청이 하나도 없고(링크 8개 전부 GitHub·Marketplace), 고객사·회사 이름도 없다. 그건 합격이다. 그런데 이미지 출처 표기는 6번째 썸네일을 눌러야 나오는 한 줄이 전부이고, 라이선스 칩이 프로젝트마다 다른 기준으로 붙어 있다. 문장은 '안정성, 추적성, 복구, 재현성'처럼 추상 명사를 나열해서 AI가 쓴 티가 난다. 이대로 올려도 큰 사고는 안 나겠지만, 올리기 전에 확인할 것이 몇 개 남아 있다.

**행동(maybe)**: 고객사명, 외부 추적, 개인정보 과다 노출 같은 즉시 중단 사유는 없다. 다만 (1) VisA CC BY 표기가 숨은 한 줄이고 링크·변경 표시가 빠져 있고, (2) 와셔·기포·HDD PCB 이미지의 출처가 사이트와 공개 README 어디에도 없고, (3) Vision SDK의 MIT 칩이 README의 재배포 보류 문구를 가리고, (4) 업무와의 관계(비밀유지·겸업·지식재산 규정)를 확인했는지 사이트로는 알 수 없다. 1~3은 수정하면 되고, 2와 4는 작성자가 사실을 확인해야 결론이 난다. 이것들을 확인하고 크레딧 블록을 붙인 뒤 공개하는 것을 권한다.

**핵심 지적**

- (high) index.html:167-170 (Labeling Studio .vnote, data-for="5" hidden), main.js:161, 푸터 index.html:537: 이 한 줄은 6번째 썸네일을 눌러야만 보인다(main.js:161이 선택된 항목에서만 hidden을 푼다). VisA 이미지는 같은 카드의 썸네일 줄과 Releases의 Labeling Studio 카드('real PCB images (VisA PCB4)')에서 이미 항상 노출되는데 거기에는 표기가 없다. 표기 내용도 CC BY 4.0이 요구하는 항목에 못 미친다. 라이선스·원본 링크가 없고, 변경 표시가 없다(화면의 이미지는 검출 박스를 그려 넣고 webp로 다시 압축한 개작본이다). 푸터는 모든 것에 걸리는 'Copyright (c) 2026 Noah Choi' 한 줄뿐이라, 읽는 사람은 이 사이트의 이미지를 전부 작성자 것으로 읽는다. 원 저작자가 요구하는 데이터셋 라이선스는 CC BY 4.0이 맞다(amazon-science/spot-diff README에서 확인).
- (high) Labeling Studio 갤러리(lab-detection-washer.webp, lab-segmentation-bubble.webp, lab-hero-smart-mask 포스터/GIF), Raw Buffer Visualizer(rbv-manual-stride-before/after.webp), assets/manifest.json: 비합성처럼 보이는 이미지의 출처가 사이트에도 공개 README에도 없다. 와셔 화면의 파일명은 '스크린샷 캡처', 기포 화면은 '스크린샷 캡처'/'Film bubble inspection'이고, RBV 스크린샷에는 하드디스크로 보이는 실제 기판 사진이 있다. 공개 README는 육각형 예제를 'generated hexagon example'로, 3D 스캔을 'synthetic'으로 밝히면서 와셔·기포·HDD 기판은 'actual app'이라고만 쓴다. 이 세 가지가 (a)직접 생성한 것인지, (b)라이선스가 있는 공개 데이터인지, (c)업무상 비공개 자료에서 온 것인지 화면만으로는 구분되지 않는다. (c)라면 비밀유지 위반이 되는 가장 직접적인 경로다. RBV README가 가리키는 docs/industrial-image-testing.md는 내가 열어 보지 못했다(미확인). manifest.json에는 파일별 source_url만 있고 이미지 자체의 출처·라이선스 항목이 없다.
- (med) Vision SDK 카드 index.html:330-332: 공개 README(License and redistribution)는 'Commercial redistribution of Core's bundled OpenCvSharp/OpenCV binaries remains blocked pending distribution/legal-owner approval'이라고 쓰고, 'MIT labeling ... do not grant that approval'이라고 못박는다. 사이트의 MIT 칩은 이 단서를 가리고, 설명 문장은 '당신의 C# 애플리케이션에서 쓰라'고 권한다. 'Source available'과 'MIT'를 한 줄에 붙이면 의미도 충돌한다. source-available은 보통 비(非)오픈소스 라이선스를 가리키는 말이다. 이 단서가 없으면 방문자가 상용 제품에 그대로 넣을 수 있다.
- (med) About index.html:75-76, Skills index.html:438,443,448: 회사명·고객사명은 사이트 어디에도 없다(index.html 전체 확인). 그러나 (1) 4개 산업군을 '20+ 장비 프로젝트'로 묶은 문장은 고객 산업군을 암시하고, (2) 'TOP / BTM independent processing and multi-worker execution', 'Timeout, recovery and delayed-callback isolation', 'Git / SVN / Jenkins'는 업무 경험과 겹치는 영역이다. 이 프로젝트가 업무와 무관하게 만들어졌다는 문구가 없고, 사이트가 이를 증명할 수도 없다. 업무와의 관계(비밀유지·겸업·직무발명 규정) 확인이 필요하며 확인 여부는 평가자가 알 수 없다(미확인). 같은 문장이 이미 GitHub 프로필 README에 공개돼 있으므로 이 사이트가 새로 늘리는 노출은 없다. 문제는 사이트가 그 사실을 한 번 더 반복해 눈에 띄게 한다는 점이다.
- (med) Releases 섹션 index.html:480-519, 상태 칩 index.html:132,188,239,291,330,375: (1) 이 저장소 9개의 GitHub releases/latest API 응답이 전부 404 'Not Found'다. 이 API는 정식(비 prerelease) 릴리스만 돌려주므로 prerelease 존재 여부는 확인하지 못했지만, 방문자가 GitHub에서 'Releases'를 눌렀을 때 아무것도 안 보일 가능성이 크다. 사이트의 항목은 README·CHANGELOG의 소스 버전 기록이다. RBV README는 'Source version is distinct from the version currently available on Marketplace'라고 쓰는데, 타임라인은 RBV 2.2.5를 같은 형식으로 나열한다. (2) 'Usable'은 어디에도 정의가 없다. 2D Workbench는 'v2.2.0-dev.12'에 'Usable'만 붙고 면책 문구가 없다. Labeling Studio도 같다(면책은 숨은 vnote에만 있다). 3D Studio와 Machine Studio에만 'not a production qualification' 문구가 있어 기준이 일관되지 않다.

**잘한 점**

- Labeling Studio vnote index.html:168, Machine Studio note index.html:296, Overview 범례 index.html:419: 'These results come from one dataset with 40 defective test images and are not evidence of production accuracy.', 'It is not qualified for production equipment control or safety functions.', 'Dashed arrows mark direct cross-project integration still in development.' 이 세 문장은 공개 README와 일치하고, 성능 수치(mAP 등)를 사이트에 옮기지 않아서 과장이 실제로 줄었다. 공개 리스크 관점에서 가장 큰 방어가 이미 들어 있다.
- index.html, js/*.js, css/style.css 전체: 외부 요청이 0이다. 링크 8개 전부 github.com 또는 marketplace.visualstudio.com이고, 외부 폰트·CDN·분석 스크립트가 없고, fetch/XHR/sendBeacon/쿠키 코드도 없다. 글꼴은 시스템 글꼴 스택이다. localStorage는 theme·lang 두 값만 쓰고 try/catch로 막힌 환경도 처리한다. insertAdjacentHTML은 코드 안의 상수로 만든 SVG에만 쓴다(main.js:223). 외부 링크 전부 target=_blank에 rel=noopener가 붙어 있다.
- assets/*.mp4, *.webp, *.gif: 내려받아 확인한 결과 MP4 두 개는 오디오 트랙이 없고 태그가 encoder 정보뿐이다. webp·GIF에 EXIF가 없다. Visual Studio 스크린샷의 계정 영역은 로그인 전 상태('로그인')이고 사용자 이름이 보이지 않는다. 2D Workbench 영상 안에 보이는 경로 표시에도 사용자명이 없다. 미디어 파일로 새는 개인정보는 못 찾았다.
- 3D Studio 캡션 index.html:216-221: 'Inspecting eight synthetic PCB scans', 'textured synthetic scan'처럼 합성 데이터를 캡션과 alt에서 매번 밝힌다. 3D Studio README(laser-line-profiler model의 synthetic C3D, 입력·레시피는 저장소에 없음)와 일치한다. 실물 측정으로 오해할 여지를 줄이는 올바른 처리다.

**딱 하나 바꾼다면**: 푸터 위에 항상 보이는 'Credits & Notices' 블록을 만든다. 이 블록을 쓰려면 먼저 와셔·기포·HDD 기판 이미지의 출처를 확정해야 하고, 거기에 VisA CC BY 4.0 표기(링크·변경 표시 포함), Vision SDK의 OpenCV 재배포 단서, 상표 문구를 함께 넣는다. 이 블록 하나가 높음 2건과 중간 1건을 한 번에 해결한다.
