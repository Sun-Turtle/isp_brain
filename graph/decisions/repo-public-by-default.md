---
status: active
priority: high
tags:
  - decisions
  - operations
  - transparency
created: 2026-05-26
---

# Repo: Public by Default

## Context

The ISP Brain knowledge graph — containing company research, decisions, supplier analysis, regulatory notes, and operational playbooks — was initially created in a personal GitHub account (coffeefilter77) as a private repo. As Sun Turtle incorporated and the graph grew, the question of where and how to host the repo arose.

## Decision

Move the repo to the company GitHub organisation (Sun-Turtle/isp_brain) and make it **public**.

## Rationale

- **Openness is a value, not a risk**: Sun Turtle's ethos is doing things differently — radical transparency, community-oriented ISP. A public knowledge graph embodies that before we've sold a single connection.
- **Differentiation**: No UK ISP publishes their internal research, decision-making, or wholesale pricing analysis. Doing so builds trust and signals confidence.
- **Accountability**: Public decisions are sharper decisions. Knowing anyone can read the rationale raises the bar.
- **Recruiting signal**: Engineers and operators who care about how an ISP works can see exactly how this one is built. It's a living credential.
- **Private_ prefix safety net**: Commercially sensitive files (pricing, NDA-descended data) are gitignored via the `graph/**/private_*.md` convention. The repo being public doesn't mean *everything* is public.

## Alternatives

- **Keep private**: Safer, conventional, but contradicts the stated ethos. No marginal benefit — the risk of exposing something genuinely damaging is already contained by .gitignore.
- **Private but open to audit**: Defeats the purpose — transparency that requires asking permission isn't transparency.

## Impact

- Anyone can fork, read, critique, or learn from the graph
- Competitors can see our playbook — but execution beats information
- Private_ files remain on disk locally, gitignored from commits
- Sets a precedent: future repos under Sun-Turtle should default to public unless there's a concrete reason not to

## See also

- [Company Manifesto](../identity/company-manifesto.md)
- [Graph Conventions](../knowledge/graph-conventions.md)
- [File Naming Convention](flat-file-convention.md)
