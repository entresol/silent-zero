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
involved = re.search(r'<h2 id="get-involved">.*?(?=<h2 id=)', src, re.S).group(0)
# in the prototype the anchors of the entry sheet lead nowhere, and links go up one folder
for part in ("header", "pulse", "involved"):
    v = locals()[part]
    v = re.sub(r'href="#[^"]*"', 'href="#" data-dead', v)
    v = re.sub(r'(href|src)="(?!https?:|#|mailto:|\.\./)([^"]+)"', r'\1="../\2"', v)
    locals()[part] = v
    globals()[part] = v

STATUS = {"now": "available now", "wip": "in progress", "plan": "planned"}


def points(items):
    out = []
    for status, title, text in items:
        out.append(f'<li><span class="st st-{status}">{STATUS[status]}</span><div><strong>{title}</strong><p>{text}</p></div></li>')
    return "<ul class=\"points\">" + "".join(out) + "</ul>"


use = points([
    ("plan", "Download the image", "A bootable image for a first board. Placeholder: there is no image yet; what exists today is the boot demo."),
    ("now", "Watch it boot", "A graphical loader checks the seL4 kernel image, shows the result and starts the kernel (video, 24 s)."),
    ("plan", "Try it in an emulator", "One command to start the image in QEMU, then on real hardware."),
    ("plan", "Check your download", "Checksums and signatures, and how to verify them before you boot."),
    ("wip", "What verification gives you", "What is proven, what is only assumed, in plain words. Links to the wiki for every claim."),
    ("wip", "What real-time gives you", "Why a robot's motion path keeps its deadlines while the AI thinks."),
    ("plan", "A robot on top", "A reference stack for a small robot. Placeholder."),
    ("plan", "A desktop on top", "What it would take to run familiar programs. Placeholder."),
    ("plan", "Which hardware works", "A list of boards and what runs on them."),
    ("plan", "What it costs to certify", "How a safety path relates to the standards a buyer must meet."),
    ("now", "Read the paper", "The working paper, 15 pages, in English."),
    ("plan", "Release notes", "What changed in each release, in plain language."),
])
dev = points([
    ("now", "The paper and the wiki", "The architecture, its sources, and what each page proves or assumes."),
    ("wip", "What verification means here", "Functional correctness, what the kernel proof covers and what it does not."),
    ("wip", "What real-time means here", "Time as a capability: budgets, scheduling, and what is not yet bounded."),
    ("plan", "Add a component on top of the kernel", "A static system description, protection domains and channels. Placeholder."),
    ("plan", "Change the kernel", "How the verified kernel is built and what a change costs in proof."),
    ("plan", "Build the image yourself", "A reproducible build from source in one container."),
    ("now", "Read the loader", "The loader code, under 8 KB on RISC-V, tested in QEMU."),
    ("plan", "Add a driver", "A user-mode driver in a protection domain. Placeholder."),
    ("plan", "Write a proof", "Where proofs live and how AI help fits in, with the checker as the judge."),
    ("now", "Report a flaw", "Issues: a wrong claim, a missing source, a bug."),
    ("now", "Propose a change", "A pull request; CONTRIBUTING.md says how we work."),
    ("plan", "Roadmap", "What comes next and in which order, with proof status for each step."),
])

body = f"""
<div class="desk">
  <div class="sheet entry" id="entry">
    {header}
    {pulse}
    <p class="proto-note">Prototype. The two sheets hold placeholder text. Pull a sheet over this one with the tabs at the edges, or with the keys <kbd>←</kbd> and <kbd>→</kbd>; <kbd>Esc</kbd> or a click on the visible edge puts it back.</p>
  </div>
  <div class="scrim" id="scrim" hidden></div>

  <div class="leaf use" id="leaf-use">
    <button class="tab" type="button" aria-controls="page-use" aria-expanded="false"><span>Use it</span></button>
    <section class="page" id="page-use" role="dialog" aria-modal="false" aria-labelledby="h-use" tabindex="-1" inert>
      <div class="page-in">
        <button class="close" type="button" aria-label="Close this sheet">Close</button>
        <h2 id="h-use">Use it</h2>
        <p class="sheet-lede">For the people who will run Silent Zero: what you get, what you can try today, and what is still to come.</p>
        {use}
      </div>
    </section>
  </div>

  <div class="leaf involved" id="leaf-involved">
    <button class="tab" type="button" aria-controls="page-involved" aria-expanded="false"><span>Get involved</span></button>
    <section class="page" id="page-involved" role="dialog" aria-modal="false" aria-labelledby="h-involved" tabindex="-1" inert>
      <div class="page-in">
        <button class="close" type="button" aria-label="Close this sheet">Close</button>
        <div class="involved-old">{involved}</div>
        <h3 class="sheet-sub">Build on it</h3>
        {dev}
      </div>
    </section>
  </div>
</div>
"""

