# 사이트 구조

`index.html`, `css/style.css`, `js/main.js`, `js/hero.js` 네 파일이 사이트 전부다. 빌드·번들·외부 요청이 없다. **이 문서는 2026-11-27 작성 시점의 코드를 읽고 쓴 것**이며, 줄 번호 대신 선택자와 함수 이름으로 가리킨다. 이 문서를 쓰는 동안 버그 수정 작업(A 구역)이 코드에 반영되고 있어서, 본문은 **작성 말미(오후 3시 20분경)에 코드를 다시 읽은 스냅샷**을 기준으로 맞췄다. 그래도 달라진 부분은 코드가 기준이다(9절의 확인 방법). 이후 성능 작업(2026-11-27, [09-performance.md](09-performance.md))으로 바뀐 `hero.js`, 테마 전환, `.reveal`, 미디어 뷰어, `layoutEco()`는 성능 작업 직전 코드와 현재 코드를 비교해 5·6절에 다시 맞췄다.

## 1. 로드 순서와 상태

1. `<head>`의 인라인 스크립트가 `<html>`에 상태를 먼저 정한다(깜빡임 방지): 클래스 `js`, 조건부 `still`·`pp`, `data-theme`(`light`/`dark`), `lang`(`en`/`ko`). `still`은 `?shot`·`?lint`이거나, 저장된 `motion`이 `off`이거나, `motion`이 `on`이 아니면서 `prefers-reduced-motion: reduce`일 때 붙는다.
2. `css/style.css` → 본문 → `js/hero.js` → `js/main.js` 순이다(둘 다 문서 끝, `defer` 없음).
3. 저장 값은 `localStorage`의 `theme`, `lang`, `motion`(`off`/`on`) 세 키뿐이다. 접근이 막혀도 예외를 삼키고 메모리 상태만 유지한다(`sget`/`sset`, 인라인 스크립트의 `try`).
4. 쿼리 우선순위: `?theme=`·`?lang=`이 `localStorage`보다 앞선다. 기본값은 `light`, `en`.

## 2. `index.html` 섹션 지도

| id | 요소 | 역할 | 구성 |
|---|---|---|---|
| (헤더) `#nav` | `header.nav` | 고정 내비 | `.progress > #bar`(스크롤 진행 막대), `nav.pill`: `a.brand`, `ul.links#menu`(About, Projects, Overview, Skills, Principles, Releases, Contact), `.tools`(`.seg`+`[data-lang]` 버튼 EN·KO, `#theme`, `#motion`(모션 정지 토글), `#burger`) |
| `#top` | `section.hero` | 인사·이름·직함·소개·버튼 | `canvas#hero-canvas`(js/hero.js), `.hello`, `h1.name`(`.w > span` 단어 마스크), `.idl`(`.kname`, `.role`), `.tag`, `.bio`, `.btns`, `a.cue` |
| `#about` | `section.sec` | 소개·통계 | `blockquote.pull`(`mark.hl`), `.copy`, `.stats > .stat`(`[data-count]` 숫자 타일 3개) |
| `#projects` | `section.sec` | 프로젝트 6개 | `article.row` 6개(아래 3절). 순서: 2D Workbench, Labeling Studio, 3D Studio, Machine Studio, Vision SDK, Raw Buffer Visualizer |
| `#ecosystem` | `section.sec` | 구성도(메뉴 이름 Overview/구성도) | `.eco#eco`: `svg.eco-svg`(`path.e.s` 실선, `path.e.x` 점선), 노드 `.nd`(`#n-concept #n-machine #n-inputs #n-sdk #n-2d #n-3d #n-lab #n-results #n-decision`), `.legend`, `.purpose` |
| `#skills` | `section.sec` | 기술 4카드 + 칩 | `.skills > article.sk.reveal` 4개, `.kw > .chips` |
| `#principles` | `section.pr-sec` | 엔지니어링 원칙 6줄(스크롤 고정) + 설명 문단 2개 | `.pr-wrap#pr-wrap`(높이 `calc(var(--vh)*4)`) > `.pr-pin`(sticky) > `.wrap` > 제목 + `ol.pr > li` 6개. 설명 문단은 핀(`.pr-pin`) 밖, `#pr-wrap` 뒤의 일반 흐름 블록 `.wrap > div.pr-note > p` 2개다(낮은 화면에서 핀 안에 두면 제목이 내비에 가려져 밖으로 뺐다. 스크롤 연동 없음). 내용은 프로필 README의 Engineering Principles 원문. 내비에 Principles 링크가 있다(작성 말미 스냅샷 기준) |
| `#releases` | `section.sec` | 최신·이력·로드맵 | `ul.lat`(Latest 3장), `ol.tl#tl`(타임라인 `li.ti`: `time`, `i.dot`, `.tc`), `.road > dl`(Next, Planned) |
| `#contact` | `section.sec.contact` | 연락 | `.big`, `.btns`, `.mail`, `.aside` |
| (푸터) | `footer.foot` | 이미지 출처·저작권 | `.credit`(VisA CC BY 4.0 링크), `Copyright (c) 2026 Noah Choi` |

