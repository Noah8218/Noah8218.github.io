# 프로젝트 쇼케이스 보고서

AI 평가자 1명(프로젝트 쇼케이스 기획자)이 프로젝트 6개를 각각 "무엇을 보여야 설득되는가" 관점에서 정리했다. 프로젝트별 핵심 메시지, 증거 장면, **촬영 대본(클릭 단계, 길이, 해상도, 강조 지점, 팁)**, 인터랙티브 모듈, 데이터 포인트, 부족한 자료, 방문자별 가치와 데모 릴 구성안, 제작 우선순위가 들어 있다. 촬영·제작은 [08-backlog.md](../08-backlog.md) C 구역이 이 문서를 가리킨다.

## 읽기 전에

- **평가자는 AI다.** 사람의 의견이 아니며 점수는 AI의 판단이다. 평가는 2026-11-27 시점의 사이트(2차 문구 수정 직후)를 정지 화면 캡처와 소스 코드로 본 것이다. Edge(Chromium) 헤드리스에서만 확인했고 Safari, Firefox, 실제 터치, 스크린리더는 확인하지 않았다.
- **이후 사용자 피드백이 우선한다.** 사용자는 이 평가 뒤에 "처음 화면이 너무 AI스럽고 과하다", "이름이 너무 크게 나와서 거부감이 들었다", "밝은 게 더 좋아 보인다"고 말했다. 그래서 이름 글자를 줄이고 기본 테마를 라이트로 바꿨다. 이 문서의 제안 중 화려한 쪽(일러스트 히어로, 글로우, 큰 글자, 캔버스 연출)은 **보류 상태**다. 배경은 [01-context-and-decisions.md](../01-context-and-decisions.md), 보류 항목은 [08-backlog.md](../08-backlog.md)의 D·E 구역에 있다.
- **줄 번호 표기.** 근거 칸의 `css:15`, `main.js L120`, `index.html:52-64` 같은 표기는 평가 시점 파일의 줄 번호다. 이후 편집으로 어긋나므로 선택자·함수 이름으로 찾는다.
- **"제약 위반" 표기.** 웹폰트 파일 없음·의존성 없음은 작업자(AI)가 정한 제약이며 사용자 요구가 아니다. 도입하려면 사용자 승인이 필요하다([02-content-policy.md](../02-content-policy.md) 참고).
- **캡처 파일은 저장소에 없다.** 평가에 쓴 스크린샷에는 제3자 자료(레퍼런스 사이트, 레퍼런스 덱)가 섞여 있어 싣지 않았다. 원문의 캡처 파일명은 "스크린샷 캡처"로 바꿨다.
- **README 사본.** `README_*.md`, `stats.md`, `meta_*.json`은 공개 저장소에서 받은 원문 사본이며 `docs/sources/`에 둔다.

- **새 사실을 만들지 않는다.** 이 문서의 수치는 공개 README 문장이거나 에셋 화면에서 읽은 값이다. 화면에서만 읽은 값에는 "README 문장 아님, 성능 주장으로 쓰지 말 것"이라고 표시돼 있다. 사이트에 옮길 때는 [02-content-policy.md](../02-content-policy.md)의 출처 규칙을 따른다.
- 촬영에 필요한 샘플 데이터·모델·실행 환경을 사용자가 가지고 있는지는 **미확인**이다([08-backlog.md](../08-backlog.md)의 "새 촬영 가능 여부").
- README가 링크하는 mp4·GIF의 실제 존재와 최신 UI 반영 여부는 확인하지 않았다.

## 평가 점수와 총평

- **증거 가시성**: 5
- **표현 다양성**: 4
- **인터랙티브**: 3
- **스토리텔링**: 4
- **종합**: 4
- **요약**: 외형은 최신식이다(다크/라이트 전환, 유리 질감 내비, clamp 기반 반응형 타이포, grid/aspect-ratio/:has, 스크롤 진행바·reveal·카운터, 포인터 spotlight·tilt, SVG 에코시스템 애니메이션, 한/영 전환, 방향키 지원 뷰어, prefers-reduced-motion 대응). 그러나 프로젝트 영역의 상호작용은 '썸네일을 눌러 큰 화면을 바꾸는 갤러리' 하나뿐이고(main.js viewer()), 6개 행이 같은 템플릿(제목·설명, 프레임+썸네일 줄, 불릿, 칩, Get it, 버튼)이다. 1056~1920px 폭 UI 스크린샷을 약 660px 프레임에 통째로 줄여 넣어 글자가 읽히지 않고, 3D PCB·3D 웨이퍼·Raw Buffer Visualizer·Labeling의 포스터(첫 프레임)가 모두 빈 화면이라 10~20초 판단 구간에서 '결과'가 나오기 전에 이탈할 수 있다. 가장 강한 증거(Labeling VisA PCB4 실측 표, 2D의 검출 5 OK / 검출 2 NG, 3D의 값 대 한계 2079.53 vs 1502-1913)는 README에 이미 있으나 화면에 숫자로 나오지 않거나 6번째 썸네일에 묻혀 있다. 권장 방향: 모든 프로젝트에 같은 4칸 증거 띠(입력 → 설정 → 결과 → 판정 근거)와 결과 한 줄 칩(값·한계·판정)을 두고, 프로젝트마다 성격이 다른 인터랙티브 1개(파이프라인 스테퍼+OK/NG 토글, 모델 A/B 토글, 로트 8칸 보드, 6탭 플레이어, 코드↔경계 스테퍼, 전/후 슬라이더)를 붙인다. 새 촬영 없이 되는 개선(포스터 교체, 빈 구간 컷, GIF→mp4, RBV 전/후 슬라이더, Labeling 실측 카드)을 먼저 하고, 새 촬영은 2D → Machine Studio → 3D 로트 순으로 한다.

## 읽은 자료

- README 영문 전부: README_OpenVisionLab.md, README_OpenVisionLab-Labeling-Studio.md, README_OpenVisionLab-3D-Studio.md, README_OpenVisionLab-Machine-Studio.md, README_OpenVisionLab-Vision-SDK.md, README_RawBufferVisualizer.md, README_Noah8218.md, stats.md
- 한국어 README: README_ko_RawBufferVisualizer_overview.md (픽셀 형식 목록, Automatic Inspector, Buffer Doctor 절 확인). 나머지 README_ko_* 는 영문 본문과 같은 내용이라 읽지 않음
- meta_OpenVisionLab.json, meta_RawBufferVisualizer.json (topics, license, star 확인). 나머지 meta 는 열지 않음
- 사이트(읽기 전용): index.html (hero, projects, ecosystem 구간), js/main.js 전체, css/style.css (최신 CSS 기능 grep), assets/manifest.json
- 에셋 직접 열람: ovl-inspection-stages, ovl-sample-catalog, lab-detection-washer, lab-segmentation-bubble, lab-anomaly-grid-disk, lab-visa-pcb4-test-result, lab-hero-smart-mask.poster, lab-multimodel-comparison.poster, 3d-pcb-lot-inspection.poster, 3d-pcb-teach, 3d-pcb-result-ng, 3d-wafer-teach, 3d-coupon-height, ms-* 6장, rbv-manual-stride-before/after, rbv-debugger-memory-image.poster, sdk-matching-result
- 움직이는 에셋: ffprobe 로 길이·프레임 확인 후 ffmpeg 컨택트시트(임시 컨택트시트)로 내용 확인: ovl-tool-settings.mp4, ovl-preprocessing-chains.mp4, lab-hero-smart-mask.gif, lab-multimodel-comparison.gif, 3d-pcb-lot-inspection.gif, 3d-wafer-lot-inspection.gif, rbv-debugger-memory-image.gif
- 화면 캡처: 스크린샷 캡처, 레퍼런스 사이트 캡처, 레퍼런스 덱 A 장면 04·08, 레퍼런스 덱 B 장면 04, 그리고 이번에 새로 찍은 스크린샷 캡처

## 미디어 실측

- ovl-tool-settings.mp4 = 1600x900, 12 fps, 35.67 s, 1,375,270 B (약 38.5 KB/s). ovl-preprocessing-chains.mp4 = 1600x900, 12 fps, 36.17 s, 1,101,047 B (약 30.4 KB/s)
- lab-hero-smart-mask.gif = 1056x536, 7 프레임, 9.3 s, 프레임 시각 0/1.6/2.8/5.8/5.9/6.2/7.4 s. lab-multimodel-comparison.gif = 1056x574, 12 프레임, 11.6 s
- 3d-pcb-lot-inspection.gif = 1100x942, 12 fps, 20.33 s. 3d-wafer-lot-inspection.gif = 1100x942, 12 fps, 24.83 s. rbv-debugger-memory-image.gif = 1920x1044, 10 fps, 4.0 s
- GIF 5개 합계 4,852,368 B -> 같은 해상도 H.264 mp4(crf 30, 무음)로 변환하면 1,263,580 B (PCB 1,169,935 -> 278,903 / 웨이퍼 1,472,101 -> 526,899 / Smart Mask 730,212 -> 87,664 / 멀티모델 993,467 -> 184,636 / RBV 486,653 -> 185,478). 화질은 눈으로 검수하지 않았고 산출물이 아니라 용량 측정용 임시 파일임
- ovl-tool-settings.mp4 앞 12 s 를 1280 폭으로 줄인 시험 = 112,408 B (내용 선택과 무관한 용량 참고값)
- site/assets 합계 9,354,962 B (du -sb). 1440x900 뷰포트에서 미디어 프레임 폭 약 660px 에 1056~1920px 폭 스크린샷이 들어감(스크린샷 캡처)

## 프로젝트별 표현안

### 1. 2D Workbench

- **핵심 메시지**: Tool을 PropertyGrid 파라미터·ROI·판정 한계로 티칭하고 Pipeline으로 이어 Recipe로 저장한 뒤, 같은 Recipe를 Good/Bad 샘플에 일괄 적용해 OK/NG와 그 근거를 확인한다.
- **근거**: Build and validate rule-based 2D inspection Recipes on Windows with OpenCvSharp 4 and C#. / Check the same Recipe against Good and Bad samples with Batch inspection. / the original returns 5 detections / OK and the missing-shape image returns 2 detections / NG: 1 OK, 1 NG and 0 errors.
- **현재 상태**: 미디어 4개 중 영상 2개가 35.7 s / 36.2 s(1600x900, 12 fps)라 10~20초 판단 구간을 넘고, 썸네일 4개 중 첫 두 개는 재생 아이콘뿐이라 무엇이 나오는지 미리 볼 수 없다(스크린샷 캡처). 영상은 Matching·Line·Blob·Contour 설정을 순서대로 보여 주는 설명용이며(컨택트시트 기준 대략 0~10 s Matching, 10~18 s Line, 18~26 s Blob, 26~36 s Contour, 4 s 간격 표본이라 추정), 이 프로젝트의 결정적 장면인 'Good은 OK, Bad는 NG' 한 화면 비교가 어떤 에셋에도 없다. 가장 정보가 많은 정지 이미지(4분할 Layer + Results, ovl-inspection-stages)는 3번째 썸네일이고 영상 포스터로만 쓰인다. 4번째 썸네일(Sample Catalog)은 샘플 이름 목록뿐이라 Good/Bad 쌍 구조가 안 보인다. Get it 문단은 공개 ZIP(v2.1.0-rc.3)이 화면의 소스 워크플로(v2.2.0-dev.12)보다 오래됐다고 밝히지만, 방문자가 ZIP으로 실제로 볼 수 있는 범위를 시각적으로 구분하지는 않는다. 정지 UI가 약 660px 프레임으로 축소돼 Results 표 글자가 읽히지 않는다.
- **기존 자료 활용**:
  - (1) 4분할 PNG(ovl-inspection-stages.webp, 1600x900)를 첫 화면 정지 이미지로 올리고 번호 지시선 4개를 얹는다: 1 Pipeline 5 steps, 2 4-up Layer(원본/Filtered/Binary/Clean), 3 Results(Blob 34 items, Contour 34 items), 4 Final verdict OK 2/2.
  - (2) 두 mp4는 뒤로 보내 '자세히' 용도로 두고, 각각 앞 12 s 클립이나 Tool 챕터 탭(Matching, Line, Blob, Contour; video.currentTime 이동)으로 쪼갠다. 구간 시작 시각은 4 s 표본 추정이라 확정 전에 영상을 직접 확인한다.
  - (3) 같은 4분할 PNG에서 960x720 Layer 4장과 Results 표를 사전 크롭(webp)해 아래 인터랙티브 모듈의 소재로 쓴다.
  - (4) ovl-sample-catalog.webp는 이름 목록만 있으므로 README의 8쌍 표(Matching, Blob, Contour, Threshold, Mean, FeatureMatching, EdgeBasedMatching, Line)를 HTML 표나 칩으로 대신 보여 주고, 이미지는 보조로 내린다.
  - (5) README가 링크하는 recipe-teaching.gif, recipe-validation.gif, sample-inspections.gif, pipeline-results.png는 사이트에 없다. 저장소에서 존재와 최신 UI 반영 여부를 먼저 확인하고 쓸 수 있으면 신규 촬영 비용이 준다(README도 '녹화물은 이후 UI 변경을 검증하지 않는다'고 적음).

#### 증거 장면

| 순서 | 장면 | 설득되는 이유 | 누구에게 |
|---|---|---|---|
| 1 | 입력: Sample Catalog에서 공개 샘플 이미지(Contour 쌍의 Good)를 연다. | 공개 샘플이라 방문자가 같은 입력으로 재현할 수 있다는 신호가 된다. | C#/.NET 개발자, 현업 엔지니어 |
| 2 | 설정 1: Threshold를 150으로 두고 F8로 실행해 원본과 binary를 나란히 비교한 뒤 Add to pipeline. | 파라미터 하나가 결과 이미지를 즉시 바꾸는 것을 보여 주면 '툴을 티칭한다'가 설명 없이 이해된다. | 현업 엔지니어 |
| 3 | 설정 2(판정 규칙): Contour ROI를 다섯 도형 둘레에 그리고 Acceptance > Detection count의 Lower/Upper를 5로 둔 뒤 F8로 '5' 확인, Ctrl+Enter로 Step 추가. | 측정값과 한계가 OK/NG 근거로 이어지는 지점이다. README가 밝히듯 Acceptance가 없으면 OK/NG 판정 없이 끝날 수 있으므로 이 장면이 빠지면 안 된다. | 현업 엔지니어, 채용 담당자(판정 규칙이 있다는 것) |
| 4 | 결과: F5로 Pipeline 실행 후 Results 표와 1/2/4분할 Layer 비교(원본·중간·출력), Final verdict. | 중간 Layer와 판정 근거가 한 화면에 있어 '왜 OK인가'에 답한다. 4분할 PNG에는 Blob·Contour가 각각 34 items, Final verdict OK 2/2 judged steps OK가 이미 찍혀 있다. | 현업 엔지니어 |
| 5 | 검증: Ctrl+S로 저장하고 다른 Recipe로 갔다 돌아와 재로드, 이어서 Good/Bad 이미지에 Batch inspection. 검출 5 / OK, 검출 2 / NG, '1 OK, 1 NG and 0 errors'. | 규칙이 불량을 실제로 가른다는 가장 직접적인 증거이고, 저장·재로드는 Recipe가 XML로 남는다는 개발자용 증거다. | 세 부류 모두(채용 담당자는 OK/NG 색 변화만 봐도 이해) |

#### 촬영 목록(대본)

