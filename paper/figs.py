#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""Figures 1 and 2 for the zOS paper, generated once as SVG (for PNG/web) and as JSX (for the Claude Doc widgets)."""
import json
import re
import sys
from pathlib import Path

out = Path(sys.argv[1])
out.mkdir(parents=True, exist_ok=True)

# literal palette for PNG/web; theme variables for the doc widget
LIT = {"ink": "#1a1d1f", "quiet": "#5c6569", "edge": "#9aa3a8", "gold": "#e8a020", "goldwash": "#fdf3e1", "paper": "#ffffff"}
VAR = {"ink": "var(--cds-text-primary)", "quiet": "var(--cds-text-secondary)", "edge": "var(--cds-chart-axis)",
       "gold": "var(--cds-chart-categorical-1)", "goldwash": "GOLDWASH", "paper": "none"}


class E:
    def __init__(self, tag, text=None, children=None, **attrs):
        self.tag, self.text, self.children, self.attrs = tag, text, children or [], attrs


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


KEEP = {"viewBox", "refX", "refY", "markerWidth", "markerHeight"}


def kebab(k):
    if k in KEEP:
        return k
    return re.sub(r"([A-Z])", lambda m: "-" + m.group(1).lower(), k)


def svg_str(e, pal):
    a = "".join(f' {kebab(k)}="{v(pal) if callable(v) else v}"' for k, v in e.attrs.items() if not k.startswith("data"))
    a += "".join(f' {k.replace("_", "-")}="{v}"' for k, v in e.attrs.items() if k.startswith("data"))
    inner = (esc(e.text) if e.text else "") + "".join(svg_str(c, pal) for c in e.children)
    return f"<{e.tag}{a}>{inner}</{e.tag}>"


def jsx_str(e, pal):
    parts = []
    for k, v in e.attrs.items():
        val = v(pal) if callable(v) else v
        name = k.replace("_", "-") if k.startswith("data") else k
        parts.append(f"{name}={json.dumps(str(val))}")
    a = (" " + " ".join(parts)) if parts else ""
    inner = (esc(e.text).replace("{", "&#123;").replace("}", "&#125;") if e.text else "") + "".join(jsx_str(c, pal) for c in e.children)
    return f"<{e.tag}{a}>{inner}</{e.tag}>"


c = lambda key: (lambda pal: pal[key])  # colour lookup by palette


def text(x, y, s, tid, size=13, weight=None, fill="ink", anchor=None):
    at = dict(x=x, y=y, fontSize=size, fill=c(fill), data_claude_text_id=tid)
    if weight:
        at["fontWeight"] = weight
    if anchor:
        at["textAnchor"] = anchor
    return E("text", s, **at)


def box(x, y, w, h, trusted, tid=None):
    if trusted:
        return E("rect", x=x, y=y, width=w, height=h, rx=6, fill=c("goldwash"), stroke=c("gold"), strokeWidth=2)
    return E("rect", x=x, y=y, width=w, height=h, rx=6, fill="none", stroke=c("edge"), strokeWidth=1.25, strokeDasharray="5 4")


def arrow(x1, y1, x2, y2):
    return E("path", d=f"M{x1} {y1}L{x2} {y2}", stroke=c("ink"), strokeWidth=1.4, fill="none", markerEnd="url(#ah)")


def defs():
    return E("defs", children=[E("marker", id="ah", viewBox="0 0 10 10", refX=9, refY=5, markerWidth=7, markerHeight=7,
                                 orient="auto-start-reverse", children=[E("path", d="M0 0L10 5L0 10z", fill=c("ink"))])])


# ---------------- Figure 1 ----------------
W1, H1 = 760, 640
f1 = [defs(),
      text(24, 30, "The zOS stack: what a guarantee depends on, and what we know about it", "title", 15, 600),
      text(24, 50, "Highlighted frame: trusted base, a guarantee depends on it. Dashed: outside the base. Tag: proven, tested or assumed.", "subtitle", 11.5, fill="quiet")]

