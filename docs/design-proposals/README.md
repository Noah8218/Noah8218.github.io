# 디자인 시안과 프로토타입

AI 평가자(아트 디렉터, 인터랙션·모션 디자이너)가 만든 **시안 이미지, 시안 HTML, 프로토타입**을 모아 둔 폴더다. 사이트 파일이 아니라 참고 자료다.

> **상태: 보류.** 사용자는 이 시안들을 **아직 보지 못했다.** 사용자가 처음 화면을 "너무 AI스럽고 과하다", "이름이 너무 크다", "밝은 게 더 좋다"고 한 뒤라서 화려한 쪽(일러스트 히어로, 글로우, 큰 글자)은 멈췄다. 이 시안을 사용자 승인 없이 사이트에 적용하지 않는다. 결정 질문은 [../08-backlog.md](../08-backlog.md)의 D1이다.

## 파일 표

| 파일 | 종류 | 내용 | 관련 문서·항목 |
|---|---|---|---|
| [concept-b-hero-cream.png](concept-b-hero-cream.png) | 시안 이미지 | **B안 Blueprint Cream** 히어로. 크림·남색 바탕, 점선으로 그린 "아직 오지 않은 장비" 위에 실선·채색 소프트웨어 화면, 번호 말풍선 6개 = 프로젝트 6개 | [art-direction.md](../05-expert-reports/art-direction.md), D1 |
| [concept-b-palette-type.png](concept-b-palette-type.png) | 시안 이미지 | B안 전체 페이지 시안과 팔레트·글꼴 크기 체계. 판정색(초록 OK, 주황 NG, 호박 ROI) | 같음 |
| [concept-b-night.png](concept-b-night.png) | 시안 이미지 | B안의 야간(다크) 버전 | 같음 |
| [concept-d-industrial-dark.png](concept-d-industrial-dark.png) | 시안 이미지 | **D안 Industrial Monitor Dark** 히어로. 남흑 바탕, 상태색 4가지(mint·amber·red·blue), 모노 라벨, 알약 단계 탭, 파이프라인과 모니터 | [art-direction.md의 부록](../05-expert-reports/art-direction.md), D1 |
| [concept-b-in-d-tokens.png](concept-b-in-d-tokens.png) | 시안 이미지 | B안의 일러스트를 D안 팔레트로 렌더한 **이중 테마 확인용** | 같음 |
| [concept-b-hero-cream.html](concept-b-hero-cream.html) | 시안 HTML | B안 히어로 SVG 시안(정적, 글꼴은 시스템 글꼴로 대체 렌더) | D1 |
| [concept-d-industrial-dark.html](concept-d-industrial-dark.html) | 시안 HTML | D안 히어로 SVG 시안 | D1 |
| [proto-pipeline-walker.html](proto-pipeline-walker.html) | 프로토타입 | **2D Workbench 파이프라인 단계 워커.** 스크린샷 위에서 원본→Filter→Threshold→Morphology→Blob→Contour→판정을 단계별로 비춘다 | [interaction-motion.md](../05-expert-reports/interaction-motion.md), E2 |
| [proto-pipeline-walker.png](proto-pipeline-walker.png) | 화면 | 위 프로토타입 화면 | 같음 |
| [proto-stride-compare.html](proto-stride-compare.html) | 프로토타입 | **Raw Buffer Visualizer stride 전/후 슬라이더**(3,840↔3,920바이트) | 같음, E1 |
| [proto-stride-compare.png](proto-stride-compare.png) | 화면 | 위 프로토타입 화면 | 같음 |

## 열어 보는 법

- **이미지**: 파일을 그대로 연다.
- **시안 HTML 두 개**: 외부 파일을 읽지 않는 SVG 시안이라 브라우저로 그냥 열면 된다.
- **프로토타입 두 개**는 사이트의 스크린샷을 `../../assets/…` **상대 경로**로 읽는다(저장소 안에서 `docs/design-proposals/` 기준으로 두 단계 위의 `assets/`). 저장소 구조를 유지한 채 열어야 이미지가 나온다. 서버로 열려면:

```
python -m http.server 8000
# http://localhost:8000/docs/design-proposals/proto-pipeline-walker.html
# http://localhost:8000/docs/design-proposals/proto-stride-compare.html
```

- 프로토타입 HTML 안의 이식 방법은 파일 위쪽 주석에 있다(`data-ko` 방식으로 라벨 교체, 좌표 상수 분리 등).

## 한계 (읽기 전에)

- 시안은 **정적 1장**이다. 모바일(390px) 배치, 인터랙션, 말풍선 링크 동작은 시안에 없다. 모션은 코드로만 구상했다.
- 시안의 글꼴은 시스템 글꼴(Bahnschrift, Segoe UI, Cascadia)로 대체 렌더했다. Barlow, Pretendard, JetBrains Mono의 실제 렌더와 웹폰트 용량(약 35KB, 약 390KB)은 추정치다.
- 이중 테마(라이트 = B 팔레트, 다크 = D 팔레트)는 정적 렌더 1장으로만 확인했고 양 테마의 대비와 스크린샷 가독성은 실측하지 않았다.
- 프로토타입은 **Edge(Chromium) 헤드리스로만** 검증했다. Safari·Firefox·실제 터치는 미검증이다. 프로토타입에 표시되는 판독값(Threshold 170, 960×720, 3.2 ms, 34 items, 2/2 judged OK 등)은 캡처 화면에서 읽은 값이라 사이트에 옮기기 전에 확인이 필요하다.
- **두 시안(B, D) 모두 이름 글자가 크다.** 사용자가 "이름이 너무 크게 나와서 거부감이 들었다"고 했으므로, 시안을 적용하게 되더라도 이름 크기는 현재 사이트 수준(`clamp(2.6rem,6vw,4.5rem)`) 이하로 유지한다.
- 시안 속 "06 프로브와 모니터를 잇는 선"은 장식이며 Overview에 없는 관계다. 색 의미 매핑(초록=OK·사용 가능 등)은 사용자 확인이 필요하다.
- 평가·점수는 모두 AI의 것이다([../04-design-evaluation.md](../04-design-evaluation.md)).

## 이 폴더에 넣지 않은 것

레퍼런스 사이트와 레퍼런스 덱의 캡처는 제3자 자료라 싣지 않았다. 취향 레퍼런스는 글로만 설명한다([../01-context-and-decisions.md](../01-context-and-decisions.md) 3절).