proto_css = """
/* the prototype: a desk with three sheets */
:root { --desk: #e6e8e9; --sheet-w: min(74rem, 86vw); --tab: 2.6rem; --ease: cubic-bezier(.2, .85, .25, 1); --slide: .6s; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --desk: #07090a; } }
html, body { height: 100%; overflow: hidden; background: var(--desk); }
.desk { position: fixed; inset: 0; }
.sheet.entry { position: absolute; inset: 0; overflow: auto; background: var(--paper); transform-origin: 50% 50%;
  transition: transform var(--slide) var(--ease), filter var(--slide) var(--ease), box-shadow var(--slide) var(--ease); }
.proto-note { max-width: var(--wide); margin: 2rem auto 4rem; padding: 0 var(--gutter-l); color: var(--muted); font-size: .9rem; }
kbd { font: inherit; border: 1px solid var(--rule); border-radius: 4px; padding: 0 .35em; }
.scrim { position: absolute; inset: 0; background: transparent; cursor: pointer; z-index: 5; }
.leaf { position: absolute; top: 0; bottom: 0; width: var(--sheet-w); z-index: 10; pointer-events: none;
  transition: transform var(--slide) var(--ease); }
.leaf > * { pointer-events: auto; }
.leaf.use { left: 0; transform: translateX(-100%); }
.leaf.involved { right: 0; transform: translateX(100%); }
.leaf.use:not(.open):has(.tab:hover), .leaf.use:not(.open):has(.tab:focus-visible) { transform: translateX(calc(-100% + .9rem)); }
.leaf.involved:not(.open):has(.tab:hover), .leaf.involved:not(.open):has(.tab:focus-visible) { transform: translateX(calc(100% - .9rem)); }
.leaf.open { transform: translateX(0); }
.page { position: absolute; inset: 0; overflow: auto; background: var(--paper); outline: none; }
.leaf.use .page { border-right: 1px solid var(--rule); box-shadow: 0 0 0 1px rgba(0,0,0,.02), 14px 0 48px -8px rgba(0,0,0,.22); }
.leaf.involved .page { border-left: 1px solid var(--rule); box-shadow: 0 0 0 1px rgba(0,0,0,.02), -14px 0 48px -8px rgba(0,0,0,.22); }
.leaf:not(.open) .page { box-shadow: none; }
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
.leaf.open .tab { visibility: hidden; }   /* the open sheet closes by its Close button, Esc or the visible edge */
/* the entry sheet sits back while a sheet lies on it */
body.open-use .sheet.entry { transform: translateX(1.2rem) scale(.985); filter: brightness(.96); }
body.open-involved .sheet.entry { transform: translateX(-1.2rem) scale(.985); filter: brightness(.96); }
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
.st-now { color: #3f7d52; } .st-wip { color: var(--accent); }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) .st-now { color: #6fbf87; } }
.involved-old h2 { font: 100 clamp(2.6rem, 6vw, 4.6rem)/1 var(--font-display); letter-spacing: -.035em; margin-bottom: 1rem; }
@media (max-width: 45rem) { :root { --sheet-w: calc(100vw - var(--tab)); } .points li { grid-template-columns: 1fr; } }
@media (prefers-reduced-motion: reduce) { :root { --slide: .01s; } }
"""

proto_js = """
(() => {
  const body = document.body, scrim = document.getElementById('scrim');
  const leaves = { use: document.getElementById('leaf-use'), involved: document.getElementById('leaf-involved') };
  let current = null, lastTab = null;
  function set(name, push) {
    if (name === current) return;
    const prev = current;
    current = name;
    for (const [k, leaf] of Object.entries(leaves)) {
      const on = k === name;
      leaf.classList.toggle('open', on);
      leaf.querySelector('.tab').setAttribute('aria-expanded', on);
      leaf.querySelector('.page').inert = !on;
    }
    body.classList.remove('open-use', 'open-involved');
    if (name) body.classList.add('open-' + name);
    scrim.hidden = !name;
    document.getElementById('entry').inert = !!name;
    if (name) { lastTab = leaves[name].querySelector('.tab'); setTimeout(() => leaves[name].querySelector('.page').focus({ preventScroll: true }), 120); }
    else if (prev && lastTab) lastTab.focus({ preventScroll: true });
    if (push) { try { history.replaceState(null, '', name ? '#' + name : location.pathname); } catch (_) {} }
  }
  for (const [k, leaf] of Object.entries(leaves)) {
    leaf.querySelector('.tab').addEventListener('click', () => set(k, true));
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
