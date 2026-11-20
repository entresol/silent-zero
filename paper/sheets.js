// The two doors of the start page. Each tab on the edge is a link to a real page (/use/, /devel/). With JavaScript a click
// lays that page over the start page as a sheet instead: it slides in from its side, one sheet at a time, and the start page
// underneath does not move. Esc, the Close button, a click on the visible edge or the tab on the sheet put it back. The
// address (/#use, /#devel) and the Back button follow the sheet; the hash keeps the start page's relative links working.
// The pages are fetched once, in the idle time after loading.
(() => {
  const tabs = [...document.querySelectorAll('a.sh-tab')];
  if (!tabs.length || !window.fetch || !window.DOMParser) return;
  const root = document.documentElement;
  const behind = [...document.querySelectorAll('header.hero, .layout, .az-band, footer, button.menu')];
  const scrim = document.createElement('div');
  scrim.className = 'sh-scrim';
  document.body.append(scrim);
  const leaves = new Map(), pages = new Map();
  let current = null, lastTab = null, seq = 0, timer = null;

  function load(url) {
    if (!pages.has(url)) {
      pages.set(url, fetch(url, { credentials: 'same-origin' }).then(r => {
        if (!r.ok) throw new Error(r.status);
        return r.text();
      }).then(text => {
        const d = new DOMParser().parseFromString(text, 'text/html');
        const name = d.querySelector('.titleblock .name'), art = d.querySelector('article');
        if (!name || !art) throw new Error('shape');
        const sub = d.querySelector('.titleblock .sub');
        return { title: name.textContent, lede: sub ? sub.textContent : '', html: art.innerHTML };
      }).catch(e => { pages.delete(url); throw e; }));
    }
    return pages.get(url);
  }

  for (const tab of tabs) {
    const name = tab.dataset.sheet, left = tab.classList.contains('sh-tab-l');
    const leaf = document.createElement('div');
    leaf.className = 'sh-leaf ' + (left ? 'sh-leaf-l' : 'sh-leaf-r');
    const page = document.createElement('section');
    page.className = 'sh-page';
    page.id = 'sh-page-' + name;
    page.setAttribute('role', 'dialog');
    page.setAttribute('aria-modal', 'false');
    page.setAttribute('aria-label', tab.textContent.trim());
    page.tabIndex = -1;
    page.inert = true;
    page.innerHTML = '<div class="sh-in"><button class="sh-close" type="button">Close</button><div class="sh-body"></div></div>';
    document.body.append(leaf);
    leaf.append(tab, page);
    tab.setAttribute('role', 'button');
    tab.setAttribute('aria-expanded', 'false');
    tab.setAttribute('aria-controls', page.id);
    leaves.set(name, { leaf, page, tab, url: new URL(tab.getAttribute('href'), location.href).pathname, body: page.querySelector('.sh-body'), ready: false });
    tab.addEventListener('click', e => { e.preventDefault(); toggle(name); });
    tab.addEventListener('pointerenter', () => load(leaves.get(name).url).catch(() => {}));
    page.querySelector('.sh-close').addEventListener('click', () => close());
  }

  function slow() {
    for (const { leaf } of leaves.values()) leaf.classList.add('moving');
    clearTimeout(timer);
    const s = parseFloat(getComputedStyle(root).getPropertyValue('--sh-slide')) || 1;
    timer = setTimeout(() => { for (const { leaf } of leaves.values()) leaf.classList.remove('moving'); }, s * 1000 + 80);
  }

  async function show(name, how, opener) {   // how: 'push' (from the start page), 'replace' (swap), or '' (the history moved already)
    const my = ++seq, L = leaves.get(name);
    if (!L.ready) {
      try {
        const c = await load(L.url);
        if (my !== seq) return;
        L.body.innerHTML = '<h2 class="sh-title">' + c.title.replace(/[&<]/g, ch => ({ '&': '&amp;', '<': '&lt;' }[ch])) + '</h2><p class="sh-lede">' +
          c.lede.replace(/[&<]/g, ch => ({ '&': '&amp;', '<': '&lt;' }[ch])) + '</p>' + c.html;
        L.ready = true;
      } catch (_) { location.href = L.url; return; }   // no sheet without its content: go to the page itself
    }
    const prev = current;
    current = name;
    slow();
    for (const [k, v] of leaves) {
      const on = k === name;
      v.leaf.classList.toggle('open', on);
      v.tab.setAttribute('aria-expanded', on);
      v.page.inert = !on;
    }
    scrim.classList.add('on');
    root.classList.add('sh-open');
    behind.forEach(el => { el.inert = true; });
    lastTab = opener || L.tab;
    setTimeout(() => { if (current === name) L.page.focus({ preventScroll: true }); }, 200);
    try {
      if (how === 'push') history.pushState({ sheet: name }, '', '#' + name);
      else if (how === 'replace') history.replaceState({ sheet: name }, '', '#' + name);
    } catch (_) {}
    if (prev && prev !== name) leaves.get(prev).page.scrollTop = 0;
  }

  function hide(fromHistory) {
    if (!current) return;
    seq++;
    current = null;
    slow();
    for (const v of leaves.values()) { v.leaf.classList.remove('open'); v.tab.setAttribute('aria-expanded', 'false'); v.page.inert = true; }
    scrim.classList.remove('on');
    root.classList.remove('sh-open');
    behind.forEach(el => { el.inert = false; });
    setTimeout(() => { if (!current && lastTab) lastTab.focus({ preventScroll: true }); }, 200);
  }

  function close() {
    if (!current) return;
    if (history.state && history.state.sheet) history.back();   // the popstate below closes the sheet
    else { hide(); try { history.replaceState(null, '', location.pathname + location.search); } catch (_) {} }
  }

  function toggle(name, opener) {
    if (current === name) close();
    else show(name, current ? 'replace' : 'push', opener);
  }

  function fromHash() {
    const s = location.hash.slice(1);
    if (leaves.has(s)) show(s, ''); else hide(true);
  }
  addEventListener('popstate', fromHash);
  // on narrow screens the doors are links in the header
  for (const a of document.querySelectorAll('.sh-inline a[data-sheet]')) a.addEventListener('click', e => { if (leaves.has(a.dataset.sheet)) { e.preventDefault(); toggle(a.dataset.sheet, a); } });
  scrim.addEventListener('click', close);
  addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  // inside a sheet the link to the other door swaps the sheets
  document.addEventListener('click', e => {
    const a = e.target.closest('.sh-page a[href]');
    if (!a) return;
    const u = new URL(a.href, location.href);
    for (const [name, v] of leaves) if (u.origin === location.origin && u.pathname === v.url && !e.metaKey && !e.ctrlKey) { e.preventDefault(); toggle(name); return; }
  });
  if (leaves.has(location.hash.slice(1))) show(location.hash.slice(1), '');   // a link to /#use or /#devel opens the sheet
  (window.requestIdleCallback || (f => setTimeout(f, 1500)))(() => { for (const v of leaves.values()) load(v.url).catch(() => {}); });
})();