- 본문 맨 앞에 `a.skip`(본문으로 건너뛰기)이 있고, `main#main`이 본문을 감싼다.
- scroll-spy는 `main.js`의 `secs` 목록(`about projects ecosystem skills principles releases contact`)과 `#menu`의 `href`를 대조한다. 새 섹션을 추가하면 **두 곳을 같이** 고친다.

## 3. 프로젝트 행과 미디어 뷰어

`article.row`(`aria-labelledby`는 제목 `h3`의 `id`: `t-ovl`, `t-lab`, `t-3d`, `t-ms`, `t-sdk`, `t-rbv`)의 구조는 6개가 같다.

```
article.row
  .hd        p.no(01~06), h3, p.desc
  .vw[data-vw] style="--ar:16/9"      <- 뷰어. --ar 은 .stage의 aspect-ratio
    .frame > .bar(가짜 창 점 3개) + .stage
        .m (img | video | div.m.code)  <- 미디어. 첫 번째만 class="on"
        i.scan                         <- 등장 시 스캔선 1회
    .caps[aria-live=polite] > p#c-xxx  <- .m 과 같은 순서·같은 개수의 캡션
    .vnote[data-for="N"][hidden]       <- N번째(0부터) 미디어가 선택될 때만 보이는 주의 문구
    .thumbs[role=group][data-aria=media] > button  <- .m 과 같은 순서의 썸네일
  .dt        ul.feat, ul.chips, p.get(.gl 라벨), p.note, p.acts
```

- **`.m`, `.caps p`, `.thumbs button`은 같은 개수·같은 순서**여야 한다. 뷰어(`viewer()`)가 인덱스로 짝을 맞춘다.
- 썸네일 버튼은 `aria-labelledby`로 캡션 `p`의 `id`를 가리킨다.
- **GIF**: `<img src="….poster.webp" data-gif="….gif">`. 선택되고 **재생 조건을 채웠을 때만** `src`를 GIF로 바꾸고, 아니면 포스터로 되돌린다(`data-p`에 포스터 원본 저장). 교체는 새 `Image`를 `decode()`한 뒤 보이는 요소에 반영한다(`show()`).
- **영상**: `<video muted loop playsinline preload="none" poster=…>`. 선택되고 재생 조건을 채웠을 때만 `play()`, 아니면 `pause()`.
- **재생 조건**(GIF·영상 공통, `viewer()`의 `IntersectionObserver`, 임계 0.35): 행이 충분히 보인 채 **300ms 머물고, 마지막 스크롤로부터 150ms가 지난 뒤에만** `vis`를 켠다(`arm()`이 `lastScroll`을 보고 모자라면 남은 시간만큼 다시 건다). 스크롤로 지나가는 행은 영상·GIF를 시작하지 않는다. 행을 벗어나면 즉시 `vis`를 끄고 정지·포스터로 돌아간다. 썸네일 클릭(`pick()`)은 이 지연을 거치지 않고 현재 `vis`를 따른다.
- 프로젝트 미디어·썸네일 `<img>` 48개는 모두 `loading="lazy" decoding="async"`다. 새 행은 기존 행을 복제하면 따라온다.
- **코드 탭**(Vision SDK): `div.m.code[tabindex=0][role=region]` 안의 `pre > code > span.ln`. 줄마다 `--i`를 주고 `.on`이 되면 순서대로 나타난다.
- `.vnote`는 `data-for`와 현재 인덱스가 같을 때만 `hidden`이 풀린다(`apply()`). Labeling Studio의 VisA 출처 문구가 6번째 썸네일을 눌러야 보이는 이유다.