##### 1. Shape Count: 검출 5 -> OK, 검출 2 -> NG (편집본 12초)

- **길이(초)**: 12
- **형식**: mp4(H.264) 1280x720, 15 fps, 무음. 필요하면 webm 추가. poster는 마지막 결과 프레임. 영상에 '편집본(유휴 시간 생략)' 자막(Labeling README의 GIF 표기 방식과 동일).
- **목표 용량**: 600 KB 이하(기존 mp4 실측 30~39 KB/s 기준 12 s = 0.4 MB 안팎, 1280 폭 시험 클립 112 KB)
- **강조 지점**: 단계 번호 칩 1~5(우상단), Threshold 값 150, Contour ROI 외곽선, 'Lower 5 / Upper 5' 입력칸, 마지막 두 결과 행의 OK(초록)/NG(빨강)와 숫자 5, 2를 확대.
- **촬영 팁**: UI 배율을 125~150%로 올려 글자를 키운다. 커서를 크게 하고 클릭 링을 켠다. F8/F5/Ctrl+S 단축키를 화면 아래 키 오버레이로 띄운다. 로딩·유휴 구간은 컷하고 속도 4~8배 편집, 무음. 소스 빌드(v2.2.0-dev.12)에서 찍으므로 캡션에 'source build'를 적는다(공개 ZIP은 v2.1.0-rc.3). Step 5(Acceptance)를 생략하지 않는다.
- **필요한 샘플 데이터**: README 표의 Public_Contour_Shapes_Good, Public_Contour_Shapes_Missing_Bad (README의 '원본/누락 이미지'와 같은 파일인지 촬영 전에 확인)

###### 클릭 단계

- Recipe Manager에서 Shape Count를 만들고 Open work with selected inspection으로 Contour 쌍의 Good 이미지를 연다(0~1.5초).
- Threshold를 열고 Run on change를 끈 뒤 값을 150으로 입력, Run tool(F8)을 눌러 원본과 binary를 비교한다.
- Add to pipeline > Add at end를 누른다.
- Contour를 열어 입력이 Threshold_1인지 보이게 하고, Use threshold를 끈 뒤 다섯 도형 둘레에 ROI를 그리고 Enter.
- Acceptance를 켜고 Detection count 선택, Lower·Upper를 체크해 둘 다 5로 입력, F8로 검출 5를 확인하고 Ctrl+Enter로 Step 추가.
- F5로 Pipeline 실행, Results의 OK와 2분할 Layer(원본/출력)를 보인다.
- Ctrl+S로 저장한다.
- Good·Bad 이미지를 추가해 Good/Bad 라벨을 지정하고 Batch inspection 실행.
- 결과 두 행을 1.5초 정지: 검출 5 / OK, 검출 2 / NG, 요약 '1 OK, 1 NG, 0 errors'.

##### 2. 공개 ZIP으로 첫 결과까지 3단계 (편집본 9초)

- **길이(초)**: 9
- **형식**: mp4 1280x720, 15 fps, 무음
- **목표 용량**: 400 KB 이하
- **강조 지점**: ZIP 파일명, OpenVisionLab.exe, Sample Catalog의 Good 선택 행, 결과 score. 상단 배지 'published ZIP v2.1.0-rc.3'.
- **촬영 팁**: 깨끗한 Windows VM이나 Windows Sandbox(README가 BUILD.md에서 언급)에서 촬영해 사용자 이름·개인 경로가 안 보이게 한다. 이 클립은 rc.3 범위만 보여야 하고, 소스 워크플로(Recipe 신규 작성 등)를 섞지 않는다.
- **필요한 샘플 데이터**: 공개 샘플 Public_Matching_DiePad_Good (Sample Catalog 내장)

###### 클릭 단계

- GitHub Releases에서 v2.1.0-rc.3 win-x64 ZIP 목록을 보인다(다운로드 대기는 생략 표기).
- 새 폴더에 압축을 푼다(짧은 폴더명 사용).
- .NET 8 Desktop Runtime(x64) 필요 문구를 README 한 줄 오버레이로 2초 보인다.
- OpenVisionLab.exe를 실행한다.
- Sample Catalog를 열고 Public_Matching_DiePad_Good을 선택한다.
- Add image로 추가한다.
- Preview 또는 Run을 누른다.
- Matching 결과 오버레이와 score가 뜬 프레임에서 정지.

##### 3. Good/Bad 쌍 결과 정지 이미지 2장 + 판정 근거 패널

- **길이(초)**: 0
- **형식**: 정지 이미지 3장, 1600x900 PNG를 webp로 변환
- **목표 용량**: 장당 120 KB 이하(기존 정지 이미지 39~105 KB)
- **강조 지점**: Detection count 5 vs 2, Lower/Upper 5 칸, OK(초록)/NG(빨강) 뱃지, 두 이미지에서 같은 위치에 있는 결과 행.
- **촬영 팁**: 두 장의 창 크기·패널 배치·줌을 똑같이 맞춰야 토글할 때 화면이 튀지 않는다.
- **필요한 샘플 데이터**: 위와 같은 Good/Bad 쌍 + 저장된 Shape Count Recipe

###### 클릭 단계

- Batch inspection 결과 목록에서 Good 이미지를 선택한다.
- 원본 패널, 처리 이미지, 오버레이, Acceptance 한계(Lower 5/Upper 5)와 검출 5가 한 화면에 보이게 배치한다.
- 정지 이미지를 저장한다(1600x900).
- Page Up/이미지 선택으로 Bad(누락) 이미지로 이동한다.
- 같은 패널 구성·같은 줌으로 검출 2 / NG가 보이게 둔다.
- 정지 이미지를 저장한다.
- Pipeline Review를 열어 acceptance 범위·값과 OK/NG 사유가 보이게 한 장을 더 저장한다(저장소의 pipeline-results.png가 있으면 그것을 우선 재사용).

#### 인터랙티브 모듈

- **이름**: Layer 스테퍼 + Good/Bad OK/NG 토글
- **설명**: 상단 단계 칩 [원본 | Filter | Threshold | Morphology | Blob·Contour]을 누르면 같은 프레임의 이미지가 해당 Layer(960x720)로 바뀌고, 옆 작은 표에 그 Step의 결과가 나온다(예: Blob 34 items, Contour 34 items). 아래 [Good | Bad] 토글을 누르면 'Detection count 5, 한계 5-5, OK' 초록 게이지와 '2, NG' 빨강 게이지가 바뀌고 이미지가 교체된다. 화살표 키 지원, aria-pressed로 상태 표시.
- **필요한 자료**: Layer 이미지 4장과 Results 표 1장은 기존 ovl-inspection-stages.webp를 사전 크롭해 만든다(추가 촬영 없음). Good/Bad 결과 스크린샷 2장은 위 촬영 3번.
- **정적 사이트에서 가능한가**: 가능. <img> 교체와 버튼만 쓰고 의존성이 없다. 현재 viewer()의 thumbs/aria-pressed/방향키 패턴을 그대로 확장하면 된다. 사전 크롭 webp는 장당 수십 KB 수준으로 예상(미측정).

#### 보조 인터랙티브 모듈

- **이름**: Tool 챕터 탭 (Matching / Line / Blob / Contour)
- **설명**: 기존 mp4 한 개에서 챕터 칩을 누르면 해당 구간으로 currentTime을 옮기고 그 Tool의 README 설명 한 줄을 보인다(Matching: 템플릿·score·검출, Line: Edge/Distance/Intersection 모드, 핀 간격 측정, Blob: 입자 검출·개수 한계, Contour: ROI·개수 한계).
- **필요한 자료**: 기존 mp4 두 개. 챕터 시작 시각은 영상을 직접 보고 확정.
- **정적 사이트에서 가능한가**: 가능. video.currentTime 설정만 필요하고 추가 용량이 없다.

#### 데이터 포인트(원문 근거 있는 값)

- 5 detections / OK, 2 detections / NG, 1 OK, 1 NG and 0 errors (README 문장). 주의: '5 OK / 2 NG'로 줄이면 이미지 수로 읽힐 수 있으니 '검출 5 -> OK, 검출 2 -> NG'로 쓴다.
- Threshold 150, Lower/Upper 5 (README 절차 3~4)
- Filter -> Threshold -> Morphology 뒤 Blob과 Contour가 모두 34 accepted holes (README)
- 공개 샘플 Good/Bad 8쌍: Matching, Blob, Contour, Threshold, Mean, FeatureMatching, EdgeBasedMatching, Line (README 표). 측정값 이름 ResultCount, ScoreMax, MeanValueAvg, DistanceMmAvg
- Pipeline Review 지표: ResultCount, AreaMax, ScoreMax, LineAngleAvg (README)
- Guide: workflow 절과 17 Tool chapters (README)
- 단축키 F8 Run step, F5 Run pipeline, Ctrl+S 저장, Ctrl+Enter Step 추가 (README)
- 소스 v2.2.0-dev.12 / 공개 ZIP v2.1.0-rc.3 / Apache-2.0 / Star 15 (README, stats.md)
- 에셋 화면에서만 확인되는 값(README 문장 아님, 성능 주장으로 쓰지 말 것): 4분할 PNG의 'Pipeline run completed OK 585 ms', Final verdict OK 2/2 judged steps OK

#### 부족한 자료

- Good과 Bad의 결과가 같은 구도로 나란히 있는 이미지 없음(촬영 3).
- '공개 ZIP으로 볼 수 있는 범위' 영상 없음(촬영 2). ZIP과 소스 워크플로의 차이를 시각적으로 구분하는 자료도 없음.
- README가 링크한 recipe-teaching.gif, recipe-validation.gif, sample-inspections.gif, pipeline-results.png 를 사이트가 쓰지 않음. 파일 존재·용량·최신 UI 반영 여부는 미확인.
- Recipe XML 한 조각(Step, 파라미터, Layer 연결). 저장소의 Product_Field_PerforatedPlate_Inspection.pipeline.xml이 README에 링크돼 있으므로 일부를 코드 탭으로 노출하면 개발자용 증거가 된다(내용 미확인).
- KO 모드에서도 영상·스크린샷 UI는 영어. README는 한/영 UI 전환이 있다고 하므로 KO 클립은 선택 사항.

#### 방문자별 가치

- **현장 엔지니어**: Acceptance 한계(Lower/Upper)와 Detection count가 OK/NG로 이어지는 과정, Good/Bad로 같은 Recipe를 검증하는 흐름.
- **리크루터**: 검출 5 -> OK, 검출 2 -> NG가 한 화면에서 바뀌는 12초 영상과 Usable 상태, Apache-2.0, Star 15.
- **.NET 개발자**: Recipe가 XML로 저장·재로드되고 Pipeline/Layer 구조가 보이는 것, OpenCvSharp 4 기반, 소스 빌드 후 F5 또는 ZIP 3단계.

### 2. Labeling Studio

- **핵심 메시지**: 산업 이미지에 박스·마스크·OK/NG 라벨을 붙이고, 같은 데이터 버전으로 여러 모델을 학습·비교해 검사 모델을 지정한 뒤 추론까지 한 PC에서 한다. AI 결과는 후보일 뿐이고 확정과 저장은 사람이 따로 한다.
- **근거**: A Windows desktop tool for labeling industrial images, training and comparing models, and running inference on one PC. / AI results are candidates for review. The operator confirms the result and saves the labels as separate actions.
- **현재 상태**: 6개 미디어가 있으나
  - (a) 첫 화면이 Smart Mask GIF의 첫 프레임, 즉 박스 도구만 선택된 주석 없는 기포 이미지라 이 도구가 무엇을 하는지 포스터만으로는 안 보인다(스크린샷 캡처).
  - (b) Smart Mask GIF는 7프레임·9.3 s의 키프레임 슬라이드(프레임 시각 0/1.6/2.8/5.8/5.9/6.2/7.4 s)이고, 멀티모델 GIF는 12프레임·11.6 s에 1056px 폭이라 약 660px 프레임에서 글자가 읽히지 않는다.
  - (c) 이 프로젝트에서 '진짜 되나'에 가장 직접 답하는 VisA PCB4 실측(1,105장, test 불량 40장/정상 402장, YOLOv8n mAP50 0.747, 놓친 불량 3/40, 정상 오검출 4/402)은 6번째 썸네일의 이미지 한 장이고, 숫자는 사이트 어디에도 없다(index.html에 0.747 없음, Releases에 서술 한 줄뿐).
  - (d) Detection/Segmentation/Anomaly 세 Task와 모델 목록(README 표)이 썸네일 사이에 섞여 구조가 안 보인다.
  - (e) 멀티모델 포스터는 작은 썸네일 벽(Dataset 화면)이라 의미가 읽히지 않는다.
- **기존 자료 활용**:
  - (1) 첫 화면을 VisA PCB4 카드로 바꾼다: lab-visa-pcb4-test-result.webp(1358x1104)를 왼쪽에, 오른쪽에 README 표를 HTML 표로(텍스트라 용량 0, 접근성 유리) 넣고 범례 3색을 이미지 아래에 적는다. 데이터 출처(VisA, CC BY 4.0)는 현재 footer와 vnote에 있으므로 같은 카드 하단에 병기한다.
  - (2) Detection/Segmentation/Anomaly는 탭 3개로 묶고, 각 탭에 README 표의 Ground truth·Models 두 줄을 붙인다. 이미지는 기존 3장(1600x812)을 그대로 쓰고, 와셔에는 번호 지시선 3개(클래스 목록 washer 4/defective washer 1, Objects 5, Save and next Ctrl+Enter)를 얹는다.
  - (3) 멀티모델 GIF는 앞 5 s(Dataset, New training, 진행)를 잘라 '비교 -> 검사 모델 지정 -> 추론' 구간만 쓰고, 포스터를 마지막 추론 프레임(washer_ok 0.97 등 박스)으로 바꾼다.
  - (4) README가 hero-smart-mask.mp4와 multimodel-comparison.mp4를 제공하므로(원본 해상도·프레임율은 미확인) GIF 대신 mp4를 쓴다. 현재 GIF를 mp4로 변환하면 730 KB -> 88 KB, 993 KB -> 185 KB(실측).

#### 증거 장면

| 순서 | 장면 | 설득되는 이유 | 누구에게 |
|---|---|---|---|
| 1 | 데이터: Dataset 화면에서 이미지 수, 클래스, Train/Valid/Test 분할을 보인다. 에셋 화면에는 와셔 300장, Train 210/Valid 45/Test 45, 클래스 2개가 보인다(README 문장은 아니고 화면 값). | '한 Recipe가 이미지·클래스·분할·버전을 묶는다'는 구조를 첫 장면에서 보여 준다. | 현업 엔지니어, 개발자 |
| 2 | 라벨링과 AI 후보: 시작 박스를 그리면 MobileSAM 후보가 뜨고, Include/Exclude 점으로 고친 뒤 Confirm, 이어서 Save and next(Ctrl+Enter). | AI가 후보를 내고 사람이 확정·저장하는 두 동작이 분리돼 있다는 제품 원칙을 장면으로 보여 준다. | 현업 엔지니어, 채용 담당자(제품 철학) |
| 3 | 학습·비교: 같은 데이터 버전으로 YOLOv8n과 YOLO11n을 학습하고 테스트 분할에서 비교(A와 B의 차이, 클래스별 AP, confidence별 F1·recall, 이미지별 일치도). | '모델을 학습시킨다'가 아니라 '같은 조건에서 비교해 고른다'가 보인다. 조건이 다르면 순위 대신 차이로 표시한다는 점도 신뢰 근거다. | 현업 엔지니어 |
| 4 | 지정과 추론: 비교 결과에서 검사 모델로 지정(Undo로 이전 모델 복원 가능)한 뒤 Inference에서 박스와 confidence 확인. | 학습 완료가 곧 모델 교체가 아니라 명시적 지정 단계가 있다는 점이 운영 사고 방지 설계로 읽힌다. | 현업 엔지니어, 채용 담당자 |
| 5 | 실데이터 증거: VisA PCB4 결과 이미지(초록=찾음, 주황=놓침, 얇은 흰색=정답)와 YOLOv8n/YOLO11n 표. | 실제 PCB 사진 1,105장에서 놓친 불량 3/40 vs 8/40, 오검출 4/402 vs 1/402의 trade-off까지 정직하게 보여 주고, '양산 정확도의 근거가 아님'이라는 한계를 같이 적었다. | 세 부류 모두 |

