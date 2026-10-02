const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
// Scroll reveal + progress bar
const io = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  e.target.classList.add('in');
  const b = $('.bar i', e.target); if (b) b.style.width = b.dataset.level + '%';
  io.unobserve(e.target);
}), { threshold: .12 });
$$('.rv').forEach((el, i) => { el.style.transitionDelay = (i % 4) * 80 + 'ms'; io.observe(el); });
// Mobile menu
$('.burger').onclick = () => $('.nav nav').classList.toggle('open');
$$('.nav nav a').forEach(a => a.onclick = () => $('.nav nav').classList.remove('open'));
// Album filter
$$('.filters button').forEach(b => b.onclick = () => {
  $$('.filters button').forEach(x => x.classList.toggle('on', x === b));
  $$('.ph').forEach(p => p.classList.toggle('hide', b.dataset.f !== 'all' && p.dataset.cat !== b.dataset.f));
});
// Lightbox (sertifikat & album) dengan next/prev
const lb = $('.lb'); let list = [], idx = 0;
const show = () => { $('img', lb).src = list[idx].dataset.lb; $('p', lb).textContent = list[idx].dataset.cap || ''; };
$$('[data-lb]').forEach(el => el.onclick = () => {
  list = $$(`[data-group="${el.dataset.group}"]:not(.hide)`); idx = list.indexOf(el); show(); lb.classList.add('on');
});
const step = d => { idx = (idx + d + list.length) % list.length; show(); };
$('.nx').onclick = () => step(1); $('.pv').onclick = () => step(-1); $('.x').onclick = () => lb.classList.remove('on');
lb.onclick = e => { if (e.target === lb) lb.classList.remove('on'); };
addEventListener('keydown', e => {
  if (!lb.classList.contains('on')) return;
  if (e.key === 'Escape') lb.classList.remove('on');
  if (e.key === 'ArrowRight') step(1);
  if (e.key === 'ArrowLeft') step(-1);
});
// Form kontak -> Flask
$('#cf').onsubmit = async e => {
  e.preventDefault(); const st = $('#st');
  try {
    const r = await fetch('/contact', { method: 'POST', body: new FormData(e.target) }), j = await r.json();
    st.textContent = j.msg; if (j.ok) e.target.reset();
  } catch { st.textContent = 'Gagal mengirim, coba lagi.'; }
};