## 4. `data-*` 속성 (실제 사용하는 것)

| 속성 | 쓰는 곳 | 뜻 | 처리 |
|---|---|---|---|
| `data-ko` | 번역되는 모든 요소 | 한국어 텍스트 | `setLang()`이 `textContent`를 `data-ko`/`data-en`으로 바꾼다. 로드 시 원래 영어를 `data-en`에 저장 |
| `data-ko-src="tr"` | `data-ko`와 함께 | AI 번역 표시 | 코드 동작 없음. `tools/check_site.py`와 `lint`가 센다 |
| `data-ko-src="ed"` | `data-ko`와 함께 | README 한국어를 고쳐 쓴 문구 | `check_site.py`용 |
| `data-ed` | 영어 요소 | README 영어를 고쳐 쓴(사용자 지정) 문구 | `check_site.py`용. `data-ko`가 반드시 같이 있어야 한다 |
| `data-aria` | `.seg`, `#theme`, `#motion`, `#burger`, `.thumbs` | `aria-label`의 종류: `lang`, `theme`, `motion`, `menu`, `media` | `setLang()`이 언어별 문구(`ARIA` 객체)를 넣는다(`motion`은 `title`도) |
| `data-lang` | EN·KO 버튼 | 대상 언어 | 클릭 시 `setLang(l, true)`. `aria-pressed` 갱신 |
| `data-stagger` | `.copy`, `.stats`, `.skills`, `.lat` 등 | 자식 `.reveal`에 지연 부여 | `--rd`를 `min(i*100, 600)ms`로 설정 |
| `data-count` | `.num > span` | 카운터 대상 | 화면에 60% 보이면 1.1초 카운트업 후 원래 문자열 복원 |
| `data-vw` | `.vw` | 미디어 뷰어 루트 | `viewer()`로 초기화 |
| `data-gif` | `img.m` | 재생용 GIF 경로 | 위 3절 |
| `data-for` | `.vnote` | 이 문구를 보일 미디어 인덱스 | `apply()` |
| `data-f` `data-t` `data-tx` | 구성도 `path.e` | 시작·끝 노드 id 접미사, 끝점 x 오프셋 비율 | `layoutEco()`가 `#n-<f>`→`#n-<t>` 경로를 계산 |
| `data-theme` | `<html>` | `light` / `dark` | CSS 변수 선택(5절) |

- 클래스 `reveal`: 등장 대상. 보이면 `in`이 붙는다. `--rd`(지연)는 인라인 `style`이나 `data-stagger`가 정한다.
- 개발용 쿼리: `?lang=ko|en`, `?theme=dark|light`, `?shot=1`, `?lint=1`, `?pp=0~1`, `?vh=px`. `?shot`·`?lint`는 `html.still`을 켜고 이미지를 즉시 로드(`loading=eager`)하며, 이때는 영상에 컨트롤을 붙이지 않는다(reduced-motion만 켠 경우에는 붙는다). 해시가 있으면 로드 후 그 섹션으로 이동한다. `?lint`는 레이아웃 검사 결과를 숨은 `pre#lintout`에 JSON으로 넣는다(`runLint()`, 도구가 읽는다). `?pp`는 원칙 구간 진행도를 고정하고 `<html>`에 `pp` 클래스를 붙인다(`html.still:not(.pp)` 규칙이 이 클래스를 본다). `?vh`는 `--vh`를 px로 고정한다(캡처용).

