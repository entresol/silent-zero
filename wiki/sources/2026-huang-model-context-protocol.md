---
type: source
id: 2026-huang-model-context-protocol
status: reviewed
read: full
kind: test
sources: [2026-huang-model-context-protocol]
updated: 2026-11-05
---

# Huang et al. 2026: MCP threat modelling and tool poisoning

Charoes Huang, Xin Huang, Ngoc Phu Tran and Amin Milani Fard (New York Institute of Technology, Vancouver). "Model Context Protocol Threat Modeling and Analyzing Vulnerabilities to Prompt Injection with Tool Poisoning". [arXiv:2603.22489](https://arxiv.org/abs/2603.22489), version 1 of 23 March 2026. A preprint. Read in full; the tables of threats (Tables 1 to 16) were skimmed.

## What it shows

- **A threat model.** STRIDE and DREAD applied to five components: host and client, the model, the server, external data stores and the authorization server. The authors count 57 threats; the conclusion says "50+". Tool poisoning, malicious instructions in a tool's metadata such as its description, scores 46.5 of 50 on their scale (threat 48) and prompt injection 50 of 50 (threat 11) (§3, §6).
- **Why the client.** The client passes server-supplied tool descriptions into the model's context without validating them, so the execution happens on the server but the exploitation in the model's reasoning. Of seven clients, five do no static validation of tool metadata and two do so in part (§1.1, §6.3.2).
- **A test of seven clients.** The authors tested Claude Desktop, Cursor, Cline, Continue, Gemini CLI, Claude Code and Langflow, in versions of November 2025. Each met four poisoned tools, which read sensitive files, logged tool use, built phishing links or ran remote scripts. Cursor was unsafe in all four. Cline was unsafe for remote scripts, and both Cursor and Cline ran them when told, with only a domain filter that obvious bad domains trip. Claude Desktop had no unsafe result, with a partial one for logging (Table 19 and §6.2).
- **Why the others held.** For file reading and remote scripts, the model's refusal. Claude Desktop, Continue and Claude Code ran Claude Sonnet 4.5 and Cline ran it alongside grok-code-fast-1, the text not saying which model produced which result; Gemini CLI ran Gemini 2.5 Pro, Cursor its default models and Langflow Claude Opus 4 (Table 18). Cline also showed pattern-based injection detection, and the two terminal clients could not render phishing links (§6.2). The authors call the reliance on model behaviour in place of sandboxing and network controls "the most critical gap" (§6.2.4).
- **Recommendations.** Four layers: validation at registration, tracking why the model chose a tool, runtime monitoring and user transparency (§4.2). Strategies rank protocol hardening as critical, runtime isolation as high and monitoring and governance as medium to high (§4.3), with a timeline of three to twelve months (§7.3).

## How

A local test with a malicious server and a benign request ("add two numbers"), classifying each result as safe, partial or unsafe from screenshots, logs and parameter values (§5.2). Logs and screenshots are in the authors' repository.

## Limits

What the authors say. The scores are the authors' own and subjective; a controlled environment may not reflect production; the results hold for the versions tested (§7.4).

A careful reader adds:

- **One run per cell.** The text reports one outcome per client and attack and no repetitions, with a model that is nondeterministic.
- **Mostly one model.** Since most clients ran the same model, the differences between them largely show what each does around that model. The safe results are largely model refusals, which the authors call a gap; [[2026-nasr-attacker-moves-second]] shows how such defences fare against adaptive attacks.
- **Rankings in the text.** Cline is named among the most secure clients while it was unsafe for remote scripts; Claude Desktop's "no observed successful attacks" sits beside a partial result for logging (§6.4).
- **Not a protocol test.** It measures clients; claims about the protocol itself rest on the threat model.

## Against the wiki

- [[model-context-protocol]]: adds the client side to the protocol-side [[2026-maloyan-breaking-protocol-security]] and the catalogue [[2026-shen-mcp-38-comprehensive]]. Its tool-poisoning case belongs to what MCP-38 calls semantic manipulation.
- [[prompt-injection]]: extends it with a test of real clients; the defences that held were the model's, in line with [[2026-nasr-attacker-moves-second]].
- [[broker]]: no change. Our reading: a poisoned description changes what the model proposes; what the broker grants stays bounded by declared authority.

## For zOS

The paper does not cite this source. No `design/` page changes state.
