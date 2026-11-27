# 에셋 출처

이 사이트의 모든 그림·영상은 사용자가 GitHub에 공개한 저장소(`Noah8218/*`)의 파일을 내려받은 것이고, 회사·고객사 자료는 없다.
새 에셋을 추가할 때는 공개 저장소에 이미 올라간 파일만 쓰고 이 표에 출처를 적는다.

## 규칙

- 출처는 `assets/` 의 파일마다 원본 주소(`source_url`)로 적는다. 주소는 모두 `raw.githubusercontent.com/Noah8218/` 아래 공개 파일이다.
- `kind` 가 PNG 인 항목은 원본이 PNG이고 사이트에는 WebP 로 변환해 쓴다(긴 변 최대 1600px, 확대 없음).
- GIF 와 MP4 는 원본 파일 그대로다.
- `*.poster.webp` 는 같은 이름의 `.gif` 의 한 프레임(첫 프레임)에서 만든 파생 이미지다(긴 변 최대 1280px). 원본은 같은 이름의 `.gif` 이고, 표의 원본 주소도 그 GIF 의 주소다.
- 크기(KB)는 에셋을 내려받을 때 기록한 값이며 1 KB = 1024 바이트다.
- 이 표는 `assets/manifest.json`(내려받을 때 자동으로 만든 기록)을 옮겨 적은 것이다. 그 파일은 `.gitignore` 대상이라 저장소에는 없고, 이 문서가 그 역할을 한다.
- "사이트에서 쓰이는 위치"는 `index.html` 에서 파일명을 검색해 어느 프로젝트 행에서 쓰이는지 적은 것이다. 파일이 바뀌면 다시 확인한다.

## 제3자 저작물: VisA 데이터셋 이미지

`lab-visa-pcb4-test-result.webp` 는 VisA 데이터셋(Zou et al., ECCV 2022)의 PCB4 테스트 이미지에 YOLOv8n 검출 결과를 겹친 화면이다. 데이터셋 이미지가 들어 있고 라이선스는 CC BY 4.0 이다.
Labeling Studio README 가 `Image source: VisA (Zou et al., ECCV 2022), CC BY 4.0.` 으로 출처를 표기한다(`docs/sources/README_OpenVisionLab-Labeling-Studio.md`).
사이트 푸터에도 같은 출처 줄이 있다. 이 이미지를 다른 곳에 옮기면 출처 줄도 함께 옮긴다.

## 에셋 표 (31개)