#### 촬영 목록(대본)

##### 1. Smart Mask: 후보 -> 확정 -> 저장 (고해상도 재촬영 10초)

- **길이(초)**: 10
- **형식**: mp4 1280x720(캔버스+우측 패널 크롭), 15 fps, 무음. poster는 확정 프레임.
- **목표 용량**: 250 KB 이하(기존 GIF를 mp4로 바꾼 실측 88 KB/9.3 s)
- **강조 지점**: 후보 외곽선, Include 점, Confirm 버튼, Save and next(Ctrl+Enter) 키 캡, Saved 배지.
- **촬영 팁**: 후보 생성 대기(모델 로딩)는 컷한다. Python과 MobileSAM 가중치가 필요하다(README: 모델별 요구 사항)고 했으므로 촬영 PC 환경을 먼저 갖춘다. runtime environment 패널과 개인 경로를 열지 않는다. 커서를 크게.
- **필요한 샘플 데이터**: 필름 기포 예시(현재 사이트 GIF에 쓰인 데이터). 저장소에 포함된 데이터인지, 사용 허가가 있는지 확인 필요.

###### 클릭 단계

- Segmentation 레시피의 Labeling 탭에서 기포 이미지를 열고, Labeling options의 Automatic contour가 켜진 상태를 확인한다.
- Box 도구로 대상 위에 시작 박스를 드래그한다.
- MobileSAM 후보가 뜨는 장면을 1초 유지하고 'AI 후보' 라벨을 오버레이한다.
- 후보가 어긋난 경우 Include 점을 한 번 찍고 Regenerate candidate, Previous/Current candidate 비교가 보이게 한다.
- Confirm을 눌러 마스크가 확정되는 것을 보인다.
- 오른쪽 Objects 목록에 1 bubble이 생긴 것을 확인한다.
- Ctrl+Enter(Save and next)로 저장하고 다음 이미지로 이동, 상단 Saved 상태를 보인다.
- 하단 자막: 'AI 후보 != 저장된 라벨. Confirm과 Save는 별도 동작'.

##### 2. 비교 -> 검사 모델 지정 -> 추론 (고해상도 재촬영 12초)

- **길이(초)**: 12
- **형식**: mp4 1280x720, 15 fps, 무음. 영역별 줌(패널 단위) 편집
- **목표 용량**: 400 KB 이하(기존 GIF를 mp4로 바꾼 실측 185 KB/11.6 s)
- **강조 지점**: Recommended 배지, A-B 차이 숫자, 검사 모델 지정 버튼, 추론 박스의 confidence.
- **촬영 팁**: UI 배율을 150%로 하거나 패널 단위로 확대 편집한다(현재 GIF는 글자가 읽히지 않음). 캡션에 '합성 와셔 데이터셋'을 적는다(README: 0.4.3 비교는 합성 와셔 데이터셋에서만 검증).
- **필요한 샘플 데이터**: 합성 와셔 데이터셋과 학습 완료된 두 모델(이미 학습·비교 기록이 있으면 재사용)

###### 클릭 단계

- Comparison 탭에서 같은 데이터 버전으로 학습된 YOLOv8n과 YOLO11n 행과 Recommended 표시를 보인다.
- A와 B의 차이 패널(mAP 등)에 포인터를 올려 강조한다.
- 클래스별 AP와 confidence별 F1/recall 그래프를 지나간다.
- 이미지별 일치도에서 두 모델이 다르게 본 이미지를 골라 박스를 나란히 보인다.
- 검사 모델로 지정 버튼을 누르고 확인 대화상자에서 확인한다.
- Inference 탭으로 이동해 이미지를 고른다.
- 추론을 실행해 박스와 confidence(예: washer_ok 0.97)를 보인다.
- (선택) Undo로 이전 모델을 복원할 수 있다는 안내를 1초 보인다.

##### 3. VisA PCB4 같은 이미지에서 모델 2종 비교 정지 이미지

- **길이(초)**: 0
- **형식**: 정지 이미지 1장(YOLO11n), 1358x1104 PNG를 webp로 변환
- **목표 용량**: 250 KB 이하(기존 YOLOv8n 이미지 245 KB)
- **강조 지점**: 놓친 결함(주황 박스), 범례 3색, 'Confidence 0.25, input 960 px' 문구.
- **촬영 팁**: 이미지 출처 표기(VisA, Zou et al., ECCV 2022, CC BY 4.0)를 카드에 병기한다. 이미지에 앱 UI를 넣지 않고 결과 이미지만 export하는 편이 크롭이 쉽다.
- **필요한 샘플 데이터**: VisA PCB4 데이터와 이미 학습한 YOLOv8n/YOLO11n 모델(README에 학습·비교 완료로 기록됨, 로컬 보관 여부 확인)

###### 클릭 단계

- 현재 사이트에 있는 VisA PCB4 test 이미지(YOLOv8n 결과)와 같은 이미지를 선택한다.
- 신뢰도 0.25, 입력 960 px, 같은 표시 옵션인지 확인한다.
- YOLOv8n 결과를 저장한다(기존 이미지가 있으면 그대로 사용).
- Comparison의 A/B 전환 또는 추론 모델 교체로 YOLO11n 결과를 만든다.
- 같은 크롭으로 저장한다(찾음=초록, 놓침=주황, 정답=얇은 흰색 규칙 유지).
- 두 이미지에서 놓친 결함의 위치가 같은지 확인하고 캡션에 쓴다.

#### 인터랙티브 모듈

- **이름**: 모델 A/B 토글 (YOLOv8n <-> YOLO11n)
- **설명**: VisA PCB4 이미지 위에 [YOLOv8n | YOLO11n] 토글을 둔다. 전환하면 박스 결과 이미지가 바뀌고 오른쪽 표의 해당 행이 강조된다: mAP50 0.747 / 0.723, 놓친 불량 3/40 / 8/40, 정상 오검출 4/402 / 1/402, TensorRT FP16 GPU 0.76 / 0.82 ms. 큰 숫자 하나('놓친 불량')가 전환 시 3에서 8로 바뀐다. 하단 고정 문구: 단일 데이터셋, 불량 40장, 양산 정확도 근거 아님.
- **필요한 자료**: YOLO11n 결과 이미지 1장(촬영 3). YOLOv8n 이미지와 표는 기존.
- **정적 사이트에서 가능한가**: 가능. 이미지 src 교체와 표 행 class 토글, 숫자 카운트(기존 count() 재사용)만 필요하고 의존성이 없다.

#### 보조 인터랙티브 모듈

- **이름**: Smart Mask 5단계 스텝 플레이어
- **설명**: 박스 -> AI 후보 -> 점 보정 -> Confirm -> Save and next 다섯 정지 프레임을 좌우 키·버튼으로 넘기고, 각 단계에 한 줄 설명과 'Confirm != Save' 배지를 붙인다. GIF 자동 재생 대신 사용자가 속도를 정한다.
- **필요한 자료**: 촬영 1에서 추출한 정지 프레임 5장(프레임당 50~90 KB 예상, 미측정). 임시로는 기존 GIF 7프레임에서 추출 가능하나 1056px 폭이라 글자가 작다.
- **정적 사이트에서 가능한가**: 가능. 현재 viewer()의 keydown 처리와 같은 패턴.

#### 데이터 포인트(원문 근거 있는 값)

- VisA PCB4: real PCB photos 1,105장(1358x1104), test 불량 40장/정상 402장 (README)
- YOLOv8n: mAP50 0.747, 놓친 불량 3 / 40, 정상 오검출 4 / 402, TensorRT FP16 GPU 0.76 ms / YOLO11n: 0.723, 8 / 40, 1 / 402, 0.82 ms. Confidence 0.25, input 960 px, RTX 4070 SUPER (README)
- 'These results come from one dataset with 40 defective test images and are not evidence of production accuracy.' (README, 화면에 같이 표시)
- 지원 Task x 모델 (README 표): Detection = 축 정렬 박스, YOLOv5·YOLOv8·YOLO11 / Segmentation = 폴리곤·픽셀 마스크, YOLOv8-seg·YOLO11-seg·U-Net / Anomaly = 이미지 단위 OK/NG, YOLOv8/YOLO11 classification·PatchCore(pilot)
- 워크플로 5단계: Dataset, Labeling, Training, Model comparison, Inference (README)
- 와셔 예시 박스 5개 = 와셔 4 + 불량 와셔 1, 기포 마스크 9개, 육각형 12장 = 정상 4·이상 4·미판정 4 (README)
- 내용 기반 데이터셋 버전 dsv2-... 와 SHA-256 식별 (README)
- 단축키: 1-9 클래스 선택, Ctrl+Enter 저장 후 다음, G 그리드 (README)
- v0.4.4 / MIT / Star 6 (README, stats.md)

#### 부족한 자료

- Smart Mask 단계별 정지 프레임(고해상도) 없음 -> 촬영 1.
- VisA에서 YOLO11n 결과 이미지 없음 -> 촬영 3. 지금은 YOLOv8n 한 장뿐이라 두 모델의 차이가 이미지로는 안 보인다.
- Comparison 화면(표, A-B 차이, per-image agreement)이 읽히는 크기의 정지 이미지 없음 -> 촬영 2.
- PatchCore heatmap('View heatmap') 화면 없음. Anomaly 탭의 핵심 증거(이미지 판정, score/threshold, 위치 후보, heatmap)이며 pilot 표기 필요.
- Dataset version(Identity details) 화면 없음.
- 엣지 런타임(0.4.1/0.4.2: ONNX, TensorRT, Modbus TCP/OPC UA, Prometheus/Grafana)은 README에 서술만 있고 화면 자료가 없다. README가 '시뮬레이터에서만 테스트, Machine Studio 연동 미검증'이라고 적었으므로 보여 줄 때도 그 한계를 같이 쓴다.

#### 방문자별 가치

- **현장 엔지니어**: VisA PCB4 표의 놓친 불량 3/40 vs 8/40, 정상 오검출 4/402 vs 1/402: 모델 선택의 trade-off와 '양산 정확도 근거 아님'이라는 한계 표기.
- **리크루터**: AI는 후보, 확정·저장은 사람이라는 원칙과 데이터 -> 학습 -> 비교 -> 추론 5단계를 한 도구로 구현한 범위.
- **.NET 개발자**: .NET 8·WPF, 빌드 명령 2줄, Python 런타임과 가중치는 모델별 별도 준비(README), Python TCP 프로토콜 예제 링크.

### 3. 3D Studio

- **핵심 메시지**: 3D 데이터(C3D height map)에서 검사 Step을 티칭하고 Recipe로 저장해 같은 형식의 여러 파일에 반복 적용하며, 파일별 측정값과 한계를 본다.
- **근거**: Teach inspection steps on 3D data, save a recipe, and apply it to compatible files. / One recipe inspects a lot of eight synthetic PCB scans. Five boards pass; the bowed, twisted and thin boards fail, and each failure shows its value and limit.
- **현재 상태**: 6개 미디어 중 가장 강한 두 개(PCB 로트 GIF 20.3 s, 웨이퍼 로트 GIF 24.8 s, 1100x942)의 포스터가 'Untested 8 / OK rate --%'인 빈 앱 화면이라, 사이트의 첫 3D 장면이 결과 없는 화면이다(스크린샷 캡처). GIF는 컨택트시트상 앞 1~2 s가 빈 상태이고 후반 몇 초는 같은 화면이 반복돼 실질 정보 구간이 10~12 s 안팎이다. 설득력이 가장 큰 장면(NG 보드의 Mean 2079.53, 허용 1502-1913, Fail, 원인 문장)은 3번째 썸네일의 정지 이미지로, 썸네일이 작아 눈에 안 띈다. 3D 뷰는 teach 이미지 1장(3d-pcb-teach)뿐이고 나머지는 컬러 높이맵이라 '3D'로는 덜 느껴진다. 합성 데이터(synthetic, raw-height, 보정되지 않음) 고지는 캡션에 있지만 화면에서 '합성'임을 알리는 표식은 없다. 좌측 파일 목록, 가운데 뷰, 하단 결과 표가 한 장에 있고 축소돼 글자를 읽기 어렵다.
- **기존 자료 활용**:
  - (1) 포스터를 결과가 채워진 프레임으로 교체: 로트 완료 후 NG 보드를 선택해 Pass/Fail 목록과 값-한계 표가 모두 보이는 프레임. 현재 GIF의 앞 1~2 s와 뒤 정지 구간을 컷하면 약 10~12 s.
  - (2) 3d-pcb-result-ng.webp(1544x874)를 오른쪽 결과 영역으로 크롭·확대해 번호 지시선 5개: 1 Reference 영역(파란 세로 막대), 2 Measure 영역, 3 Mean 2079.53, 4 허용 1502-1913, 5 Fail과 Cause 문장.
  - (3) 3d-pcb-teach.webp는 3D 뷰이면서 결과 라벨이 붙어 있어 3D 증거 첫 컷 후보.
  - (4) 3d-wafer-teach.webp는 9개 ROI를 핫스팟으로 만든다(아래).
  - (5) 3d-coupon-height.webp는 저장소에 들어 있는 유일한 실행 가능 샘플(Thickness Coupon: 1280 x 840, 8 pad, 16 ROI)이므로 'Try it' 쪽 근거로 옮기고 PCB·웨이퍼는 '합성 데모(입력·Recipe 저장소 미포함)' 배지를 단다.
  - (6) GIF를 mp4로 변환하면 1.17 MB -> 279 KB(PCB), 1.47 MB -> 527 KB(웨이퍼)(실측). viewer()가 이미 <video>를 처리하므로 마크업만 바꾸면 된다.

#### 증거 장면

##### 1. 입력 확인: Recipe와 C3D 입력을 열고 3D / Height / Section 뷰에서 텍스처가 입혀진 합성 PCB 스캔에 측정 라벨(Board meas…

- **순서**: 1
- **장면**: 입력 확인: Recipe와 C3D 입력을 열고 3D / Height / Section 뷰에서 텍스처가 입혀진 합성 PCB 스캔에 측정 라벨(Board measurement 1709.92 OK, IC top 1403.8 OK, 196.27 OK)이 겹쳐 보인다(3d-pcb-teach).
- **설득되는 이유**: 진짜 3D 데이터를 열었다는 첫인상과, 측정 결과가 3D 위에 바로 표시된다는 것을 한 장면에서 보인다.
- **누구에게**: 채용 담당자, 현업 엔지니어

##### 2. 티칭: Reference ROI(기준면)와 Measurement ROI를 짝지어 지정. 웨이퍼는 9지점마다 척 위 기준 ROI가 있다.

