---
type: source
id: 2026-shen-mcp-38-comprehensive
status: reviewed
read: full
kind: survey
sources: [2026-shen-mcp-38-comprehensive]
updated: 2026-11-05
---

# Shen, Toyoda and Leung 2026: MCP-38

Yi Ting Shen, Kentaroh Toyoda and Alex Leung (Vulcan Research, AIFT). "MCP-38: A Comprehensive Threat Taxonomy for Model Context Protocol Systems (v1.0)", arXiv 2603.18063, 18 March 2026, 49 pages. A preprint by a company research group. [arXiv](https://arxiv.org/abs/2603.18063). Read in full.

## What it shows

- **A taxonomy.** 38 threat categories, MCP-01 to MCP-38, each tied to the protocol element it exploits and mapped to STRIDE, the OWASP Top 10 for LLM applications (2025) and the OWASP Top 10 for agentic applications (2026) (abstract; §4).
- **The semantic attack surface.** The model picks tools from free-text descriptions that the protocol does not validate, so whoever controls such text can steer the agent without changing any code (§2.2).
- **Five groups.** The categories are grouped by the countermeasure they need: semantic manipulation and poisoning; prompt injection and boundary breaking; identity, trust and supply chain; access control and logic drift; data exfiltration and resource abuse (§3.5).
- **Method.** Four phases: decomposition of the specification, cross-mapping to existing frameworks, filtering against real-world evidence, grouping. The evidence comes from four layers, among them CVE records and published attack studies; candidates without evidence were dropped, so threats nobody has yet demonstrated are left out (§3.1, §3.4).
- **Tool coverage.** Five open-source scanners and proxies together cover at most 18 of the 38 categories (§5.2). Table 5, which lists the categories each tool covers, names ten distinct ones and gives gaps of 34 to 36 per tool, so the figure of 18 and the table do not agree.

## How

The taxonomy is derived from the MCP specification and from incident reports, CVE records and published attack studies. It is not an experiment. The two incidents it uses as motivation are a 2025 GitHub-repository injection and CVE-2025-6514 in the `mcp-remote` package (§2.2).

## Limits

The paper aims at comprehensiveness of the specification's elements, but its evidence filter excludes threats without documented attacks, and the coverage test of §5.2 uses five tools. A careful reader adds that it is a preprint from a vendor-adjacent group, and that it catalogues threats and countermeasure classes and proves nothing about a defence.

## Against the wiki

- [[prompt-injection]]: **extends** it with a protocol-level catalogue of how injected text reaches an agent through tool descriptions.
- [[broker]]: **confirms** the premise that text from tools and servers must not carry authority; the paper's countermeasures are a mix: input validation, signing and monitoring, and for some categories least privilege and explicitly granted capability-style roles ([[object-capabilities]]).

## For zOS

[[broker]]: no change of state. Our reading: many categories, roughly a third to a half, describe how text persuades a model. For those, the zOS rule that the broker grants only declared authority limits how far a deceived agent can reach, but not what leaks through channels it may use, as exfiltration through tool output (MCP-24) and aggregation leakage (MCP-25) do. The classical categories, such as command injection in a client package or DNS rebinding, are not addressed by that rule.
