---
status: active
priority: high
tags:
  - knowledge
  - policy
  - legal
  - compliance
created: 2026-05-24
---

# Terms and Conditions

Published at `terms.html` on the website. Required under Ofcom General Conditions and the Consumer Rights Act 2015 before accepting orders. Synthesised from Green ISP and Andrews & Arnold models — structured as formal clauses in plain English rather than legalese.

## Structure

| Clause | Covers |
|---|---|
| 1. The service | What we provide, Openreach dependency, unlimited plans, no traffic management |
| 2. Contract and duration | 12-month minimum, 14-day cooling-off, Ofcom contract summary requirement |
| 3. Fees and payment | Direct Debit, fixed price for minimum term, no mid-contract rises, late payment suspension |
| 4. Equipment | Router on loan, return on termination, engineer missed appointment fees |
| 5. Use of the service | Lawful use only, no spam/hacking/copyright infringement, IP addresses remain ours |
| 6. Ending the contract | 30-day notice, early termination = remaining months, OTS support, cease fees passed through |
| 7. Service availability and faults | Best-effort, Openreach dependency, 5-day outage credit |
| 8. Liability | 12-month aggregate cap at total fees paid, no indirect loss, force majeure |
| 9. Personal data | Incorporates privacy policy by reference |
| 10. Complaints | ADR path, 8-week deadline, deadlock letter |
| 11. Changes to terms | 30-day notice for material changes |
| 12. Governing law | England and Wales |

## Design decisions

- **No mid-contract price rises**: Core differentiator — Green ISP and A&A both commit to fixed pricing for the term. Matches values positioning.
- **Liability cap at 12-month fees paid**: Conservative. A&A caps at £250 total. Green ISP caps at £250. Sun Turtle's model scales with the customer relationship — reasonable.
- **Router on loan**: Green ISP and A&A both do this. Avoids the customer paying full retail for equipment they don't own at end of contract.
- **No minimum term for VoIP add-on**: If VoIP is added later, 1-month rolling (Green ISP model) rather than bundled into the broadband minimum.
- **ADR membership noted as pending**: Honest — required before onboarding, but not hidden.

## Regulatory coverage

- Consumer Rights Act 2015: fair terms, cooling-off, transparency
- Ofcom General Conditions: contract summaries, switching (OTS), price clarity
- Consumer Contracts Regulations 2013: 14-day cancellation right
- UK GDPR: incorporates privacy policy, data processing referenced

## See also

- [Privacy Policy](policies-privacy.md)
- [Complaints Handling Policy](policies-complaints-handling.md)
- [Ofcom General Conditions](regulatory-ofcom-general-conditions.md)
- [Website](website.md)
- [Core Admin Stack](company-core-admin-stack.md)
