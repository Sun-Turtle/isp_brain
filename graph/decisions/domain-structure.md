---
status: active
priority: high
tags:
- decision
- architecture
- graph-structure
---

# Domain Structure: 5 Domains

## Context

The original graph had 7 domains: direction, health, identity, knowledge, operations, relationships, resources.

## Problem

Boundaries between domains were fuzzy. Many topics could reasonably go in 2–3 places. Examples:

- AI support automation → operations, knowledge, or resources?
- Router strategy → operations, resources, or knowledge?
- Wholesale architecture → direction, strategy, knowledge, or resources?
- Competitive intelligence → knowledge, relationships, or direction?

This made placement arbitrary and forced constant second-guessing. We ended up with cross-references between everything, defeating the purpose of separation.

## Decision

Collapse to 5 domains with clearer, mutually exclusive boundaries:

| Domain    | Answers                     | What lives here                                                                              |
| --------- | --------------------------- | -------------------------------------------------------------------------------------------- |
| identity  | Who are we?                 | Company details, incorporation, ownership                                                    |
| knowledge | What do we need to know?    | Facts, rules, context — regulatory, technical, market, policies, procedures, meta-graph docs |
| decisions | What did we choose and why? | Architectural decisions, trade-offs, rationales                                              |
| tasks     | What are we doing?          | Active work, blockers, todos                                                                 |
| resources | What do we have?            | Assets, tools, people, money, contracts, CLI references                                      |


The litmus test: if you can't decide which domain something goes in, it probably needs its own decision, or the thing itself is spanning concerns and should be split.

## Alternatives considered

- Keep 7 domains with clearer definitions — but the overlap was structural, not definitional
- Flat namespace (no domains) — loses navigability
- Tag-based navigation only — IWE supports this, but directory hierarchy is still useful for human browsing and `iwe tree`

## Impact

Cleaner navigation, less deliberation when adding files. The `iwe tree` output is still 32 files but grouped more logically.
