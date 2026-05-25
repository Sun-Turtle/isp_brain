---
status: active
priority: medium
tags:
  - knowledge
  - company
  - banking
  - supplier
created: 2026-05-24
---

# Tide

Business bank account provider for Sun Turtle. See [decision](../decisions/company-bank-tide.md).

## Key facts

- **CLG-compatible**: One of few UK business banks that accepts Companies Limited by Guarantee. Starling and Monzo Business both rejected the structure (their onboarding expects share capital fields).
- **Free tier**: No monthly fee for standard accounts. Transaction fees apply above certain volumes.
- **FSCS-protected**: Deposits held with ClearBank, protected up to £85,000.
- **Open Banking**: UK bank feeds integrate with QuickFile for automated bookkeeping.
- **Fast online setup**: No branch visits, no paper forms. Incorporation certificate + director ID.

## Limitations

- No physical branches — online/app only. Acceptable for a lean ISP.
- Transaction fees above the free tier threshold. Will need to model at scale (~500+ customer payments/month).

## See also

- [Bank Account Decision](../decisions/company-bank-tide.md)
- [Core Admin Stack](company-core-admin-stack.md)
- [QuickFile](company-quickfile.md)
