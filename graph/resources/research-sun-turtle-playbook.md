---
status: active
priority: medium
tags:
  - research
  - playbook
  - strategy
  - isp
---

# Sun Turtle Playbook — Ultra-Lean UK ISP

**Source**: `sun-turtle-internet-1.pdf`

The ultra-lean UK ISP playbook. Openreach-oriented resale · reseller-only · as small as we can run it

Audience: Friendly pirates
Stance: Reseller-only — retail layer on someone else's pipes
Vibe: AI-first ops, people where it matters, not a 1990s telco cosplay

## TL;DR — three things to remember

1. USO ≠ "they must wholesale to us". The universal service obligation is about designated providers serving qualifying end users — not about guaranteeing your wholesale deal.
2. The winning shape is "ISP as a software company". Wholesale network → automation → self-service → tiny human layer.
3. Lead UK references: Andrews & Arnold (A&A), Aquiss, and Green ISP — niche, technical, automation-friendly cultures — not "me-too big bundle telcos". Green ISP (2-person team, not-for-profit, solar-powered) proves tiny headcount ISPs are viable.

## Executive summary (regulatory + commercial)

A lean, reseller-only ISP that does not own fibre or cabinets avoids most physical network regulation and capex, but still carries consumer rules, data protection, telecoms security (depends what you actually run), and wholesale dependency.

Your access story is commercial wholesale: aggregated (e.g. BT Wholesale sitting above Openreach) or direct Openreach as a Communication Provider (CP) — contracts, credit, integration — not a universal "right to resell".

## Lead examples: Andrews & Arnold & Aquiss

These two are useful north stars for "small team, high automation, technical honesty" — exactly the lane an AI-first reseller would want to study (from the outside).

| | Andrews & Arnold (A&A) | Aquiss |
|---|---|---|
| Positioning | Famous for no-nonsense, tech-literate service; IPv6, static IPs, geeks welcome | Smaller UK ISP, lean footprint, broadband-first focus |
| Why they matter here | Proof that a niche ISP can win on trust + capability without looking like BT adverts | Proof that non-huge brands can stay viable with focused ops |
| Pattern to steal | Automation, clear docs, community/forum energy, low traditional marketing | Same ballpark: efficient ops, loyal niche, avoid spray-and-pray TV ads |

Not claiming their exact headcount or stack — treat them as cultural and strategic references, then validate everything in diligence.

Other EU/UK "tiny ISP" stories exist; for this doc, A&A and Aquiss are the lead pair.

## Core principle: the ISP is a software company

Traditional telco org chart (expensive):
- network engineers
- call centre
- sales
- marketing
- provisioning team
- billing team
- NOC

Ultra-lean replaces most of that with software + wholesale infrastructure:

```
Wholesale network (Openreach etc.)
        ↓
Automation platform
        ↓
Self-service customer portal
        ↓
Small support team
```

Typical under-10-person shape:

| Role | Headcount |
|---|---|
| Founder / CEO | 1 |
| Engineer (automation + integrations) | ~1 |
| Network engineer | ~0.5 (part-time / shared) |
| Customer support | 2–3 |
| Growth / marketing | ~1 |

**Ballpark total**: 5–8 people — credible only if you design as a platform from day one.

## The "full outsourcing" path (easiest launch)

### Infrastructure: wholesale aggregation

Use BT Wholesale (or similar aggregated wholesale) instead of wiring everything straight to Openreach on day one. The wholesaler typically carries line provisioning, authentication, aggregation, backhaul. You become the retail layer: brand, price, care, billing narrative, router strategy.

```
Customer router
     ↓
Openreach line
     ↓
BT Wholesale (aggregation)
     ↓
Internet
```

| You own | Wholesale partner owns |
|---|---|
| Billing & positioning | Core network plumbing |
| Customer support & tone | Much of provisioning complexity |
| Brand & trust | Scale economics you don't have yet |
| Router choice / logistics strategy | — |

This is how many small UK ISPs start — speed > ego.

## OSS/BSS: buy the spine, don't invent it

Lean ISPs don't build Salesforce + custom BSS from scratch on v1. Typical commercial stacks people actually use in this space include:

| Layer | Example platforms (illustrative) |
|---|---|
| Provisioning + billing + CRM-ish | Splynx, Sonar, CloudBlue, OpenISP — verify current fit for UK fixed resale |

Those systems can cover: signup → billing → line activation → router workflows → fault tickets → payments

Automation = deleting whole departments. That's the game.

## AI vs the call centre (where ~70% of cost hides)

Classic structure: AI / workflow bot → human (only when needed)

AI handles well:

| Task | Why it matters |
|---|---|
| WiFi vs line diagnosis | Most "slow internet" is in-home WiFi, not backhaul |
| Line status / known outage checks | Deflects pointless tickets |
| Router reboot / guided checks | Cheap wins before ££ humans |
| Explaining sync vs throughput | Cuts repeat contacts |

If you auto-resolve "WiFi + education" problems, support volume collapses — that's the financial unlock for AI-first.

## The self-service ISP (customers do the work happily)

Portal features:
- Speed tests · line status · fault checker
- Router / sync diagnostics · packet loss
- WiFi tips & channel overlap hints

**Example flow**: customer says "slow" → system runs line test + sync + loss + WiFi hints → responds: "Likely WiFi congestion — try channel 11 / move router" → no human.

## Network minimalism (you are not BT yet)

If you must add your own IP layer later:

| Building block | Notes |
|---|---|
| Transit (e.g. Cogent, GTT — examples only) | Buy full transit early; peering can wait |
| IX (e.g. LINX) | Nice-to-have once scale justifies complexity |

