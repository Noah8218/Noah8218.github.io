# Noah Choi Portfolio

산업용 머신비전 소프트웨어 엔지니어 Noah Choi(최노아)의 개인 포트폴리오 사이트 소스입니다. 본인이 GitHub에 공개한 OpenVisionLab 프로젝트 6개(2D Workbench, Labeling Studio, 3D Studio, Machine Studio, Vision SDK, Raw Buffer Visualizer)를 소개하는 **스크롤형 정적 웹사이트**이고, 영어 기본에 한국어 전환, 라이트 기본에 다크 토글을 지원합니다. 빌드 도구와 외부 의존성이 없고 GitHub Pages로 배포합니다. 비공개 경력 포트폴리오는 이 저장소와 별개이며 포함하지 않습니다.

A static, scroll-style personal portfolio site for Noah Choi, an industrial machine-vision software engineer. It presents the six public OpenVisionLab projects, with English by default, a Korean toggle, a light default theme and a dark toggle. No build step and no external dependencies; it is served by GitHub Pages. The private career portfolio is separate and is not part of this repository.

- 사이트 / Site: https://noah8218.github.io
- GitHub 프로필 / Profile: https://github.com/Noah8218

## 로컬 실행 / Run locally

```
python -m http.server 8000
# http://localhost:8000/ 을 연다 / open http://localhost:8000/
```

`index.html`을 `file://`로 직접 열어도 보이지만, 브라우저가 `localStorage`를 막으면 테마·언어 저장이 되지 않습니다. 확인은 서버로 하세요. Opening `index.html` directly also works, but some browsers block `localStorage` on `file://`.

## 구조 / Structure

```
index.html        한 페이지 전체(문구와 EN/KO 쌍) / the whole page, with EN/KO text pairs
css/style.css     스타일과 테마 토큰 / styles and theme tokens
js/main.js        언어·테마·내비·미디어 뷰어·구성도 / i18n, theme, nav, media viewers, diagram
js/hero.js        히어로 캔버스 / hero canvas
assets/           스크린샷·영상 / screenshots and videos
tools/            검사·성능 측정 도구(Python) / check and performance tools (Python)
docs/             문서 / documentation
```

## 문서 / Documentation

- 작업하는 사람과 AI는 먼저 [AGENTS.md](AGENTS.md)를 읽으세요(규칙, 고치는 방법, 검증, 지금 할 일). Contributors and AI agents: start with [AGENTS.md](AGENTS.md).
- 전체 문서 지도: [docs/00-index.md](docs/00-index.md)
- 작업 목록: [docs/08-backlog.md](docs/08-backlog.md)
- 성능 측정 결과와 재측정 도구(`tools/perf_site.py` 등): [docs/09-performance.md](docs/09-performance.md). Performance measurements and the re-measurement tools.

## 라이선스 / License

사이트 소스의 라이선스는 **아직 정해지지 않았습니다.** 포함된 스크린샷·영상은 각 원본 저장소의 라이선스를 따릅니다(출처 표는 [docs/assets-provenance.md](docs/assets-provenance.md)). Labeling Studio의 일부 이미지는 VisA 데이터셋(Zou et al., ECCV 2022, CC BY 4.0)에서 왔습니다.

The license for the site source is **not decided yet.** Screenshots and videos follow the licenses of their original repositories (see [docs/assets-provenance.md](docs/assets-provenance.md)). Some Labeling Studio images come from the VisA dataset (Zou et al., ECCV 2022, CC BY 4.0).