# lanes
f1 += [box(24, 78, 150, 176, False), text(99, 158, "Agents", "agents", 14, 600, anchor="middle"),
       text(99, 178, "untrusted", "agents-tag", 11.5, fill="quiet", anchor="middle"),
       text(99, 196, "own budget, own domain", "agents-sub", 11.5, fill="quiet", anchor="middle")]
f1 += [box(250, 78, 236, 72, True), text(266, 104, "Capability broker", "broker", 14, 600),
       text(266, 124, "isolated, yet in the trusted base", "broker-sub", 11.5, fill="quiet"),
       text(266, 141, "tested → target: proven", "broker-tag", 11.5, 600, fill="ink")]
f1 += [box(530, 78, 206, 72, False), text(546, 104, "Tools · model access", "tools", 14, 600),
       text(546, 124, "outside the base", "tools-sub", 11.5, fill="quiet"),
       text(546, 141, "reached only via the broker", "tools-tag", 11.5, fill="quiet")]
f1 += [box(250, 182, 236, 72, True), text(266, 208, "Safety controller · loops", "safety", 14, 600),
       text(266, 228, "highest criticality, MCS budget", "safety-sub", 11.5, fill="quiet"),
       text(266, 245, "tested → target: proven", "safety-tag", 11.5, 600)]
f1 += [E("rect", x=530, y=182, width=206, height=72, rx=6, fill="none", stroke=c("ink"), strokeWidth=1.25),
       text(546, 208, "Actuator", "actuator", 14, 600),
       text(546, 228, "moved only by the loop", "actuator-sub", 11.5, fill="quiet"),
       text(546, 245, "through its own driver", "actuator-tag", 11.5, fill="quiet")]
f1 += [arrow(174, 114, 248, 114), text(211, 106, "authority", "path-a", 11.5, fill="quiet", anchor="middle"),
       arrow(486, 114, 528, 114),
       arrow(174, 218, 248, 218), text(211, 210, "motion", "path-m", 11.5, fill="quiet", anchor="middle"),
       arrow(486, 218, 528, 218)]

layers = [
    ("User-mode drivers · Linux driver island", "isolated, outside the base; assumed where a device writes memory directly", False, "outside*"),
    ("Static system description (Microkit)", "fixed at build time: domains, channels, memory, budgets", True, "tested"),
    ("seL4 microkernel with MCS", "only code at kernel privilege; time as a capability", True, "proven†"),
    ("Bootloader", "measures and loads one signed image", True, "assumed"),
    ("Firmware (OpenSBI / TF-A) · hardware · root of trust", "more privileged than the kernel; named and profiled", True, "assumed"),
]
y = 282
for i, (name, sub, trusted, tag) in enumerate(layers):
    f1 += [box(24, y, 712, 48, trusted), text(40, y + 21, name, f"l{i}-name", 13.5, 600),
           text(40, y + 38, sub, f"l{i}-sub", 11.5, fill="quiet"),
           text(720, y + 29, tag, f"l{i}-tag", 12, 600, anchor="end")]
    y += 58
f1 += [text(24, y + 14, "* A driver is outside the trusted base only where the IOMMU confines its device.", "fn1", 11.5, fill="quiet"),
       text(24, y + 32, "† Functional correctness for the verified configurations, which leave out kernel boot and IOMMU support.", "fn2", 11.5, fill="quiet")]

# ---------------- Figure 2 ----------------
W2, H2 = 760, 620
stations = [
    ("2031", "One robot, one task, on zOS from boot to actuator", "Forty years after Linux; device, task and operating conditions defined.",
     "TEST", "No compromised agent moves the actuator outside its safe envelope, under stated assumptions."),
    ("2030", "Linux shrinks to a driver island", "Only accelerators still need legacy drivers.",
     "TEST", "No Linux code on any control or authority path, checked against the system description."),
    ("2029", "Broker and safety controller proven", "The two parts with the last word join the kernel as proven.",
     "PROOF", "The proofs check. Plus a test: an external red team fails to escalate authority."),
    ("2028", "First robot, Simplex style", "The agent proposes, the loop disposes. Multikernel proof due (announced).",
     "TEST", "Control deadlines hold under defined load while the agent is hijacked."),
    ("2027", "zOS 0.01: one board, one kernel, one agent, one loop", "On an open RISC-V core. MCS proof for AArch64 due (announced).",
     "DEMO", "Boots from a measured image; a stranger builds it from source."),
    ("2026", "The base exists as open source (documented)", "seL4 MCS · Microkit · LionsOS · Verus · OpenTitan · CHERI · ROS 2 on seL4 · MCP",
     "", "Missing: the broker, the tool adapters, the safety path, and evidence that the parts fit."),
]
f2 = [text(24, 30, "Five years back from 2031: each station names its evidence", "title", 15, 600),
      text(24, 50, "Demonstration: works once. Test: holds under defined load or attack. Proof: holds for every case the specification covers.", "subtitle", 11.5, fill="quiet"),
      E("path", d="M100 76V600", stroke=c("edge"), strokeWidth=1.25, fill="none")]
