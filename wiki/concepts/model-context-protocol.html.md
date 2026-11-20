# Model Context Protocol

> The open protocol that connects agents to tools; three preprints measure its security, one runtime treats it as a client only.

Concept · LLM reviewed · updated 2026-11-05 · 4 sources · https://silentzero.ooo/wiki/concepts/model-context-protocol.html

An open protocol, introduced by Anthropic in November 2024, with which an AI application connects to external tools and data. A client inside a host application manages connections to servers; a server offers tools, resources and prompts over JSON-RPC, on a local pipe or over HTTP. The model chooses tools from the free-text descriptions the servers supply ([breaking the protocol](https://silentzero.ooo/wiki/sources/2026-maloyan-breaking-protocol-security.html.md), §II; [MCP threat modelling and tool poisoning](https://silentzero.ooo/wiki/sources/2026-huang-model-context-protocol.html.md), §1; [MCP-38](https://silentzero.ooo/wiki/sources/2026-shen-mcp-38-comprehensive.html.md), §2.2). The paper says it has been governed by the Agentic AI Foundation under the Linux Foundation since December 2025, citing an announcement this wiki has not yet worked in (paper, Section 3 and the table in Section 5), and describes a humanoid robot's agent moving its joints through MCP tools (Section 7).

## What the sources say about its security, November 2026

Four preprints, none peer-reviewed, look at it from different sides.

- **A catalogue.** MCP-38 lists 38 threat categories derived from the specification, incidents and CVE records, and finds that five open-source scanners and proxies together cover at most 18, a figure its own Table 5 does not match ([MCP-38](https://silentzero.ooo/wiki/sources/2026-shen-mcp-38-comprehensive.html.md)).
- **The protocol.** Maloyan and Namiot name three weaknesses in an early specification: capabilities a server declares are not checked, a server can request model completions from the client without the host marking their origin, and several servers share one context without provenance. In the authors' own harness, with five servers, attack success was 52.8 per cent through MCP against 26.4 per cent through equivalent direct calls, and their proposed extension, run as a client-side shim, cut it to 12.4 per cent; they did not test attempts to bypass it ([breaking the protocol](https://silentzero.ooo/wiki/sources/2026-maloyan-breaking-protocol-security.html.md)).
- **The clients.** Huang et al. tested seven clients against four kinds of poisoned tool descriptions. One client failed all four; for file reading and remote scripts the clients that held did so largely because the model refused ([MCP threat modelling and tool poisoning](https://silentzero.ooo/wiki/sources/2026-huang-model-context-protocol.html.md)).
- **Use as a client only.** A runtime for self-evolving agents registers servers and tools by the host and treats a server's capability declaration as neither a grant nor a process's authority. Its MCP part is a client subset, with its newest manifest pinned to a specification revision of July 2026; sampling is not implemented ([Agent libOS](https://silentzero.ooo/wiki/sources/2026-zhang-agent-libos-runtime.html.md), §6.4).

Our reading: the sources agree that the model reads unvalidated text from whoever runs a server, and differ on where to fix it, in the protocol, in the clients or around the model. Only Maloyan and Namiot and Huang et al. measure anything, and they measure how often attacks work and not what a mediator that grants only declared authority would change.

## Open questions

- Whether the weaknesses of the early specification hold for the revisions since; Maloyan and Namiot analyse one version.
- What a [The broker](https://silentzero.ooo/wiki/design/broker.html.md) in front of MCP tools would cover: it limits the reach of a deceived agent and not leaks through channels the agent may use. See [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md).

## Sources

- [Agent libOS](https://silentzero.ooo/wiki/sources/2026-zhang-agent-libos-runtime.html.md)
- [breaking the protocol](https://silentzero.ooo/wiki/sources/2026-maloyan-breaking-protocol-security.html.md)
- [MCP threat modelling and tool poisoning](https://silentzero.ooo/wiki/sources/2026-huang-model-context-protocol.html.md)
- [MCP-38](https://silentzero.ooo/wiki/sources/2026-shen-mcp-38-comprehensive.html.md)

## Related pages

- [The broker](https://silentzero.ooo/wiki/design/broker.html.md)
- [Prompt injection](https://silentzero.ooo/wiki/concepts/prompt-injection.html.md)
- [Towards an Agent Operating System](https://silentzero.ooo/wiki/sources/2026-steinder-towards-agent-operating.html.md)