## 5. CSS 구조와 토큰

`css/style.css`는 위에서 아래로: 토큰(`:root`, `[data-theme]`) → 리셋 → `.reveal` → 내비 → 히어로 → 섹션 공통(`.sec`, `.ttl`, `.u`) → About → Projects(`.row`, `.frame`, `.stage`, `.m`, `.caps`, `.thumbs`, `.code`) → 구성도(`.eco`, `.nd`, `.e`) → Skills → Principles(`.pr-wrap`, `.pr-note`) → Releases(`.lat`, `.tl`, `.road`) → Contact → `html.still` → 반응형.

**`:root` 공통 토큰**: `--ease`, `--vh`(`100svh`를 지원하면 `100svh`), `--pad`(`clamp(20px,5vw,64px)`), `--wrap`(1200px), `--font`, `--mono`.

**테마 토큰**(`html[data-theme=dark|light]`):

| 변수 | 뜻 | 다크 | 라이트 |
|---|---|---|---|
| `--bg` | 페이지 배경 | `#090c0e` | `#f5f7f7` |
| `--card` | 카드·프레임 면 | `#12181c` | `#fff` |
| `--fg` / `--muted` | 본문 / 보조 글자 | `#e9eef0` / `#9aa8b0` | `#0c1316` / `#475861` |
| `--line` / `--line2` | 옅은 / 진한 테두리 | `rgba(255,255,255,.1/.2)` | `rgba(12,19,22,.12/.24)` |
| `--accent` / `--on-accent` / `--aline` | 포인트색 / 그 위 글자 / 포인트 테두리 | `#2dd4bf` / `#04201c` / 50% | `#0b766f` / `#fff` / 50% |
| `--stage` | 미디어 스테이지 배경 | `#06090b` | `#dde4e6` |
| `--glass` / `--menu` | 유리 내비 / 모바일 메뉴 배경 | 반투명 어두움 | 반투명 밝음 |
| `--hl` / `--scan` / `--spot` | 형광펜 / 스캔선 / 호버 스포트라이트 | 포인트 계열 | 포인트 계열 |
| `--cv-dot` / `--cv-acc` | 히어로 캔버스의 점·포인트 RGB(`r,g,b`) | `200,214,220` / `45,212,191` | `20,34,40` / `11,118,111` |

- **포인트색은 청록 1색**이다. 색에 의미를 부여하는 안(OK 초록, NG 주황 등)은 사용자 결정 대기다([08-backlog.md](08-backlog.md) D).
- 테마 전환은 `setTheme()`이 `data-theme`를 바꾸고 `themechange` 이벤트를 쏜다(히어로는 색을 바로 읽지 않고 다음 프레임에 다시 읽는다). 전환 중에는 `html.nt` 클래스가 모든 요소(`*`, `::before`, `::after`)의 `transition`을 `none !important`로 끄고, 두 프레임 뒤에 `setTheme()`이 해제한다(연속 클릭은 마지막 요청만 해제). 이전의 `html.tm`(0.7초간 색 전환을 켜는 방식)은 없다.
- `--font` 스택은 작성 말미 스냅샷에서 `"Segoe UI Variable Text","Segoe UI",-apple-system,BlinkMacSystemFont,"Pretendard","Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",sans-serif`이다(원래는 `ui-sans-serif,system-ui,"Segoe UI","Pretendard",…` 순서라 `system-ui`가 먼저 매칭되는 문제가 있었다. [08-backlog.md](08-backlog.md) A1). 웹폰트 파일은 없다.
- 한국어 모드(`html[lang=ko]`)에서는 영문 대문자용 넓은 자간이 한글에 걸리지 않게 `letter-spacing:0`으로 덮어쓴다(`.cue .ttl .ttl.sm .sub .road dt .get .gl .pull p .pr li .big .sk h3 .tag`).
- 이름 글자: `.name{font-size:clamp(2.6rem,6vw,4.5rem)}`. **키우지 않는다**(AGENTS.md 7절).

