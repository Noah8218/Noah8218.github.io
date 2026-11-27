/* Portfolio behaviour: i18n, theme, nav, reveal, counters, media viewers, ecosystem diagram, scroll-linked sections. */
(function () {
  'use strict';
  var D = document, H = D.documentElement, W = window, q = new URLSearchParams(location.search);
  var shot = q.has('shot'), lint = q.has('lint'), still = H.classList.contains('still');
  function $(s, r) { return (r || D).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || D).querySelectorAll(s)); }
  function clamp(v, a, b) { return v < a ? a : v > b ? b : v; }
  var st; try { st = W.localStorage; } catch (e) { st = null; }
  function sget(k) { try { return st.getItem(k); } catch (e) { return null; } }
  function sset(k, v) { try { st.setItem(k, v); } catch (e) { /* storage blocked: keep the in-memory state only */ } }
  var fixedVh = parseFloat(q.get('vh')) || 0;
  if (fixedVh) H.style.setProperty('--vh', fixedVh + 'px');
  function VH() { return fixedVh || W.innerHeight; }

  /* ---------- language ---------- */
  var ARIA = {
    en: { lang: 'Language', theme: 'Dark theme', menu: 'Menu', media: 'Media', motion: 'Pause motion' },
    ko: { lang: '언어', theme: '다크 테마', menu: '메뉴', media: '미디어 선택', motion: '모션 정지' }
  };
  var koEls = $$('[data-ko]');
  koEls.forEach(function (e) { e.setAttribute('data-en', e.textContent); });
  function syncAlt(vw) {
    var caps = $$('.caps p', vw);
    $$('.m', vw).forEach(function (m, i) { if (m.tagName === 'IMG' && caps[i]) m.alt = caps[i].textContent; });
  }
  function setLang(l, save) {
    H.lang = l;
    koEls.forEach(function (e) { e.textContent = e.getAttribute(l === 'ko' ? 'data-ko' : 'data-en'); });
    $$('[data-aria]').forEach(function (e) { e.setAttribute('aria-label', ARIA[l][e.getAttribute('data-aria')]); });
    $$('[data-aria=motion]').forEach(function (e) { e.title = ARIA[l].motion; });
    $$('[data-lang]').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-lang') === l); });
    $$('[data-vw]').forEach(syncAlt);
    if (save) sset('lang', l);
    layoutEco();
  }
  $$('[data-lang]').forEach(function (b) {
    b.addEventListener('click', function () { setLang(b.getAttribute('data-lang'), true); });
  });

  /* ---------- theme ---------- */
  var themeBtn = $('#theme'), ntk = 0;
  function setTheme(t, anim, save) {
    if (anim && !still) { // 바꾸는 동안 모든 전환을 끄고(.nt) 두 프레임 뒤에 푼다. 연속 클릭은 마지막 요청만 푼다
      var k = ++ntk; H.classList.add('nt');
      requestAnimationFrame(function () { requestAnimationFrame(function () { if (k === ntk) H.classList.remove('nt'); }); });
    }
    H.dataset.theme = t;
    themeBtn.setAttribute('aria-pressed', t === 'dark');
    var m = $('meta[name=theme-color]'); if (m) m.setAttribute('content', t === 'dark' ? '#090c0e' : '#f5f7f7');
    if (save) sset('theme', t);
    W.dispatchEvent(new Event('themechange'));
  }
  themeBtn.addEventListener('click', function () { setTheme(H.dataset.theme === 'dark' ? 'light' : 'dark', true, true); });

  /* ---------- nav ---------- */
  var nav = $('#nav'), bar = $('#bar'), burger = $('#burger');
  var navLinks = $$('.links a'), secs = ['about', 'projects', 'ecosystem', 'skills', 'principles', 'releases', 'contact'].map(function (id) { return D.getElementById(id); });
  function menu(open) { nav.classList.toggle('open', open); burger.setAttribute('aria-expanded', open); }
  burger.addEventListener('click', function () { menu(!nav.classList.contains('open')); });
  navLinks.forEach(function (a) { a.addEventListener('click', function () { menu(false); }); });
  D.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { menu(false); burger.focus(); } });
  D.addEventListener('click', function (e) { if (nav.classList.contains('open') && !nav.contains(e.target)) menu(false); });

  /* ---------- scroll-linked: progress bar, active link, principles, timeline ---------- */
  var prw = $('#pr-wrap'), prl = $$('.pr li'), pp = parseFloat(q.get('pp'));
  function principles() {
    if (!prw) return;
    if (still && isNaN(pp)) { prl.forEach(function (li) { li.classList.remove('cur'); }); return; } // 정지 상태는 정적 목록
    var r = prw.getBoundingClientRect(), v = VH(), cur = -1, S = 0.9 / prl.length;
    var p = isNaN(pp) ? clamp(-r.top / (r.height - v), 0, 1) : pp;
    prl.forEach(function (li, i) {
      var k = clamp((p - i * S - 0.02) / (S * 0.8), 0, 1);
      k = k * k * (3 - 2 * k);
      li.style.setProperty('--k', k.toFixed(3));
      li.classList.remove('cur');
      if (k > 0.5) cur = i;
    });
    if (cur >= 0) prl[cur].classList.add('cur');
  }
  var tl = $('#tl'), tis = $$('.ti');
  function timeline() {
    if (!tl) return;
    if (still) { tl.style.setProperty('--fill', 1); return; }
    var r = tl.getBoundingClientRect(), y = VH() * 0.62 - r.top;
    tl.style.setProperty('--fill', clamp(y / r.height, 0, 1).toFixed(4));
    tis.forEach(function (it) { it.classList.toggle('on', it.offsetTop + 12 <= y); });
  }
  var ticking = false, lastScroll = 0;
  function onScroll() {
    ticking = false;
    var max = H.scrollHeight - VH(), cur = '', line = VH() * 0.4;
    bar.style.transform = 'scaleX(' + (max > 0 ? clamp(W.scrollY / max, 0, 1) : 0).toFixed(4) + ')';
    secs.forEach(function (s) { if (s && s.getBoundingClientRect().top <= line) cur = s.id; });
    navLinks.forEach(function (a) {
      var on = a.getAttribute('href') === '#' + cur;
      a.classList.toggle('act', on);
      if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
    });
    principles(); timeline();
  }
  W.addEventListener('scroll', function () { lastScroll = performance.now(); if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  W.addEventListener('resize', onScroll);

  /* ---------- reveal ---------- */
  $$('[data-stagger]').forEach(function (p) {
    $$('.reveal', p).forEach(function (e, i) { e.style.setProperty('--rd', Math.min(i * 100, 600) + 'ms'); });
  });
  var eco = $('#eco');
  // Skills 카드: 등장 전환(.reveal, 스태거 포함)이 끝난 뒤에 .done 을 붙여 호버 틸트용 짧은 전환으로 바꾼다
  function settle(e) {
    if (e.classList.contains('sk')) setTimeout(function () { e.classList.add('done'); }, 860 + (parseFloat(e.style.getPropertyValue('--rd')) || 0));
  }
  if (still || !W.IntersectionObserver) {
    $$('.reveal').forEach(function (e) { e.classList.add('in'); });
    $$('.sk').forEach(function (e) { e.classList.add('done'); });
    if (eco) eco.classList.add('in');
  } else {
    var io = new IntersectionObserver(function (en) {
      en.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); settle(x.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    $$('.reveal').forEach(function (e) { io.observe(e); });
    if (eco) {
      var eio = new IntersectionObserver(function (en) {
        if (en[0].isIntersecting) { eco.classList.add('in'); eio.disconnect(); }
      }, { threshold: 0.25 });
      eio.observe(eco);
    }
  }
  // 히어로는 IntersectionObserver 콜백을 기다리지 않고 첫 프레임에 바로 등장시킨다(LCP)
  requestAnimationFrame(function () { $('#top').classList.add('in'); $$('.hero .reveal').forEach(function (e) { e.classList.add('in'); }); });

  /* ---------- counters ---------- */
  function count(el) {
    var txt = el.textContent, n = parseInt(txt, 10), suf = txt.replace(/^\d+/, ''), t0 = null;
    function step(ts) {
      if (still) { el.textContent = txt; return; }
      t0 = t0 || ts;
      var p = clamp((ts - t0) / 1100, 0, 1), e = 1 - Math.pow(1 - p, 3);
      el.textContent = p < 1 ? Math.round(n * e) + suf : txt; // restore the original string at the end
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if (!still && W.IntersectionObserver) {
    var cio = new IntersectionObserver(function (en) {
      en.forEach(function (x) { if (x.isIntersecting) { count(x.target); cio.unobserve(x.target); } });
    }, { threshold: 0.6 });
    $$('[data-count]').forEach(function (e) { cio.observe(e); });
  }

  /* ---------- media viewers ---------- */
  $$('.code .ln').forEach(function (l, i) { l.style.setProperty('--i', i); });
  function syncVideos() { // 정지 상태에서는 자동 재생 대신 기본 컨트롤로 직접 재생하게 한다
    $$('video').forEach(function (v) { if (still) v.preload = 'metadata'; v.controls = still && !shot && !lint; });
  }
  if (shot || lint) $$('img[loading=lazy]').forEach(function (i) { i.loading = 'eager'; });
  var viewers = [];
  function viewer(vw) {
    var ms = $$('.m', vw), caps = $$('.caps p', vw), ths = $$('.thumbs button', vw), notes = $$('.vnote', vw);
    var cur = 0, vis = false, dwell = 0;
    ms.forEach(function (m) { if (m.getAttribute('data-gif')) m.setAttribute('data-p', m.getAttribute('src')); });
    // GIF ↔ 포스터 교체는 새 이미지를 decode() 한 뒤에 보이는 요소에 반영한다(디코드가 메인 스레드 프레임을 막지 않게). 마지막 요청만 반영한다
    function show(m, s) {
      m._to = s;
      if (m.getAttribute('src') === s) return;
      var im = new Image(), set = function () { if (m._to === s) m.setAttribute('src', s); };
      im.src = s;
      (im.decode ? im.decode() : Promise.reject()).then(set, set);
    }
    function apply() {
      ms.forEach(function (m, i) {
        var on = i === cur, run = on && vis && !still && !D.hidden;
        m.classList.toggle('on', on);
        if (caps[i]) caps[i].classList.toggle('on', on);
        if (ths[i]) { ths[i].classList.toggle('on', on); ths[i].setAttribute('aria-pressed', on); }
        if (m.tagName === 'VIDEO') {
          if (run) { var pr = m.play(); if (pr && pr.catch) pr.catch(function () { /* autoplay refused: stays on the first frame */ }); } else m.pause();
        } else if (m.getAttribute('data-gif')) {
          var s = run ? m.getAttribute('data-gif') : m.getAttribute('data-p');
          if (m._to !== s) show(m, s);
        }
      });
      notes.forEach(function (n) { n.hidden = +n.getAttribute('data-for') !== cur; });
    }
    function pick(i) { cur = i; apply(); }
    ths.forEach(function (b, i) { b.addEventListener('click', function () { pick(i); }); });
    var strip = $('.thumbs', vw);
    strip.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : e.key === 'Home' ? -99 : e.key === 'End' ? 99 : 0;
      if (!d) return;
      e.preventDefault();
      var n = clamp(Math.abs(d) > 1 ? (d < 0 ? 0 : ths.length - 1) : cur + d, 0, ths.length - 1);
      pick(n); ths[n].focus();
    });
    if (W.IntersectionObserver) {
      // 재생은 행이 충분히 보인 채 300ms 머물고 스크롤이 150ms 이상 멈춘 뒤에만 시작한다(스크롤로 지나가는 행은 영상·GIF 를 시작하지 않는다). 벗어나면 즉시 정지
      var arm = function (ms) {
        dwell = setTimeout(function () {
          var rest = 150 - (performance.now() - lastScroll);
          if (rest > 0) arm(rest); else { vis = true; apply(); }
        }, ms);
      };
      new IntersectionObserver(function (en) {
        clearTimeout(dwell);
        if (en[en.length - 1].isIntersecting) arm(300);
        else { vis = false; apply(); }
      }, { threshold: 0.35 }).observe(vw);
      new IntersectionObserver(function (en, o) {
        if (en[0].isIntersecting) { ms.forEach(function (m) { if (m.tagName === 'VIDEO' && m.classList.contains('on')) m.preload = 'metadata'; }); o.disconnect(); }
      }, { rootMargin: '600px 0px' }).observe(vw);
    }
    D.addEventListener('visibilitychange', apply);
    viewers.push(apply);
    syncAlt(vw);
    apply();
  }
  $$('[data-vw]').forEach(viewer);

  /* ---------- spotlight + tilt (fine pointers only) ---------- */
  if (W.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    $$('.frame,.sk').forEach(function (el) {
      var tilt = el.classList.contains('sk'); // 미디어 프레임(.frame)은 스포트라이트만: 기울이면 스크린샷을 읽기 어렵다
      el.addEventListener('pointermove', function (e) {
        if (still) return;
        var r = el.getBoundingClientRect(), px = (e.clientX - r.left) / r.width, py = (e.clientY - r.top) / r.height;
        el.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
        el.style.setProperty('--my', (py * 100).toFixed(1) + '%');
        if (tilt) el.style.transform = 'perspective(1000px) rotateX(' + ((0.5 - py) * 8).toFixed(2) + 'deg) rotateY(' + ((px - 0.5) * 8).toFixed(2) + 'deg)';
      });
      el.addEventListener('pointerleave', function () { el.style.transform = ''; });
    });
  }

  /* ---------- motion pause (WCAG 2.2.2): html.still, localStorage 'motion' = off | on, default follows prefers-reduced-motion ---------- */
  var motionBtn = $('#motion'), rm = W.matchMedia('(prefers-reduced-motion: reduce)');
  function setMotion(off, save) {
    still = off || shot || lint; // ?shot=1, ?lint=1 은 사용자 선택과 별개로 항상 정지
    H.classList.toggle('still', still);
    motionBtn.setAttribute('aria-pressed', off);
    if (save) sset('motion', off ? 'off' : 'on');
    if (still) $$('.sk').forEach(function (e) { e.style.transform = ''; });
    syncVideos();
    viewers.forEach(function (f) { f(); });
    W.dispatchEvent(new Event('motionchange')); // hero.js 가 캔버스 루프를 멈추거나 다시 시작한다
    onScroll();
  }
  motionBtn.addEventListener('click', function () { setMotion(motionBtn.getAttribute('aria-pressed') !== 'true', true); });
  // OS 설정이 바뀌면 저장된 선택을 지우고 OS 설정을 따른다
  function onRm() { sset('motion', ''); setMotion(rm.matches, false); }
  if (rm.addEventListener) rm.addEventListener('change', onRm); else if (rm.addListener) rm.addListener(onRm);

  /* ---------- ecosystem diagram ---------- */
  function layoutEco() {
    if (!eco) return;
    var svg = $('.eco-svg', eco), heads = '', ew = eco.offsetWidth, eh = eco.offsetHeight, paths = $$('.e', svg), ds = [];
    paths.forEach(function (p) { // 읽기를 먼저 모두 끝낸다: setAttribute 가 사이에 끼면 노드마다 레이아웃이 다시 돈다
      var f = D.getElementById('n-' + p.getAttribute('data-f')), t = D.getElementById('n-' + p.getAttribute('data-t'));
      if (!f || !t) { ds.push(null); return; }
      var fx = f.offsetLeft, fy = f.offsetTop, fw = f.offsetWidth, fh = f.offsetHeight;
      var tx = t.offsetLeft, ty = t.offsetTop, tw = t.offsetWidth, th = t.offsetHeight;
      var off = parseFloat(p.getAttribute('data-tx')) || 0, d, hd, sx, sy, ex, ey, m;
      if (Math.abs(fy + fh / 2 - (ty + th / 2)) < 24) { // same row: left-to-right
        sy = ey = Math.round((fy + fh / 2 + ty + th / 2) / 2); sx = fx + fw; ex = tx;
        d = 'M' + sx + ' ' + sy + 'L' + ex + ' ' + ey;
        hd = 'M' + (ex - 9) + ' ' + (ey - 5) + 'L' + ex + ' ' + ey + 'L' + (ex - 9) + ' ' + (ey + 5) + 'Z';
      } else { // different rows: S-curve from bottom edge to top edge
        sx = Math.round(fx + fw / 2); sy = fy + fh; ex = Math.round(tx + tw / 2 + off * tw); ey = ty; m = (ey - sy) / 2;
        d = 'M' + sx + ' ' + sy + 'C' + sx + ' ' + (sy + m) + ' ' + ex + ' ' + (ey - m) + ' ' + ex + ' ' + ey;
        hd = 'M' + (ex - 5) + ' ' + (ey - 9) + 'L' + ex + ' ' + ey + 'L' + (ex + 5) + ' ' + (ey - 9) + 'Z';
      }
      ds.push(d);
      heads += '<path class="eh" style="--d:' + p.style.getPropertyValue('--d') + '" d="' + hd + '"/>';
    });
    svg.setAttribute('viewBox', '0 0 ' + ew + ' ' + eh);
    $$('.eh', svg).forEach(function (n) { n.parentNode.removeChild(n); });
    paths.forEach(function (p, i) {
      if (ds[i] === null) return;
      p.setAttribute('d', ds[i]);
      if (p.classList.contains('s')) p.setAttribute('pathLength', '1');
    });
    svg.insertAdjacentHTML('beforeend', heads);
  }
  if (eco && W.ResizeObserver) new ResizeObserver(layoutEco).observe(eco); else W.addEventListener('resize', layoutEco);

  /* ---------- lint (?lint=1): layout self-check read by the headless tool ---------- */
  function runLint() {
    var out = { w: W.innerWidth, scrollWidth: H.scrollWidth, clientWidth: H.clientWidth, height: H.scrollHeight, issues: [] };
    function add(kind, el, detail) {
      var t = (el.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 40);
      out.issues.push({ kind: kind, sel: el.tagName.toLowerCase() + (el.className && el.className.baseVal === undefined ? '.' + String(el.className).split(' ').join('.') : ''), text: t, detail: detail });
    }
    if (H.scrollWidth > H.clientWidth) out.issues.push({ kind: 'hscroll', sel: 'html', text: '', detail: H.scrollWidth + ' > ' + H.clientWidth });
    $$('body *').forEach(function (el) {
      if (el.closest('#lintout')) return;
      var cs = getComputedStyle(el);
      if (cs.display === 'none' || cs.visibility === 'hidden') return;
      var r = el.getBoundingClientRect();
      if (!r.width && !r.height) return;
      if (r.right > H.clientWidth + 1 && !el.closest('.thumbs,.code')) add('right', el, Math.round(r.right) + ' > ' + H.clientWidth);
      var own = false;
      el.childNodes.forEach(function (n) { if (n.nodeType === 3 && n.nodeValue.trim()) own = true; });
      if (own && parseFloat(cs.fontSize) < 14) add('font', el, cs.fontSize);
    });
    $$('img').forEach(function (i) { if (!i.hasAttribute('alt')) add('alt', i, i.getAttribute('src')); });
    out.dataKo = $$('[data-ko]').length;
    out.dataKoTr = $$('[data-ko-src="tr"]').length;
    var pre = D.createElement('pre'); pre.id = 'lintout'; pre.hidden = true;
    pre.textContent = JSON.stringify(out);
    D.body.appendChild(pre);
  }

  /* ---------- init ---------- */
  var l0 = q.get('lang') || sget('lang');
  setLang(l0 === 'ko' ? 'ko' : 'en', false);
  setTheme(H.dataset.theme === 'light' ? 'light' : 'dark', false, false);
  var m0 = sget('motion');
  setMotion(m0 === 'off' || (m0 !== 'on' && rm.matches), false);
  layoutEco();
  onScroll();
  W.addEventListener('load', function () {
    layoutEco();
    if (location.hash && (shot || lint)) { var t = D.getElementById(location.hash.slice(1)); if (t) t.scrollIntoView(); }
    onScroll();
    if (lint) setTimeout(runLint, 300);
  });
})();