- **순서**: 2
- **설득되는 이유**: Thickness가 '기준면 대비 높이차'라는 측정 정의가 ROI 모양으로 한눈에 이해된다. README는 이것이 위·아래 면 사이 두께가 아니라고 밝힌다.
- **누구에게**: 현업 엔지니어

##### 3. 한 파일 결과: 기판 두께 1709.92 (1502-1913), IC 높이 1403.8 (1234-1572), 기판 휨 PV 196.27 (<= 296), 전…

- **순서**: 3
- **장면**: 한 파일 결과: 기판 두께 1709.92 (1502-1913), IC 높이 1403.8 (1234-1572), 기판 휨 PV 196.27 (<= 296), 전부 OK.
- **설득되는 이유**: 값과 허용 범위가 같은 행에 있고 Margin 막대로 여유가 보인다.
- **누구에게**: 현업 엔지니어

##### 4. 로트 검사: 8개 파일을 한 번에 Inspect, OK rate가 오르고 5 Pass / 3 Fail이 확정된다.

- **순서**: 4
- **설득되는 이유**: 한 Recipe가 여러 파일에 반복 적용된다는 점이 결과 목록 하나로 이해된다.
- **누구에게**: 채용 담당자, 개발자(Recipe 재사용)

##### 5. NG 근거: 휜 보드는 2079.53으로 상한 1913 초과, Cause 문장 표시. 웨이퍼는 불량 종류별로 실패 지점이 다르다(연삭 pit은 중앙만, 국소 …

- **순서**: 5
- **장면**: NG 근거: 휜 보드는 2079.53으로 상한 1913 초과, Cause 문장 표시. 웨이퍼는 불량 종류별로 실패 지점이 다르다(연삭 pit은 중앙만, 국소 bulge는 해당 지점만, 비틀림은 반대편 대각 두 점). NG items only로 실패 Step만 나열.
- **설득되는 이유**: '어디가, 얼마나, 한계 대비 어떻게' 나쁜지 설명해 주므로 단순 OK/NG 도구가 아니라 원인 추적 도구로 보인다.
- **누구에게**: 현업 엔지니어

#### 촬영 목록(대본)

##### 1. 로트 8장: 5 Pass / 3 Fail -> NG 원인 (재촬영 12초)

- **길이(초)**: 12
- **형식**: mp4 H.264, 앱이 세로형(1100x942)이므로 결과 영역 위주로 1280x720 재구성하거나 4:3 유지(예: 960x720), 12 fps, 무음
- **목표 용량**: 300 KB 이하(실측: 기존 20 s GIF를 mp4로 변환 279 KB)
- **강조 지점**: Pass/Fail 칩, '값 대 한계' 문장, Fail 빨강 뱃지, 높이 컬러 바(수동 범위 11400-12600 raw-height)는 유지.
- **촬영 팁**: README에 따르면 애니메이션의 마우스 포인터는 기록된 위치에 그려진 것이다. 포인터를 크게 하고 대기 시간은 컷한다. 영어 UI. 합성 데이터이므로 화면 구석에 'synthetic scan' 배지를 얹는다. 기존 GIF의 앞뒤 컷만으로도 1차 해결이 되므로(S) 이 재촬영은 크롭·줌을 포함한 품질 개선용이다.
- **필요한 샘플 데이터**: 합성 PCB 8장과 pcb 레시피(README: 저장소에 없음). 공개 재현은 불가하다는 표기가 필요하다.

###### 클릭 단계

- Inspect 탭에서 8개 파일(체크됨, Untested) 목록을 0.5초만 보인다.
- Inspect 8 checked를 누른다.
- 진행 바와 OK rate가 오르고 행이 Pass/Fail로 채워지는 과정을 가속 편집으로 보인다.
- 상단 요약(Pass 5, Fail 3)을 확대 강조한다.
- NG 파일(휜 보드)을 선택해 높이맵의 Reference/Measure ROI를 보인다.
- 결과 표에서 Board thickness Mean 2079.53, 허용 1502-1913, Fail, Cause 문장을 강조한다.
- NG items only를 체크해 NG 행만 남긴다.
- 다른 NG 보드(얇은 보드)를 선택해 실패 값을 보인다(값은 촬영 때 확인해 캡션에 쓴다).
- 마지막 프레임을 0.8초 정지.

##### 2. 웨이퍼 9지점: 불량마다 다른 실패 위치 (12초)

- **길이(초)**: 12
- **형식**: mp4 H.264 4:3(960x720) 또는 1280x720, 12 fps, 무음
- **목표 용량**: 450 KB 이하(실측: 기존 24.8 s GIF를 mp4로 변환 527 KB, 길이를 절반으로 줄이면 감소 예상)
- **강조 지점**: 9개 ROI 중 실패한 지점의 테두리 색, 컬러 맵의 hot spot, 결과 표의 Fail 행, 웨이퍼 높이 색 수동 범위 10650-10730.
- **촬영 팁**: 어느 웨이퍼가 어느 불량인지는 파일명과 README 서술(연삭 pit, 국소 bulge, 비틀림)을 촬영 전에 맞춰 둔다. 컬러 범위 설정이 바뀌면 hot spot이 안 보이므로 수동 범위를 유지한다.
- **필요한 샘플 데이터**: 합성 웨이퍼 8장과 레시피(저장소 미포함)

###### 클릭 단계

- 웨이퍼 레시피 Teach 화면에서 9개 Measure ROI(중앙 1, 중간 반경 4, 대각 4)와 척 기준 ROI를 보인다.
- Inspect 8 checked를 실행한다.
- 정상 웨이퍼를 선택해 'The selected file has no failed steps.'(에셋 화면에서 확인된 문구)를 보인다.
- 연삭 pit 웨이퍼를 선택: 중앙 지점만 Fail, 색 맵의 국소 hot spot.
- 국소 bulge 웨이퍼를 선택: 해당 지점만 Fail.
- 비틀린 웨이퍼를 선택: 반대편 대각 두 지점과 warpage가 Fail.
- NG items only로 실패 Step만 나열한다.
- 마지막 프레임을 정지.

##### 3. 3D <-> Height <-> Section 전환 (7초)

- **길이(초)**: 7
- **형식**: mp4 H.264 4:3, 12 fps, 무음
- **목표 용량**: 300 KB 이하(3D 회전 때문에 움직임이 커서 추정, 미측정)
- **강조 지점**: 뷰 전환 탭(3D / Height / Section), Show texture 토글, 좌표 읽기값.
- **촬영 팁**: README가 밝히듯 이미지 밝기는 높이 측정이 아니다. 텍스처를 켠 장면에는 '텍스처는 표시용, 측정값 아님' 한 줄을 넣는다.
- **필요한 샘플 데이터**: 합성 PCB 1장(텍스처 포함)

###### 클릭 단계

- 같은 PCB 스캔을 3D 뷰(텍스처 표시)로 연다.
- 마우스로 궤도 회전을 2초 보인다.
- Show texture를 끄고 높이 색으로 전환한다.
- Height 뷰로 전환해 ROI 겹침을 보인다.
- Section 뷰에서 단면선을 하나 그린다.
- Fit으로 돌아온다.

#### 인터랙티브 모듈

- **이름**: 로트 8칸 보드 + 값-한계 게이지
- **설명**: A01-A08 타일 8개에 Pass/Fail 색을 칠하고 상단에 'Pass 5 / Fail 3'을 보인다. 타일을 누르면 해당 파일의 높이맵(ROI 포함) 스틸이 바뀌고, 아래에 허용 범위 막대 위에 값 마커가 놓이는 게이지(앱의 Margin 열 모양)와 Cause 문장이 나온다. Fail 타일은 약하게 맥박(prefers-reduced-motion이면 정지). NG만 보기 토글.
- **필요한 자료**: 파일별 높이맵 크롭 8장과 값/한계(webp 장당 60 KB 이하 예상, 합계 0.5 MB 안팎, 미측정). 기존 GIF에서 A01·A03·A07 3개 프레임은 추출할 수 있고(1100x942), 나머지 5개는 새 촬영. 값은 앱 표에서 읽어 data-* 속성으로 넣는다. README에 값이 적힌 것은 휜 보드 2079.53(허용 1502-1913)뿐이다.
- **정적 사이트에서 가능한가**: 가능. 타일 8개, <img> 교체, CSS 막대 하나면 된다. 의존성 없음. 단 .frame에 걸린 pointermove tilt는 이 프레임에서 꺼야 한다(아래 findings 참고).

#### 보조 인터랙티브 모듈

- **이름**: 웨이퍼 9점 핫스팟 스크린샷
- **설명**: 3d-wafer-teach 위에 9개 투명 버튼을 얹고, 누르면 해당 지점의 Thickness 값·허용 범위·OK가 말풍선으로 뜬다. 중앙 698.83, 상 691.13, 우 700.77, 하 685.86, 좌 690.67(허용 661-732)은 에셋 화면에 보이고, 대각 4점은 결과 표를 스크롤한 화면이 없어 새로 찍어야 한다.
- **필요한 자료**: 기존 3d-wafer-teach.webp + 결과 표 나머지 행 스크린샷 1장(새 촬영), 지점별 좌표 JSON
- **정적 사이트에서 가능한가**: 가능. 퍼센트 좌표 버튼과 tooltip(aria-describedby)이면 충분하다.

#### 데이터 포인트(원문 근거 있는 값)

- 합성 PCB 8장: 5 pass, 휨·비틀림·얇은 보드 3장 fail (README)
- PCB: Board thickness 1709.92 (허용 1502-1913), IC height 1403.8 (1234-1572), Board warpage PV 196.27 (<= 296). 휜 보드 2079.53은 상한 초과 (README)
- 웨이퍼 9지점(중앙 1, 중간 반경 4, 대각 4), 좋은 웨이퍼 warpage PV <= 56. 불량 3장: 연삭 pit(중앙만), 국소 bulge(해당 지점만), 비틀림(반대편 대각 두 점). 셋 다 warpage도 fail (README)
- Thickness Coupon: Height grid 1280 x 840, Eight pads in a 4 x 2 arrangement, Eight Thickness steps with 16 editable ROIs, 단위 raw-height (README)
- 웨이퍼 높이 색 수동 범위 10650-10730 raw-height, wafer scans에는 고립 outlier 픽셀 없음 (README)
- 도구: 전처리(Median filter, noise removal, leveling, nine-point surface compensation, ROI crop) / Warpage(PV, RMS) / Thickness (README 표)
- 입력: C3D는 Recipe 입력, GLB·STL·LAS·LAZ는 Viewer 전용 (README)
- 단축키: F5 선택 도구 실행, Ctrl+F5 전체 Recipe 실행, Enter 적용, Esc 취소, Delete 삭제 (README)
- v0.8.2-dev / Apache-2.0 / .NET 10 / Star 5 (README, stats.md)
- 에셋 화면에서만 확인되는 값(README 문장 아님): Board warpage RMS 50.86 (<= 69), 웨이퍼 OK 10(Thickness 9 + warpage 1)

#### 부족한 자료

- 로트 8개 전체 결과 스틸(파일별 높이맵 + 값/한계) 없음.
- NG 보드 3장의 실패 유형(휨/비틀림/얇음)별 값 표 없음. README는 휜 보드 2079.53만 적었으므로 앱에서 읽어 정리해야 한다.
- NG 위치를 3D 뷰 위에 표시한 이미지 없음. README는 '3D Viewer와 결과 표에서 값과 OK/Fail 확인'이라고 하나 에셋이 없다.
- PCB·웨이퍼 입력과 Recipe는 저장소에 없음(README). 방문자가 재현할 수 있는 것은 Thickness Coupon뿐이고 그 실행 영상도 없다.
- Records 탭에서 저장된 Run Record를 열어 조건·결과를 확인하는 화면 없음(README 6단계).
- 'synthetic' 배지 같은 시각 표식 없음.

#### 방문자별 가치

- **현장 엔지니어**: 값 대 한계 + Cause 문장, 결함마다 다른 실패 지점, datum 기준 Thickness와 PV/RMS의 의미. raw-height가 보정된 물리 단위가 아니라는 고지.
- **리크루터**: 8장 중 5 Pass / 3 Fail이 한눈에 보이는 로트 검사 화면과 3D·높이맵 시각화 완성도.
- **.NET 개발자**: Recipe(JSON)와 C3D 입력, Run Record 구조, .NET 10(global.json 10.0.300), 번들된 Thickness Coupon으로 바로 재현.

### 4. Machine Studio

- **핵심 메시지**: 가상 장비(컨베이어·축·센서·실린더·가상 카메라)와 제어 시퀀스를 구성하고, 실물 장비 시운전 전에 동작·인터록·획득·검사 결과를 같은 프로젝트에서 확인한다.
- **근거**: Configure a virtual machine, write its control sequence, and check machine behavior before hardware commissioning. / It is not qualified for production equipment control or safety functions.
- **현재 상태**: 움직이는 미디어가 0개이고 전부 정지 스크린샷 6장(1600x860)이다. 첫 화면인 Simulation 정지 장면은 PAUSED, RUNNING 0/2, 빈 테이블 2개뿐이라 장비처럼 보이지 않는다(스크린샷 캡처). 가장 풍부한 장면(Equipment setup: Wafer 워크피스와 9개 장치 - EFEM Frame, OHT Conveyor, Load Sensor, Prealign Sensor, Camera Trigger Zone, WTR Stage, Top Surface 2D Camera, Height Verdict Camera, FOUP Gate Cylinder)과 11단계 시퀀스 흐름도(OK/NG 분기)는 2번·3번 썸네일에 묻혀 있다. 4~6번째(Capture/Experiments/Result analysis)는 회색 사각형 이미지, 값이 0인 빈 입력칸, 기록 목록이라 '데이터가 차 있는' 장면이 아니다. UI 라벨 일부가 한글(예: 병렬 공정 관찰, 검사 유닛 A, 두 위치 촬영 공정)이라 영어 페이지와 섞인다. 글 쪽에는 불릿 3줄과 'not qualified for production' 고지뿐이라 '무엇을 확인할 수 있는가'가 시각적으로 답해지지 않는다.
- **기존 자료 활용**:
  - (1) 순서를 바꾼다: Equipment setup(풍부한 장면)을 첫 화면, 다음 Process and actions(OK/NG 분기), Simulation, Capture, Experiments, Result analysis. README 상단 링크 줄의 6개 작업 화면 순서 그대로 번호를 붙여 '작업 흐름 6탭'으로 보인다.
  - (2) 각 이미지에 번호 지시선을 얹는다(사용자 레퍼런스 인포그래픽 스타일): Equipment setup = 1 장비 트리, 2 3D 장면, 3 Configuration 패널, 4 하단 'Simulation only / no physical device control'.
  - (3) ms-capture-and-inspection은 회색 사각형 대신 화면 아래의 'Mock · deterministic model (not a real inspection)' 상태 문구를 크롭·강조해 정직한 시뮬레이션이라는 증거로 쓴다.
  - (4) ms-simulation은 정지 상태가 약하므로 새 촬영으로 교체하고 기존 것은 뒤로 보낸다.
  - (5) 영어 장치명이 있는 Equipment setup 화면을 대표로 삼고, 한글 라벨이 많은 화면은 영어 샘플로 다시 찍을 때까지 크롭으로 라벨 영역을 줄인다.

#### 증거 장면

##### 1. 장비 구성: Equipment setup에서 장비 트리와 3D 장면이 같은 선택을 공유하고, Wafer 워크피스와 장치 9개가 보인다.

