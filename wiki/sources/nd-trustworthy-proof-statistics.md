---
type: source
id: nd-trustworthy-proof-statistics
status: reviewed
read: full
kind: report
sources: [nd-trustworthy-proof-statistics]
updated: 2026-11-04
---

# Trustworthy Systems n.d.: Proof Statistics

Project page of the Trustworthy Systems group at UNSW Sydney: [Proof Statistics](https://trustworthy.systems/projects/OLD/l4.verified/numbers). It is undated and sits under the group's archive of the original verification project. Read in full from the page as saved on 2 November 2026; it is short.

## What it shows

The page gives numbers for the seL4 correctness proof "at the point of its first completion in 2009", and says they have changed since.

- **Size of the kernel.** 8,700 lines of C and 600 lines of Arm assembler. The proof covers 7,500 lines of C. The page says the assembler and the boot code (1,200 lines) are not verified; it does not say whether the 1,200 lines are the boot code alone or both.
- **Size of the proof.** About 200,000 lines of Isabelle proof script, written by hand and checked by machine, which the page puts at roughly 3,500 A4 pages. By 2015, all proof files related to seL4 came to about 500,000 lines.
- **Effort.** About 25 person-years for design, documentation, implementation and verification together, including new research, tools and libraries. The authors think a repeat would take under ten.
- **Cost comparison.** The page cites an industry rule of thumb of 1,000 US dollars per line of code for Common Criteria evaluation level 6. On that rule a traditional process would cost about 8.7 million dollars for seL4 "and would give less assurance". The assurance claim is the authors' own.
- **Bugs.** 160 bugs in the C code: 16 found during testing and in student projects before the C verification began in earnest, 144 during the verification phase.
- **Scale.** The page calls the proof one of the largest formal proofs ever done, against about 60,000 lines for a machine-checked proof of the four colour theorem. It names one larger proof, the only one it knows of, from the Verisoft project, at about 245,000 proof steps, a different unit from lines.

## How

A project page that collects counts. It gives no method and no split between the parts of the effort; it ties its figures to the first completion in 2009. The SOSP paper is the page's pointer for detail ([[2009-klein-sel4-formal-verification]]).

## Limits

What the page says itself: the numbers are those of 2009 and have grown. A careful reader adds:

- **Effort figure.** The page's 25 person-years and the paper's 22 (2.2 for kernel design and implementation, about 20 for the proof) differ. The page's total includes documentation, which the paper's estimate does not mention ([[2009-klein-sel4-formal-verification]], §5.2). Both are estimates by the authors.
- **Boot code.** The difference between 8,700 and 7,500 lines is 1,200, the number the page gives for the unverified parts. Our reading: those lines belong to the 8,700 and sit outside the proof, as [[nd-sel4-verified-configurations]] also says for boot code.
- **Comparison.** The assurance claim against Common Criteria is the group's opinion, and the page gives no source for the dollar rule.
- **Old.** The page says its numbers have changed over time. Later sources in the wiki give a larger kernel (see [[sel4]]). The repeat estimate is not a measurement of a repeat.

## Against the wiki

- [[sel4]]: **extends** the size and cost paragraph with the page's totals and the bug count.
- [[2009-klein-sel4-formal-verification]]: **extends**. The page is the project page its note asked for; the figures differ in scope, as above.
- [[functional-correctness]]: unchanged. The page restates no assumption.

## For zOS

Section 2.3 of the paper cites this page together with the 2009 paper for "roughly 25 person-years" and a repeat of "under ten". The page says exactly that for the effort, and the 2009 paper gives about 22 and an estimate of 8 for a new kernel. The paper's figure follows this page. Its next sentence says the first proof "covered about 8,700 lines of C"; this page says 8,700 lines were written and 7,500 verified. [[kernel]] is the design page that carries the claim. No `design/` page changes state.
