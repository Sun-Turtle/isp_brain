---
status: active
priority: medium
tags:
  - decisions
  - bookkeeping
  - api
  - automation
created: 2026-05-28
---

# Automation via QuickFile API

## Context

We can see how much time bookkeeping takes. Especially chasing invoices from people, reconciling invoices to charges, uploading and taggin PDFs. An automated approach can save a huge amount of time.
The QuickFile bookkeeping decision was made on the premise that its REST API would enable billing automation, reconciliation, and financial dashboards without manual entry. This needed to be proven before building anything on top of it.

## Decision

Commit to using the QuickFile API as the programmatic interface to Sun Turtle's bookkeeping. Tested successfully — it works. It can upload PDFs, tag invoices, etc.

## Evidence

On 2026-05-28, the following operations were executed via the API against the live Sun Turtle account:

- `System_GetAccountDetails` — confirmed company name, company number, year-end dates
- `Bank_GetAccounts` — discovered existing Current Account (1200) and Director's Loan Account (1201)
- `Bank_GetAccountBalances` — verified zero balances, then confirmed -£7.50 after transaction
- `Ledger_GetNominalLedgers` — explored the chart of accounts (nominal codes 1200–1250, 5000–5200, 7400–7600)
- `Supplier_Create` — created FreeThought (ID 34662) with default nominal code 7506
- `Purchase_Create` — created domain registration invoice (#129268, £7.50) paid from Director's Loan Account (1201)
- `Document_Upload` — attached the domain invoice PDF as a receipt to purchase #129268

All operations returned clean responses with no errors after adjusting for schema quirks.

## Rationale

- **Proven**: The API handles the core bookkeeping workflow end-to-end — supplier → purchase → receipt attachment
- **Director's loan tracking works**: `BankNominalCode: 1201` correctly debits the loan account
- **Schema quirks manageable**: `CountryISO` required on supplier creation (despite docs), `Document_Upload.Type` must be nested object — but both are one-time learnings
- **Ready for automation**: Any expense type can now be recorded programmatically. Future work: CI-bound reconciliation, invoice generation, financial dashboards

## Caveats

- MD5-based authentication is simplistic but adequate over HTTPS
- 1,000 calls/day limit — sufficient for current scale, needs monitoring as automation grows
- API key, account number, and application ID must remain in pass vault — never in code or config

## See also

- [QuickFile API Reference](../knowledge/company-quickfile-api.md)
- [API Permissions & Credentials](../knowledge/company-quickfile-api-permissions.md)
- [Bookkeeping Decision](company-bookkeeping.md)
- [Director's Loan Account](company-directors-loan-account.md)