- **순서**: 1
- **설득되는 이유**: '가상 장비를 직접 구성한다'가 장치 이름으로 구체화된다. 상단/비스듬한 뷰는 도식이며 CAD·접촉 물리 모델이 아니라는 한계도 README에 있다.
- **누구에게**: 현업 엔지니어, 채용 담당자

##### 2. 시퀀스: 11단계 공정 흐름도. 'Wait for vision result'에서 OK/NG로 분기한다.

- **순서**: 2
- **설득되는 이유**: 검사 결과가 장비 시퀀스를 가른다는 구조가 한 장의 도식으로 보인다. 에코시스템 그림의 '결과 -> 장비 시퀀스 판정' 화살표(점선)와 대응한다.
- **누구에게**: 현업 엔지니어

##### 3. 시뮬레이션 실행: Start 후 제품이 컨베이어를 이동하고 촬영 위치에서 Inspection request가 생긴다. Pause와 1 step으로 한 스텝씩 …

- **순서**: 3
- **장면**: 시뮬레이션 실행: Start 후 제품이 컨베이어를 이동하고 촬영 위치에서 Inspection request가 생긴다. Pause와 1 step으로 한 스텝씩 진행.
- **설득되는 이유**: 정지 화면이 아니라 '돌아가는' 장비라는 증거. 고정 5 ms tick은 시뮬레이션 시간이며 hard real-time 보장이 아니라는 점을 같이 적는다.
- **누구에게**: 현업 엔지니어, 채용 담당자

##### 4. 고장 주입: Equipment faults에서 runtime target을 명시하고 Activate, 알람이 생기고 run이 멈추는지 확인(실제 표시는 촬영 …

- **순서**: 4
- **장면**: 고장 주입: Equipment faults에서 runtime target을 명시하고 Activate, 알람이 생기고 run이 멈추는지 확인(실제 표시는 촬영 때 확인). 에셋 화면의 Run history에는 Completed normally와 Stopped by alarm 두 기록이 있다.
- **설득되는 이유**: 현업 엔지니어가 가장 궁금한 '예외·인터록 흐름을 장비 전에 볼 수 있나'에 답한다.
- **누구에게**: 현업 엔지니어

##### 5. 결과 분석: Result analysis에서 기록된 run을 열고 획득 이미지와 OK/NG를 보고, 같은 Recipe의 두 기록을 비교(Compare runs).

- **순서**: 5
- **설득되는 이유**: 시뮬레이션이 끝으로 기록·재생·비교까지 이어진다는 것이 '검증 도구'다운 마무리다. 상태바 'Simulation only / no physical device control'이 한계를 정직하게 못 박는다.
- **누구에게**: 현업 엔지니어, 개발자

#### 촬영 목록(대본)

##### 1. Automatic Transfer Cell 시뮬레이션: 투입 -> 촬영 -> 검사 -> 결과 (12초)

- **길이(초)**: 12
- **형식**: mp4 1280x720, 15 fps, 무음. poster는 제품이 이동 중인 프레임.
- **목표 용량**: 500 KB 이하(3D 장면 움직임 때문에 정지형 UI보다 클 수 있음, 추정, 미측정)
- **강조 지점**: 움직이는 제품, 현재 step 강조, OK/NG 카운터, 'Fixed 5 ms tick = 시뮬레이션 시간' 주석.
- **촬영 팁**: 예제 프로젝트의 한글 이름은 영어로 바꾼 사본을 쓴다. 30 s 같은 긴 Delay 구간은 가속 편집하고 표기한다. Process diagnostics 패널을 열어 둔다. 커서를 크게.
- **필요한 샘플 데이터**: README의 Automatic Transfer Cell 예제, 또는 samples/SemiconductorRecipes 예제(README 링크, 내용 미확인)

###### 클릭 단계

- 시작 화면에서 Automatic Transfer Cell을 열고 편집 전 사본으로 저장한다(README 안내).
- Simulation 탭에서 3D 뷰를 Fit으로 맞춰 전체 장비를 보인다.
- Start를 누른다(속도 x1). 제품이 투입돼 이동한다.
- 센서·상태 칩이 바뀌는 것을 보인다(RUNNING n/m 등).
- 촬영 위치에서 Inspection requests 하단 탭 숫자가 올라가는 것을 보인다.
- 상태바 OK/NG 카운터가 변하는 것을 보인다.
- Process diagnostics에서 현재 step이 강조되는 것을 보인다.
- Pause 후 1 step을 눌러 한 스텝씩 진행한다.
- 마지막 프레임에 카운터와 상태바 'Simulation only / no physical device control'을 정지.

##### 2. 고장 주입 -> 정지 -> 기록 확인 (10초)

- **길이(초)**: 10
- **형식**: mp4 1280x720, 15 fps, 무음
- **목표 용량**: 350 KB 이하(추정, 미측정)
- **강조 지점**: Stopped by alarm 뱃지 대 Completed normally 뱃지, Alarms 탭 카운트, 고장 대상(runtime target) 선택.
- **촬영 팁**: 캡션은 '가상 장비 시뮬레이션'으로 쓰고 PLC·안전 제어를 암시하지 않는다(README: 실제 PLC·로봇·카메라 제어와 안전 제어는 범위 밖). 알람이 실제로 어떻게 표시되는지 촬영 전에 한 번 확인한 뒤 대본을 확정한다.
- **필요한 샘플 데이터**: 위와 같은 예제 프로젝트에 고장 정의가 있는지 확인(없으면 Equipment faults 화면에서 직접 선택 가능한지 확인)

###### 클릭 단계

- Experiments and data > Equipment faults 탭을 연다.
- runtime target(예: 축 하나)을 명시적으로 선택한다.
- 고장 종류를 골라 Activate한다(고장은 현재 세션에만 속하고 Recipe로 저장되지 않는다는 README 설명을 자막으로).
- Simulation 탭으로 돌아와 run 상태 변화를 보인다(실제 표시는 촬영 때 확인).
- 하단 Alarms 탭에 항목이 생기는 것을 보인다.
- Result analysis > Run history에서 Stopped by alarm 기록을 연다.
- 정상 기록(Completed normally)과 Compare runs로 나란히 본다.
- 고장을 Clear한다.

##### 3. 6탭 워크플로 정지 이미지 6장 재촬영 (영어 UI, 데이터가 찬 상태)

- **길이(초)**: 0
- **형식**: 정지 이미지 6장, 1600x860 PNG를 webp로 변환(기존 59~85 KB 수준)
- **목표 용량**: 장당 90 KB 이하
- **강조 지점**: 각 장에 번호 지시선 3~4개를 사이트에서 얹을 수 있도록 여백과 해상도를 확보한다.
- **촬영 팁**: 영어 이름의 샘플로 통일. 개인 경로와 저장 경로가 상태바에 보이면 가린다.
- **필요한 샘플 데이터**: 영어 이름으로 바꾼 예제 프로젝트 사본

###### 클릭 단계

- Equipment setup: Wafer 워크피스와 장치 9개 트리가 보이게 한 장.
- Process and actions: OK/NG 분기가 있는 시퀀스 흐름도 한 장.
- Capture and inspection: 2D 카메라와 3D height map 카메라 두 대가 목록에 보이는 장면 한 장.
- Simulation: 실행 중 상태(제품이 이동, 카운터 증가) 한 장.
- Experiments and data: Scenario, Seed, Duration, Repetitions가 채워진 요약 패널(에셋 화면 값은 Normal, Seed 1001, Duration 200 cycles, Repetitions 3) 한 장.
- Result analysis: 두 기록을 비교하는 화면 한 장.

#### 인터랙티브 모듈

- **이름**: 6탭 워크플로 플레이어 + 번호 핫스팟
- **설명**: 상단에 6개 탭 칩(Equipment setup -> Process and actions -> Capture and inspection -> Simulation -> Experiments and data -> Result analysis). 칩을 누르거나 좌우 키를 누르면 스크린샷이 바뀌고, 화면 위에 번호 말풍선 3~4개가 뜬다. 오른쪽 열에는 '여기서 확인하는 것'과 '하지 않는 것'을 한 줄씩 적는다(예: Simulation = 시작·일시정지·단계 실행·리셋 / 하지 않는 것 = hard real-time 보장, 5 ms tick은 시뮬레이션 시간).
- **필요한 자료**: 기존 6장 또는 재촬영 6장, 번호 좌표 JSON, README 기반 한 줄 설명 12개
- **정적 사이트에서 가능한가**: 가능. viewer() 패턴 확장. 말풍선은 button + tooltip(aria-describedby).

#### 보조 인터랙티브 모듈

- **이름**: 공정 흐름 SVG + OK/NG 분기 토글
- **설명**: ms-process-and-actions의 구조(Cycle Start -> 1 Delay -> 2-4 Position and capture -> 5-7 Position and capture -> 8 Wait for vision result -> OK/NG -> 9 Delay -> 10 Move axis -> 11 Complete)를 인라인 SVG로 다시 그린다. OK 또는 NG 버튼을 누르면 해당 분기가 강조된다. '구조 설명용 다이어그램(앱 화면 아님)'이라고 표기한다.
- **필요한 자료**: 없음(SVG 약 2 KB 예상). 단계 이름은 에셋 화면에서 읽은 것이므로 README 용어(Delay, Position and capture, Wait for vision result, Move axis, Complete)와 대조해 영어로 통일.
- **정적 사이트에서 가능한가**: 가능. 인라인 SVG와 class 토글만 필요.

#### 데이터 포인트(원문 근거 있는 값)

- 6개 작업 화면: Equipment setup, Process and actions, Capture and inspection, Simulation, Experiments and data, Result analysis (README)
- 예제: Automatic Transfer Cell, Semiconductor equipment examples (README)
- Start, pause, resume, step, reset / 고정 5 ms tick = simulation time, hard real-time 아님 (README)
- 고장은 현재 세션에만 속하고 Recipe 설정으로 저장되지 않음 (README)
- 범위 밖: 실제 PLC·로봇·카메라 제어, 안전 제어, MES/클라우드, CAD 작성, 보정된 물리 시뮬레이션, 양산 AI 검사. Height 데이터는 수치 시험 데이터 (README)
- v0.2.0-dev.81 / MIT / Star 1 / 상태 Active development (README, stats.md)
- 에셋 화면에서만 확인되는 값(README 문장 아님): Wafer 워크피스, 장치 9개, 시퀀스 11 steps, Scenario Normal/Seed 1001/Duration 200 cycles/Repetitions 3, Run history 두 건(Completed normally, Stopped by alarm), 상태바 'Simulation only / no physical device control', 'Mock · deterministic model (not a real inspection)'

#### 부족한 자료

- 움직이는 시뮬레이션 영상이 없음. 모든 증거가 정지 화면.
- 고장 주입 -> 알람 -> 기록의 연속 증거 없음. 실제로 그렇게 표시되는지는 README만으로 확정할 수 없어 촬영 때 확인이 필요.
- 2D/3D/Labeling과의 직접 연동은 README가 'remain in development'라고 하므로 연동 장면은 만들 수 없다. 외부 검사 앱 연결 설정(Inspection connection 탭)만 보일 수 있고, 이 탭의 스크린샷도 없다.
- 영어 UI 샘플 없음(현재 에셋은 한글 이름 혼재).
- 5 ms tick과 시뮬레이션 시간 설명 도식 없음.

#### 방문자별 가치

- **현장 엔지니어**: 시퀀스 분기(OK/NG), 고장 주입과 run 기록으로 예외 흐름을 장비 전에 볼 수 있는지. 실제 PLC·안전 제어는 범위 밖이라는 명시.
- **리크루터**: 장비 개념 -> 가상 장비 -> 시퀀스 -> 결과 분석까지 한 앱으로 설계한 범위와 'Active development'의 정직한 상태 표기.
- **.NET 개발자**: .NET 8, 로컬 NuGet feed 포함, dotnet build/run 두 줄, Architecture 문서와 ASSET-PROVENANCE.json, MIT.

### 5. Vision SDK

- **핵심 메시지**: UI 없이 2D 검사 도구와 height-map / full-XYZ 3D 알고리즘을 내 C# 앱에서 호출한다. SDK는 이미지·측정값·결과 근거를 돌려주고, 취득·표시·ROI 편집·레시피 저장·최종 설비 판정은 호출한 앱이 맡는다.
- **근거**: The SDK returns images, measurements and result evidence. Your application owns acquisition, display, ROI editing, recipe storage and the final equipment decision.
- **현재 상태**: 미디어는 합성 템플릿 매칭 결과 이미지 1장(900x520, 14.6 KB, Score 1.000 x3)과 코드 탭 1개다. 코드는 Threshold 16x16 예제이고 이미지는 Matching 결과라 서로 다른 예제이며, 코드와 결과가 다른 탭이라 연결이 보이지 않는다(스크린샷 캡처). README의 'Expected output: 16x16'이 사이트에는 없어 코드가 돌아간다는 증거가 없다. 이 프로젝트의 핵심 DX 메시지인 SDK/내 앱 책임 경계는 불릿 두 줄 텍스트뿐이다. 모듈 6개(Vision2D, Vision2D.Blob, Vision3D, Inspection, Core, Compute), 7행 버전 이력, 패키지(.nupkg 6개와 SHA-256)가 화면에 없다. Get it 문단은 OpenCvSharp/OpenCV 번들 바이너리의 상업 재배포 차단 문구가 굵은 글씨로 길게 이어져 설치 방법보다 눈에 띈다. README 자신이 기존 결과 이미지를 '합성 예시이며 재현 매니페스트 없음'이라고 밝히므로 이미지 한 장으로는 '진짜 되나'를 입증하기 약하다.
- **기존 자료 활용**:
  - (1) 코드와 결과를 한 프레임에 나란히 둔다: 왼쪽에 기존 .code 마크업(10줄), 오른쪽에 결과 패널('16x16' 콘솔 + 흰 16x16 칸). 줄 번호 변수(--i)가 이미 있어 줄 하이라이트가 쉽다.
  - (2) sdk-matching-result.webp는 'Matching' 모듈 칩을 눌렀을 때의 결과 카드로 쓰되 '합성 예시'라고 표기한다(README도 그렇게 밝힘). 이 이미지를 만든 코드는 README 본문에 없으므로 코드와 짝짓지 않고 docs/sdk-reference.md의 해당 절 링크만 둔다(내용 미확인).
  - (3) 모듈 6개를 칩으로 만들고 README 'Core capabilities' 표의 한 줄 설명을 툴팁으로 쓴다.
  - (4) 버전 이력은 최근 3행(3.3.0-rc.3 2026-11-16, 3.3.0-rc.2 2026-11-16, 3.3.0-rc.1 2026-11-02)만 타임라인 점으로 보이고 나머지는 저장소 링크.
  - (5) 라이선스 굵은 문단은 한 줄 요약과 '전문 보기' 접기로 바꾼다(법적 문구는 원문 그대로 유지).

#### 증거 장면

