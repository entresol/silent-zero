#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""Builds the GitHub Pages landing page (index.html) for the Silent Zero paper. No author names."""
import re
import shutil
import subprocess
import sys
from pathlib import Path

src_dir = Path(sys.argv[1])   # folder with src.md, fig1.png, fig2.png, stations.json, paper.pdf
out = Path(sys.argv[2])       # site output folder
pdf_name = "zos-zero-os.pdf"
sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import changelog
import glossary
gl_groups = glossary.parse(Path(__file__).resolve().parent / "glossary.md")

md = (src_dir / "src.md").read_text(encoding="utf-8")
lines = md.splitlines()
body = "\n".join(lines[4:]).split("\n", 1)[1]      # drop title, subtitle, date/author line

# the prologue's first two paragraphs become the hero; remove them from the body
pro = re.search(r"## Prologue: Imagine it's 1991\n\n((?:> [^\n]*\n|>\n)+\n)?Imagine it's 1991\. We are about to release a few lines of code into a world that will be very different from today\.\n\n", body)
body = body[:pro.start()] + "## Prologue: Imagine it's 1991\n\n" + (pro.group(1) or "") + body[pro.end():]

import json, html as _h
cap1 = "Figure 1. The Silent Zero stack. A gold frame marks the trusted base: every part a guarantee depends on, isolated or not. The tag says what we know about it. Authority runs from the agent through the broker, motion through the safety controller; there is no third path."
alt1 = ("Diagram of the Silent Zero stack. Top: agents (untrusted, outside the trusted base) send authority requests to the capability broker "
        "(isolated but in the trusted base, tested, target proven), which alone reaches tools and model access (outside the base). "
        "Agents send motion proposals to the safety controller and control loops (trusted base, tested, target proven), which alone move the actuator. "
        "Below: user-mode drivers and the Linux driver island (outside the base where the IOMMU confines the device), the static system description (trusted, tested), "
        "the seL4 microkernel with MCS (trusted, proven for its verified configurations), the bootloader (trusted, assumed) and firmware, hardware and root of trust (trusted, assumed).")
fig1 = (f'<figure class="wide"><div class="fig-scroll"><img src="assets/fig1.png" alt="{_h.escape(alt1)}" width="1344" loading="lazy"></div>'
        f'<figcaption>{cap1}</figcaption></figure>')
body = re.sub(r"&#91;embedded content: Fig\. 1[^\n]*", "\n```{=html}\n" + fig1 + "\n```\n", body)

stations = json.loads((src_dir / "stations.json").read_text(encoding="utf-8"))
kinds = {"DEMO": "Demonstration", "TEST": "Test", "PROOF": "Proof"}
items = []
for yr, name, sub, kind, check in stations:
    badge = f'<span class="kind">{kinds[kind]}</span> ' if kind else ""
    cls = ' class="start"' if not kind else ""
    items.append(f'<li{cls}><span class="year">{yr}</span><div><p class="st-name">{_h.escape(name)}</p>'
                 f'<p class="st-sub">{_h.escape(sub)}</p><p class="st-check">{badge}{_h.escape(check)}</p></div></li>')
cap2 = "Figure 2. The path from 2026 to 2031, read from the bottom up. Each station names its evidence and whether it is a demonstration, a test or a proof; a failed check stops the path."
fig2 = (f'<figure class="timeline"><ol>{"".join(items)}</ol><figcaption>{cap2}</figcaption></figure>')
body = re.sub(r"&#91;embedded content: Fig\. 2[^\n]*", "\n```{=html}\n" + fig2 + "\n```\n", body)

body = body.replace("Table 1 lists them", "The table lists them")
body = body.replace("## References", glossary.markdown(gl_groups, anchors=True) + "\n## References", 1)
html_body = subprocess.run(
    ["pandoc", "-f", "markdown", "-t", "html5", "--wrap=none"],
    input=body, capture_output=True, text=True, check=True).stdout

# external links open in a new tab; tables get a wrapper for horizontal scroll on phones
html_body = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" rel="noopener" target="_blank"', html_body)
html_body = html_body.replace("<table>", '<div class="table-wrap wide"><table>').replace("</table>", "</table></div>")

