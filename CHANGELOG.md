# Changes

What changed in substance, newest first: in the paper, on its page and in the project. Every change is also in the commit history; this list says what a reader or contributor should know.

Format: `## <version> · <scope>`, then one paragraph. A paper version is `YYYY-MM-DD-vX.Y` and has its own PDF in `versions/`; the newest one is the version the build prints on the paper and the page. A change without a new paper version carries only its date (`YYYY-MM-DD`). Scope is `Paper`, `Site` or `Project`. The build turns this file into the list at the end of the page.

## 2026-10-26 · Site

Phones and tablets have no hover, so a tap on a term went straight to the glossary. Now a tap opens the term's meaning in a popover anchored to it; a second tap, or a tap elsewhere, closes it, and its footer links to the glossary entry.

## 2026-10-26-v0.15 · Paper

The text now explains each glossary term where a reader first meets it. MCS, MCP and WCET are spelled out at their first use; real time, functional correctness, capabilities, the IOMMU, RISC-V, Microkit, the safety controller, timing side channels and information-flow control get a short explanation in the body. No claim, figure or source changed.

## 2026-10-26 · Project

The paper explains a term where a reader first meets it: an abbreviation is spelled out at its first use, and every other glossary term gets a short explanation at its first use in the body. CONTRIBUTING.md states the rule, and paper/tools/glossary_check.py checks it.

## 2026-10-25 · Project

CONTRIBUTING.md gains rules for sentences: say first what a sentence is about, bring the verb early, and rewrite a section from its facts instead of patching it. Two scripts in paper/tools measure a draft for machine prose.

## 2026-10-25 · Project

Every pull request that touches the paper or the changelog now rebuilds this page by itself, so a quick fix in GitHub's web editor no longer leaves it out of date. CONTRIBUTING.md says which changes need a second pair of eyes before they are merged.

## 2026-10-25-v0.14 · Paper

The whole text reviewed and partially reworded to sound more natural. Colon reveals fell from 66 to 9, contrasts of the form "X, not Y" from 17 to 3, and most paragraphs no longer end on an aphorism. No claim, figure or source changed; In brief and the opening lines of the prologue stay as they were.

## 2026-10-25-v0.13 · Paper

Section 6 names three more limits. zOS can make weapons more reliable too; the authors state where they stand, as a declaration next to what is proven, tested or assumed. Small does not mean frugal: most of an agent's energy goes into its model, so no saving is claimed before it is measured. And the doubts that are the authors' own: whether AI can supply the work between the parts, whether people stay, whether there will be money. Section 2.3 says why the project is attempted now.

## 2026-10-24-v0.12 · Paper

In brief: half a page before the abstract for readers who want to know in a minute what this is about. The problem, the principle (we do not trust the agent, so authority and safety move beneath it), the building blocks that exist, where it can fail and what we need now.

## 2026-10-24 · Project

The list of changes covers the whole public project: the paper, this page and the repository. Its source is CHANGELOG.md. CONTRIBUTING.md describes how we work: branches and pull requests, paper versions, what goes into the changelog, how claims are sourced.

## 2026-10-24 · Site

On phones and tablets, a menu button at the top left opens the contents as a panel. The contents, here and on wide screens, lead with a link back to the top.

## 2026-10-23-v0.11 · Paper

A glossary of 38 terms in five groups, each explained in plain words and with its role in zOS: as an appendix in the PDF and on this page, where the first use of a term in each section shows its meaning.

## 2026-10-23-v0.10 · Paper

Revision after checking every cited claim against its source. The first robot is a demonstrator before zOS 0.01, which runs on RISC-V: on the Raspberry Pi 4, MCS is not verified, no WCET bound is possible and the Linux island joins the trusted base. Provable timing named as a goal. Updated: OpenTitan in production, seL4 WCET being rebuilt on RISC-V, fence.t on a second core, multikernel verification. New: the trusted path for approvals as an open seam, EU machinery law from 2027, ELISA. Corrected: agentOS, LionsOS, Felt et al., the cost of seL4.

## 2026-10-23-v0.9 · Paper

The name is marked as a working title: zOS gets a name of its own before its first release.

## 2026-10-23-v0.8 · Paper

Section 1 opens with the motivation for everything else: Don't trust the agent. Verify the system. The agent is treated as a Byzantine component; the size of the system follows from the reference monitor's oldest requirement, to be small enough to be analysed and tested.

## 2026-10-23-v0.7 · Paper

The abstract states the thesis up front: zOS does not try to make AI trustworthy, it stays safe although the agent is not. Section 5 adds AgenticOS and Agent libOS as designs for the broker's job and the first verified LionsOS driver. He et al. cited in its OSDI '26 version.

## 2026-10-23-v0.6 · Project

Text and figures are licensed under CC BY 4.0.

## 2026-10-20-v0.5 · Paper

The bootloader paragraph says what the first prototype does: one fixed rule; the first screen drawn by the loader, because nothing else could report a failed check; its size counted as trusted base.

## 2026-10-20-v0.4 · Paper

The slogan becomes the subtitle: Bare minimum. Verified. Real-time. An OS for the AI era. The authors are named on the paper.

## 2026-10-20-v0.3 · Paper

pib as a possible first robot. The driver island, the seams on critical paths and the dependency on seL4 dates made explicit. Anthropic's vulnerability figures qualified as self-reported.

## 2026-10-20-v0.2 · Paper

Revision after the first external review: a first use case; two questions per part instead of three trust classes; firmware above the kernel; what has to be built and who else is building it; the hardened-Linux alternative; reviews described as AI-assisted; every roadmap station labelled demonstration, test or proof. New figures.

## 2026-10-19-v0.1 · Paper

First publication.