| 파일명 | 종류 | 크기(KB) | 원본 주소 | 사이트에서 쓰이는 위치 |
| --- | --- | ---: | --- | --- |
| `3d-coupon-height.webp` | PNG 원본 → WebP 변환 | 41.3 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-3D-Studio/main/3D/Samples/ThicknessCouponV1/source-height-preview.png` | 프로젝트 행: 3D Studio |
| `3d-pcb-lot-inspection.gif` | GIF 원본 | 1142.5 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-3D-Studio/main/docs/assets/openvisionlab-3d-pcb-lot-inspection-en.gif` | 프로젝트 행: 3D Studio |
| `3d-pcb-lot-inspection.poster.webp` | GIF 파생(첫 프레임, WebP) | 44.6 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-3D-Studio/main/docs/assets/openvisionlab-3d-pcb-lot-inspection-en.gif` | 프로젝트 행: 3D Studio |
| `3d-pcb-result-ng.webp` | PNG 원본 → WebP 변환 | 66.5 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-3D-Studio/main/docs/assets/openvisionlab-3d-pcb-result-ng-en.png` | 프로젝트 행: 3D Studio |
| `3d-pcb-teach.webp` | PNG 원본 → WebP 변환 | 60.1 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-3D-Studio/main/docs/assets/openvisionlab-3d-pcb-teach-en.png` | 프로젝트 행: 3D Studio |
| `3d-wafer-lot-inspection.gif` | GIF 원본 | 1437.6 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-3D-Studio/main/docs/assets/openvisionlab-3d-wafer-lot-inspection-en.gif` | 프로젝트 행: 3D Studio |
| `3d-wafer-lot-inspection.poster.webp` | GIF 파생(첫 프레임, WebP) | 44.7 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-3D-Studio/main/docs/assets/openvisionlab-3d-wafer-lot-inspection-en.gif` | 프로젝트 행: 3D Studio |
| `3d-wafer-teach.webp` | PNG 원본 → WebP 변환 | 124.4 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-3D-Studio/main/docs/assets/openvisionlab-3d-wafer-teach-en.png` | 프로젝트 행: 3D Studio |
| `lab-anomaly-grid-disk.webp` | PNG 원본 → WebP 변환 | 73.7 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Labeling-Studio/main/docs/tutorial/images/readme/en/anomaly-grid-disk.png` | 프로젝트 행: Labeling Studio |
| `lab-detection-washer.webp` | PNG 원본 → WebP 변환 | 59.2 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Labeling-Studio/main/docs/tutorial/images/readme/en/detection-washer.png` | 프로젝트 행: Labeling Studio |
| `lab-hero-smart-mask.gif` | GIF 원본 | 713.1 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Labeling-Studio/main/docs/tutorial/images/readme/en/hero-smart-mask.gif` | 프로젝트 행: Labeling Studio |
| `lab-hero-smart-mask.poster.webp` | GIF 파생(첫 프레임, WebP) | 50.8 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Labeling-Studio/main/docs/tutorial/images/readme/en/hero-smart-mask.gif` | 프로젝트 행: Labeling Studio |
| `lab-multimodel-comparison.gif` | GIF 원본 | 970.2 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Labeling-Studio/main/docs/tutorial/images/readme/en/multimodel-comparison.gif` | 프로젝트 행: Labeling Studio |
| `lab-multimodel-comparison.poster.webp` | GIF 파생(첫 프레임, WebP) | 87.6 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Labeling-Studio/main/docs/tutorial/images/readme/en/multimodel-comparison.gif` | 프로젝트 행: Labeling Studio |
| `lab-segmentation-bubble.webp` | PNG 원본 → WebP 변환 | 138.8 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Labeling-Studio/main/docs/tutorial/images/readme/en/segmentation-bubble.png` | 프로젝트 행: Labeling Studio |
| `lab-visa-pcb4-test-result.webp` | PNG 원본 → WebP 변환 | 239.1 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Labeling-Studio/main/docs/tutorial/images/readme/visa-pcb4-test-result.png` | 프로젝트 행: Labeling Studio |
| `ms-capture-and-inspection.webp` | PNG 원본 → WebP 변환 | 61.6 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Machine-Studio/main/docs/images/capture-and-inspection.png` | 프로젝트 행: Machine Studio |
| `ms-equipment-setup.webp` | PNG 원본 → WebP 변환 | 82.5 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Machine-Studio/main/docs/images/equipment-setup.png` | 프로젝트 행: Machine Studio |
| `ms-experiments-and-data.webp` | PNG 원본 → WebP 변환 | 58.9 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Machine-Studio/main/docs/images/experiments-and-data.png` | 프로젝트 행: Machine Studio |
| `ms-process-and-actions.webp` | PNG 원본 → WebP 변환 | 59.7 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Machine-Studio/main/docs/images/process-and-actions.png` | 프로젝트 행: Machine Studio |
| `ms-result-analysis.webp` | PNG 원본 → WebP 변환 | 59.3 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Machine-Studio/main/docs/images/result-analysis.png` | 프로젝트 행: Machine Studio |
| `ms-simulation.webp` | PNG 원본 → WebP 변환 | 67.1 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Machine-Studio/main/docs/images/simulation.png` | 프로젝트 행: Machine Studio |
| `ovl-inspection-stages.webp` | PNG 원본 → WebP 변환 | 102.6 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab/main/docs/assets/demo/readme-workflows/inspection-stages.png` | 프로젝트 행: 2D Workbench (저장소 OpenVisionLab) |
| `ovl-preprocessing-chains.mp4` | MP4 원본 | 1075.2 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab/main/docs/assets/demo/readme-workflows/preprocessing-chains.mp4` | 프로젝트 행: 2D Workbench (저장소 OpenVisionLab) |
| `ovl-sample-catalog.webp` | PNG 원본 → WebP 변환 | 39.0 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab/main/docs/assets/demo/readme-workflows/sample-catalog.png` | 프로젝트 행: 2D Workbench (저장소 OpenVisionLab) |
| `ovl-tool-settings.mp4` | MP4 원본 | 1343.0 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab/main/docs/assets/demo/readme-workflows/tool-settings.mp4` | 프로젝트 행: 2D Workbench (저장소 OpenVisionLab) |
| `rbv-debugger-memory-image.gif` | GIF 원본 | 475.2 | `https://raw.githubusercontent.com/Noah8218/RawBufferVisualizer/main/docs/images/debugger-memory-image.gif` | 프로젝트 행: Raw Buffer Visualizer |
| `rbv-debugger-memory-image.poster.webp` | GIF 파생(첫 프레임, WebP) | 98.2 | `https://raw.githubusercontent.com/Noah8218/RawBufferVisualizer/main/docs/images/debugger-memory-image.gif` | 프로젝트 행: Raw Buffer Visualizer |
| `rbv-manual-stride-after.webp` | PNG 원본 → WebP 변환 | 138.5 | `https://raw.githubusercontent.com/Noah8218/RawBufferVisualizer/main/docs/images/manual-stride-after.png` | 프로젝트 행: Raw Buffer Visualizer |
| `rbv-manual-stride-before.webp` | PNG 원본 → WebP 변환 | 158.1 | `https://raw.githubusercontent.com/Noah8218/RawBufferVisualizer/main/docs/images/manual-stride-before.png` | 프로젝트 행: Raw Buffer Visualizer |
| `sdk-matching-result.webp` | PNG 원본 → WebP 변환 | 14.6 | `https://raw.githubusercontent.com/Noah8218/OpenVisionLab-Vision-SDK/main/docs/images/matching_detection_result.png` | 프로젝트 행: Vision SDK |

## 매니페스트에 없는 파일

`assets/` 폴더에 있지만 `manifest.json` 에 없는 파일이다.

- `favicon.svg`: 브라우저 탭 아이콘(`index.html` 의 `<link rel="icon">`). 외부에서 내려받은 파일이 아니라 도형 몇 개로 된 작은 SVG(315바이트)이며 원본 주소가 없다. 내려받기 기록에 없는 파일이므로 만든 경위는 이 문서가 확인하지 않았다.

반대로 매니페스트에는 있는데 폴더에 없는 파일은 없다(표의 31개 모두 확인).
`manifest.json` 자체는 위 규칙대로 저장소에 올리지 않는다.
