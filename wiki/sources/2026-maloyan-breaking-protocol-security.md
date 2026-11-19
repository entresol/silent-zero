---
type: source
id: 2026-maloyan-breaking-protocol-security
status: reviewed
read: full
kind: test
sources: [2026-maloyan-breaking-protocol-security]
updated: 2026-11-05
---

# Maloyan and Namiot 2026: breaking the protocol

Narek Maloyan and Dmitry Namiot. "Breaking the Protocol: Security Analysis of the Model Context Protocol Specification and Prompt Injection Vulnerabilities in Tool-Integrated LLM Agents". [arXiv:2601.17549](https://arxiv.org/abs/2601.17549), version 1 of 24 January 2026. A preprint. Read in full.

## What it shows

- **Three protocol weaknesses.** The authors read the specification as "v1.0, December 2024" (§III, Table I). In their reading, first, a server's declared capabilities are self-asserted and unchecked, so a server that declared only resources can later send sampling requests. Second, a server can ask the client for model completions, and the three hosts examined (Claude Desktop, Cursor, Continue) show no sign of origin on them. Third, with several servers the model's context mixes all their outputs without provenance, so one server can steer calls to another.
- **A measurement.** A framework called ProtoAmp wraps benchmark tools in MCP servers and compares with direct function calls. Over 847 scenarios, five server implementations and three models (Claude-3.5-Sonnet, GPT-4o, Llama-3.1-70B), overall attack success was 52.8 % through MCP against 26.4 % without it. Cross-server propagation rose from 19.7 % to 61.3 %, and sampling-based injection, which has no baseline, reached 67.2 % (§IV, §V, Table IV).
- **Scaling.** With one compromised server among 1, 2, 3 and 5, attack success was 47.8, 58.4, 67.1 and 78.3 % (Table VI).
- **A fix.** AttestMCP adds signed capability certificates, message authentication, origin tags on sampling requests, user-authorized cross-server flows and replay protection. As a client-side shim it brought overall success from 52.8 % to 12.4 %, at a median of 8.3 ms per message when cold and 2.4 ms warm (§VI, Tables IX, X).
- **How servers arrive.** From 127 installation guides: typosquatting 34 %, supply-chain compromise 28 %, social engineering 23 %, marketplace poisoning 15 %; 73 % of the guides tell the user to run `npx` from a GitHub URL with no integrity check (§II-B).

## How

Controlled experiments with the authors' own harness, attacks adapted from InjecAgent and AgentDojo plus 137 new ones, one baseline of equivalent non-MCP tools with matched latency (§IV).

## Limits

What the authors say. They tested five servers only, and AttestMCP is not formally verified. The federated certificate authority needs an ecosystem that may not follow, and the authors did not evaluate attempts to bypass AttestMCP (§VII-B). It does not cover a legitimate server that serves malicious content, social engineering, or first contact with a malicious server. The remaining 12.4 % is mostly injection through legitimately retrieved content, and the effect depends on users reading authorization prompts (§VI-G).

A careful reader adds:

- **Not formal.** The "formal property violated" lines name principles such as least privilege and isolation; no model or proof is given.
- **The headline range.** The abstract speaks of amplification by "23 to 41 %"; Table IV shows +16.6, +23.7 and +41.6 percentage points for its three comparable rows, +26.4 overall, and the text of §V-D speaks of 7 to 15 points for other benchmarks, though Table VII mixes attack rates and a safety score.
- **Table X against Table II.** The text says AttestMCP uses "user-prompted" isolation, which Table II puts at 31.7 % attack success; Table X gives 8.7 % for cross-server attacks, the figure of Table II's strict isolation. The paper does not explain the difference.
- **A shim for servers that do not sign.** It is not said how the five existing servers presented certificates in the evaluation.
- **Older versions.** The analysis fixes one early specification; Zhang's runtime pins a revision of July 2026 ([[2026-zhang-agent-libos-runtime]]). Our reading: later revisions may differ on these points.

## Against the wiki

- [[model-context-protocol]]: created with this source; it adds protocol-level weaknesses and a measured amplification.
- [[prompt-injection]]: extends it with a measurement of how a protocol with several servers raises the success of the same attacks. Compare [[2026-shen-mcp-38-comprehensive]], which catalogues threats without measuring.
- [[broker]]: the cross-server and sampling weaknesses are cases of text from one party steering authority held for another. Our reading: they sit in front of the broker in zOS, since the broker grants only declared authority; the paper offers no evidence on that.

## For zOS

The paper does not cite this source. It names MCP as an open protocol under the Linux Foundation (Anthropic 2025) and, in the pib example, has an agent move joints through MCP tools that check joint limits in software on the Linux side (pib.rocks 2026). Our reading: the weaknesses described here, poisoned descriptions and steering between servers, apply to such tools, and the paper's plan to put a broker in front of them is aimed at them. No `design/` page changes state.