| 순서 | 장면 | 설득되는 이유 | 누구에게 |
|---|---|---|---|
| 1 | 가장 작은 호출: Mat 생성 -> ThresholdTool.SetProperty(Threshold = 50) -> Execute -> result.Success 확인, 10줄. | 라이브러리가 '이만큼의 코드로 쓰인다'를 한 화면에 보인다. | C#/.NET 개발자 |
| 2 | 실행 결과: 콘솔에 16x16이 찍히고 결과 이미지는 흰색(README: 상수 입력에서 기본 binary threshold가 흰 이미지를 만든다). | 예제가 실제로 돌아간다는 최소 증거. 지금 사이트에는 없다. | 개발자, 채용 담당자 |
| 3 | 소유권과 수명: 호출자가 source를 소유하고 결과가 출력 이미지를 소유하며, source·결과·tool을 모두 Dispose한다(using 줄 강조). | 네이티브 이미지 수명 규칙을 처음부터 알려 주는 라이브러리는 믿을 만하다는 신호. | 개발자 |
| 4 | 결과 근거: 이미지, 측정값, evidence가 반환되는 모양(매칭 결과의 Score 1.000, 템플릿 노란 박스). | SDK가 판정이 아니라 근거를 돌려준다는 책임 경계를 시각화한다. | 현업 엔지니어, 개발자 |
| 5 | 실제 사용 맥락: FirstInspection 콘솔 샘플(prepare -> teach -> inspect -> load -> inspect again)과 에코시스템 표의 2D Workbench·3D Studio(SDK를 쓰는 앱으로 README에 나열). | 예제 한 줄이 아니라 저장·복원·재검사까지의 흐름과 내 다른 앱이 이를 쓴다는 점이 보인다. | 개발자, 채용 담당자 |

#### 촬영 목록(대본)

##### 1. 10줄 코드 실행 -> 16x16 (8초)

- **길이(초)**: 8
- **형식**: mp4 1280x720, 15 fps, 무음. 정지 이미지(코드+출력 한 장)도 같이 저장.
- **목표 용량**: 250 KB 이하(정적 화면 위주)
- **강조 지점**: Threshold = 50 줄, using 줄, 콘솔의 16x16.
- **촬영 팁**: 코드 글자 18pt 이상, 사이트와 같은 다크 테마, 짧은 경로. README는 '관리형/네이티브 의존성을 구성한 뒤' 16x16이 나온다고 하고 프로젝트 참조만으로는 OpenCvSharp 런타임이 완성되지 않는다고 적었으므로, 촬영 전에 이 구성이 실제로 되는지 먼저 확인한다.
- **필요한 샘플 데이터**: README 코드 그대로. 외부 데이터 없음.

###### 클릭 단계

- 새 콘솔 프로젝트(.NET 8, win-x64)에서 패키지 참조(로컬 feed의 SDK .nupkg, PackageVersion=3.3.0-rc.2) 설정을 2초 보인다.
- Program.cs에 README 예제를 붙여 넣는다(타이핑 대신 붙여넣기).
- Threshold = 50 줄을 하이라이트한다.
- using 줄에 자막 'caller owns source, result owns output image'를 얹는다.
- 실행(Ctrl+F5)한다.
- 콘솔에 16x16이 출력된다.
- (선택) Threshold를 다른 값으로 바꿔 재실행하고 출력을 그대로 보인다(결과는 촬영 때 확인해 캡션에 쓴다).

##### 2. FirstInspection 샘플 실제 출력 (텍스트 우선, 영상은 선택)

- **길이(초)**: 12
- **형식**: 권장: 실제 출력을 <pre> 텍스트로 사이트에 싣는다(영상 불필요, 용량 0). 영상이 필요하면 터미널 녹화 mp4 1280x720.
- **목표 용량**: 텍스트 2 KB 이하, 영상이면 300 KB 이하
- **강조 지점**: 각 단계 이름 5개, Accepted 줄, load 때 검사가 돌지 않았다는 점.
- **촬영 팁**: 출력에 개인 경로가 있으면 가린다. 결과 파일(이미지, XML)이 생성되는지는 README에서 확인되지 않았으므로 생성될 때만 보인다.
- **필요한 샘플 데이터**: package-only 콘솔 샘플(samples/OpenVisionLab.FirstInspection)

###### 클릭 단계

- PowerShell에서 FirstInspection 샘플을 prepare로 실행한다(정확한 명령은 docs/sdk-reference.md의 First inspection example 절에서 확인, 현재 미확인).
- teach 단계를 실행한다.
- inspect 단계에서 Accepted 상태와 측정값 줄을 확대한다.
- load 단계를 실행한다. README에 따르면 load는 검사나 CUDA 점검 없이 검증·복원만 한다.
- inspect again을 실행해 결과가 같은지 보인다.
- 자막: 'Accepted는 제한된 근거이며 최종 판정은 호출한 앱의 몫'.

##### 3. 같은 입력의 Matching 결과: SDK 호출 vs 2D Workbench (정지 이미지 1장)

- **길이(초)**: 0
- **형식**: 정지 이미지 1장, 1600x900 webp
- **목표 용량**: 100 KB 이하(기존 sdk-matching-result 14.6 KB)
- **강조 지점**: SDK 출력의 score와 Workbench의 score가 같다는 점, 호출 코드 줄수.
- **촬영 팁**: README가 기존 이미지를 '합성 예시, 재현 매니페스트 없음'이라고 적었으므로 실제 호출 결과로 교체하면 신뢰가 오른다. 단 2D Workbench와 SDK가 같은 Matching 구현을 쓰는지는 README에 명시돼 있지 않아(에코시스템 표는 2D Workbench를 SDK 소비 앱으로 나열) 먼저 확인해야 한다.
- **필요한 샘플 데이터**: Public_Matching_DiePad_Good (2D Workbench 공개 샘플)

###### 클릭 단계

- 2D Workbench 공개 샘플 Public_Matching_DiePad_Good을 선택한다.
- SDK 쪽 Matching 호출 코드를 docs/sdk-reference.md에서 찾아 같은 이미지로 실행한다(코드 위치 미확인).
- 결과 이미지(ResultImage)를 저장한다.
- 점수와 좌표 출력을 텍스트로 복사한다.
- 같은 입력을 2D Workbench의 Matching Tool에서 열어 결과를 비교한다(같은 결과가 나오는지는 확인 필요, 다르면 이 촬영은 취소).
- 두 결과를 나란히 한 장으로 합친다.

#### 인터랙티브 모듈

- **이름**: SDK <-> 내 앱 경계 스테퍼 (코드 줄 연동)
- **설명**: README의 흐름(Host acquires input -> configure/teach -> execute explicitly -> inspect errors, metrics, evidence -> Host decides and displays -> dispose) 6칸 가로 스테퍼. 칸을 누르면 아래 코드창에서 대응 줄이 하이라이트된다: new Mat(...) = 입력 취득(호스트), SetProperty = 설정, Execute = 실행, result.Success/ErrorName/Message = 오류·근거 확인, Console.WriteLine = 표시(호스트), using = 수명/Dispose. 칸 배경색으로 'SDK가 하는 일'과 '내 앱이 하는 일'을 구분하고 오른쪽 결과 패널에는 16x16을 보인다.
- **필요한 자료**: README 코드(기존 .code 마크업), 줄-단계 매핑 데이터, 결과 이미지/출력 1장(촬영 1).
- **정적 사이트에서 가능한가**: 가능. 기존 .ln 줄에 class 토글만 하면 되고 의존성 없음.

#### 보조 인터랙티브 모듈

- **이름**: 모듈 칩 -> 용도 카드
- **설명**: Vision2D / Vision2D.Blob / Vision3D / Inspection / Core / Compute 칩을 누르면 README 한 줄 설명과 문서 링크가 뜬다. Compute 칩에는 'CPU 기본, 선택 CUDA는 일부 edge 매칭 점수와 3D Median/LocalMedian, 결과의 AccelerationApplied/FallbackReason 확인' 배지.
- **필요한 자료**: 없음(텍스트)
- **정적 사이트에서 가능한가**: 가능.

#### 데이터 포인트(원문 근거 있는 값)

- 기대 출력 16x16. 입력은 Mat(16, 16, CV_8UC1, Scalar(100)), Threshold 50 -> 기본 binary threshold가 흰 이미지 (README)
- 소스 v3.3.0-rc.3 (2026-11-16). 3.3.0-rc.2 GitHub prerelease에 SDK .nupkg 6개와 SHA-256 목록 (README)
- 라이브러리 .NET Standard 2.0, 네이티브 런타임 Windows x64. 소비자 검증: net48/x64/C# 7.3, net8/win-x64, FirstInspection CLI (README)
- 모듈 6개: Vision2D, Vision2D.Blob, Vision3D, Inspection, Core, Compute (README 표)
- Matching/Edge matching 포즈 예산 합계 10,000 poses, 활성 각도/스케일 격자만 검증 (README)
- CPU가 기본, CUDA는 선택 edge 매칭 점수와 결정적 3D Median/LocalMedian에 한정 (README)
- 버전 이력 7행: 3.0.0 (2026-08-05) -> 3.3.0-rc.3 (2026-11-16) (README 표)
- MIT / Star 10. OpenCvSharp/OpenCV 번들 바이너리의 상업 재배포는 승인 전까지 차단 (README)
- 한계: 합성 smoke 검사는 센서 정확도, Gauge R&R, 고객 공차, 양산 takt를 입증하지 않음 (README)

#### 부족한 자료

- 코드 실행 결과(콘솔 캡처 또는 결과 이미지) 없음. README에는 'Expected output 16x16' 문장뿐.
- Matching·Blob·3D 쪽 코드 예제 화면 없음. README 본문 코드는 Threshold 하나이고 나머지는 링크.
- FirstInspection, device-free frame Host의 실제 콘솔 출력 없음.
- 결과 이미지 재현 매니페스트 없음(README가 인정) -> 합성 예시 표기가 필요.
- NuGet.org에는 게시되지 않았고 GitHub 사전 릴리스만 있음. '설치 한 줄' GIF는 오해를 부르므로 로컬 feed 설정 2단계 화면이 필요.
- Vision3D(height-map thickness) 코드 예제 화면 없음(sdk-reference.md의 3D quick start는 링크만 확인, 내용 미확인).

#### 방문자별 가치

- **현장 엔지니어**: 2D/3D 알고리즘 목록(Matching, Edge, LineGauge, caliper, QR, Thickness 등)과 합성 smoke의 한계 고지, CPU 기본/CUDA 선택과 fallback 증거 필드.
- **리크루터**: 라이브러리를 버전·패키지·CI 단위로 관리하고(7행 버전 이력, SHA-256 목록) 책임 경계를 문서화하는 설계 역량.
- **.NET 개발자**: 10줄 코드, 수명 규칙(using), netstandard2.0, net48 지원, '프로젝트 참조만으로는 OpenCvSharp 런타임이 완성되지 않는다'는 함정 정보.

### 6. Raw Buffer Visualizer

- **핵심 메시지**: Visual Studio 중단점에서 이미지 변수와 원시 2D 버퍼를 변환 코드 없이 한 도킹 뷰어에서 열어 크기·형식·stride·픽셀·주소를 확인한다.
- **근거**: Image Watch-style debugging for C# machine vision: inspect image variables and raw 2D buffers at a Visual Studio breakpoint in one docked viewer.
- **현재 상태**: 첫 미디어 GIF는 4.0 s, 40프레임, 1920x1044인데 앞 약 2 s가 'No image selected' 빈 뷰어이고(컨택트시트에서 0~1.6 s 5프레임이 빈 상태) 포스터(첫 프레임)도 빈 상태라 사이트의 첫 RBV 장면이 빈 Visual Studio 화면이다(스크린샷 캡처). 가장 강한 증거인 stride 3,840 -> 3,920 전/후가 2번·3번 썸네일로 따로 있어 비교하려면 두 번 눌러야 한다. 전체 Visual Studio 화면이 약 660px로 줄어 코드와 뷰어 글자가 읽히지 않고, 숫자(3,840, 3,920, padding 80 B/row)는 이미지 속 작은 글씨로만 있다. README가 갖고 있는 GIF 2개(manual-stride.gif 5.2 s, pixel-neighborhood.gif 5 s)는 사이트에 없다(manifest.json에 RBV 에셋 3개뿐). Marketplace 버튼은 있으나 설치 단계 화면은 없다. Visual Studio UI가 한글이라 영어 페이지와 섞인다.
- **기존 자료 활용**:
  - (1) before/after 두 장을 한 프레임의 전/후 슬라이더로 합친다. 핸들 위치에 따라 칩이 'stride 3,840 / padding 0 B/row'와 'stride 3,920 / padding 80 B/row'로 바뀐다. 오른쪽 Layout 패널(Stride, Row bytes, 버퍼 3,763,200 B)은 크롭해 확대 삽입해 숫자가 읽히게 한다. 두 이미지는 같은 1600x870이고 같은 화면 레이아웃이므로 정렬 문제는 없다고 보이나 겹쳐서 확인한다.
  - (2) 현재 GIF는 앞 약 2 s를 자르고 포스터를 뷰어에 장비 사진이 열린 프레임으로 바꾼다. mp4 변환 실측 487 KB -> 185 KB.
  - (3) Visual Studio 화면에서 뷰어 패널(오른쪽 약 55%)만 크롭하고, 코드 창은 중단점 줄(627행 GC.KeepAlive(obj)) 한 줄만 작은 삽입으로 보인다.
  - (4) README에 이미 있는 manual-stride.gif(5.2 s)와 pixel-neighborhood.gif(5 s)를 mp4로 변환해 추가한다(파일 존재·용량 미확인).
  - (5) 지원 입력 5종(Bitmap, OpenCvSharp Mat, Emgu CV Mat, RawBufferView, RawBufferSnapshot)을 칩으로 보인다.

#### 증거 장면

| 순서 | 장면 | 설득되는 이유 | 누구에게 |
|---|---|---|---|
| 1 | 중단점: 디버거가 이미지 변수 다음 줄에서 멈춘 상태에서 Watch의 돋보기로 Raw Buffer Visualizer를 연다(또는 Automatic Inspector). | 디버깅 흐름을 끊지 않고 쓴다는 점이 한 동작으로 보인다. | C#/.NET 개발자 |
| 2 | 도킹 뷰어에 이미지가 열리고 크기, 형식, stride, 포인터 아래 X/Y와 원시 바이트가 보인다. | 변환 코드 없이 열린다는 약속이 지켜지는 장면. | 개발자, 현업 엔지니어 |
| 3 | 깨진 이미지: 1280x960 BGR24 버퍼를 stride 3,840(Row bytes 3,840, padding 0 B/row)으로 해석하면 줄무늬로 무너진다. | 현업에서 실제로 겪는 문제(행 패딩 무시)를 시각적으로 즉시 알아본다. | 현업 엔지니어 |
| 4 | 수정: Format에서 stride를 3,920으로 적용(padding 80 B/row)하면 정상 PCB 사진이 나온다. 원본 바이트는 바뀌지 않는다(README). | 원인과 해결이 숫자 하나로 연결되고 되돌릴 수 있다는 점이 도구의 가치를 한 장면으로 보인다. | 세 부류 모두 |
| 5 | 픽셀 확인: 확대하고 핀을 꽂아 5x5 이웃 값 읽기. | 영상 중심의 도구가 아니라 값 중심의 디버깅 도구임을 보인다. | 현업 엔지니어, 개발자 |

#### 촬영 목록(대본)

##### 1. 중단점 -> 돋보기 -> 뷰어 열림 (고해상도 재촬영 8초)

