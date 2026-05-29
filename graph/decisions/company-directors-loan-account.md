---
status: active
priority: high
tags:
  - decisions
  - bookkeeping
  - financial
  - clg
created: 2026-05-28
---

# Director's Loan Account

## Context

Sun Turtle is a CLG — no share capital. Startup costs (incorporation, domain, subscriptions, etc.) are paid by the director from personal funds. These must be recorded as a director's loan, not as share purchases. The Articles allow it (clause 21: "reasonable expenses which the directors properly incur").

## Decision

Record all director-funded expenses as debits against the **Director's Loan Account** in QuickFile (BankId 53414, NominalCode 1201, type LOAN). Reimburse from the Tide current account (NominalCode 1200) once the company has funds.

## Current state

| Attribute | Value |
|---|---|
| BankId | 53414 |
| NominalCode | 1201 |
| BankType | LOAN |
| Name | Director's Loan Account |
| LedgerDescription | Money withdrawn by the director of a limited company on a loan basis. |
| Balance (2026-05-28) | £0.00 |
| Status | Created, zero balance |

## Workflow for expenses

1. **Director pays out-of-pocket** for a company expense (e.g. domain registration, incorporation fee)
2. **Log the expense as a bank transaction** on the Director's Loan account (BankId 53414, NominalCode 1201) — debit to increase loan balance
3. **Attach receipt/invoice** against the transaction
4. **Later**: transfer from Tide Current Account (NominalCode 1200) to Director's Loan Account (credit against 1201) to reimburse — reducing the loan balance

## Why a bank account, not a liability ledger

QuickFile represents the Director's Loan as a bank account (type LOAN) rather than a pure nominal ledger. This gives it:
- A balance on the dashboard
- Transaction history with tagging against expense categories
- Bank feeds compatibility (even though this account has no real bank)

## API reference

- **Get balance**: `Bank_GetAccountBalances` with `NominalCode: 1201`
- **Add transaction**: `Bank_CreateTransaction` against `BankId: 53414`
- **Search transactions**: `Bank_Search` with `NominalCode: 1201`

## See also

- [QuickFile API Reference](../knowledge/company-quickfile-api.md)
- [API Permissions & Credentials](../knowledge/company-quickfile-api-permissions.md)
- [Bookkeeping Decision](company-bookkeeping.md)
- [CLG Structure Decision](company-structure-clg.md)
- [Core Admin Stack](../knowledge/company-core-admin-stack.md)
- [QuickFile Bookkeeping](../knowledge/company-quickfile.md)
