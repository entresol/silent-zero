#!/usr/bin/env python3
"""Local prototype of the two sheets ("Use it" from the left, "Get involved" from the right) over the entry sheet.

Not part of the site and not wired into paper/build.sh. It takes the built ../index.html (its styles, header, the band of
latest changes and the existing Get involved section), adds two sheets with placeholder content, and writes
proto-sheets/index.html. Open that file in a browser, or serve the repository root and open /proto-sheets/.
Run: python3 proto-sheets/build.py"""
import re
from pathlib import Path

here = Path(__file__).resolve().parent
src = (here.parent / "index.html").read_text(encoding="utf-8")

css = re.search(r"<style>(.*?)</style>", src, re.S).group(1)
css = css.replace("url(assets/", "url(../assets/")   # the prototype lives one folder down
header = re.search(r'<header class="hero".*?</header>', src, re.S).group(0)
pulse = re.search(r'<section class="pulse".*?</section>', src, re.S).group(0)
involved = re.search(r'<h2 id="get-involved">.*?(?=<h2 id=)', src, re.S).group(0).replace('<h2 id="get-involved">Get involved</h2>', '<h3 class="sheet-sub first">Get involved</h3>')
# in the prototype the anchors of the entry sheet lead nowhere, and links go up one folder
for part in ("header", "pulse", "involved"):
    v = locals()[part]
    v = re.sub(r'href="#[^"]*"', 'href="#" data-dead', v)
    v = re.sub(r'(href|src)="(?!https?:|#|mailto:|\.\./)([^"]+)"', r'\1="../\2"', v)
    locals()[part] = v
    globals()[part] = v

STATUS = {"now": "available now", "wip": "in progress", "plan": "planned", "open": "open question"}
GH = "https://github.com/entresol/silent-zero"


def points(items):
    out = []
    for status, title, text, *link in items:
        more = f' <a href="{link[0][1]}">{link[0][0]}</a>' if link else ""
        out.append(f'<li><span class="st st-{status}">{STATUS[status]}</span><div><strong>{title}</strong><p>{text}{more}</p></div></li>')
    return "<ul class=\"points\">" + "".join(out) + "</ul>"


use = points([
    ("now", "What it is for", "AI agents that deliver work and, increasingly, move arms or wheels. Silent Zero treats every agent as untrusted, whatever model drives it, and keeps the agent's authority and the machine's safety beneath it.", ("The paper", "../silent-zero.pdf")),
    ("now", "See it boot", "A graphical loader checks the seL4 kernel image, shows the result and starts the kernel. 24 seconds of video.", ("Watch", "../assets/video/loader-sel4-boot.mp4")),
    ("now", "What verification gives you", "The proven part of the kernel does what its specification says. Everything else is labelled tested or assumed and never passed off as proven; firmware and graphics hardware stay trusted.", ("Which is which", "../wiki/design/kernel.html")),
    ("wip", "What real-time gives you", "By design, processor time is held like memory: an agent cannot starve the control loop, and a small deterministic loop has the last word on every motion. Timing bounds for modern processors are not yet proven.", ("The design", "../wiki/design/safety-path.html")),
    ("now", "Open and free", "The code is BSD-2-Clause, the paper and the texts CC BY 4.0.", ("Licence", GH + "/blob/main/README.md#licence")),
    ("now", "Ask a question", "Discussions for questions and ideas, Issues for a flaw or a wrong claim.", ("Discussions", GH + "/discussions")),
    ("plan", "Try it", "A bootable image, first in an emulator."),
    ("plan", "Check your download", "Checksums and signatures, and how to verify them before you boot."),
    ("plan", "Which hardware", "A first board, then a list of what runs on what."),
    ("open", "Is it certified?", "Not yet. How a safety path like ours relates to the standards a buyer must meet is still open, and we say so."),
])
dev = points([
    ("now", "Architecture on one page", "What the parts are and why nothing at the base is new.", ("The paper", "../silent-zero.pdf")),
    ("now", "What is proven, what is assumed", "The kernel page lists the proof status per configuration: proven, not stated, tested, assumed.", ("Kernel", "../wiki/design/kernel.html")),
    ("now", "Read the code", "The loader (under 8 KB on RISC-V), the splash renderer and the build scripts.", ("Code", GH + "/tree/main/loader")),
    ("now", "Run the loader in QEMU", "Needs clang with the RISC-V target, ld.lld and QEMU; <code>make test</code> boots a good image and tampered ones. The steps are in the README; not yet checked on a clean machine.", ("README", GH + "/blob/main/loader/README.md")),
    ("now", "Where we are unsure and want help", "Every wiki page ends with its open questions; the Issues collect what the team has to decide.", ("Wiki", "../wiki/")),
    ("now", "How AI helps with proofs", "A model proposes, the proof checker judges. The wiki collects what is known.", ("Proof automation", "../wiki/concepts/proof-automation.html")),
    ("wip", "The broker: how authority is handed out", "A design, no code yet, nothing proven.", ("Design", "../wiki/design/broker.html")),
    ("plan", "Add a component on top of the kernel", "A static system description with protection domains and channels.", ("Static system", "../wiki/design/static-system.html")),
    ("plan", "Build the image yourself", "A reproducible build from source."),
    ("now", "Contribute", "CONTRIBUTING.md says how we work: branches, pull requests, the changelog.", ("CONTRIBUTING.md", GH + "/blob/main/CONTRIBUTING.md")),
    ("now", "Follow along", "The changelog says what changed in substance, the wiki log what was worked in each day.", ("Changelog", GH + "/blob/main/CHANGELOG.md")),
])

