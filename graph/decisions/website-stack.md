---
status: active
priority: high
tags:
  - decisions
  - website
  - technical
  - brand
created: 2026-05-24
---

# Website: Plain HTML/CSS, No Framework

## Context

The company website needs public-facing pages for the brand identity, financial transparency, and regulatory compliance (complaints procedure). The stack choice reflects the company's philosophy: simple, fast, maintainable by a small team.

## Decision

Build the website with **plain HTML and CSS** — no JavaScript framework, no build step, no CMS.

Files live in the `Sun-Turtle/website` repo:
- `index.html` — homepage with mission, what we offer, quick-action cards
- `open.html` — public financial transparency page (costs, revenue, staff pay)
- `complaints.html` — Ofcom-compliant complaints procedure
- `style.css` — shared minimal stylesheet

## Rationale

- **Zero overhead**: No dependencies, no build pipeline, no node_modules. A text editor and a browser is the entire dev toolchain.
- **Fast**: Single CSS file, semantic HTML, no JavaScript. Loads instantly on any connection — including the slow ones we'll be selling.
- **Maintainable by one person**: Editing a page is opening a file and changing text. No content management, no database, no auth.
- **Philosophically aligned**: The company is "human-scale internet." The website shouldn't require a JavaScript runtime just to display text.
- **Git-native**: Changes go through git. The repo IS the CMS. This matches the "everything in public" posture — anyone can see the edit history.

## Alternatives

- **Static site generators (Hugo, Jekyll, Eleventy)**: Add a build step and templating for a 3-page site. Overkill.
- **React / Next.js / SvelteKit**: JavaScript frameworks for a text website. Contradicts the lean philosophy and adds maintenance burden.
- **WordPress / CMS**: Database, plugins, updates, security patches — all for 3 pages. Not worth it.
- **Wix / Squarespace**: Closed-source, vendor-locked, subscription fees. Misaligned with the open-by-default ethos.

## Page architecture

- **Homepage** (`index.html`): "Do everything useful from here." Cards link to GitHub org, open books, ISP Brain, and complaints. Company identity in footer (company number, registered office placeholder). No upselling, no CTA buttons, no hero banners.
- **Open books** (`open.html`): Costs table (current recurring), staff pay table (empty, with explanation of intent), surplus philosophy. Archive section for future monthly snapshots.
- **Complaints** (`complaints.html`): Ofcom-compliant procedure — email channel, timeframes (2-day acknowledge, 10-day resolve, 8-week deadlock), ADR mention (not yet joined — flagged as pre-launch requirement).

## Impact

- Website is live-ready with zero ongoing cost
- Complaints procedure satisfies Ofcom General Conditions (published, transparent, with timeframes)
- Financial transparency page establishes trust before a single customer signs up
- No JavaScript means no cookies, no trackers, no consent banners needed

## See also

- [Company Details](../identity/company-details.md)
- [Core Admin Stack](../knowledge/company-core-admin-stack.md)
- [Domain FreeThought](../decisions/company-domain.md)