- **길이(초)**: 8
- **형식**: mp4 1440x783 이하(뷰어 영역 중심 크롭), 15 fps, 무음. poster는 이미지가 열린 프레임.
- **목표 용량**: 250 KB 이하(기존 GIF를 mp4로 바꾼 실측 185 KB/4 s)
- **강조 지점**: 돋보기 아이콘, 'Raw Buffer Visualizer' 메뉴 항목, 뷰어 상단 정보줄(해상도, 형식, stride), 포인터 밑 픽셀 값.
- **촬영 팁**: VS 영어 UI 또는 한글 UI 중 하나로 통일한다. 상단 타이틀바(솔루션·계정 영역)는 크롭한다. 현재 GIF의 사진(붉은 선반과 모니터)은 작업 공간 식별 요소가 없는지 확인하고, 가능하면 README의 industrial-image-testing.md에 출처가 기록된 공개 이미지를 쓴다.
- **필요한 샘플 데이터**: 저장소의 디버기 샘플 앱(프로젝트 이름 미확인, README의 Start Here 경로 참고)과 공개 출처 이미지

###### 클릭 단계

- Visual Studio에서 샘플 앱 디버깅을 시작해 이미지 변수가 초기화된 다음 줄의 중단점에서 멈춘다.
- Watch 창의 Mat 또는 Bitmap 변수 옆 돋보기를 클릭한다.
- 메뉴에서 Raw Buffer Visualizer를 선택한다.
- 도킹 뷰어에 이미지가 즉시 열리고 이름·1280x720·BGR24·stride가 보이는 것을 1초 정지.
- 이미지 위로 포인터를 움직여 X/Y, 채널, 원시 바이트를 보인다.
- Fit과 1:1을 한 번 전환한다.
- F10으로 한 줄 진행해 같은 행이 현재 값으로 갱신되는 것을 보인다(README: Break/F10 반복 시 행이 중복되지 않고 갱신됨).
- 정지 프레임: 뷰어에 이미지와 정보 패널.

##### 2. stride 3,840 -> 3,920 보정 (6초)

- **길이(초)**: 6
- **형식**: mp4 1280x720, 15 fps, 무음. 1순위는 저장소의 기존 manual-stride.gif(5.2 s)를 mp4로 변환해 재사용, 없거나 최신 UI가 아닐 때만 재촬영.
- **목표 용량**: 200 KB 이하
- **강조 지점**: Stride 입력칸, Apply 버튼, 전/후 이미지, padding 80 B/row.
- **촬영 팁**: 영상 속 이미지는 최종 프레임을 1.5초 유지해 읽히게 한다.
- **필요한 샘플 데이터**: PCB 스냅샷 파일(.rbuf.json + .raw). 저장소의 docs/images 자료와 같은 파일.

###### 클릭 단계

- 스냅샷 파일(.rbuf.json + .raw)을 열어 줄무늬로 무너진 이미지를 보인다.
- Format 탭의 Stride 칸(3840)과 'Row bytes 3,840, padding 0 B/row'를 강조한다.
- (선택) Diagnose buffer(Buffer Doctor)로 후보 순위가 뜨는 것을 1초 보인다. README는 후보 탐색 범위가 제한적이며 이 예시는 알고 있는 값을 직접 적용한 것이라고 밝힌다.
- Stride에 3920을 입력하고 Apply를 누른다.
- 이미지가 정상 PCB로 바뀐다.
- 'padding 80 B/row'를 확대한다.
- 자막: '원본 바이트는 바뀌지 않는다'.

##### 3. 픽셀 이웃 확인 (5초) + Buffer Doctor 후보 순위 정지 이미지

- **길이(초)**: 5
- **형식**: mp4 1280x720 + 정지 webp 1장
- **목표 용량**: 영상 200 KB 이하, 정지 100 KB 이하. 영상은 README의 pixel-neighborhood.gif 재사용이 1순위.
- **강조 지점**: 핀, 5x5 박스, 이웃 값 표, Buffer Doctor 후보 목록.
- **촬영 팁**: Buffer Doctor 화면은 README에 서술만 있고 화면 자료가 없어 새로 찍어야 한다.
- **필요한 샘플 데이터**: 위와 같은 스냅샷 파일

###### 클릭 단계

- 캡처된 스냅샷 이미지를 연다.
- 확대한다.
- 한 픽셀 위에 핀을 꽂는다.
- 5x5 이웃 값 표를 보인다.
- (정지 이미지) Format > Diagnose buffer를 눌러 후보 순위(가능한 크기, stride, 형식, 유효 비트, 바이트 순서)가 보이는 화면을 저장한다.
- 원본 바이트가 바뀌지 않는다는 문구가 함께 보이게 한다.

#### 인터랙티브 모듈

- **이름**: Stride 전/후 슬라이더
- **설명**: before/after 두 장을 겹치고 가운데 핸들을 드래그하거나 좌우 키를 누르면 왼쪽은 stride 3,840(줄무늬), 오른쪽은 3,920(정상)이 나온다. 핸들 위 칩이 '3,840 B / padding 0'과 '3,920 B / padding 80'으로 따라 바뀐다. 하단 한 문장: '1280x960 BGR24 버퍼의 한 행은 3,840 B인데 실제 행 길이는 3,920 B였다(행마다 80 B 패딩).'
- **필요한 자료**: 기존 rbv-manual-stride-before/after.webp 두 장(둘 다 1600x870). 숫자 패널 크롭 1~2장.
- **정적 사이트에서 가능한가**: 가능. clip-path: inset()과 <input type=range> 오버레이만으로 구현. 의존성 없음, 접근성은 range input이 담당.

#### 보조 인터랙티브 모듈

- **이름**: Stride 체험 캔버스 (개념 시연)
- **설명**: 작은 raw BGR24 버퍼(예: 320x240)를 JS로 직접 해석해 stride 슬라이더를 움직이면 어긋남이 연속적으로 변하는 것을 보인다. 제품 화면이 아니므로 '개념 시연' 라벨을 필수로 단다. 3,840과 3,920이라는 두 상태만 실제 도구 화면이고 중간값은 시연용이다.
- **필요한 자료**: 공개 라이선스 이미지를 행 패딩을 넣어 만든 .raw(수백 KB 이하 예상) 또는 webp로 두고 canvas에서 패딩을 재구성. 출처·라이선스 확인 필요.
- **정적 사이트에서 가능한가**: 가능. canvas ImageData 40줄 안팎, 의존성 없음.

#### 데이터 포인트(원문 근거 있는 값)

- 1280x960 BGR24, Row bytes 3,840 -> 3,920 (padding 80 B/row), 버퍼 3,763,200 B = 3,920 x 960 (README의 3840/3920 + 에셋 화면 값 + 산술)
- 지원 입력: Bitmap, OpenCvSharp Mat, Emgu CV Mat, RawBufferView, RawBufferSnapshot, 지원 컬렉션 (README)
- 지원 픽셀 형식: Mono8, Mono16, Mono10PackedLsb, Mono12PackedLsb, Binary, RGB24, BGR24, BGRA32, Float32, Int32, 8비트 Bayer(RGGB, GRBG, GBRG, BGGR) (한국어 개요 README)
- Visual Studio 2022 17.9+ x64, 안정판 Visual Studio 2026 18.x. VS2019, 32비트, Preview/Insiders는 대상 아님 (README)
- 소스 v2.2.5(Marketplace 버전과 별개) / MIT / Star 4 / VS Marketplace 게시 (README, stats.md)
- 버전 이력 10행: 2.0.7 -> 2.2.5 (README 표)
- 영상 설명 원문: 'Raw Buffer Visualizer 2.2.4.0 final UI, VS2026, 2026-11-03. Edited demonstration; not a processing-time measurement.' (README)
- 수명 한계: 라이브 포인터는 원래 프로세스·할당에 묶이고 Continue, 해제, 프로세스 종료로 무효가 될 수 있음. 주소는 객체 식별자가 아님 (README)

#### 부족한 자료

- Marketplace 설치 -> VS 재시작 -> 돋보기 메뉴로 이어지는 설치 첫 사용 화면 없음(한국어 개요 README의 기본 작업 흐름 1~3단계).
- Automatic Inspector(Auto Inspect on Break, [Auto]/[Map]/[Failed] 배지)와 Connect Your Buffer 매핑 화면 없음.
- Buffer Doctor 후보 순위 화면 없음.
- 히스토그램, 라인 프로파일, A/B 비교 화면 없음.
- 라이브 포인터 수명 경고를 시각화한 자료 없음(README의 중요한 안전 고지).
- 현재 GIF 속 사진(붉은 선반과 모니터)의 출처·식별 요소를 확인해야 함(공개 안전).
- VS UI가 한글이라 영어 페이지와 혼재.

#### 방문자별 가치

- **현장 엔지니어**: 이미지가 왜 깨졌는지 stride·형식·유효 비트·바이트 순서로 좁히는 도구(3,840 vs 3,920 사례)와 픽셀 값·주소 확인.
- **리크루터**: Visual Studio Marketplace에 게시된 실제 배포물(VS 2022 17.9+/2026 지원)과 10행 버전 이력.
- **.NET 개발자**: Bitmap/Mat/Emgu Mat/RawBufferView 지원, 돋보기 -> 뷰어 흐름, 라이브 포인터 수명 한계(Continue·해제 후 무효).

## 공통 이야기

서사는 README의 한 문장으로 모은다: 장비가 오기 전에 구조·시퀀스·검사·고장 모드·통합 검증을 앞당긴다(Noah8218 README: 'move architecture, sequence, inspection, failure-mode and integration verification earlier'). 시각 장치는 두 겹이다.

[1겹: 한 장의 이미지가 지나가는 길] 프로필 README의 흐름도가 이미 그 구조다: 장비 개념·공정 설계 -> Machine Studio(시퀀스, 축, I/O, 고장) -> 가상 카메라와 이미지 입력 -> (2D Workbench / 3D Studio / Labeling Studio, 모두 Vision SDK의 공통 알고리즘 위) -> 검사 결과·지표 -> 장비 시퀀스 판정·재생. 사이트 Overview 다이어그램을 클릭 가능하게 만들어 노드를 누르면 해당 프로젝트 행으로 스크롤하고, 각 행 머리에 같은 다이어그램의 미니맵(자기 노드만 점등)을 둔다. 실선(지금 되는 흐름·SDK 재사용)과 점선(Machine Studio 입력 -> 2D/3D/Labeling 직접 연동, 결과 -> 장비 판정은 개발 중)의 구분을 그대로 유지하고, 점선 구간에는 실제 화면을 만들어 붙이지 않는다(README가 직접 연동을 'in development'로 적음). 이야기로 풀면: Machine Studio에서 가상 웨이퍼 한 장이 이동·촬영되고(Equipment setup 화면에 Wafer 워크피스와 2D·높이 카메라가 있음), 그 입력이 2D에서는 규칙 Recipe로, 3D에서는 높이맵 Thickness·Warpage로, 규칙이 안 풀리는 불량은 Labeling에서 학습 모델로 판정되고, 결과가 시퀀스 OK/NG 분기로 돌아간다. 3D 웨이퍼 데모(wafer-150mm)와 Machine Studio의 Wafer 워크피스는 에셋 화면상 같은 소재이지만 두 도구가 실제로 이어져 있다는 증거는 아니므로 '개념 흐름'으로만 쓴다. SDK는 아래 가로 띠(공통 알고리즘), Raw Buffer Visualizer는 옆 레인('내 앱의 버퍼가 깨졌을 때')에 둔다.

[2겹: 모든 행에 같은 증거 모티프] 프로필 README의 원칙 'Preserve evidence. Validate explicitly.'를 화면 규칙으로 만든다. 각 행 상단에 4칸 증거 띠(입력 -> 설정 -> 결과 -> 판정 근거)와 결과 한 줄 칩(값 / 한계 / 판정)을 둔다: 2D '검출 5 / 한계 5-5 / OK', 3D '2079.53 / 1502-1913 / Fail', Labeling '놓친 불량 3/40 / 단일 데이터셋 / 참고용', Machine Studio 'Stopped by alarm / 시뮬레이션만', SDK 'result.Success + 근거 / 최종 판정은 앱', RBV 'stride 3,840 -> 3,920'. 칩 옆에는 README의 한계를 한 줄 'Scope'로 붙인다(합성 데이터, raw-height 미보정, 단일 데이터셋, 시뮬레이션만, 편집본 영상). 과장 없이 한계를 먼저 쓰는 것이 현업 엔지니어에게 가장 큰 신뢰 신호다. 공통 표기: 번호 지시선은 사용자의 모션 HTML 인포그래픽처럼 틸 액센트의 번호 원형 ①~④, OK=초록, NG=빨강, 놓침/경고=주황, 정답=얇은 흰색(VisA 이미지의 기존 규칙과 통일). 프레임은 앱 전체 화면 대신 핵심 영역 크롭을 기본으로 하고 전체 화면은 '전체 보기'로 확대한다.

## 데모 릴 구성안

14초, 1280x720, 15 fps, H.264 mp4(필요하면 webm 추가), 무음, loop, playsinline. 컷 6개 + 끝 카드 0.8초. 컷마다 왼쪽 아래에 '프로젝트명 + 결과 한 단어' 칩, 컷 전환은 하드컷 또는 80 ms 디졸브. 앱 UI는 전체 화면이 아니라 캔버스와 결과 표만 크롭한다.

- (1) 0-2.5 s Machine Studio: 제품이 컨베이어를 따라 이동(촬영 MS-1의 앞부분), 칩 '1 Machine Studio / 가상 장비'.
- (2) 2.5-5 s 2D Workbench: 검출 5 -> OK, 검출 2 -> NG로 바뀌는 Batch 결과(촬영 2D-1의 마지막부), 칩 '2 2D Workbench / OK · NG'.
- (3) 5-7.5 s 3D Studio: 로트 8장이 채워지며 'Pass 5 / Fail 3'과 2079.53 vs 1502-1913(기존 GIF의 2~10 s 구간을 재사용 가능), 칩 '3 3D Studio / Fail 3'.
- (4) 7.5-10 s Labeling Studio: Smart Mask 후보 -> Confirm(기존 GIF 프레임 3~6 재사용 가능)에 이어 마지막 0.8 s에 VisA PCB4 결과 이미지, 칩 '4 Labeling Studio / Confirm'.
- (5) 10-12 s Vision SDK: 10줄 코드에서 실행 -> 콘솔 16x16(촬영 SDK-1), 칩 '5 Vision SDK / 16x16'.
- (6) 12-14 s Raw Buffer Visualizer: 줄무늬 이미지가 와이프로 정상 PCB로 바뀌며 3,840 -> 3,920(기존 before/after 두 장, 신규 촬영 불필요), 칩 '6 Raw Buffer Visualizer / 3,920'. (끝 카드 14-14.8 s) 'OpenVisionLab' + github.com/Noah8218. 배치: Overview 섹션 맨 위(다이어그램 위)에 놓고, 영상 currentTime에 맞춰 같은 다이어그램의 해당 노드가 점등되게 동기화한다. Hero에는 영상을 넣지 않고(이미 이름 타이포와 canvas 배경이 주의를 쓰고 있어 경쟁) 버튼 'Watch 14 s'만 두어 <dialog>로 재생한다. prefers-reduced-motion이면 자동재생 없이 poster(2D 결과 프레임)와 재생 버튼만 보인다. 재생은 현재 viewer()의 IntersectionObserver 방식(보일 때만 재생)을 재사용. 용량 목표 1 MB 이하(기존 GIF 5개를 mp4로 바꾼 합계가 실측 1.26 MB이므로 14초 릴은 그보다 작을 것으로 예상, 미측정). 단계적 제작: v0(새 촬영 없이) = 컷 3·4·6과 SDK 코드 정지 화면으로 구성한 약 9초 릴, v1 = 2D·Machine Studio·SDK 촬영 후 위 14초 완성본. 모든 컷에 '편집본(유휴 시간 생략)'과 합성/시뮬레이션 표기를 칩으로 남긴다.

