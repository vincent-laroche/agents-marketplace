---
name: storefront-release
description: Commit and push completed hairsolutions.co theme changes. main = live (GitHub-synced). Use when shipping a finished, validated change. Strictly local repo to GitHub — never Shopify CLI or dev server.
---

# Storefront release (push = live)

`main` is GitHub-synced to the live theme. A push deploys. Never push partial or unvalidated work.

## Preconditions
- `storefront-preflight` passed: on `main`, clean intent, no active rebase.
- Definition of Done checklist from `storefront-build` passed for every changed section/block.
- Changes are inside `/Users/vMac/06_storefront/shopify_github_synched_theme_files`.

## Validate before commit
From the repo: `npm run validate` and `npm run validate:full` (full Theme Check). Fix all errors. Do relevant visual/critical-flow QA (use chrome-devtools at 320–1440px for customer-facing changes).

## Commit & push (Desktop Commander only)
```
cd /Users/vMac/06_storefront/shopify_github_synched_theme_files
git add -A && git commit -m "<type(scope): summary>" && git push origin main
```
If push is rejected (Shopify reverse-sync added a commit):
```
git pull --rebase origin main && git push origin main
```

## Verify
- Local `HEAD` == `origin/main`.
- Verify live output when observable (edge cache can lag on the bare domain).
- `dev` will be fast-forwarded to `main` automatically by `sync-dev.yml`.

## Never
- `shopify theme delete`, `app deploy`, `app release`, `hydrogen deploy`. The Bash guard hook blocks these. (`theme dev/check/push/publish/pull/share` are all allowed — note a CLI push to `atelier-zero-storefront/main` goes live with no GitHub record.)
- Touch product/order/customer/inventory/checkout/billing data or app-managed `ecom-*`/`ss-*`/`foxify-*` files without explicit approval.

## Report
Files changed, checks run, commit hash, push status, remaining production risk.
