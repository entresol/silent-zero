# Changes

What changed in substance, newest first: in the paper, on its page and in the project. Every change is also in the commit history; this list says what a reader or contributor should know.

Format: `## <version> · <scope>`, then one paragraph. A paper version is `YYYY-MM-DD-vX.Y` and has its own PDF in `versions/`; the newest one is the version the build prints on the paper and the page. A change without a new paper version carries only its date (`YYYY-MM-DD`). Scope is `Paper`, `Site` or `Project`. The build turns this file into the list at the end of the page.

## 2026-10-31 · Project

`THIRD-PARTY.md` lists everything the project uses from others: source, exact version, licence, and whether we pass it on. The seL4 kernel and ELF loader in the boot image are GPL-2.0; seL4's licence note keeps our own code, which only starts the image or runs on the kernel, outside the GPL. A release that contains GPL code carries the complete source of the exact seL4 commits and all licence texts as attachments; `loader/release.sh` assembles them. The boot image builds bit for bit the same in two directories on one machine; on other machines this is not yet checked.

## 2026-10-31 · Site

The loader video calls its second run what it stands for: a tampered image, one byte changed after it was built and hashed, instead of a flipped bit. A card says what the stored hash does not catch, an attacker who rewrites the hash as well, and that signing the image comes next. The labels read in plainer English.

## 2026-10-31 · Project

The boot screen names the project: "zOS" stays in the title bar, and below it "silent zero OS" in Inter Thin, close above the slogan. The bar and ring are gone from the screen. The glyphs now store only the pixels that are drawn, which made the existing type almost 600 bytes smaller and paid for the name; the loader is 7,809 bytes for QEMU's `virt` and 7,333 for its HiFive model, still just under 8 KB. The video of the loader starting seL4 shows the new screen.

## 2026-10-31-v0.17 · Paper

Section 3 gives the loader's current size: just under 8 KB instead of just under 9 KB, more than two thirds of it the renderer and its font data. The boot screen now draws the project's mark instead of setting a large wordmark in a font of its own; the figures are measured with GCC 15.2, 7,687 bytes for QEMU's `virt` machine and 7,211 bytes for its HiFive model.

## 2026-10-31 · Site

The header's First light line now links the video of the loader starting the official seL4 kernel: the image checks out and seL4 runs to user space, then the same image with one bit flipped is stopped (24 seconds). The source code is linked behind it. The separate line for the earlier video of seL4's own boot chain is gone; the wiki's bootloader page still lists that video.

## 2026-10-31 · Project

The zOS loader now boots the official seL4 kernel. On QEMU's model of the HiFive Unleashed, the platform of seL4's verified MCS configuration, the chain runs OpenSBI, the loader, its hash check, seL4's ELF loader, the kernel and a root task; the same image with one bit flipped is stopped before seL4's ELF loader. The model has no display, so the loader draws into memory and a recorder copies each picture out; `loader/recording/` holds a video of both runs. The boot screen shows the project's mark, a bar and a ring, in place of the large "zOS"; the title bar keeps "zOS". Drawing the mark instead of setting it in Inter Thin makes the renderer 745 bytes smaller. `assets/brand/` holds the round group icon and the brand sheet.

## 2026-10-30 · Project

The boot video can be rebuilt. `loader/sel4-demo/` fetches the official seL4 16.0.0 sources at fixed commits, builds the kernel with the unmodified preset `RISCV64_MCS_verified`, checks all 22 settings and the kernel's hash, boots it in QEMU and records the serial console. The video on the page is now this build: 58,300 bytes instead of the earlier build without MCS. The wiki's bootloader page says what it shows and what it does not.

## 2026-10-30 · Site

The header has a second line under First light: an unmodified seL4 16.0.0 release kernel boots to user space on RISC-V in QEMU, as a 41-second video of the serial console. The wiki's bootloader page lists it, and notes that the video shows seL4's own boot chain, not our loader, and that it is open whether the kernel was built in one of seL4's verified configurations for this platform.