## 제작·촬영 우선순위

### 1. 기존 영상·GIF 정리: 포스터를 결과가 있는 프레임으로 교체, 빈 시작 구간 컷(3D 앞 1~2 s, RBV 앞 약 2 s), GIF 5개를 mp4로 …

- **항목**: 기존 영상·GIF 정리: 포스터를 결과가 있는 프레임으로 교체, 빈 시작 구간 컷(3D 앞 1~2 s, RBV 앞 약 2 s), GIF 5개를 mp4로 변환, 2D mp4 두 개를 앞 12 s 클립 또는 Tool 챕터 탭으로 분할
- **이유**: 새 촬영이 0이다. 첫인상 문제(포스터가 빈 화면)가 전 프로젝트에서 한 번에 풀리고, 용량은 GIF 4.85 MB -> mp4 1.26 MB(실측)와 2D mp4 2.5 MB -> 약 0.25 MB(1280 폭 12 s 시험 112 KB x2 기준)로 총 약 5.8 MB 줄어 사이트 합계가 현재 9.35 MB에서 약 3.5 MB 안팎(절반 이하)이 된다(마크업 변경 시 viewer()가 이미 <video>를 처리).
- **난이도**: S

### 2. Labeling Studio: VisA PCB4 실측 카드(이미지 + README 표 HTML)를 첫 화면으로, Task 3탭(Detection/Segm…

- **항목**: Labeling Studio: VisA PCB4 실측 카드(이미지 + README 표 HTML)를 첫 화면으로, Task 3탭(Detection/Segmentation/Anomaly + Ground truth·Models 두 줄)
- **이유**: 6개 프로젝트 중 '진짜 되나'를 숫자로 답하는 가장 강한 자료가 이미 있는데 6번째 썸네일에 묻혀 있고 숫자가 화면에 없다. 에셋·README만으로 해결되고 출처 표기(CC BY 4.0)도 이미 있다.
- **난이도**: S

### 3. Raw Buffer Visualizer: stride 전/후 슬라이더(기존 2장) + README의 manual-stride.gif·pixel-neigh…

- **항목**: Raw Buffer Visualizer: stride 전/후 슬라이더(기존 2장) + README의 manual-stride.gif·pixel-neighborhood.gif를 mp4로 변환해 추가
- **이유**: 에셋이 이미 있고 구현이 약 40줄이며, 한 장면으로 도구의 가치(깨진 이미지가 숫자 하나로 정상이 됨)가 전달된다. 두 GIF는 저장소에 있다고 README에 적혀 있으나 존재·용량은 미확인.
- **난이도**: S

### 4. 2D Workbench Shape Count 12초 클립(검출 5 -> OK, 검출 2 -> NG) + Good/Bad 정지 이미지 + Layer 스테퍼…

- **항목**: 2D Workbench Shape Count 12초 클립(검출 5 -> OK, 검출 2 -> NG) + Good/Bad 정지 이미지 + Layer 스테퍼/OK·NG 토글
- **이유**: 사이트에서 가장 먼저 보이는 프로젝트이고(01), Usable·Star 15로 가장 성숙하며, 핵심 장면(같은 Recipe가 Good은 OK, Bad는 NG)이 어떤 에셋에도 없다. README에 절차가 번호까지 적혀 있어 대본 위험이 낮다.
- **난이도**: M

### 5. 3D Studio: 값-한계 게이지 + 로트 타일(1차: 기존 GIF에서 A01·A03·A07 프레임 추출한 3타일, 2차: 8타일 재촬영) + 웨이퍼 …

- **항목**: 3D Studio: 값-한계 게이지 + 로트 타일(1차: 기존 GIF에서 A01·A03·A07 프레임 추출한 3타일, 2차: 8타일 재촬영) + 웨이퍼 9점 핫스팟
- **이유**: 이미 강한 자료(로트 GIF, NG 결과 표)가 있어 크롭과 게이지만으로 효과가 크다. 8타일 완성은 촬영이 필요하므로 단계로 나눈다. PCB·웨이퍼가 합성이고 저장소에 입력이 없다는 점은 배지로 표시한다.
- **난이도**: M

### 6. Machine Studio: 시뮬레이션 실행 12초 + 고장 주입 10초 + 6탭 번호 핫스팟 플레이어

- **이유**: 모션이 0인 유일한 프로젝트이고 전체 서사의 시작점이다. Equipment setup과 Process 화면(기존)은 핫스팟만으로 당장 개선되지만 시뮬레이션·고장 영상은 새로 찍어야 한다. 예제에서 시각적으로 충분히 풍부한지, 알람이 어떻게 표시되는지 먼저 확인이 필요하다(위험).
- **난이도**: M

### 7. Vision SDK: 코드 <-> 경계 스테퍼 + 콘솔 출력 텍스트(16x16, FirstInspection 출력), 라이선스 문단 접기

- **이유**: 코드·마크업 위주라 비용이 낮고 .NET 개발자 전환에 직접 효과가 있다. 영상 대신 실제 출력 텍스트를 싣는 편이 용량 0이고 신뢰도도 높다. README가 요구하는 네이티브 의존성 구성이 촬영 PC에서 되는지 먼저 확인해야 한다.
- **난이도**: S

### 8. Overview 노드 클릭 연동 + 행 머리 미니맵 + 14초 데모 릴(v0는 기존 재료, v1은 신규 클립 합성) + hero 'Watch 14 s' 버튼

- **이유**: 앞 단계의 클립을 재사용하므로 마지막에 한다. 서사(실선/점선 구분)를 사이트 전체에 묶는 효과가 크지만 재료가 없으면 만들 수 없다.
- **난이도**: L

### 9. 보조 화면 촬영: PatchCore heatmap, Dataset version(Identity details), Buffer Doctor 후보 순위, …

- **항목**: 보조 화면 촬영: PatchCore heatmap, Dataset version(Identity details), Buffer Doctor 후보 순위, Automatic Inspector, Records 탭의 Run Record
- **이유**: 각 프로젝트의 차별 기능이지만 첫 판단(10~20초)에는 필수가 아니다. 1~8 이후 '자세히' 영역에 단계적으로 추가한다.
- **난이도**: M

## 발견 사항

### 1. assets / 3D Studio, Raw Buffer Visualizer, Labeling Studio, Machine Studio 첫 …

- **위치**: 3D Studio, Raw Buffer Visualizer, Labeling Studio, Machine Studio 첫 미디어(포스터)
- **관찰**: 첫 프레임이 모두 '결과 없는 화면'이다. 3D PCB/웨이퍼는 'Untested 8, OK rate --%'의 빈 앱, RBV는 'No image selected', Labeling은 주석 없는 이미지에 박스 도구만 선택, Machine Studio는 PAUSED, RUNNING 0/2의 빈 테이블. GIF가 재생되기 전과 방문자가 스크롤로 지나갈 때 보이는 것이 이 포스터다.
- **근거**: 스크린샷 캡처. RBV GIF 컨택트시트에서 0~1.6 s 5프레임이 빈 뷰어, 3D GIF 컨택트시트 첫 칸이 빈 목록(스크린샷 캡처)
- **영향**: 높음

### 2. assets / 2D Workbench 영상 2개와 썸네일

- **관찰**: ovl-tool-settings.mp4 35.67 s, ovl-preprocessing-chains.mp4 36.17 s로 10~20초 판단 구간의 두 배 이상이며 1600x900 UI가 660px 프레임에 들어가 글자가 읽히지 않는다. 썸네일 첫 두 개는 재생 아이콘뿐이라 내용을 알 수 없다. 결정적 장면(Good OK / Bad NG)이 영상에도 정지 이미지에도 없다.
- **근거**: ffprobe 실측(measurements). 스크린샷 캡처
- **영향**: 높음

### 3. evidence / Labeling Studio 6번째 썸네일 (VisA PCB4)

- **관찰**: 프로젝트 전체에서 '진짜 되나'에 가장 직접 답하는 실측(1,105장, YOLOv8n mAP50 0.747, 놓친 불량 3/40, 오검출 4/402 등)이 썸네일 하나이고 숫자는 사이트에 없다. README에는 표와 한계 문구(양산 정확도 근거 아님)가 완성돼 있다.
- **근거**: index.html에서 '0.747', 'mAP' 검색 결과 없음(Releases 서술 한 줄만). README_OpenVisionLab-Labeling-Studio.md 'Results on real PCB images' 절
- **영향**: 높음

### 4. variety / Projects 섹션 전체

- **관찰**: 6개 행이 같은 템플릿(제목·설명, 프레임+썸네일 줄, 3~4개 불릿, 칩, Get it, 버튼)과 같은 뷰어이다. 프로젝트 성격(데스크톱 앱 / 시뮬레이터 / 라이브러리 / 디버거 확장)이 다른데 표현 방식이 같아 '이 프로젝트만의 증거'가 안 보인다. 코드 탭이 있는 SDK 행만 다르다.
- **근거**: index.html 95~391행 구조, main.js viewer() 한 함수가 모든 행을 처리
- **영향**: 높음

### 5. variety / main.js 상호작용

- **관찰**: 현재 인터랙션은 장식과 갤러리다: 스크롤 reveal, 카운터, 진행바, spotlight/tilt, SVG 화살표 애니메이션, 테마/언어 전환, 썸네일 전환. 증거를 탐색하게 하는 상호작용(핫스팟, 전/후, 스텝, 토글, 게이지)은 없다.
- **근거**: main.js 140~196행(viewer, spotlight+tilt). 에코시스템 SVG는 레이아웃과 draw 애니메이션만 있고 클릭 동작 없음
- **영향**: 높음

### 6. evidence / 모든 스크린샷 프레임

- **관찰**: 1056~1920px 폭 앱 전체 화면을 약 660px 프레임(1440 뷰포트 기준)에 그대로 줄여 넣어 UI 글자가 읽히지 않는다. 핵심 영역 크롭, 번호 지시선, 확대 보기가 없다.
- **근거**: 스크린샷 캡처 (프레임 폭 약 660px). 사용자 레퍼런스(레퍼런스 덱 A 장면 04/s08, 레퍼런스 덱 B 장면 04)는 번호 지시선·큰 숫자 카드 중심
- **영향**: 높음

### 7. assets / Labeling Smart Mask GIF, 멀티모델 GIF

- **관찰**: Smart Mask GIF는 7프레임(0/1.6/2.8/5.8/5.9/6.2/7.4 s) 슬라이드이고 멀티모델 GIF는 12프레임이다. 부드러운 모션이 아니라 키프레임 전환이다. README는 같은 내용의 MP4를 제공한다고 적었다(원본의 해상도·프레임율은 미확인).
- **근거**: ffprobe 프레임 시각. README_OpenVisionLab-Labeling-Studio.md의 'Watch the MP4' 링크 2개
- **영향**: 중간

### 8. assets / GIF 5개 (3D x2, Labeling x2, RBV)

- **관찰**: GIF 합계 4.85 MB가 같은 해상도 mp4로 1.26 MB가 된다(실측). 현재 viewer()는 <video>의 play()/pause()를 이미 지원하므로 마크업 교체만 하면 된다.
- **근거**: ffmpeg libx264 crf 30 변환 측정값(measurements). 화질은 눈으로 검수하지 않음
- **영향**: 중간

### 9. assets / 사이트에 없는 README 자산

- **관찰**: 2D: recipe-teaching.gif, recipe-validation.gif, sample-inspections.gif, pipeline-results.png. RBV: manual-stride.gif(5.2 s), pixel-neighborhood.gif(5 s). 3D: result-ng-compact 이미지. 사이트는 대신 35 s 영상이나 정지 이미지를 쓴다. 파일의 실제 존재·용량·최신 UI 반영 여부는 미확인.
- **근거**: README_OpenVisionLab.md 10행, 56행, 117행, 139행. README_RawBufferVisualizer.md 19~21행. assets/manifest.json에 해당 파일 없음
- **영향**: 중간

### 10. story / Overview 다이어그램과 Projects 행

- **관찰**: 에코시스템 다이어그램(실선=사용 가능, 점선=개발 중)은 프로젝트 행과 연결돼 있지 않다. 각 행이 이 도구가 전체 흐름의 어디인지, 연동이 지금 되는지(Machine Studio 연동은 개발 중)를 말하지 않는다.
- **근거**: index.html 393~428행(#eco는 aria-hidden SVG와 div만, 링크 없음). README_OpenVisionLab-Machine-Studio.md 'Works with OpenVisionLab'
- **영향**: 중간

### 11. evidence / Machine Studio 행

- **관찰**: 모션 자료가 없고, 대표 정지 화면(Simulation)이 비어 있으며, 더 풍부한 화면(Equipment setup, Process 흐름도)이 뒤에 있다. 하단 상태바의 정직한 고지('Simulation only / no physical device control', 'Mock deterministic model, not a real inspection')가 크롭돼 보이지 않는다.
- **근거**: 스크린샷 캡처, ms-simulation.webp, ms-equipment-setup.webp, ms-process-and-actions.webp, ms-capture-and-inspection.webp
- **영향**: 높음

### 12. evidence / Vision SDK 행

- **관찰**: 코드(Threshold 16x16)와 이미지(Matching)가 서로 다른 예제이고 다른 탭이라 연결이 안 보인다. 'Expected output 16x16'이 없다. 이미지는 합성 예시이고 README도 재현 매니페스트가 없다고 인정한다. 라이선스 경고가 굵은 글씨로 Get it을 지배한다.
- **근거**: 스크린샷 캡처, index.html 313~339행, README_OpenVisionLab-Vision-SDK.md 29행, 222~223행
- **영향**: 중간

### 13. variety / .frame에 걸린 tilt와 핫스팟/슬라이더 모듈의 충돌

- **관찰**: main.js는 .frame과 .sk에 pointermove로 perspective rotate를 건다. 핫스팟·전/후 슬라이더·게이지를 이 프레임 안에 넣으면 기울어진 프레임 위에서 드래그 좌표와 클릭 대상이 어긋나 보인다. 인터랙티브 모듈이 들어가는 프레임에서는 tilt를 꺼야 한다.
- **근거**: main.js 186~196행 ($$('.frame,.sk') 대상, transform 설정)
- **영향**: 중간

### 14. evidence / 2D Workbench 결과 문구

- **관찰**: '5 OK / 2 NG'로 줄이면 이미지 수로 읽히지만 README의 값은 검출 개수다: 원본 5 detections / OK, 누락 이미지 2 detections / NG, 요약은 1 OK, 1 NG, 0 errors. 화면 자막과 칩은 README 문장 그대로 써야 한다.
- **근거**: README_OpenVisionLab.md 51~54행
- **영향**: 낮음

### 15. assets / 공개 안전: RBV GIF, 필름 기포·VisA 이미지

- **관찰**: RBV GIF에는 붉은 선반과 모니터가 보이는 작업 공간 사진이 있다(식별 요소 유무 미확인). VS 타이틀바에는 솔루션·계정 영역이 있다. VisA 이미지는 CC BY 4.0 표기가 필요하며 현재 footer와 vnote에 있다. 새로 만들 PCB/웨이퍼/기포 데이터는 저장소 포함 여부와 사용 허가를 확인해야 한다.
- **근거**: 스크린샷 캡처, rbv-manual-stride-after.webp 우상단 크롭('관리자', 'RBVN...'은 개인 식별 정보로 보이지 않으나 크롭 권장), index.html 169행·539행
- **영향**: 낮음