body = f"""
<div class="desk">
  <div class="sheet entry" id="entry">
    {header}
    {pulse}
    <p class="proto-note">Prototype. The two sheets hold placeholder text. Pull a sheet over this one with the tabs at the edges, or with the keys <kbd>←</kbd> and <kbd>→</kbd>; <kbd>Esc</kbd> or a click on the visible edge puts it back.</p>
  </div>
  <div class="scrim" id="scrim"></div>

  <div class="leaf use" id="leaf-use">
    <button class="tab" type="button" aria-controls="page-use" aria-expanded="false"><span>Users</span></button>
    <section class="page" id="page-use" role="dialog" aria-modal="false" aria-labelledby="h-use" tabindex="-1" inert>
      <div class="page-in">
        <button class="close" type="button" aria-label="Close this sheet">Close</button>
        <h2 id="h-use">Use Silent Zero</h2>
        <p class="sheet-lede">Silent Zero is a small operating system for machines where AI acts in the physical world. You cannot install it yet. This sheet says what you can look at today and what is still to come.</p>
        {use}
      </div>
    </section>
  </div>

  <div class="leaf involved" id="leaf-involved">
    <button class="tab" type="button" aria-controls="page-involved" aria-expanded="false"><span>Developers</span></button>
    <section class="page" id="page-involved" role="dialog" aria-modal="false" aria-labelledby="h-involved" tabindex="-1" inert>
      <div class="page-in">
        <button class="close" type="button" aria-label="Close this sheet">Close</button>
        <h2 id="h-involved">Develop with Silent Zero</h2>
        <p class="sheet-lede">For people who build, verify or just want to look inside. Everything here is open; the label says what works today.</p>
        <div class="involved-old">{involved}</div>
        <h3 class="sheet-sub">Start here</h3>
        {dev}
      </div>
    </section>
  </div>
</div>
"""