# references get ids; in-text citations link to them
ref_part = html_body.split('<h2 id="references">', 1)
refs_html = ref_part[1]
cites = {}
def cite_key(li_text):
    m = re.match(r"\s*(.+?) \((?:eds\.\) \()?((?:\d{4}|n\.d\.)[a-z]?(?:-[a-z])?)\)", li_text)
    if not m:
        return None
    who, year = m.group(1), m.group(2)
    who = re.sub(r"\s*\(eds\.\)", "", who)
    if " et al." in who:
        names = who.split(",")[0] + " et al."
    elif ";" in who:
        parts = [p.strip().split(",")[0] for p in who.split(";")]
        names = parts[0] + " and " + parts[1] if len(parts) == 2 else parts[0] + " et al."
    elif re.match(r"^[^,]+, [A-Z]\.", who):
        names = who.split(",")[0]
    else:
        names = who
    return f"{names} {year}"
n = 0
def add_id(m):
    global n
    n += 1
    txt = re.sub("<[^>]+>", "", m.group(1)).replace("\xa0", " ")
    k = cite_key(txt)
    rid = f"ref-{n}"
    if k:
        cites[k] = rid
    return f'<li id="{rid}">{m.group(1)}</li>'
refs_html = re.sub(r"<li>(.*?)</li>", add_id, refs_html, flags=re.S)
main_html = ref_part[0]
keys = sorted(cites, key=len, reverse=True)
pat = re.compile("|".join(re.escape(k).replace(r"\ ", "[ \xa0]") for k in keys))
def link_text(chunk):
    return pat.sub(lambda m: f'<a class="cite" href="#{cites[m.group(0).replace(chr(160), " ")]}">{m.group(0)}</a>', chunk)
# only touch text outside tags and outside existing links
segs = re.split(r"(<a\b.*?</a>|<[^>]+>)", main_html, flags=re.S)
main_html = "".join(seg if seg.startswith("<") else link_text(seg) for seg in segs)
# glossary terms: the first use in each section links to its entry and shows the meaning on hover
gl_terms = sorted(((m, e) for _, es in gl_groups for e in es for m in e["matches"]), key=lambda t: len(t[0]), reverse=True)
gl_lookup = dict(gl_terms)
gl_pat = re.compile(r"(?<![\w-])(" + "|".join(re.escape(m) for m, _ in gl_terms) + r")(?![\w-])")
def link_terms(section):
    seen = set()
    def rep(m):
        e = gl_lookup[m.group(1)]
        if e["id"] in seen:
            return m.group(0)
        seen.add(e["id"])
        return f'<a class="gl" href="#{e["id"]}" data-def="{_h.escape(e["meaning"])}">{m.group(0)}</a>'
    segs = re.split(r"(<a\b.*?</a>|<h[1-6]\b.*?</h[1-6]>|<figure\b.*?</figure>|<[^>]+>)", section, flags=re.S)
    return "".join(seg if seg.startswith("<") else gl_pat.sub(rep, seg) for seg in segs)
text_part, gl_part = main_html.split('<h2 id="glossary">', 1)
text_part = "".join(link_terms(sec) for sec in re.split(r"(?=<h2 )", text_part))
main_html = text_part + '<h2 id="glossary">' + gl_part
html_body = main_html + '<h2 id="references">' + refs_html
n_refs = n
unlinked = sorted(set(re.findall(r"\(([A-Z][^()]*?\d{4}[a-z]?)\)", re.sub(r"<a\b.*?</a>", "", main_html).replace("\xa0", " "))))
if unlinked:
    print("check citations:", unlinked[:12])

def label_table(m):
    t = m.group(0)
    heads = [re.sub("<[^>]+>", "", h).strip() for h in re.findall(r"<th[^>]*>(.*?)</th>", t, flags=re.S)]
    def lab_row(r):
        cells = iter(heads)
        return re.sub(r"<td([^>]*)>", lambda c: f'<td{c.group(1)} data-label="{next(cells, "")}">', r.group(0))
    return re.sub(r"<tr.*?</tr>", lab_row, t, flags=re.S)
html_body = re.sub(r"<table>.*?</table>", label_table, html_body, flags=re.S)

