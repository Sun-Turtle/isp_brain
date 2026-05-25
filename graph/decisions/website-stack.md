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

# Website: Next.js (Migrated from Plain HTML)

## Context

The company website needs public-facing pages for the brand identity, financial transparency, and regulatory compliance. The stack choice reflects the company's philosophy: simple, fast, maintainable by a small team.

## Decision

Build the website with **Next.js (App Router)** with TypeScript and Tailwind CSS. Output is statically generated at build time.

Files live in `Sun-Turtle/website`:
- `app/layout.tsx` — shared layout with `<head>`, metadata, footer, and theme script
- `app/footer.tsx` — company identity footer component (reused across all pages)
- `app/theme-toggle.tsx` / `app/theme-script.tsx` — dark/light theme with `localStorage` persistence
- `app/page.tsx` → `/` — homepage
- `app/buy/page.tsx` → `/buy` — availability checker (client component for form interactivity)
- `app/about/page.tsx` → `/about` — who we are
- `app/open/page.tsx` → `/open` — financial transparency
- `app/complaints/page.tsx` → `/complaints` — Ofcom-compliant complaints procedure
- `app/privacy/page.tsx` → `/privacy` — UK GDPR privacy policy
- `app/terms/page.tsx` → `/terms` — terms and conditions

## Rationale (revised)

- **Component architecture**: Header, footer, and theme toggle are write-once components. Pages only contain their content. No duplication across 7 files.
- **API integration path**: Next.js API routes (`/api/check-availability`, `/api/notify`) are baked into the framework. ICUK REST API calls can be proxied server-side — API keys stay off the client.
- **TypeScript safety**: Props, metadata, and component interfaces prevent drift across pages.
- **Tailwind utility classes + custom properties**: Design tokens (colors, spacing) in `globals.css` with Tailwind for layout. The accent/border/muted colors use CSS custom properties for dark mode.
- **Static output**: `next build` produces plain HTML/CSS/JS — same deploy footprint as before. Can be served from anywhere.
- **Maintainable by one person**: Clean separation of concerns. Adding a page is creating a folder with a `page.tsx`.

## Migration from plain HTML

Initial site was built as 7 `.html` files with a single `style.css`. After discussion about component reuse and future ICUK API integration, migrated to Next.js. Content preserved verbatim — only the structure changed.

The initial plain HTML decision was the right one for prototyping. Now that the site has grown to 7 pages with shared chrome, the component model pays for itself.

## Alternatives considered

- **Astro**: Strong contender — zero JS by default, `.astro` components. But Next.js has deeper API route and form-handling ecosystem for future ICUK integration.
- **SvelteKit**: Cleaner syntax, smaller bundles. But React has a larger ecosystem for forms, validation, and API integration.
- **Plain HTML (previous)**: Worked for 7 pages but duplicated footer/nav/theme script 7 times. Adding ICUK API calls would require a separate backend.

## Impact

- Build step required (`npm run build`) — acceptable trade-off for component reuse
- TypeScript adds type safety at the cost of stricter authoring
- All 7 pages statically prerendered — no server runtime needed
- Footer, nav, theme toggle defined once, used everywhere

## See also

- [Company Details](../identity/company-details.md)
- [Core Admin Stack](../knowledge/company-core-admin-stack.md)
- [Domain FreeThought](../decisions/company-domain.md)
- [Website Knowledge](../knowledge/website.md)