**레이아웃·반응형 기준**
- `.wrap`: `width:min(var(--wrap), calc(100% - 2*var(--pad)))`, 가운데 정렬.
- `.row`: 데스크톱은 2열 그리드(`5fr 7fr`, 짝수 행은 `7fr 5fr`으로 좌우 교대, 영역 이름 `hd vw dt`).
- 중단점: `max-width:1000px`(내비 링크 여백), `900px`(`.row`·`.about-grid`·`.lat`·`.skills` 1열), `768px`(햄버거 메뉴, 구성도 6열 격자, 타임라인 세로 정렬), `640px`(통계 간격, 코드 뷰어 1:1, 썸네일 높이).
- 구성도 노드는 `.eco`의 8열 격자에 `grid-area`로 배치(모바일은 6열로 재배치). 선은 `layoutEco()`가 노드 위치를 읽어 계산한다.
- 최소 글자 크기: `lint`가 14px 미만을 잡는다.

**모션 관련 CSS**: `.reveal`(opacity + `translateY(16px)` 전환, 블러 없음. 히어로 안의 `.hero .reveal`은 전환 .4s·지연 15%로 더 빠르다), `.u`·`.hl`(밑줄·형광펜 채움), `.scan`(스캔선), `@keyframes cue scan`(`.cue i`, `.vw.in .scan`; 구성도 점선용 `flow`는 작성 말미 스냅샷에서 사라졌다), `.pr li`의 `--k` 불투명도(스크롤 연동), `.tl`의 `--fill`. 전부 `html.still`에서 최종 상태로 풀린다.

## 6. JS 모듈

### `js/main.js` (IIFE 하나, 위에서 아래로)