proto_css = """
/* the prototype: a desk with three sheets */
:root { --desk: #e6e8e9; --sheet-w: min(74rem, 86vw); --tab: 2.6rem; --ease: cubic-bezier(.45, .05, .25, 1); --slide: 1s; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --desk: #07090a; } }
html, body { height: 100%; overflow: hidden; background: var(--desk); }
.desk { position: fixed; inset: 0; }
.sheet.entry { position: absolute; inset: 0; overflow: auto; background: var(--paper); }
.proto-note { max-width: var(--wide); margin: 2rem auto 4rem; padding: 0 var(--gutter-l); color: var(--muted); font-size: .9rem; }
kbd { font: inherit; border: 1px solid var(--rule); border-radius: 4px; padding: 0 .35em; }
.scrim { position: absolute; inset: 0; background: rgba(0,0,0,.05); opacity: 0; pointer-events: none; z-index: 5; transition: opacity var(--slide) var(--ease); }
.scrim.on { opacity: 1; pointer-events: auto; cursor: pointer; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .scrim { background: rgba(0,0,0,.22); } }
.leaf { position: absolute; top: 0; bottom: 0; width: var(--sheet-w); z-index: 10; pointer-events: none; will-change: transform; backface-visibility: hidden;
  transition: transform .3s ease-out; }
.leaf.moving { transition: transform var(--slide) var(--ease); }
.leaf > * { pointer-events: auto; }
.leaf.use { left: 0; transform: translateX(-100%); }
.leaf.involved { right: 0; transform: translateX(100%); }
.leaf.use:not(.open):has(.tab:hover), .leaf.use:not(.open):has(.tab:focus-visible) { transform: translateX(calc(-100% + .9rem)); }
.leaf.involved:not(.open):has(.tab:hover), .leaf.involved:not(.open):has(.tab:focus-visible) { transform: translateX(calc(100% - .9rem)); }
.leaf.open { transform: translateX(0); }
.page { position: absolute; inset: 0; overflow: auto; background: var(--paper); outline: none; }
.leaf::before { content: ""; position: absolute; inset: 0; opacity: 0; pointer-events: none; transition: opacity var(--slide) var(--ease); }
.leaf.open::before { opacity: 1; }
.leaf.use .page { border-right: 1px solid var(--rule); }
.leaf.involved .page { border-left: 1px solid var(--rule); }
.leaf.use::before { box-shadow: 14px 0 48px -8px rgba(0,0,0,.22); }
.leaf.involved::before { box-shadow: -14px 0 48px -8px rgba(0,0,0,.22); }
.tab { position: absolute; top: 34vh; width: var(--tab); height: 9.5rem; display: flex; align-items: center; justify-content: center;
  background: var(--paper); border: 1px solid var(--rule); color: var(--ink-deep); font: 600 .9rem/1 var(--font-text); letter-spacing: .05em; cursor: pointer; padding: 0; }
.tab span { writing-mode: vertical-rl; }
.leaf.use .tab { left: 100%; border-left: 0; border-radius: 0 10px 10px 0; box-shadow: 4px 0 14px -6px rgba(0,0,0,.2); }
.leaf.use .tab span { transform: rotate(180deg); }
.leaf.involved .tab { right: 100%; border-right: 0; border-radius: 10px 0 0 10px; box-shadow: -4px 0 14px -6px rgba(0,0,0,.2); }
.tab::before { content: ""; position: absolute; top: 0; bottom: 0; width: 3px; background: var(--accent); opacity: 0; transition: opacity .25s; }
.leaf.use .tab::before { left: 0; } .leaf.involved .tab::before { right: 0; }
.tab:hover::before, .tab:focus-visible::before, .leaf.open .tab::before { opacity: 1; }
.tab:focus-visible, .close:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

.page-in { max-width: 44rem; margin: 0 auto; padding: 9vh var(--gutter-r) 12vh var(--gutter-l); }
.page-in h2 { font: 100 clamp(2.6rem, 6vw, 4.6rem)/1 var(--font-display); letter-spacing: -.035em; color: var(--ink-deep); margin: 0 0 1rem; }
.page-in h2::before { display: none; }
.sheet-lede { max-width: var(--measure); color: var(--ink); margin: 0 0 2.2rem; }
.sheet-sub { font: 100 clamp(1.8rem, 3.6vw, 2.6rem)/1.05 var(--font-display); letter-spacing: -.03em; margin: 3.2rem 0 1.2rem; color: var(--ink-deep); }
.close { position: sticky; top: 0; float: right; margin: -4vh 0 0 1rem; background: var(--paper); border: 1px solid var(--rule); border-radius: 999px; padding: .45rem .95rem;
  font: 600 .85rem/1 var(--font-text); color: var(--ink-deep); cursor: pointer; z-index: 2; }
.close:hover { border-color: var(--accent); }
.points { list-style: none; padding: 0; margin: 0; }
.points li { display: grid; grid-template-columns: 7.6rem 1fr; gap: .2rem 1rem; padding: .85rem 0; border-top: 1px solid var(--rule); }
.points li:first-child { border-top: 0; }
.points strong { color: var(--ink-deep); font-weight: 600; }
.points p { margin: .15rem 0 0; font-size: .95rem; color: var(--ink); }
.st { font-size: .74rem; font-weight: 600; letter-spacing: .05em; text-transform: uppercase; padding-top: .25rem; color: var(--muted); }
.st-now { color: #3f7d52; } .st-wip { color: var(--accent); } .st-open { color: var(--ink-deep); font-style: italic; }
.points p a { margin-left: .2rem; }
.sheet-sub.first { margin-top: 2rem; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .st-now { color: #6fbf87; } }
@media (max-width: 45rem) { :root { --sheet-w: calc(100vw - var(--tab)); } .points li { grid-template-columns: 1fr; } }
@media (prefers-reduced-motion: reduce) { :root { --slide: .01s; } }
"""