Many tiny ISPs skip peering entirely at first and just buy transit. Less glory, fewer surprises.

## Router standardisation + outsourced logistics

| Pillar | Play |
|---|---|
| One router family (e.g. Ubiquiti / MikroTik / AVM Fritz — examples) | Predictable configs, remote diagnostics, firmware strategy |
| 3PL / fulfilment | Warehouse, flash, ship, returns — you never touch boxes if you don't want to |

AI + telemetry on known hardware beats random ISP hub the user bought in 2017.

## Automated fault handling (Openreach-shaped reality)

Most access faults are Openreach's world — your win is orchestration:

```
detect → diagnose → ticket Openreach → book engineer → nag customer politely → close loop
```

Goal: minimal human touches on routine paths; humans for edge and angry.

## Growth model (slow can still be profitable)

Illustrative trajectory (not a forecast):

| Year | Customers (example) |
|---|---|
| 1 | ~500 |
| 2 | ~2,000 |
| 4 | ~8,000 |

Rough sanity check (illustrative maths only):
5,000 customers × £25/mo ≈ £125k/month gross

At lean opex and sensible CAC, small teams can work — if support per line stays boring.

## What an AI-first stack could look like (target picture)

```
Customer
   ↓
Openreach access
   ↓
Wholesale provider (e.g. BT Wholesale)
   ↓
Your OSS/BSS + automation
   ↓
AI diagnostics + human escalation
   ↓
Self-service portal
```

AI modules to plan for:
- LLM support assistant · router telemetry analysis · fault triage
- billing anomaly hints · knowledge base that doesn't rot

**Biggest durable advantage**: automated troubleshooting that treats WiFi + home LAN as first-class — because that's what floods everyone's queues.

## The "dirty secret": avoid phone as default

| Channel | Cost vibe |
|---|---|
| Phone | 💸💸💸 |
| Chat · email · tickets · forum | ✅ scalable |

Ultra-lean operators steer people to async channels. Humans answer hard things — not "have you tried turning it off and on again" 500×/day.

## Key insight (your AI ISP headcount)

An AI-driven reseller could look like:
- 1 founder
- 2 engineers (automation + network touch)
- 3 support (high leverage, not infinite)
- 1 growth
- **~7 people total**

Only if you refuse to build a mini-BT and commit to software + self-service as the product.

## Regulatory posture (reseller-only) — still real

| Topic | Lean reseller relevance |
|---|---|
| USO | For end users & designated providers — not your wholesale entitlement |
| General Conditions | Retail service duties: contracts, complaints, info, switching where applicable, vulnerability |
| UK GDPR / PECR | Data, marketing, AI logs — tight governance wins |
| Telecoms security | Scope depends on architecture — verify early; don't assume "pure reseller = exempt" |
| Consumer law | Price clarity & fairness — especially if you're cheap positioning |

## Assumptions table

| # | Assumption | If wrong |
|---|---|---|
| A1 | Fixed broadband (+ optional VoIP) to consumers/SMEs in GB | Numbering, 999, product rules shift |
| A2 | No owned access network; traffic on wholesale | Duties may widen |
| A3 | Aggregator-first or lean direct CP | Economics & roadmap change |
| A4 | AI = support/ops, not opaque automated underwriting | Regulatory heat |
| A5 | Low cost = automation, not unlimited human SLAs | Margin fire |

## Wholesale architecture choices

| Approach | Lean fit | Trade-off |
|---|---|---|
| Aggregated wholesale | Fastest MVP | Less control, partner dependency |
| Direct Openreach CP | More ownership of story | Deposits, integration, headcount for edge cases |

Default for "as lean as possible": aggregator first → prove economics → optionally go more direct later.

## Risk register

| ID | Risk | ~L | ~I | Mitigation |
|---|---|---|---|---|
| R1 | Wholesale margin squeeze | H | H | Niche segment; don't race to zero on headline price |
| R2 | Single wholesale dependency | M–H | H | Contract clarity; plan B route |
| R3 | Fault / install opex tsunami | H | H | Great comms + AI first-line + honest SLAs |
| R4 | Ofcom / reputation spikes | M | H | Quality before vanity growth |
| R5 | PSTN / voice complexity | M | M | Broadband-only v1 or partnered voice |
| R6 | AI / data mis-steps | M | M–H | Privacy-by-design; transparent bots |
| R7 | Breach on your systems | M | H | MFA, backups, patch religion |
| R8 | Security regime mis-scoped | L–M | H | Counsel before build freeze |
| R9 | Brand says "human", reality is bot | H | M | Define human lanes (vulnerable users, escalation) |

## Biggest challenges (merged view)

1. **Economics**: Support per line and CAC eat you — wholesale cost is known, chaos is variable.
2. **Ops**: You own the relationship; Openreach + wholesale own fulfilment — friction shows on delays and faults.
3. **Regulation**: Still meaningful at retail — especially consumer touchpoints + data.
4. **AI**: Powerful for triage; dangerous if marketed as magic without reliability and oversight.

## Suggested next steps

1. Lock segments & whether voice is v1.
2. Model 3-year P&L with support FTE per 1k lines (make it scary on purpose).
3. Counsel sign-off: General Conditions, GDPR/PECR, telecoms security for your stack.
4. Ship one product family, one portal journey, one honest support story.
5. Study A&A & Aquiss positioning (tone, product shapes, community) — not to copy branding, but to internalise trust + lean.

## See also

- [Making a Reseller ISP — Legal & Regulatory Guide](research-making-a-reseller-isp.md)