# changes: from ../CHANGELOG.md, each paper version with the PDF as it was
REPO = "https://github.com/entresol/silent-zero"
changes = changelog.parse()
rev_items = []
for ver, scope, text in changes:
    pdf = f' · <a href="versions/zos-zero-os-{ver}.pdf">PDF of this version</a>' if changelog.has_pdf(ver) else ""
    rev_items.append(f'<li><p class="rev-date"><span class="rev-ver">{ver}</span> · {scope}{pdf}</p><p>{text}</p></li>')
revisions_html = ('<h2 id="changes">Changes</h2>'
                  f'<p>Every change is recorded in the <a href="{REPO}/commits/main">commit history</a>. '
                  f'This list says what changed in substance: in the paper, on this page and in the project. Its source is <a href="{REPO}/blob/main/CHANGELOG.md">CHANGELOG.md</a>.</p>'
                  f'<ol class="revisions">{"".join(rev_items)}</ol>')
html_body = html_body + revisions_html

# the page, not the paper, says how to take part: after In brief, before the Abstract
REPO_URL = "https://github.com/entresol/silent-zero"
involved = (f'<h2 id="get-involved">Get involved</h2>\n'
            f'<p>We are looking for people who know firmware, formal verification or robots, and who want to test this argument before the architecture hardens around it.</p>\n'
            f'<ul>\n<li>Discuss an idea or ask a question: <a href="{REPO_URL}/discussions" rel="noopener" target="_blank">Discussions</a>.</li>\n'
            f'<li>See what the sources behind the paper show, page by page: the <a href="wiki/">wiki</a>.</li>\n'
            f'<li>Point out a flaw, a wrong claim or a missing source: <a href="{REPO_URL}/issues" rel="noopener" target="_blank">Issues</a>.</li>\n'
            f'<li>Propose a change to the paper or the code: a pull request; <a href="{REPO_URL}/blob/main/CONTRIBUTING.md" rel="noopener" target="_blank">CONTRIBUTING.md</a> says how we work.</li>\n</ul>\n')
assert html_body.count('<h2 id="abstract">') == 1
html_body = html_body.replace('<h2 id="abstract">', involved + '<h2 id="abstract">')
CURRENT_VERSION = changelog.current(changes)
pdf_name = f"versions/zos-zero-os-{CURRENT_VERSION}.pdf"

