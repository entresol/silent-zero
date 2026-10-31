---
type: source
id: 2026-anthropic-project-glasswing-initial
status: drafted
read: full
kind: report
sources: [2026-anthropic-project-glasswing-initial]
updated: 2026-10-31
---

# Anthropic 2026b: Project Glasswing, an initial update

Anthropic, 22 May 2026. [Page](https://www.anthropic.com/research/glasswing-initial-update). Read from the page as saved on 23 October 2026.

## What it shows

- **Partners.** About 50 partners together found more than ten thousand high- or critical-severity vulnerabilities in a month. Most partners found hundreds each, and several report a bug-finding rate more than ten times higher. Cloudflare reports 2,000 bugs, 400 of them high or critical, with a false-positive rate its team rates better than human testers. Mozilla reports 271 vulnerabilities found and fixed in Firefox 150, over ten times as many as it found in Firefox 148 with Claude Opus 4.6.
- **Open-source scan.** Anthropic scanned more than 1,000 open-source projects. Mythos Preview estimates 6,202 high- or critical-severity vulnerabilities among 23,019 in total. Six independent security firms, or in a few cases Anthropic, assessed 1,752 of the 6,202: 90.6 per cent (1,587) were valid true positives, and 62.4 per cent (1,094) were confirmed as high or critical. Anthropic extrapolates nearly 3,900 high- or critical-severity findings if the post-triage rates hold.
- **Disclosure and patching.** Anthropic estimates it has disclosed 530 high- or critical-severity bugs to maintainers, with 827 more confirmed and waiting; 75 of the 530 are patched and 65 of those have public advisories. A high or critical bug takes two weeks to patch on average. 1,129 bugs were reported without Anthropic's own assessment at maintainers' request, of which Mythos Preview estimated 175 high or critical.
- **The bottleneck.** Progress used to be limited by finding vulnerabilities; the post says it is now limited by how quickly they can be verified, disclosed and patched. Some maintainers asked Anthropic to slow its disclosures.
- **A wolfSSL example.** An exploit that lets an attacker forge certificates, since patched (CVE-2026-5194), with the technical analysis announced for later.
- **Advice** the post calls "not new": shorter patch cycles for developers, shorter patch testing for network defenders, and the basic controls of NIST and the UK's NCSC (hardened defaults, multi-factor authentication, logging).
- **Outlook.** The post says similar models will soon come from other companies, that no company has safeguards strong enough yet, and that Anthropic intends a general release of Mythos-class models once it has them.

## How

A progress report on an unreleased model. Severity and true-positive rates for the open-source scan come from human assessment of the 1,752 findings, partly by outside firms. The partners' counts are as reported to Anthropic; the post links a dashboard of the open-source disclosure process, which this reading did not include.

## Limits

What the post says itself: disclosed vulnerabilities lag the model's capability, so it gives examples and aggregates; and the patch count is low partly because the 90-day disclosure window has not run, and some patches carry no advisory.

A careful reader adds:

- **Two populations.** The 10,000 findings are the partners'; the 1,752 assessed, the 90.6 and the 62.4 per cent belong to the open-source scan only.
- **Estimates by the model.** Severity of the 6,202 and of the 175 unvetted bugs is the model's own estimate; the 62.4 per cent is the only severity rate that rests on outside assessment, and only for the sample.
- **A sample of unknown selection.** The post does not say how the 1,752 were chosen from the 6,202, so the extrapolation to 3,900 is Anthropic's, not a measurement.
- **The vendor's own word,** from the maker of the Claude models that write this wiki.
- **Findings, not defences.** Nothing here says which of the flaws memory safety, capabilities or proofs would have prevented.

## Against the wiki

- [[ai-vulnerability-discovery]]: extends it with counts, the disclosure bottleneck and the false-positive rates.
- [[2026-anthropic-project-glasswing-securing]]: the later post gives numbers for what the first called "thousands".

## For zOS

The paper cites this post in Section 1 for the sentence that the company and around 50 partners reported more than 10,000 findings rated high or critical, that these are the company's own figures, and that the bottleneck moved from finding to verifying, disclosing and patching (Anthropic 2026b). Those three points are confirmed. The 62 per cent in the paper's sentence is the post's 62.4 per cent. No `design/` page changes state.