proto_js = """
(() => {
  const body = document.body, scrim = document.getElementById('scrim');
  const leaves = { use: document.getElementById('leaf-use'), involved: document.getElementById('leaf-involved') };
  let current = null, lastTab = null;
  let movingTimer = null;
  function set(name, push) {
    if (name === current) return;
    const prev = current;
    current = name;
    for (const leaf of Object.values(leaves)) leaf.classList.add('moving');
    clearTimeout(movingTimer);
    movingTimer = setTimeout(() => { for (const leaf of Object.values(leaves)) leaf.classList.remove('moving'); }, parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--slide')) * 1000 + 80);
    for (const [k, leaf] of Object.entries(leaves)) {
      const on = k === name;
      leaf.classList.toggle('open', on);
      leaf.querySelector('.tab').setAttribute('aria-expanded', on);
      leaf.querySelector('.page').inert = !on;
    }
    body.classList.remove('open-use', 'open-involved');
    if (name) body.classList.add('open-' + name);
    scrim.classList.toggle('on', !!name);
    document.getElementById('entry').inert = !!name;
    if (name) { lastTab = leaves[name].querySelector('.tab'); setTimeout(() => leaves[name].querySelector('.page').focus({ preventScroll: true }), 200); }
    else if (prev && lastTab) setTimeout(() => lastTab.focus({ preventScroll: true }), 200);
    if (push) { try { history.replaceState(null, '', name ? '#' + name : location.pathname); } catch (_) {} }
  }
  for (const [k, leaf] of Object.entries(leaves)) {
    leaf.querySelector('.tab').addEventListener('click', () => set(current === k ? null : k, true));
    leaf.querySelector('.close').addEventListener('click', () => set(null, true));
  }
  scrim.addEventListener('click', () => set(null, true));
  addEventListener('keydown', e => {
    if (e.key === 'Escape') set(null, true);
    else if (e.key === 'ArrowLeft' && !/input|textarea/i.test(e.target.tagName)) set(current === 'involved' ? null : 'use', true);
    else if (e.key === 'ArrowRight' && !/input|textarea/i.test(e.target.tagName)) set(current === 'use' ? null : 'involved', true);
  });
  const h = location.hash.slice(1); if (leaves[h]) set(h, false);
})();
"""

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Silent Zero OS, sheets prototype</title>
<meta name="robots" content="noindex">
<style>
{css}
{proto_css}
</style>
</head>
<body>
{body}
<script>
{proto_js}
</script>
</body>
</html>
"""
(here / "index.html").write_text(page, encoding="utf-8")
print("wrote", here / "index.html", len(page), "bytes")