| 블록 | 함수·변수 | 하는 일 |
|---|---|---|
| i18n | `setLang(l, save)`, `syncAlt(vw)`, `ARIA`, `koEls` | `data-ko`↔`data-en` 교체, `aria-label` 언어별 설정, 이미지 `alt`를 현재 캡션과 동기화, `lang` 저장 |
| 테마 | `setTheme(t, anim, save)`, `ntk` | `data-theme`, `aria-pressed`, `meta[name=theme-color]`(다크 `#090c0e`, 라이트 `#f5f7f7`) 갱신. `anim`이고 정지 상태가 아니면 `html.nt`를 켜고 두 프레임 뒤 해제(`ntk`로 마지막 요청만 해제). `themechange` 이벤트를 쏜다 |
| 내비 | `menu(open)`, `#burger` | 모바일 메뉴 열기·닫기. Esc, 바깥 클릭, 링크 클릭으로 닫힘 |
| 스크롤 연동 | `onScroll()`, `principles()`, `timeline()`, `lastScroll` | 진행 막대(`#bar`), 현재 섹션 강조(scroll-spy, `.links a.act`, `aria-current`), 원칙 줄의 `--k`·`.cur`, 타임라인 `--fill`·`.ti.on`. `scroll` 리스너(passive)가 마지막 스크롤 시각 `lastScroll`을 기록한다(미디어 재생 지연 판단용) |
| reveal | `IntersectionObserver`, `settle(e)` | `.reveal`에 `in` 부착. `#eco`는 따로 관찰. 임계 0.12. 히어로(`#top`, `.hero .reveal`)는 관찰자를 기다리지 않고 첫 `requestAnimationFrame`에 바로 `in`을 붙인다(LCP). Skills 카드(`.sk`)는 등장 전환이 끝난 뒤 `done` 클래스를 붙여 호버용 짧은 전환으로 바꾼다 |
| 카운터 | `count(el)` | `[data-count]` 숫자 카운트업(원래 문자열로 복원). 정지 상태면 즉시 원래 문자열 |
| 미디어 뷰어 | `viewer(vw)`, `apply()`, `pick(i)`, `arm(ms)`, `show(m, s)`, `syncVideos()`, `viewers` | 썸네일 클릭·방향키(←→ Home End), 재생 지연 규칙(행이 보인 채 300ms 머물고 스크롤이 150ms 멈춘 뒤에만 재생, 벗어나면 즉시 정지. 3절), 포스터↔GIF 교체(`show()`가 `Image.decode()` 뒤에 반영, 마지막 요청만), `.vnote` 전환, 탭 숨김 시 정지(`visibilitychange`). 정지 상태면 영상에 `controls` |
| 스포트라이트·틸트 | 포인터 이벤트 | 마우스 환경에서 `.frame,.sk`에 `--mx/--my` 스포트라이트. 기울기(`perspective`)는 `.sk`(Skills 카드)에만 남아 있고 미디어 프레임 `.frame`에는 없다(작성 말미 스냅샷, [08](08-backlog.md) A7) |
| 모션 정지 | `setMotion(off, save)`, `rm`(`prefers-reduced-motion`), `motionchange` 이벤트 | `#motion` 토글이 `html.still`을 켜고 끄고 `localStorage`의 `motion`에 저장한다. OS 설정이 바뀌면(`change`) 저장값을 지우고 OS 설정을 따른다. `?shot`·`?lint`는 항상 정지. `hero.js`가 `motionchange`를 듣는다 |
| 구성도 | `layoutEco()`, `ResizeObserver` | `data-f`→`data-t` 노드 사이 경로(`d`)와 화살촉(`.eh`) 생성. 같은 행이면 직선, 다른 행이면 S 곡선. **읽기와 쓰기를 분리**한다: 모든 노드의 `offsetLeft`·`offsetWidth` 등을 먼저 읽어 `d` 목록을 만든 뒤에야 `viewBox`·`d`·화살촉을 쓴다(노드마다 번갈아 쓰면 레이아웃이 반복된다) |
| 린트 | `runLint()` | `?lint=1`일 때 가로 넘침·오른쪽 밖 요소·14px 미만 글자·`alt` 누락을 JSON으로 출력 |
| 초기화 | | `setLang`, `setTheme`, `layoutEco`, `onScroll`, `load` 이벤트 처리 |

### `js/hero.js`

점 격자(간격 28px, 모바일·거친 포인터 36px), 16초 주기로 위아래를 오가는 스캔 빔, 모서리 괄호 박스(수명 약 3.2~5.4초, 동시에 데스크톱 2개·모바일 1개)를 그린다. **포인터에서 점이 밀려나는 효과는 성능 작업에서 제거했다**(포인터 핸들러 없음). 성능 근거와 전후 수치는 [09-performance.md](09-performance.md).

