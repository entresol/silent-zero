---
type: source
id: 2025-darpa-ai-cyber-challenge
status: reviewed
read: full
kind: report
sources: [2025-darpa-ai-cyber-challenge]
updated: 2026-10-31
---

# DARPA 2025: results of the AI Cyber Challenge

DARPA, news release of 8 August 2025. [Page](https://www.darpa.mil/news/2025/aixcc-results). Read from the page as saved on 23 October 2026.

## What it shows

- **The competition.** AIxCC, a two-year competition run with ARPA-H and AI companies, in which autonomous "cyber reasoning systems" find and patch vulnerabilities in open-source software. Team Atlanta won, Trail of Bits came second and Theori third.
- **Final results.** Across 54 million lines of code, the systems found 54 of 63 synthetic vulnerabilities (86 per cent) and patched 43 (68 per cent of the 63). They also found 18 real vulnerabilities, six in C and twelve in Java code, and provided 11 patches for real ones.
- **Progress since the semifinal** of August 2024: 37 per cent of synthetic vulnerabilities identified then, 86 per cent now; patched, 25 per cent then and 68 per cent now. The release calls the patch rates shares "of the vulnerabilities identified", but 43 is 68 per cent of 63, not of 54; its editor's note gives both rates against all 63.
- **Cost and speed.** About $152 per competition task; patches in 45 minutes on average.
- **Open source.** All seven finalists' systems are to be released under an OSI-approved licence, four of them on the day of the announcement.
- **A correction.** An earlier version of the release gave 70 synthetic vulnerabilities; the administrator corrected it to 63.

## How

A press release from the organiser. It describes the scoring only in outline: patches were scored by speed and by the analysis of bug reports.

## Limits

A careful reader adds:

- **The organiser's own figures**, from a release written to announce success; the challenge data were to be published later and are not read here.
- **Synthetic vulnerabilities.** The headline rates are for planted flaws. The 18 real ones are a by-product, and the release does not say how severe they are.
- **Patching is not proving.** A patch that passed the competition's checks is not shown to be correct beyond them.

## Against the wiki

- [[ai-vulnerability-discovery]]: extends it with the earliest of its figures and a source independent of the model vendors, though not of the competition's sponsors. Anthropic, Google and OpenAI each gave $350,000 in model credits for the final, $50,000 per team.

## For zOS

Section 2.2 of the paper: "autonomous systems found 54 of 63 planted vulnerabilities, patched 43 and discovered 18 real ones (DARPA 2025)". Confirmed. No `design/` page changes state.
