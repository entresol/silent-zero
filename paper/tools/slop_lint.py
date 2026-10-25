#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-2-Clause
"""Measures the machine patterns in a Markdown or plain text, German or English.

Usage:
  python3 slop_lint.py FILE [FILE ...] [--section "Heading"] [--lang de|en] [--all]

Counts per 1000 words against quotas, lists every hit with its sentence, and
compares the paragraph skeleton. Warnings only: style is a judgement, not a defect.
The quotas are defaults; see CONTRIBUTING.md, "Writing the paper".
"""
import argparse
import re
import statistics as st
from pathlib import Path

# figure, pattern per language, quota per 1000 words
FIGURES = {
    "colon turn ('claim: elaboration')": {
        "en": r"[a-z0-9)'’]: [a-z]", "de": r"[a-zäöüß0-9)]: [a-zäöüA-ZÄÖÜ]", "quota": 2},
    "contrast ('X, not Y' / 'not X but Y')": {
        "en": r", not (?:a |an |the )?\w+|\bnot\b[^.;:]{2,50}?,? but\b|\bnot\b[^.]{2,50}\. (?:It|They|That) (?:is|are|was)\b|\brather than\b",
        "de": r"\bnicht\b[^.;]{2,60}?,?\s*sondern\b|, nicht (?:ein|eine|der|die|das)?\s?\w+", "quota": 1},
    "triad ('A, B and C')": {
        "en": r"\b[\w-]+, [\w-]+(?: [\w-]+)?,? (?:and|or) [\w-]+", "de": r"\b[\w-]+, [\w-]+(?: [\w-]+)? (?:und|oder) [\w-]+", "quota": 2},
    "anaphora ('one X, one Y')": {
        "en": r"\b(\w+) \w+, \1 \w+", "de": r"\b(\w+) \w+, \1 \w+", "quota": 1},
    "cleft ('What X is Y' / 'Was X ist')": {
        "en": r"(?:^|[.!?] )What [^.]{3,60}? (?:is|was|does)\b", "de": r"(?:^|[.!?] )Was [^.]{3,60}?, (?:ist|war)\b", "quota": 1},
    "signpost ('Here is the thing', 'Das Entscheidende')": {
        "en": r"\b(?:here'?s the thing|the key (?:is|insight)|the real \w+ is|it'?s worth noting|in other words|put simply|the bottom line|at its core|the short answer)\b",
        "de": r"\b(?:das Entscheidende|der springende Punkt|die eigentliche Frage|kurz gesagt|im Kern|anders gesagt|am Ende des Tages|genau das|was bleibt)\b", "quota": 0},
}
VOCAB = {
    "en": r"\b(?:delve|crucial|pivotal|landscape|tapestry|seamless(?:ly)?|robust|leverag\w+|foster\w*|underscor\w+|navigat\w+ the|realm|testament|intricate|multifaceted|holistic|game[- ]chang\w+|unlock\w*|empower\w*|elevat\w+|showcas\w+|vibrant|nuanced|ever-evolving|in today's)\b",
    "de": r"\b(?:facettenreich|vielschichtig|nahtlos|ganzheitlich|maßgeschneidert|spielt eine entscheidende Rolle|bahnbrechend|revolutionär|in der heutigen|Landschaft|Reise|eintauchen|unerlässlich)\b",
}


def clean(md):
    """Markdown to running text, one paragraph per item; headings, tables, code and citations out."""
    md = re.sub(r"```.*?```", "", md, flags=re.S)
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    md = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", md)
    md = re.sub(r"\((?:[A-Z][^()]*?(?:\d{4}[a-z]?|n\.d\.)[^()]*?)\)", "", md)   # (Author 2024; ...)
    md = re.sub(r"<[^>]+>", "", md)
    paras = []
    for block in re.split(r"\n\s*\n", md):
        b = block.strip()
        if not b or b.startswith(("#", "|", "&#91;", ">")) or re.match(r"^\*\*Keywords", b):
            continue
        b = re.sub(r"[*_`]", "", b)
        b = re.sub(r"^\s*[-*\d.]+\s+", "", b, flags=re.M)
        paras.append(" ".join(b.split()))
    return paras


def sentences(p):
    return [s for s in re.split(r"(?<=[.!?])\s+(?=[A-ZÄÖÜ0-9\"„“]|[a-z]{1,3}[A-Z])", p) if len(s.split()) > 1]