| 함수 | 하는 일 |
|---|---|
| `colors()` | `themechange` 핸들러. 색을 바로 읽지 않고 `stale`만 켠다(클릭 핸들러 안에서 읽으면 스타일 재계산이 강제된다). 정지 상태면 정지 프레임을 다시 그린다 |
| `readColors()` | 다음 `draw()`에서 `--cv-dot`·`--cv-acc`를 읽고, 강조색 문자열·빔 꼬리 그라디언트(0~56 좌표로 한 번 만들어 `translate`로 재사용)를 만든다 |
| `build()` | 정적 점 격자를 오프스크린 캔버스 `grid`에 한 번 그리고, 강조색 점 한 줄을 `strip`에 그린다. 크기·색이 바뀌어 `dirty`일 때만 다시 한다 |
| `resize()` | DPR(상한 1.5), 캔버스 크기, 격자 간격, 행·열 수를 정하고 `dirty`로 표시한 뒤 한 프레임을 즉시 그린다(정지 상태면 `showStatic()`) |
| `showStatic()` | 정지 상태: 괄호 박스 하나를 고정하고 한 프레임만 그린다 |
| `spawn(now)` | 새 괄호 박스를 무작위 위치·크기·수명으로 만든다 |
| `bracket(b, a)` | 박스 하나의 네 모서리 괄호를 알파 `a`로 그린다 |
| `draw(now)` | 한 프레임: `grid`를 `drawImage`로 복사 → 빔 근처 줄(빔에서 90px 이내)만 지우고 `strip`을 거리에 따른 알파로 덮기 → 빔 꼬리와 선 → 괄호 박스. 크기가 0이면(첫 `ResizeObserver` 호출 전) 건너뛴다 |
| `loop(now)`, `wake()`, `start()` | 그린 뒤 24ms 타이머를 거쳐 다음 `requestAnimationFrame`을 건다(마지막으로 그린 시각에서 30ms 미만이면 건너뛰어 최대 약 30fps). `start()`는 정지·화면 밖·탭 숨김이 아닐 때만 시작한다 |
| `onSize()` | 크기 변경을 150ms 디바운스해 `resize()`를 부른다. `ResizeObserver`의 첫 호출만 즉시 `resize()`(레이아웃이 끝난 뒤라 강제 레이아웃 없이 `clientWidth`를 읽는다) |

멈추는 조건: 화면 밖(`IntersectionObserver`), 탭 숨김(`visibilitychange`), 정지 모드(`still`, `motionchange`를 구독해 켜면 루프와 타이머를 끊고 정적 프레임을 그리고, 끄면 박스를 비우고 다시 시작한다). `themechange`를 구독해 테마가 바뀌면 다음 프레임에 색을 다시 읽는다.

## 7. 접근성 처리

- 건너뛰기 링크(`a.skip`), 언어별 `aria-label`(`data-aria`), `aria-pressed` 토글(언어·테마·썸네일), `aria-current`(현재 내비), `aria-expanded`/`aria-controls`(햄버거), 캡션 `aria-live=polite`.
- 썸네일은 `aria-labelledby`로 캡션 이름을 쓰고, 키보드(←→ Home End)로 이동한다. 이미지 `alt`는 현재 언어 캡션과 같다(`syncAlt`).
- 코드 탭은 `tabindex=0`, `role=region`.
- `html.still`: `prefers-reduced-motion`이거나 사용자가 `#motion`으로 끄면 켜져서 진입 모션·스캔선·구성도 그리기·코드 줄 등장을 최종 상태로 풀고 원칙 구간을 정적 목록으로 접는다. 영상에는 `controls`가 붙는다. 작성 시점에는 로드 시점에만 판단하고 이후 변경을 구독하지 않았으나, 작성 말미 스냅샷에서는 `#motion` 토글과 OS 설정 `change` 구독이 있다.
- 포커스 표시(`:focus-visible`), 색 대비(원칙 줄 꺼진 상태 불투명도 하한 .5로 대비 확보).

## 8. 알려진 한계

평가(작성 시점)에서 코드로 확인된 한계와, **작성 말미(오후 3시 20분경)에 코드를 다시 읽었을 때의 상태**다. "반영돼 보임"은 코드에서 해당 수정이 눈에 띈다는 뜻이며 [08-backlog.md](08-backlog.md)의 완료 기준으로 **검증하지 않았다.** 현재 상태는 코드와 `git log`로 확인한다. **갱신(2026-11-27)**: 이후 A1~A7은 완료·검증됐다([08-backlog.md](08-backlog.md) A 구역). 아래 표의 "반영돼 보임"과 "미확인"은 그 이전 시점의 기록이고, 표 마지막 행은 성능 작업 뒤에 남은 한계다.

