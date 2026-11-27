# 문서 지도

이 저장소의 문서 전체를 한 장으로 정리한다. 처음 오면 [../AGENTS.md](../AGENTS.md)부터 읽는다(2분). 아래 표의 "언제 읽는가"로 필요한 문서만 고른다. 문서의 사실은 **2026-11-27 작성 시점** 기준이며, 사이트 코드는 이후 바뀔 수 있으니 코드와 `git log`로 확인한다.

## 핵심 문서

| 문서 | 한 줄 설명 | 언제 읽는가 |
|---|---|---|
| [../AGENTS.md](../AGENTS.md) | 규칙, 저장소 지도, 고치는 방법, 검증, 지금 할 일 | **모든 작업 전** |
| [../README.md](../README.md) | 사람용 소개, 로컬 실행, 라이선스 안내 | 저장소를 처음 볼 때 |
| [01-context-and-decisions.md](01-context-and-decisions.md) | 사용자 발언과 결정을 시간순으로, 폐기한 방향과 이유 | "왜 이렇게 만들었나", "이걸 바꿔도 되나"가 궁금할 때 |
| [02-content-policy.md](02-content-policy.md) | 공개 안전 규칙, 문구 출처·번역·이미지·수치 정책, 라이선스 표기 | **문구·이미지·수치를 건드릴 때** |
| [03-site-architecture.md](03-site-architecture.md) | `index.html` 섹션 지도, `data-*` 속성, CSS 토큰, JS 모듈, 접근성, 알려진 한계 | 코드를 고칠 때 |
| [08-backlog.md](08-backlog.md) | 실행 가능한 작업 목록(우선순위, 완료 기준, 검증, 사용자에게 물을 질문) | **무엇을 할지 정할 때** |
| [09-performance.md](09-performance.md) | 성능 측정 방법, 전/후 수치, 원인과 조치, 남은 한계와 선택지, 재측정 명령, 다시 넣지 말 것 | 성능 문제 조사, 느리다는 제보, 무거운 효과·미디어 추가 전 |

## 평가와 근거

| 문서 | 한 줄 설명 | 언제 읽는가 |
|---|---|---|
| [04-design-evaluation.md](04-design-evaluation.md) | AI 4명의 디자인 평가와 개선안(점수, 진단, 제안, 프로젝트별 표현, 진행 순서). **화려한 제안은 보류** | 디자인·구조를 바꾸자는 얘기가 나올 때(먼저 맨 위 경고를 읽는다) |
| [05-expert-reports/](05-expert-reports/) | 평가자별 상세 보고서 4개: [art-direction](05-expert-reports/art-direction.md), [interaction-motion](05-expert-reports/interaction-motion.md), [ux-benchmark](05-expert-reports/ux-benchmark.md), [project-showcase](05-expert-reports/project-showcase.md) | 실행 상세가 필요할 때(촬영 대본, 모션 인벤토리, 벤치마크, 방향 3안+D안) |
| [06-persona-evaluation.md](06-persona-evaluation.md) | AI 평가자 8명의 입장별 평가(점수, 공통 지적, 딱 하나 바꾼다면) | 방문자가 무엇을 못 찾는지 알고 싶을 때 |
| [07-copy-audit.md](07-copy-audit.md) | 문구 AI 티 점검 방법, 1·2차 수정 표(삭제 원문 보존), 한국어 번역 94건 검토 목록, 용어 불일치 | 문구를 바꾸거나 번역을 검토할 때 |
| [design-proposals/README.md](design-proposals/README.md) | 시안 이미지·HTML과 프로토타입(사용자가 아직 못 봤고 보류) | 시안·프로토타입을 열어 볼 때 |

## 자료와 도구 (다른 작업자가 만든 파일)

| 파일 | 한 줄 설명 | 언제 읽는가 |
|---|---|---|
| `sources/` ([stats.md](sources/stats.md) 등) | 공개 README·메타 사본과 Star·라이선스 현황. 사이트 문구의 근거 말뭉치 | 문구 출처를 확인하거나 수치를 갱신할 때 |
| [assets-provenance.md](assets-provenance.md) | `assets/` 파일별 원본 출처·라이선스 표 | 이미지·영상을 추가하거나 출처를 점검할 때 |
| `../tools/` | 검사 도구 5개(`check_site`, `lint_site`, `shot_site`, `scan_public`, `fetch_sources`)와 성능 측정 도구 3개(`perf_site`, `perf_profile`, `perf_ab`) | 검증할 때(사용법은 AGENTS.md 5절, [tools/README.md](../tools/README.md)) |

## 읽는 순서 제안

- **문구를 고친다**: AGENTS.md → 02 → 07
- **코드를 고친다**: AGENTS.md → 03 → 08(해당 항목). 무거운 효과·미디어를 넣거나 느리다는 제보가 있으면 09도 읽는다
- **디자인·인터랙션을 제안받았다**: 04 맨 위 경고 → 01(사용자 피드백) → 08 D·E 구역
- **새 영상·클립을 만든다**: 08 C 구역 → [05-expert-reports/project-showcase.md](05-expert-reports/project-showcase.md) → 02(미디어 정책)
- **수치를 갱신한다**: 02의 "수치 정책" → 08 F 구역

## 문서를 고칠 때

- 새 문서를 만들면 이 표에 한 줄을 더한다. 파일 이름은 ASCII, 본문은 한국어, 인코딩은 BOM 없는 UTF-8과 LF다.
- 로컬 경로, 계정명, 회사·학교 이름, 제3자 캡처를 문서에 넣지 않는다(푸시 전 `python tools/scan_public.py`).
- 점수·평가는 모두 AI 평가자의 것이다. 사람의 의견처럼 쓰지 않는다.
