---
status: active
priority: high
tags:
  - decisions
  - bookkeeping
  - financial
  - operations
created: 2026-05-24
---

# Bookkeeping: QuickFile

## Context

The company needs bookkeeping software from day one — to track the director's loan (CLG startup capital), incorporation costs, domain/email subscriptions, and later wholesale invoices and customer revenue. Options considered: QuickFile, FreeAgent.

## Decision

Use **[QuickFile](https://www.quickfile.co.uk/)** as the bookkeeping platform.

## Rationale

- **Free tier**: QuickFile has a generous free tier for small businesses — no cost until transaction volume is significant. At 500–2,000 customers this may need upgrading, but early-stage costs stay near zero.
- **UK-focused**: Built for UK accounting — handles VAT, MTD (Making Tax Digital), corporation tax, and UK bank feeds. FreeAgent and Xero are also UK-capable but cost from day one.
- **No lock-in**: QuickFile stores data in an accessible format. Switching to Xero or an accountant-managed setup later is straightforward.
- **Lean ops fit**: Clean, functional interface with just enough features — no bloat. Matches the "ISP as a software company" philosophy of buying smart tools, not enterprise suites.
- **Director's loan tracking**: CLGs rely on director's loans for startup capital. QuickFile handles loan accounts cleanly — essential for proper separation of personal and company finances from the start.

## Alternatives

- **FreeAgent**: Free with Mettle/NatWest business accounts, strong UK support. But ties the bookkeeping decision to a specific bank — undesirable if the bank account choice is still open.
- **Xero**: Market leader, excellent ecosystem. £15–42/mo from day one. Overkill for a pre-revenue CLG.
- **Akaunting**: Open-source, self-hosted. Interesting for control, but adds hosting/maintenance overhead a 5-person team doesn't need.
- **Spreadsheet + accountant**: Viable for the first few months but error-prone. Moving to software later creates double work.

## Impact

- Zero-cost start for bookkeeping
- UK tax compliance (MTD, VAT) covered when needed
- Clean audit trail from day one — important for CLG transparency
- Works independently of bank account choice

## See also

- [Core Admin Stack](../knowledge/company-core-admin-stack.md)
- [Financial Model](../resources/financial-accounts.md)
- [CLG Structure Decision](company-structure-clg.md)