| 한계(작성 시점) | 작성 말미 코드 상태 | 확인 방법 | 항목 |
|---|---|---|---|
| `.sk`의 `transition`이 `.reveal`을 덮어써 Skills 카드의 페이드·스태거가 없다 | `.sk.done`(등장 후 호버용 전환)과 `settle()`이 보인다. 반영돼 보임 | `css/style.css`의 `.sk`, `.sk.done`, `main.js`의 `settle` | A2 |
| Principles 구간에서 내비 활성 항목이 0개다(링크 없음) | `#menu`에 Principles 링크가 있다. 반영돼 보임 | `index.html`의 `#menu` | A3 |
| 자동 재생 GIF·영상·캔버스를 멈출 수단이 없다. reduced-motion은 로드 시점에만 판단 | `#motion` 토글, `setMotion()`, OS 설정 `change` 구독이 있다. 반영돼 보임 | `main.js`의 `setMotion` | A4 |
| 구성도의 점선(개발 중)이 흐르는 모션으로 "작동 중"처럼 읽힌다 | `.eco.in .e.x`에 `animation`이 없고 `flow` 키프레임도 없다. 반영돼 보임 | `css/style.css`의 `.e.x` | A5 |
| 3D·RBV·Labeling·Machine Studio 첫 포스터가 빈 화면이다. GIF 앞 1~2초가 비어 있다 | 3D PCB 포스터는 결과 프레임(Pass 5 / Fail 3)으로 바뀐 것을 확인했다. 나머지는 미확인. GIF 앞 구간 컷은 C2(미착수로 보임) | `assets/*.poster.webp` | A6, C |
| 미디어 프레임이 마우스에서 기울어 UI 글자를 읽기 어렵다. 스크린샷이 약 656px에 축소 표시되고 확대 수단이 없다 | `.frame`은 스포트라이트만, `.sk`만 기울기가 남았다. 확대 수단은 여전히 없다 | `main.js`의 포인터 블록 | A7, D5 |
| 글꼴 스택 순서 | `--font`가 Segoe UI 계열 → Pretendard → 한글 글꼴 순으로 바뀌었다. 반영돼 보임 | `css/style.css` `:root` | A1 |
| 한국어 모드에서 `<title>`·meta description이 바뀌지 않는다. 일부 영어 문장(타임라인 RBV 2.0.9·2.0.8 등)은 `data-ko`가 없다. `html[lang=ko]`인데 영어 문장에 `lang="en"`이 없다 | 그대로로 보임 | `index.html` | B3, B11 |
| 페이지가 길다(정지 모드 약 15,000px, 라이브는 원칙 구간 때문에 더 길다). 첫 제품 화면이 스크롤 약 2.7화면 뒤에 나온다 | 구조 개편은 보류 | `lint_site.py` 높이 | D3 |
| 브라우저 검증은 Edge(Chromium) 헤드리스뿐이다. Safari·Firefox·실제 터치·스크린리더 **미검증**. `.vw:has(.code)`와 `backdrop-filter`는 구형 브라우저에서 다를 수 있다 | 변동 없음 | 사람이 확인 | F7 |
| 성능: 첫 로드 직후 레이아웃 긴 작업(데스크톱 최장 0~297ms, CPU 4배 스로틀에서 최장 약 0.9~1.7초), 첫 언어 전환(4배 스로틀 약 1.0~1.5초), 느린 기기의 GIF·mp4 재생 CPU | 성능 작업 뒤에도 남음. 수치와 선택지는 [09-performance.md](09-performance.md) 3·5절 | `tools/perf_site.py` | P1~P6 |

## 9. 이 문서의 사실을 확인하는 방법 (작성 말미 스냅샷)

선택자·속성·함수 이름은 코드에서 `grep`으로 확인한다. 예: `grep -n "data-stagger" index.html js/main.js`, `grep -n "function setLang" js/main.js`, `grep -n "html.still" css/style.css`. 작성 시점 이후 코드가 바뀌어 이 문서와 다르면 **코드를 믿고 이 문서를 고친다.**