bx, bw, rh, gap, y0 = 120, 616, 74, 12, 72
for i, (yr, name, body, kind, check) in enumerate(stations):
    yy = y0 + i * (rh + gap)
    main = i == len(stations) - 1
    f2 += [E("rect", x=bx, y=yy, width=bw, height=rh, rx=6, fill=c("goldwash") if main else "none",
             stroke=c("gold") if main else c("edge"), strokeWidth=2 if main else 1.25),
           E("circle", cx=100, cy=yy + rh / 2, r=4, fill=c("gold") if main else c("edge")),
           text(56, yy + rh / 2 + 5, yr, f"y{yr}-year", 15, 600, anchor="middle"),
           text(136, yy + 24, name, f"y{yr}-name", 13.5, 600),
           text(136, yy + 43, body, f"y{yr}-body", 11.5, fill="quiet")]
    if kind:
        f2 += [E("rect", x=136, y=yy + 51, width=46, height=16, rx=3, fill="none", stroke=c("gold"), strokeWidth=1),
               text(159, yy + 63, kind, f"y{yr}-kind", 10.5, 700, anchor="middle"),
               text(190, yy + 63, check, f"y{yr}-test", 11.5, fill="ink")]
    else:
        f2 += [text(136, yy + 63, check, f"y{yr}-test", 11.5, fill="ink")]


def svg_doc(children, w, h, label, pal):
    root = E("svg", children=children, viewBox=f"0 0 {w} {h}", xmlns="http://www.w3.org/2000/svg",
             fontFamily="Inter, 'Helvetica Neue', Arial, sans-serif", role="img", ariaLabel=label)
    s = svg_str(root, pal).replace(' aria-label=', ' aria-label=')
    return s


def jsx_doc(children, w, h, label):
    root = E("svg", children=children, viewBox=f"0 0 {w} {h}", role="img", fontSize="13")
    root.attrs["aria-label"] = label
    j = jsx_str(root, VAR).replace('markerEnd=', 'markerEnd=')
    j = j.replace('fill="GOLDWASH"', 'fill="var(--cds-chart-categorical-1)" fillOpacity="0.12"')
    return "export default () => " + j + ";"


figs = {
    "fig1": (f1, W1, H1, "zOS stack: agents and tool access outside the trusted base; broker, safety controller, static system, kernel, bootloader and firmware inside it; authority runs through the broker, motion through the safety controller."),
    "fig2": (f2, W2, H2, "Path from 2026 to 2031, one station per year, each with its evidence: demonstration, test or proof."),
}
for name, (ch, w, h, label) in figs.items():
    s = svg_doc(ch, w, h, label, LIT)
    (out / f"{name}.svg").write_text(s, encoding="utf-8")
    (out / f"{name}.jsx").write_text(jsx_doc(ch, w, h, label), encoding="utf-8")
    fontcss = "@font-face{{font-family:Inter;font-weight:100 900;src:url(../fonts/dist/inter-latin-opsz-normal.woff2) format('woff2')}}"
    html = f"<!doctype html><meta charset=utf-8><style>{fontcss}body{{margin:0;background:#fff}}svg{{display:block;width:1344px;height:auto}}</style>{s}"
    (out / f"{name}.html").write_text(html, encoding="utf-8")
# station data for the HTML timeline on the website
(out / "stations.json").write_text(json.dumps(stations, ensure_ascii=False), encoding="utf-8")
print("ok")