def section(md, title):
    m = re.search(rf"^(#+) [^\n]*{re.escape(title)}[^\n]*\n", md, re.M)
    if not m:
        raise SystemExit(f"section not found: {title}")
    level = len(m.group(1))
    rest = md[m.end():]
    end = re.search(rf"^#{{1,{level}}} ", rest, re.M)
    return rest[: end.start()] if end else rest


def lint(md, lang, show_all):
    paras = clean(md)
    text = " ".join(paras)
    words = len(text.split())
    if words < 50:
        return print("too short to measure")
    k = words / 1000
    sents = [s for p in paras for s in sentences(p)]
    lens = [len(s.split()) for s in sents]
    plens = [len(p.split()) for p in paras]
    print(f"{words} words, {len(paras)} paragraphs, {len(sents)} sentences, language {lang}\n")

    sd = st.pstdev(lens) if len(lens) > 1 else 0
    flag = "  << flat, machine-like (human 6-12)" if sd < 4 else ""
    print(f"sentence length  mean {st.mean(lens):.1f}  SD {sd:.1f}{flag}  short (<=6 words): {sum(l <= 6 for l in lens)}")
    if len(plens) >= 4:
        spread = max(plens) - min(plens)
        flag = "  << uniform paragraphs" if spread < 20 or st.pstdev(plens) < 0.25 * st.mean(plens) else ""
        print(f"paragraph length {min(plens)}-{max(plens)} words, mean {st.mean(plens):.0f}{flag}")
    dashes = text.count("—") + text.count(" – ")
    per_para = [i + 1 for i, p in enumerate(paras) if p.count("—") + p.count(" – ") > 1]
    print(f"dashes (— and spaced –) {dashes}" + (f"  << more than one in paragraph {', '.join(map(str, per_para))}" if per_para else ""))
    print(f"semicolons {text.count(';')} ({text.count(';') / k:.1f}/1000)")
    bold = len(re.findall(r"^\*\*[^*]+\*\*", md, re.M))
    if bold:
        print(f"bold run-in paragraph leads {bold}")
    print()

    for name, f in FIGURES.items():
        hits = []
        for s in sents:
            for m in re.finditer(f[lang], s, re.I if lang == "en" else 0):
                hits.append((s, s[max(0, m.start() - 40):m.end() + 40]))
        quota = f["quota"] * k
        over = len(hits) > max(quota, f["quota"])
        mark = "  << over quota" if over else ""
        print(f"{name:44s} {len(hits):3d}   ({len(hits) / k:.1f}/1000, quota {f['quota']}){mark}")
        if over or show_all:
            for s, h in hits:
                print(f"      · …{h}…")
    vocab = re.findall(VOCAB[lang], text, re.I)
    print(f"{'stock vocabulary':44s} {len(vocab):3d}   {', '.join(sorted(set(v.lower() for v in vocab)))}")

    print("\nparagraph closers (short last sentence = aphorism suspect):")
    closers = 0
    for p in paras:
        last = sentences(p)[-1] if sentences(p) else p
        n = len(last.split())
        if 2 < n <= 9 and len(p.split()) > 25:
            closers += 1
            print(f"      · {last}")
    print(f"  {closers} of {len(paras)} paragraphs" + ("  << pattern" if closers > max(2, 0.15 * len(paras)) else ""))

    openers = [" ".join(p.split()[:2]).lower() for p in paras]
    rep = {o: openers.count(o) for o in set(openers) if openers.count(o) > 1}
    if rep:
        print("\nrepeated paragraph openers: " + ", ".join(f"'{o}' x{n}" for o, n in rep.items()))
    if not re.search(r"\d", text):
        print("\nno number, year or quantity anywhere: nothing concrete?")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--section")
    ap.add_argument("--lang", choices=["de", "en"])
    ap.add_argument("--all", action="store_true", help="list hits even under quota")
    a = ap.parse_args()
    for f in a.files:
        md = Path(f).read_text(encoding="utf-8")
        if "## References" in md:
            md = md[: md.index("## References")]
        if a.section:
            md = section(md, a.section)
        lang = a.lang or ("de" if len(re.findall(r"\b(?:und|der|die|das|nicht)\b", md)) > len(re.findall(r"\b(?:and|the|not)\b", md)) else "en")
        print(f"=== {f}" + (f" · {a.section}" if a.section else ""))
        lint(md, lang, a.all)
        print()


if __name__ == "__main__":
    main()
