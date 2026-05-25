---
status: active
priority: high
tags:
  - decisions
  - legal
  - compliance
created: 2026-05-24
---

# T&Cs: No Mid-Contract Price Rises, Router on Loan

## Context

The terms and conditions needed a fixed price model and equipment policy. Three real-world precedents were studied: Green ISP (CLG, not-for-profit, small ISP), Andrews & Arnold (technical ISP, fixed pricing), and TalkTalk (large commercial ISP with mid-contract CPI+ rises). The choices had to balance trust-signalling with financial sustainability.

## Decision 1: No mid-contract price rises

Monthly fee is **fixed for the duration of the minimum contract period**. At renewal, pricing may be adjusted with 30 days' notice.

**Rationale**: Mid-contract CPI+ rises are industry standard (BT, TalkTalk, Sky, Virgin Media all do them) but they are universally hated by consumers and regularly criticised by Ofcom. Green ISP and A&A both fix prices for the term. As a new, unknown ISP competing on trust, fixed pricing is a concrete differentiator — not a marketing claim.

**Risk**: If wholesale costs rise during the contract term, Sun Turtle absorbs it. This is manageable at small scale (500 customers) and a known risk at larger scale. The fixed-term model means costs can be adjusted at renewal.

## Decision 2: Router on loan, not sold

The router is **supplied on loan and remains Sun Turtle's property**. Must be returned within 30 days of termination; replacement fee applies if not.

**Rationale**: Green ISP and A&A both do this. Avoids the customer paying full retail for equipment they won't own at contract end. Keeps the upfront cost for customers low (no £50-100 router purchase). For Sun Turtle, it means the router stock is a company asset, recoverable, and standardised — one model to configure, support, and replace.

**Risk**: Chasing unreturned routers costs time and money. The replacement fee needs to be high enough to motivate return but not punitive. Standard Openreach-model ISP practice handles this through the cease process.

## Decision 3: Liability cap at 12-month fees paid

Total liability capped at **total fees paid in the preceding 12 months**. Green ISP and A&A cap at £250 flat.

**Rationale**: A flat £250 cap is very low — potentially unenforceable under the Consumer Rights Act for a service costing £35/mo. A cap at "fees paid in the last 12 months" scales with the relationship (higher for longer-tenured customers, lower for new ones) and is more likely to be upheld as reasonable. It also mirrors common Ofcom-approved models.

## Impact

- No CPI+ rises means no bad press, no Ofcom attention on pricing transparency
- Router loan model keeps upfront cost near zero for customers
- Liability cap is defensible and proportional

## See also

- [Terms and Conditions](../knowledge/policies-ts-and-cs.md)
- [Complaints Handling Policy](../knowledge/policies-complaints-handling.md)
- [Website](../knowledge/website.md)