# table of contents from h2, led by a link back to the top
toc = '<li><a href="#top">\u2191 Top</a></li>' + "".join(f'<li><a href="#{i}">{re.sub("<[^>]+>", "", t)}</a></li>'
              for i, t in re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', html_body))

# A published version never changes. Once its PDF is on origin/main, the build keeps that file,
# and the page describes the PDF it serves, not the one just built (another TeX gives other pages).
published = subprocess.run(["git", "-C", str(out), "cat-file", "-e", f"origin/main:{pdf_name}"],
                           capture_output=True).returncode == 0
served = out / pdf_name if published else src_dir / "paper.pdf"
pages = subprocess.run(["pdfinfo", str(served)], capture_output=True, text=True).stdout
pages = re.search(r"Pages:\s+(\d+)", pages).group(1)
# the header in five languages; English is in the page, the script swaps in the others
hero_src = json.loads((Path(__file__).resolve().parent / "hero.json").read_text(encoding="utf-8"))
fill = {"version": CURRENT_VERSION, "pdf": pdf_name, "pages": pages, "refs": n_refs,
        "loader": "https://github.com/entresol/silent-zero/tree/main/loader", "issues": "https://github.com/entresol/silent-zero/issues"}
hero = {l: {k: v.format_map(fill) for k, v in t.items()} for l, t in hero_src.items() if not l.startswith("_")}
en = hero["en"]
langs = "".join(f'<button type="button" lang="{l}" aria-pressed="{str(l == "en").lower()}">{t["label"]}</button>' for l, t in hero.items())
hero_json = json.dumps({l: {k: v for k, v in t.items() if k != "label"} for l, t in hero.items()}, ensure_ascii=False).replace("</", "<\\/")
css = (Path(__file__).resolve().parent / "site.css").read_text(encoding="utf-8")
css = "\n".join(l for l in css.splitlines() if "SPDX-License-Identifier" not in l) + "\n"
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Silent Zero OS</title>
<meta name="description" content="Silent Zero OS – Bare minimum. Verified. Real-time. An OS for the AI era. A working paper: a bootloader, a formally verified microkernel and the bare minimum to run AI safely and in real time, built entirely from existing open source.">
<!-- link previews in social media and chats; the image comes from paper/ogshot.py -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://silentzero.ooo/">
<meta property="og:site_name" content="Silent Zero OS">
<meta property="og:title" content="Silent Zero OS – Imagine it's 1991">
<meta property="og:description" content="Bare minimum. Verified. Real-time. An OS for the AI era. A working paper: a formally verified microkernel and the bare minimum to run AI agents safely and in real time.">
<meta property="og:image" content="https://silentzero.ooo/assets/og.png">
<meta property="og:image:width" content="2400">
<meta property="og:image:height" content="1260">
<meta property="og:image:alt" content="Imagine it's 1991. We are about to release a few lines of code into a world that will be very different from today. Silent Zero OS: Bare minimum. Verified. Real-time. An OS for the AI era.">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="favicon.ico" sizes="32x32">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/inter-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/nunito-sans-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<style>
{css}
</style>
</head>
<body>
<header class="hero" id="top" lang="en">
  <div class="langs" role="group" aria-label="Language" hidden>{langs}</div>
  <div class="hero-inner">
    <h1 data-t="h1">{en["h1"]}</h1>
    <p class="lede" data-t="lede">{en["lede"]}</p>
    <div class="titleblock">
      <p class="name">Silent Zero OS</p>
      <p class="sub" data-t="sub">{en["sub"]}</p>
      <p class="ver" data-t="ver">{en["ver"]}</p>
    </div>
    <p class="status" data-t="status">{en["status"]}</p>
    <div class="actions">
      <a class="btn" href="silent-zero.pdf" download="silent-zero.pdf" data-t="btn">{en["btn"]}</a>
      <span class="meta" data-t="meta">{en["meta"]}</span>
    </div>
  </div>
</header>
<script>
// the header in five languages. Plain lines flip like a split-flap board, lines with links are swapped;
// the choice is remembered. On a first visit whose browser prefers German, French, Spanish or Italian, the header
// starts in English and flips into that language after two seconds, unless the visitor arrived at an anchor
// further down or prefers reduced motion. Without JavaScript the selector stays hidden and the header stays English.
(() => {{
  const T = {hero_json}, head = document.getElementById('top'), bar = head.querySelector('.langs');
  const still = matchMedia('(prefers-reduced-motion: reduce)').matches, FLAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  function flip(el, to) {{
    const from = [...el.textContent], next = [...to], n = Math.max(from.length, next.length);
    const stagger = Math.max(6, Math.round(1400 / n)), flips = n > 80 ? 3 : n > 40 ? 4 : 5, tick = n > 80 ? 30 : 35;
    clearInterval(el._flap);
    const t0 = performance.now();
    el._flap = setInterval(() => {{
      const now = performance.now() - t0;
      el.textContent = Array.from({{ length: n }}, (_, i) => {{
        const c = next[i] ?? '', start = i * stagger;
        if (now < start) return from[i] ?? '';
        if (now >= start + flips * tick || c === ' ' || c === '') return c;
        return FLAP[Math.random() * FLAP.length | 0];
      }}).join('');
      if (now >= (n - 1) * stagger + flips * tick) {{ clearInterval(el._flap); el.textContent = to; }}
    }}, tick);
  }}
  function set(l, animate) {{
    head.lang = l;
    bar.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', b.lang === l));
    head.querySelectorAll('[data-t]').forEach(el => {{
      const v = T[l][el.dataset.t];
      if (/</.test(v)) el.innerHTML = v;
      else if (animate && !still) flip(el, v);
      else el.textContent = v;
    }});
  }}
  function keep(l) {{ try {{ localStorage.setItem('lang', l); }} catch (_) {{}} }}
  let teaser = null;
  bar.addEventListener('click', e => {{
    const b = e.target.closest('button');
    if (!b) return;
    clearTimeout(teaser);
    keep(b.lang);
    if (b.lang !== head.lang) set(b.lang, true);
  }});
  let saved = null;
  try {{ saved = localStorage.getItem('lang'); }} catch (_) {{}}
  if (T[saved]) {{ if (saved !== 'en') set(saved, false); }}
  else {{
    // the first of the browser's preferred languages that we offer; English means no teaser
    const want = (navigator.languages || [navigator.language]).map(x => String(x).slice(0, 2).toLowerCase()).find(x => T[x]);
    if (want && want !== 'en' && !still && (!location.hash || location.hash === '#top'))
      teaser = setTimeout(() => {{ set(want, true); keep(want); }}, 2000);
    else if (want && want !== 'en') {{ set(want, false); keep(want); }}
  }}
  bar.hidden = false;
}})();
</script>
<button class="menu" type="button" aria-controls="toc" aria-expanded="false" aria-label="Contents" hidden><span></span></button>
<div class="layout">
  <nav class="toc" id="toc" aria-label="Contents"><p>Contents</p><ol>{toc}</ol></nav>
  <article>
{html_body}
  </article>
</div>
<footer><div><span class="about"><span>Silent Zero OS</span><span class="sep"> · </span><span>Working paper {CURRENT_VERSION}</span><span class="sep"> · </span><span>Text and figures <a href="https://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a></span></span><span class="links"><a href="silent-zero.pdf" download="silent-zero.pdf">PDF</a> <a href="wiki/">Wiki</a> <a href="https://github.com/entresol/silent-zero">GitHub</a> <a href="https://unwritten.studio/impressum">Imprint</a></span></div></footer>
<script>
// glossary tooltips open to the left where they would run off the right edge
document.querySelectorAll('a.gl').forEach(a => a.addEventListener('pointerenter', () => {{
  a.classList.toggle('flip', a.getBoundingClientRect().left + 360 > document.documentElement.clientWidth - 16);
}}));
// touch screens have no hover: a tap on a term opens its meaning in a popover anchored to it (Apple HIG, Material
// rich tooltips); a second tap on the term or a tap elsewhere closes it, and its footer links to the glossary entry.
// The popover sits in the page below the term's line, or above it where the screen has no room, so it scrolls with it.
if (matchMedia('(hover: none)').matches) {{
  const col = document.querySelector('article'), pop = document.createElement('div');
  pop.className = 'gl-pop'; pop.id = 'gl-pop'; pop.hidden = true; document.body.append(pop);
  let open = null;
  function close() {{ if (open) open.setAttribute('aria-expanded', 'false'); open = null; pop.hidden = true; }}
  function show(a) {{
    close();
    const def = document.createElement('p'), foot = document.createElement('p'), link = document.createElement('a');
    def.textContent = a.dataset.def;
    foot.className = 'gl-pop-foot'; link.href = a.getAttribute('href'); link.textContent = 'In the glossary \u2192';
    foot.append(link); pop.replaceChildren(def, foot); pop.hidden = false;
    const c = col.getBoundingClientRect(), cs = getComputedStyle(col), r = a.getClientRects()[0];
    const left = c.left + parseFloat(cs.paddingLeft), width = Math.min(c.width - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight), 576);
    pop.style.left = left + scrollX + 'px'; pop.style.width = width + 'px';
    const h = pop.offsetHeight, above = r.bottom + 10 + h > innerHeight - 8 && r.top - 10 - h > 8;
    pop.classList.toggle('above', above);
    pop.style.top = (above ? r.top - 10 - h : r.bottom + 10) + scrollY + 'px';
    pop.style.setProperty('--arrow', Math.min(Math.max(r.left + r.width / 2 - left, 12), width - 12) + 'px');
    open = a; a.setAttribute('aria-expanded', 'true');
  }}
  document.querySelectorAll('article a.gl').forEach(a => {{
    a.setAttribute('aria-controls', 'gl-pop'); a.setAttribute('aria-expanded', 'false');
    a.addEventListener('click', e => {{ e.preventDefault(); open === a ? close() : show(a); }});
  }});
  pop.addEventListener('click', e => {{ if (e.target.closest('a')) close(); }});
  // a tap elsewhere closes it. iOS Safari sends no click for a tap on plain text, so this listens to pointer events
  // and counts a touch as a tap only if the finger barely moved; a scroll leaves the popover open
  let down = null;
  document.addEventListener('pointerdown', e => {{ down = {{ x: e.clientX, y: e.clientY }}; }}, {{ passive: true }});
  document.addEventListener('pointerup', e => {{
    const tap = down && Math.hypot(e.clientX - down.x, e.clientY - down.y) < 10;
    down = null;
    if (tap && open && !pop.contains(e.target) && !e.target.closest('article a.gl')) close();
  }}, {{ passive: true }});
  document.addEventListener('pointercancel', () => {{ down = null; }}, {{ passive: true }});
  document.addEventListener('keydown', e => {{ if (e.key === 'Escape') close(); }});
  let w = innerWidth;   // phones resize when the address bar slides away while scrolling; close only on a real change
  addEventListener('resize', () => {{ if (innerWidth !== w) {{ w = innerWidth; close(); }} }});
  document.querySelector('button.menu').addEventListener('click', close);
}}
// narrow screens: the menu button opens the contents as a panel; while it is open the page behind it is inert
const menu = document.querySelector('button.menu'), toc = document.getElementById('toc');
const behind = document.querySelectorAll('header.hero, article, footer');
const isOpen = () => menu.getAttribute('aria-expanded') === 'true';
function setMenu(open) {{
  menu.setAttribute('aria-expanded', open);
  document.documentElement.classList.toggle('menu-open', open);
  behind.forEach(el => el.inert = open);
  if (open) toc.querySelector('a').focus();
}}
menu.hidden = false;   // without JavaScript the button stays hidden and the page works as before
menu.addEventListener('click', () => setMenu(!isOpen()));
toc.addEventListener('click', e => {{ if (e.target.closest('a')) setMenu(false); }});
document.addEventListener('click', e => {{ if (isOpen() && !toc.contains(e.target) && !menu.contains(e.target)) setMenu(false); }});
document.addEventListener('keydown', e => {{ if (e.key === 'Escape' && isOpen()) {{ setMenu(false); menu.focus(); }} }});
matchMedia('(min-width: 76rem)').addEventListener('change', e => {{ if (e.matches) setMenu(false); }});
// the contents mark the section being read: the last heading that has passed the upper fifth of the screen
const heads = [...document.querySelectorAll('article h2[id]')], links = new Map([...toc.querySelectorAll('a')].map(a => [a.hash.slice(1), a]));
let current = null, queued = false;
function mark() {{
  queued = false;
  const h = heads.filter(h => h.getBoundingClientRect().top < innerHeight / 5).pop(), a = h ? links.get(h.id) : null;
  if (a === current) return;
  current?.removeAttribute('aria-current'); a?.setAttribute('aria-current', 'location'); current = a;
}}
addEventListener('scroll', () => {{ if (!queued) {{ queued = true; requestAnimationFrame(mark); }} }}, {{ passive: true }});
mark();
</script>
</body>
</html>
"""

out.mkdir(parents=True, exist_ok=True)
(out / "assets").mkdir(exist_ok=True)
(out / "index.html").write_text(page, encoding="utf-8")
fontdir = Path(__file__).resolve().parent.parent / "assets" / "fonts"   # self-hosted fonts, SIL OFL 1.1
(out / "assets" / "fonts").mkdir(exist_ok=True)
if (out / "assets" / "fonts").resolve() != fontdir.resolve():
    for f in list(fontdir.glob("*.woff2")) + list(fontdir.glob("LICENSE*")):
        shutil.copy(f, out / "assets" / "fonts" / f.name)
shutil.copy(src_dir / "fig1.png", out / "assets" / "fig1.png")
old_fig2 = out / "assets" / "fig2.png"
if old_fig2.exists():
    old_fig2.unlink()
(out / "versions").mkdir(exist_ok=True)
# warn if the paper just built differs in its words from the published one: that needs a new version
if published:
    def text(p):
        raw = subprocess.run(["pdftotext", str(p), "-"], capture_output=True, text=True).stdout
        return re.sub(r"-\n", "", raw).split()                # line breaks and hyphenation vary with TeX
    if text(src_dir / "paper.pdf") != text(out / pdf_name):
        print(f"warning: the paper differs from published {CURRENT_VERSION}, which stays as it was; "
              "add a new paper version to CHANGELOG.md", file=sys.stderr)
else:
    shutil.copy(src_dir / "paper.pdf", out / pdf_name)      # this version, named by its version
shutil.copy(out / pdf_name, out / "silent-zero.pdf")         # stable name, always the newest version
shutil.copy(out / pdf_name, out / "zos-zero-os.pdf")         # the same under the old name, for existing links
(out / ".nojekyll").write_text("")
print("ok", len(page))
