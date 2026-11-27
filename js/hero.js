/* Hero canvas: dot grid, a slow scan beam, and corner-bracket detection boxes. */
(function () {
  'use strict';
  var cv = document.getElementById('hero-canvas');
  if (!cv || !cv.getContext) return;
  var hero = cv.parentNode, ctx = cv.getContext('2d'), root = document.documentElement;
  var still = root.classList.contains('still');
  var small = window.matchMedia('(max-width: 768px), (pointer: coarse)');
  var w = 0, h = 0, dpr = 1, gap = 28, cols = 0, rows = 0, raf = 0, tm = 0, inView = true, t0 = performance.now(), last = 0;
  var rgb = { dot: '200,214,220', acc: '45,212,191' }, acc = '', lineFill = '', beam = null;
  var boxes = [], nextBox = 0, dirty = true, stale = true, rt = 0;
  // 점 격자는 크기·색이 바뀔 때 오프스크린 캔버스에 한 번만 그리고, 프레임마다 drawImage 한다. strip 은 스캔 빔 근처 한 줄(강조색 점)
  var grid = document.createElement('canvas'), strip = document.createElement('canvas');

  function colors() { // 테마 전환: 색 값은 다음 draw 에서 읽는다(여기서 읽으면 클릭 핸들러 안에서 스타일 재계산을 강제한다)
    stale = true;
    if (still) draw(5000);
  }

  function readColors() {
    var s = getComputedStyle(root);
    rgb.dot = s.getPropertyValue('--cv-dot').trim() || rgb.dot;
    rgb.acc = s.getPropertyValue('--cv-acc').trim() || rgb.acc;
    acc = 'rgb(' + rgb.acc + ')';
    lineFill = 'rgba(' + rgb.acc + ',0.55)';
    beam = ctx.createLinearGradient(0, 0, 0, 56); // 빔 꼬리: 0..56 좌표로 한 번 만들고 translate 로 재사용
    beam.addColorStop(0, 'rgba(' + rgb.acc + ',0)'); beam.addColorStop(1, 'rgba(' + rgb.acc + ',0.1)');
    stale = false; dirty = true;
  }

  function build() {
    var g = grid.getContext('2d'), a = strip.getContext('2d'), i, j;
    grid.width = cv.width; grid.height = cv.height;
    strip.width = cv.width; strip.height = Math.ceil(2 * dpr);
    g.setTransform(dpr, 0, 0, dpr, 0, 0); a.setTransform(dpr, 0, 0, dpr, 0, 0);
    g.fillStyle = 'rgba(' + rgb.dot + ',0.3)'; a.fillStyle = acc;
    for (i = 0; i < cols; i++) a.fillRect(i * gap - 1, 0, 2, 2);
    for (j = 0; j < rows; j++) for (i = 0; i < cols; i++) g.fillRect(i * gap - 1, j * gap - 1, 2, 2);
    dirty = false;
  }

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 1.5);
    w = hero.clientWidth; h = hero.clientHeight;
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    gap = small.matches ? 36 : 28;
    cols = Math.ceil(w / gap) + 1; rows = Math.ceil(h / gap) + 1;
    dirty = true;
    if (still) showStatic(); else draw(performance.now()); // 크기를 바꾸면 캔버스가 비므로 바로 한 프레임 그린다
  }

  function showStatic() { // 정지 상태: 고정 프레임 한 장
    boxes = [{ x: Math.round(w * 0.62 / gap) * gap, y: Math.round(h * 0.24 / gap) * gap, w: gap * 6, h: gap * 4, born: 0, life: 1e9 }];
    draw(5000);
  }

  function spawn(now) {
    var cw = 3 + Math.floor(Math.random() * 5), ch = 2 + Math.floor(Math.random() * 3);
    boxes.push({
      x: Math.floor(Math.random() * Math.max(1, cols - cw - 1)) * gap, y: Math.floor(Math.random() * Math.max(1, rows - ch - 1)) * gap,
      w: cw * gap, h: ch * gap, born: now, life: 3200 + Math.random() * 2200
    });
  }

  function bracket(b, a) {
    var l = Math.min(16, b.w / 3, b.h / 3), x = b.x, y = b.y, r = x + b.w, d = y + b.h;
    ctx.globalAlpha = a;
    ctx.beginPath();
    ctx.moveTo(x, y + l); ctx.lineTo(x, y); ctx.lineTo(x + l, y);
    ctx.moveTo(r - l, y); ctx.lineTo(r, y); ctx.lineTo(r, y + l);
    ctx.moveTo(r, d - l); ctx.lineTo(r, d); ctx.lineTo(r - l, d);
    ctx.moveTo(x + l, d); ctx.lineTo(x, d); ctx.lineTo(x, d - l);
    ctx.stroke();
  }

  function draw(now) {
    if (!w || !h) return; // 첫 ResizeObserver 호출 전
    if (stale) readColors();
    if (dirty) build();
    var t = (now - t0) / 1000, ph = (t / 16) % 1, by = h * (ph < 0.5 ? ph * 2 : 2 - ph * 2);
    var band = 90, i, j, y, bd, j1;
    if (still) by = h * 0.36;
    ctx.globalAlpha = 1;
    ctx.clearRect(0, 0, w, h);
    ctx.drawImage(grid, 0, 0, w, h);
    // 빔 근처 줄만 격자 점을 지우고 강조색 점 줄로 바꾼다(알파는 빔과의 거리로 정해진다)
    j1 = Math.min(rows - 1, Math.floor((by + band) / gap));
    for (j = Math.max(0, Math.ceil((by - band) / gap)); j <= j1; j++) {
      y = j * gap; bd = Math.abs(y - by);
      if (bd >= band) continue;
      ctx.clearRect(0, y - 2, w, 4);
      ctx.globalAlpha = 0.2 + 0.6 * Math.pow(1 - bd / band, 2);
      ctx.drawImage(strip, 0, y - 1, w, strip.height / dpr);
    }
    ctx.globalAlpha = 1;
    ctx.save(); ctx.translate(0, by - 56); ctx.fillStyle = beam; ctx.fillRect(0, 0, w, 56); ctx.restore();
    ctx.fillStyle = lineFill; ctx.fillRect(0, by, w, 1);
    ctx.strokeStyle = acc; ctx.lineWidth = 1.5;
    for (i = boxes.length - 1; i >= 0; i--) {
      var b = boxes[i], p = (now - b.born) / b.life;
      if (b.life > 1e8) { bracket(b, 0.7); continue; }
      if (p >= 1) { boxes.splice(i, 1); continue; }
      var e = Math.min(1, p / 0.18), fade = p > 0.8 ? (1 - p) / 0.2 : 1, s = 1 + 0.08 * (1 - e);
      var cx = b.x + b.w / 2, cy = b.y + b.h / 2;
      bracket({ x: cx - b.w * s / 2, y: cy - b.h * s / 2, w: b.w * s, h: b.h * s }, 0.75 * e * fade);
    }
    ctx.globalAlpha = 1;
  }

  // 주사율(60~144Hz)마다 rAF 를 걸면 그리지 않는 프레임도 메인 스레드를 깨우므로, 그린 뒤 24ms 타이머를 거쳐 다음 rAF 를 건다(최대 약 30fps)
  function wake() { tm = 0; raf = requestAnimationFrame(loop); }
  function loop(now) {
    raf = 0;
    if (still || !inView || document.hidden) return;
    if (now - last < 30) { raf = requestAnimationFrame(loop); return; }
    last = now;
    if (now > nextBox && boxes.length < (small.matches ? 1 : 2)) { spawn(now); nextBox = now + 1200 + Math.random() * 1800; }
    draw(now);
    tm = setTimeout(wake, 24);
  }
  function start() { if (!still && !raf && !tm && inView && !document.hidden) wake(); }

  window.addEventListener('themechange', colors);
  // 크기 변경은 150ms 디바운스한다. 첫 호출(레이아웃이 끝난 뒤)은 즉시 처리해 강제 레이아웃 없이 clientWidth 를 읽는다
  function onSize() { clearTimeout(rt); rt = setTimeout(resize, 150); }
  if (window.ResizeObserver) {
    var first = true;
    new ResizeObserver(function () { if (first) { first = false; resize(); } else onSize(); }).observe(hero);
  } else { resize(); window.addEventListener('resize', onSize); }
  // main.js 의 모션 정지 토글: 켜면 루프를 끊고 정적 프레임, 끄면 루프를 다시 시작한다
  window.addEventListener('motionchange', function () {
    var s = root.classList.contains('still');
    if (s === still) return;
    still = s;
    if (still) { cancelAnimationFrame(raf); clearTimeout(tm); raf = tm = 0; showStatic(); }
    else { boxes = []; nextBox = 0; start(); }
  });
  if (window.IntersectionObserver) {
    new IntersectionObserver(function (en) { inView = en[0].isIntersecting; if (inView) start(); }).observe(hero);
  }
  document.addEventListener('visibilitychange', start);
  start();
})();
