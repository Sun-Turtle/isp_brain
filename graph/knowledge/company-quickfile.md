---
status: active
priority: medium
tags:
  - knowledge
  - company
  - bookkeeping
  - supplier
created: 2026-05-24
---

# QuickFile

Bookkeeping platform chosen for Sun Turtle. See [decision](../decisions/company-bookkeeping.md).

## Key features

- **Free tier**: 1,000 invoices/year — covers Year 1 comfortably (~500 customers × 12 invoices = 6,000, but most are recurring and managed via API)
- **REST API**: Endpoints for invoicing, client management, bank transactions, and reporting. Enables automated billing reconciliation and financial dashboards without manual entry.
- **UK compliance**: MTD (Making Tax Digital), VAT, corporation tax, UK bank feeds (Open Banking).
- **No lock-in**: Data exportable; straightforward migration to Xero or accountant-managed setup later.
- **Director's loan accounts**: CLG-friendly — tracks startup capital as a loan account, clean separation from day one.

## Limitations at scale

- Free tier caps at 1,000 invoices. Power-user plans are ~£45–95/yr — still negligible.
- Not as deep an ecosystem as Xero (fewer integrations). Acceptable trade-off for a lean ISP that can build its own integrations via the API.

## See also

- [Bookkeeping Decision](../decisions/company-bookkeeping.md)
- [Core Admin Stack](company-core-admin-stack.md)
- [Financial Model](../resources/financial-accounts.md)
