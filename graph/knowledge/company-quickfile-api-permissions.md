---
status: active
priority: high
tags:
  - knowledge
  - company
  - bookkeeping
  - api
  - secrets
  - credentials
created: 2026-05-28
---

# QuickFile API — Permissions & Credentials

Authentication credentials and app registration for the Sun Turtle QuickFile account.

## Credential storage

All QuickFile credentials stored in `pass` vault `SunInternet` (Proton Pass CLI):

```bash
# API key
pass-cli item view --vault-name "SunInternet" --item-title "quickfile_api_key" --field "password"

# Account number
pass-cli item view --vault-name "SunInternet" --item-title "quickfile_account_number" --field "password"

# Application ID
pass-cli item view --vault-name "SunInternet" --item-title "quickfile_application_id" --field "password"
```

**Never persist these values in files.** Only the retrieval commands are documented here.

## Required credentials

| Credential | pass item | Status |
|---|---|---|
| **API Key** | `quickfile_api_key` | Verified (2026-05-28) |
| **Account Number** | `quickfile_account_number` | Verified (2026-05-28) — 7131410154 |
| **Application ID** | `quickfile_application_id` | Verified (2026-05-28) |

## App registration

App registered as **Sun Turtle Automation** in QuickFile (3rd Party Integrations). Method permissions enabled:

- `System_GetAccountDetails`
- `Bank_GetAccounts`, `Bank_CreateAccount`, `Bank_CreateTransaction`, `Bank_GetAccountBalances`
- `Ledger_GetNominalLedgers`, `Ledger_Search`
- `Journal_Create`
- `Supplier_*` (for logging expenses)
- `Purchase_*` (for purchase invoices)

## Security notes

- **API key is sensitive** — treated as a credential, stored in pass, never committed to git
- **MD5 auth is not HMAC** — the API key is concatenated and MD5-hashed with the submission number. This is reasonable for bookkeeping data but not bank-grade. QuickFile's API runs over HTTPS.
- **Submission number must be unique per request** — use UUID v4 or similar. Do not reuse.
- **Rate limit**: 1,000 calls/day. Burst capacity adequate for automation but watch batching patterns.

## See also

- [QuickFile API Reference](company-quickfile-api.md)
- [Directors Loan Account Setup](../decisions/company-directors-loan-account.md)
- [QuickFile Bookkeeping](company-quickfile.md)
- [Bookkeeping Decision](../decisions/company-bookkeeping.md)
