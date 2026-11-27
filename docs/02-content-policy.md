# 콘텐츠 정책

사이트와 문서에 **무엇을 써도 되고 무엇을 쓰면 안 되는지**를 정한다. 이 저장소는 공개라서 한 번 올라가면 되돌리기 어렵다. 문구, 이미지, 수치, 문서를 건드리기 전에 읽는다.

## 1. 공개 안전 규칙 (모든 파일에 적용)

| 쓰지 않는 것 | 대신 | 확인 |
|---|---|---|
| 회사·고객사·전 직장 이름, 전화번호 | 아무것도 쓰지 않는다. 필요하면 "비공개 경력 포트폴리오는 이 저장소와 별개이며 포함하지 않는다" 한 문장만 | `tools/check_site.py`(사이트 파일), `tools/scan_public.py`(전체) |
| 학교(대학원) 정보, 팀원 이름, 학교 발표 자료의 제목·과목·발표자 | 쓰지 않는다 | `scan_public.py` |
| 회사 제출용 포트폴리오 문서의 이름·버전 표기 | 쓰지 않는다 | `scan_public.py` |
| 로컬 경로, 계정명, 임시 폴더 이름 | 저장소 상대 경로(`assets/…`, `docs/…`)나 "스크린샷 캡처" 같은 일반 표현 | `scan_public.py` |
| 제3자 자료의 캡처(다른 사람 사이트, 발표 자료) | 글로만 설명한다. 레퍼런스 주소(https://www.nazmussayad.com/)와 벤치마크 대상 URL은 공개 주소라 써도 된다 | 사람 검토 |
| 이메일 | 사이트에 이미 공개된 연락 이메일 한 곳 외에 문서에 쓰지 않는다. 문서에서는 "공개 프로필에 있는 연락 이메일"이라고만 쓴다 | `scan_public.py` |
| 새 사실·경력·수치 | 원자료에 있는 것만 쓴다. 확인되지 않은 것은 "미확인"이라고 쓴다 | 사람 검토, `check_site.py` |

- 사이트의 경력 문장(8년, 20개 이상 장비 프로젝트, 반도체·디스플레이·배터리·자동차)은 사이트와 프로필 README에 이미 공개된 문장 **그대로만** 쓴다. 회사·장비 단위로 풀어 쓰지 않는다. 경력 블록을 추가하려면 사용자가 제공한 내용만 쓴다([08-backlog.md](08-backlog.md) B1).
- 금지어 정규식은 `tools/check_site.py`의 `FORBIDDEN`과 `tools/scan_public.py`에 있다. 문서에 열거하면 그 문서가 검사에 걸리므로 여기서도 나열하지 않는다.
- 평가 점수는 AI 평가자의 것이다. 사람의 의견처럼 쓰지 않는다.

## 2. 문구 출처 규칙

사이트의 모든 문장은 다음 중 하나여야 한다.

| 유형 | 영어 | 한국어 | 표시 |
|---|---|---|---|
| README 원문 | `docs/sources/README_*.md` 문장 **그대로** | `README_ko_*.md`(예: 사용자가 쓴 `README.ko.md` 계열) 문장 **그대로** 우선 | 없음 |
| 한국어 원문 없음 | README 영어 그대로 | **AI 번역** | `data-ko-src="tr"` |
| README 한국어를 고쳐 씀 | README 영어 그대로 | 고친 한국어 | `data-ko-src="ed"` |
| 사용자가 지정한 문구 | 지정 문구 | 지정 문구(번역은 `tr`) | `data-ed`(영어) |
| UI 라벨(문장 아님) | 짧은 단어 | 번역 | `tools/allowed_labels.txt`에 등록 |

- 사용자가 지정한 문구: About 인용문, Overview 목적 문단, Contact 큰 문구, 히어로 한국어 인사(상세: [07-copy-audit.md](07-copy-audit.md)의 A2, B, E1, H1).
- 영어 원문을 쓸 때는 문장을 줄이거나 다듬어도 안 된다. 고치려면 사용자 승인을 받고 `data-ed`를 붙이고 `07-copy-audit.md`에 전/후를 남긴다.
- README 문장이 영어 편집 눈으로 어색해도(예: 릴리스 노트의 명령형·과거형·명사구 혼재) **출처 규칙이 우선**한다. 고칠지는 사용자가 정한다.
- 원칙 구간(`#principles`)의 여섯 줄과 설명 문단 2개(`.pr-note`)는 `docs/sources/README_Noah8218.md`의 `Engineering Principles` 상세 블록 영어 원문 그대로다(`data-ed` 없음). 한국어는 README에 원문이 없어 AI 번역이며 `data-ko-src="tr"`을 붙였다(사용자 검토 전).
- 허용 라벨(작성 시점): `Skip to content`, `EN`, `KO`, `Skills`, `Contact`, `Hello, I'm`, `Scroll`, `open-source projects`, `Technologies`, `Get it`, 그리고 Contact 큰 문구 한 문장. 최신 목록은 `tools/allowed_labels.txt`.

### 금지 표현 (AI 티)

- **영어**: 홍보·과장 어휘(ecosystem, seamless, robust, leverage 등), 줄표(em dash, 제목 포함), "not X, but Y" 부정 병렬, 추상명사 나열, 한 문단 안의 동의어 순환, 빈 틀 표현("I prefer engineering that …"; 단 원칙 구간의 README 원문 문단은 출처 규칙이 우선하므로 그대로 쓴다). `Ecosystem`은 `Overview`로 이미 바꿨다.
- **한국어**: humanizer-ko의 37개 패턴(번역투, 불필요한 피동·명사형, 상투적 연결어, 영어 직역). 단 장비 현업어(티칭, 양산 샘플, 광학계 등)와 도구 이름은 고치지 않는다.
- **과교정 금지**: 사람이 쓴 문장을 일부러 어색하게 바꾸지 않는다. 수치, 제품명, 주장의 세기는 불변이다. 방법과 1·2차 수정 기록은 [07-copy-audit.md](07-copy-audit.md).

## 3. 번역 정책

- 한국어는 사용자가 쓴 `README_ko_*.md` 문장을 그대로 쓴다. 원문이 없는 문장만 AI가 번역하고 `data-ko-src="tr"`을 **반드시** 붙인다. 번역 목록은 사용자 검토 대기 상태다([07-copy-audit.md](07-copy-audit.md)의 94건).
- 용어는 `docs/sources/README_ko_*.md`의 표기를 따른다. 알고리즘 이름, UI 이름(Recipe, Pipeline, Layer 등), 제품명은 영어 그대로 둔다.
- `Recipe`/`레시피`, `툴`/`도구`, OK·NG/pass·fail은 저장소마다 README가 다르게 써서 섞여 있다. 통일은 **사용자 결정**이다([08-backlog.md](08-backlog.md) B4). 새 번역을 쓸 때 기존 표기를 따르고, 임의로 통일하지 않는다.
- 한국어 모드에서는 영문 대문자용 넓은 자간(`letter-spacing`)이 한글에 걸리지 않게 한다(`html[lang=ko]` 규칙, `css/style.css`).
- 한국어 README가 없는 저장소(Raw Buffer Visualizer 본문)는 영어를 번역한다. 표에 `tr` 표시와 검토 목록 등재를 함께 한다.

## 4. 이미지·영상 정책

- **공개 저장소 파일만** 쓴다(이 사이트의 `assets/`는 사용자의 공개 저장소 6개의 README 이미지다). 파일마다 원본 URL과 라이선스를 [assets-provenance.md](assets-provenance.md)에 적는다. `assets/manifest.json`은 원본 매니페스트이고 `.gitignore` 대상이다.
- **출처가 불확실한 이미지는 넣지 않는다.** 와셔·기포·Raw Buffer Visualizer의 기판 사진은 출처(직접 만든 것인지, 공개 데이터인지) 확인 대기다([08-backlog.md](08-backlog.md) B2).
- 새로 촬영하는 화면은 **공개 데이터 또는 합성 데이터**만 쓴다. 화면에 사용자 이름, 개인 경로, 계정, 업무 자료가 보이면 안 된다(깨끗한 Windows 계정·샌드박스에서 촬영, 설정 패널 열지 않기). 합성 스캔은 캡션과 `alt`에 `synthetic`이라고 밝힌다.
- 파일 규격(권장): 카드·히어로 영상은 mp4(H.264, muted loop playsinline) 6~12초, 1280×720, 15 fps, 1MB 이하 + 결과가 채워진 프레임의 `poster.webp`. GIF는 상세 뷰어에서만. 실측: 현재 GIF 5개 4.85MB를 같은 해상도 mp4로 바꾸면 1.26MB(화질은 눈으로 검수하지 않음).
- **포스터는 결과가 보이는 프레임**이어야 한다. 빈 앱 화면이나 재생 아이콘만 있는 썸네일은 첫인상을 해친다.
- `alt` 텍스트는 현재 언어의 캡션과 같게 유지한다(`syncAlt`가 처리). 캡션에도 `data-ko`를 붙인다.
- 이미지·영상 메타데이터(EXIF, 작성자, 경로 문자열)가 없는지 `tools/scan_public.py`의 바이너리 경고로 확인한다.

## 5. 수치 정책

| 수치 | 값 | 규칙 |
|---|---|---|
| GitHub Star·팔로워 | 표시하지 않음 | 사용자 결정(2026-11-27). 기록용 수치는 `docs/sources/stats.md`. 다시 넣으려면 먼저 묻는다 |
| 경력 | 8년, 장비 프로젝트 20개 이상, 오픈소스 프로젝트 6개 | 사용자가 제공한 값. 임의로 바꾸지 않는다 |
| 버전 | 프로젝트마다 소스 버전과 게시본 버전이 다를 수 있다 | `Source version`과 `Version`을 구분해 쓰고, 게시본(ZIP, Marketplace)이 소스보다 오래됐으면 그 문장을 지우지 않는다 |
| 성능·정확도(mAP, ms 등) | 현재 사이트에는 싣지 않는다 | 싣는다면 README 문장 그대로 + 한계 문장 동반. **화면에서만 읽은 값은 성능 주장으로 쓰지 않는다** |

**갱신 방법**
1. `python tools/fetch_sources.py`로 README·메타 사본을 새로 받는다(`--dry-run`으로 미리 확인). `docs/sources/stats.md`(Star·팔로워·라이선스)는 손으로 쓴 문서라 덮어쓰지 않으므로 GitHub 화면에서 값을 읽어 직접 고친다.
2. `python tools/check_site.py`로 근거 대조를 다시 한다.

## 6. 한계 문장을 약하게 만들지 않는 규칙

이 문장들은 사이트의 신뢰를 가장 크게 떠받친다(평가자 다수가 가장 신뢰가 가는 문장으로 꼽았다). **줄이거나 부드럽게 바꾸거나 접어서 숨기지 않는다.** 위치를 옮길 때도 눈에 띄게 유지한다.

- "These results come from one dataset with 40 defective test images and are not evidence of production accuracy."(Labeling Studio)
- "It is not qualified for production equipment control or safety functions."(Machine Studio)
- "This version is a development source snapshot, not a production qualification."(3D Studio)
- "OpenVisionLab does not replace testing on the real machine."와 "Dashed arrows mark direct cross-project integration still in development."(Overview)
- "Edited demonstration; not a processing-time measurement."(Raw Buffer Visualizer 영상)
- "The published ZIP is v2.1.0-rc.3; it predates the source workflow shown here."(2D Workbench)
- Vision SDK: "Commercial redistribution of Core's bundled OpenCvSharp/OpenCV binaries remains blocked pending distribution/legal-owner approval of the final notice bundle, Intel notice conditions and distribution workflow." (아래 7절)
- 합성 데이터 표기(`synthetic`), 놓친 결함을 숨기지 않는 캡션("three defects found, one small defect missed").

## 7. 라이선스·출처 표기 필수 사항

| 대상 | 필수 표기 | 상태·메모 |
|---|---|---|
| **VisA 데이터셋 이미지**(Labeling Studio의 PCB4 결과 이미지, 관련 Releases 문장) | "Image source: VisA (Zou et al., ECCV 2022), CC BY 4.0." 원 저작자 링크 https://github.com/amazon-science/spot-diff | 푸터에 항상 보이게 두었다. 변경 표시(검출 박스를 그려 넣고 webp로 재압축한 개작본)와 상시 크레딧 블록은 아직 없다([08-backlog.md](08-backlog.md) B7) |
| **Vision SDK**: MIT는 OpenVisionLab이 작성한 부분만 | OpenCvSharp/OpenCV 번들 바이너리의 **상업적 재배포는 승인 전까지 차단 상태**라는 단서. MIT 칩만 보이면 방문자가 상용 제품에 그대로 넣을 수 있다 | 접더라도 **한 줄은 항상 보이게** 한다. `Source available` 칩과 `MIT` 칩이 한 줄에 있어 의미가 충돌해 보인다는 지적이 있다 |
| 프로젝트별 라이선스 칩 | OpenVisionLab(2D) Apache-2.0, Labeling Studio MIT, 3D Studio Apache-2.0, Machine Studio MIT, Vision SDK MIT, Raw Buffer Visualizer MIT (`docs/sources/stats.md`) | Raw Buffer Visualizer는 GitHub의 라이선스 판정이 `NOASSERTION`이라 MIT 표기와 `LICENSE` 파일을 확인해야 한다(B5) |
| Labeling Studio의 YOLO 계열 모델 | 라이선스 안내를 넣을지 미정 | B6 |
| 이 사이트의 소스 | **라이선스 미정**(새 라이선스를 지어내지 않는다) | `README.md`가 그렇게 안내한다 |
| 푸터 `Copyright (c) 2026 Noah Choi` | 모든 이미지가 작성자 것으로 읽힐 수 있다 | 출처가 다른 이미지는 크레딧 블록에서 구분(B7) |

- 이미지 출처가 다른 사람의 것이거나 라이선스가 확인되지 않은 파일은 사이트와 저장소에 넣지 않는다.
- 상표 문구와 제3자 제품명(Visual Studio, YOLO, OpenCV 등)은 README에 나온 형태로만 쓴다.