## 2026-10-30 · Site

Every wiki page ends with two lists: Sources, everything the page rests on, and Related pages, every page it links to or that links to it. Before, the end of a page showed only the pages linking to it, so a source the page rested on could be missing there.

## 2026-10-30 · Site

The wiki is on the page, at [/wiki/](wiki/), in the page's own style: a catalogue in four groups (design, systems, concepts, sources), each page with its status (draft, LLM reviewed, human curated), its sources and the pages that link to it. A source page shows its topic first and its authors in the line below. The page links to the wiki from Get involved and the footer. The build renders the wiki with the page, and pull requests that change the wiki rebuild it.

## 2026-10-30 · Site

The newest PDF has a stable address, `silent-zero.pdf`, and downloads under that name; the version stays printed in the paper. The old address `zos-zero-os.pdf` still works, and every version keeps its own file in `versions/`.

## 2026-10-30 · Site

A new section after In brief, Get involved, says whom we are looking for and where to take part: Discussions, Issues and pull requests. The contents mark the section being read. The grey for meta text is darker and now meets WCAG AA contrast on white. The page has an icon, a slashed zero. The footer separates what the page is from its links: PDF, GitHub and the imprint. A downloaded PDF is named silent-zero and its version, no longer zos-zero-os.

## 2026-10-30 · Project

The wiki on the paper's sources now lives in this repository, in `wiki/`: 63 pages on the sources, the concepts, the systems and the parts of the design, each saying what is proven, tested or assumed and on which source that rests. Claude writes and reviews it; a page shows whether a person has also checked it. The page does not show the wiki yet.

## 2026-10-30 · Project

A minifix may go straight to `main` without a pull request: a typo, a broken link, formatting, an outdated path or name, as long as it changes no claim, no source and no behaviour and leaves the files the page is built from alone. For now only the repository's admins may push directly. Such commits start with `Minifix:`, and the history keeps every one of them. CONTRIBUTING.md states the rule.

## 2026-10-29 · Site

The header says more plainly what exists: a graphical loader that checks the kernel image and shows the result. The German text reads more naturally, and links in the header are no longer hyphenated.

## 2026-10-29 · Site

A link to the page now shows a preview in social media and chats: the header with its title, the name and the slogan.

## 2026-10-29 · Site

The header speaks five languages: English, German, French, Spanish and Italian. A selector at the top right switches it, and the lines flip like a split-flap board. On a first visit from a browser set to one of the four, the header starts in English and flips into that language after two seconds; the choice is remembered. The paper stays in English. Without JavaScript the header stays in English.

## 2026-10-26 · Project

The repository is now called silent-zero. Links to the old name forward to it.

## 2026-10-26-v0.16 · Paper

The project has its name: Silent Zero. zOS was the working title up to v0.15. Section 1 explains the name: zero means starting from nothing and adding only what cannot be left out, silent means that nothing runs that is not needed. The prologue opens with a motto, Never trust an OS you can't verify, after the line the Macintosh spoke about IBM's mainframes at its launch in 1984.

## 2026-10-26 · Site

Phones and tablets have no hover, so a tap on a term went straight to the glossary. Now a tap opens the term's meaning in a popover anchored to it; a second tap, or a tap elsewhere, closes it, and its footer links to the glossary entry.

## 2026-10-26-v0.15 · Paper

The text now explains each glossary term where a reader first meets it. MCS, MCP and WCET are spelled out at their first use; real time, functional correctness, capabilities, the IOMMU, RISC-V, Microkit, the safety controller, timing side channels and information-flow control get a short explanation in the body. No claim, figure or source changed.

## 2026-10-26 · Project

The paper explains a term where a reader first meets it: an abbreviation is spelled out at its first use, and every other glossary term gets a short explanation at its first use in the body. CONTRIBUTING.md states the rule, and paper/tools/glossary_check.py checks it.

## 2026-10-26 · Site

The page moves to its own address, silentzero.ooo.

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
