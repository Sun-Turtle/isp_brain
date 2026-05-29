---
status: active
priority: high
tags:
  - knowledge
  - company
  - bookkeeping
  - api
  - automation
created: 2026-05-28
---

# QuickFile API

REST API for Sun Turtle's bookkeeping platform. Base URL: `https://api.quickfile.co.uk/1_2/`. Supports JSON and XML. Full docs at [api.quickfile.co.uk](https://api.quickfile.co.uk/).

## Authentication

Every request requires an `Authentication` block in the JSON body:

```json
{
  "payload": {
    "Header": {
      "MessageType": "Request",
      "SubmissionNumber": "<unique-alphanumeric>",
      "Authentication": {
        "AccNumber": "<account-number>",
        "MD5Value": "<md5(AccNumber + APIKey + SubmissionNumber)>",
        "ApplicationID": "<app-id>"
      }
    },
    "Body": { ... }
  }
}
```

- **AccNumber**: QuickFile account number (found in account settings)
- **APIKey**: Static key from account settings → 3rd Party Integrations
- **SubmissionNumber**: Must be unique per request (prevents replay). Alphanumeric string.
- **MD5Value**: Lowercase hex MD5 of `AccNumber + APIKey + SubmissionNumber` concatenated.
- **ApplicationID**: From registered QuickFile App (required since 10 Dec 2013)

**Do not use a real password/API key in the SubmissionNumber** — it gets hashed into MD5Value and sent in the clear, so it must be an opaque nonce-like identifier.

## Request limits

1,000 calls/day reset at midnight. Can be increased via QuickFile support.

## Key endpoints relevant to Sun Turtle

| Category | Method | Purpose |
|---|---|---|
| System | `System_GetAccountDetails` | Get account number, company name, VAT reg, year-end date |
| Bank | `Bank_GetAccounts` | List all bank accounts by type (CURRENT, LOAN, etc.) |
| Bank | `Bank_CreateAccount` | Create a new bank account (account types: CURRENT, LOAN, PETTY, etc.) |
| Bank | `Bank_CreateTransaction` | Tag bank transactions against nominal codes |
| Bank | `Bank_Search` | Search transactions by date/amount/nominal code |
| Ledger | `Ledger_GetNominalLedgers` | List nominal ledger codes and descriptions |
| Ledger | `Ledger_Search` | Search ledger transactions by date/amount/nominal code |
| Journal | `Journal_Create` | Create manual journal entries (debit/credit pairs) |
| Purchase | `Purchase_*` | Record supplier invoices |
| Supplier | `Supplier_*` | Manage supplier records |
| Client | `Client_*` | Manage customer records |
| Invoice | `Invoice_*` | Create and manage sales invoices |

## Nominal code conventions (QuickFile default chart of accounts)

Standard range. QuickFile may use custom ranges; verify with `Ledger_GetNominalLedgers`.

| Range | Category |
|---|---|
| 0010–0999 | Fixed Assets |
| 1000–1999 | Current Assets (debtors, bank, etc.) |
| 2000–2999 | Current Liabilities (creditors, loans, VAT) |
| 2200–2299 | Directors' Loan Accounts (typical) |
| 3000–3999 | Capital & Reserves |
| 4000–4999 | Sales/Revenue |
| 5000–5999 | Direct Costs / Cost of Sales |
| 6000–7999 | Overheads / Admin Expenses |
| 8000–8999 | Other Income |
| 9000–9999 | Suspense / Provisions |

## Workflow: Recording a purchase invoice

Useful for logging director-funded expenses (domain, subscriptions, incorporation costs) as director's loan transactions.

### 1. Create supplier (if new)

`Supplier_Create` — minimum fields: `CompanyName`, `CountryISO`. Set `DefaultNominalCode` to an appropriate overhead code (e.g. 7506 for hosting/domain fees).

### 2. Create purchase invoice

`Purchase_Create` — requires `SupplierID`, `ReceiptDate`, `InvoiceLines` (each with `ItemNominalCode`, `ItemDescription`, `SubTotal`, `VatRate`).

To record as a **director's loan** payment: include `PaymentData` with `BankNominalCode: 1201` (Director's Loan Account), `PayMethod`, `PaidDate`, `AmountPaid`. This debits the loan account — the company now formally owes the director.

For expenses not yet paid by the director, omit `PaymentData` — the invoice sits as an unpaid purchase.

### 3. Attach the receipt/invoice PDF

`Document_Upload` — `Type.Receipt.PurchaseId` to attach to the purchase. `EmbeddedFileBinaryObject` must be base64-encoded. On macOS: `base64 -i file.pdf | tr -d '\n'`.

### Key nominal codes for Sun Turtle

| Code | Name | Use |
|---|---|---|
| 1201 | Director's Loan Account | Bank account representing the loan |
| 7503 | Broadband Internet and Fax | Telecoms/ISP subscriptions |
| 7506 | Hosting Fees and IT Consumables | Domain registrations, hosting fees |
| 7600 | Legal Fees | Incorporation, Ofcom registration, solicitor fees |

## Error handling

- Duplicate `SubmissionNumber` → API returns error. Always generate fresh nonces.
- Invalid MD5 → authentication error.
- Missing `ApplicationID` → request rejected.
- Method-specific validation errors returned in response body.
- `CountryISO` is mandatory on `Supplier_Create` even though schema marks it optional.
- `Document_Upload` `Type` must be a nested object (`Type.Receipt.PurchaseId`), not a flat string.
- `BankNominalCode` on purchase `PaymentData` must match an actual bank account nominal code, not an arbitrary ledger.

## See also

- [API Permissions & Credentials](company-quickfile-api-permissions.md)
- [Directors Loan Account Setup](../decisions/company-directors-loan-account.md)
- [QuickFile Bookkeeping](company-quickfile.md)
- [Bookkeeping Decision](../decisions/company-bookkeeping.md)
- [Core Admin Stack](company-core-admin-stack.md)
