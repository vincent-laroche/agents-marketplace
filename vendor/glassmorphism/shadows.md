# Shadows

| Token | CSS value |
|---|---|
| shadow-2xs | `0 1px 2px rgba(0, 0, 0, 0.05)` |
| shadow-xs | `0 2px 8px rgba(0, 0, 0, 0.08)` |
| shadow-sm | `0 4px 16px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255, 255, 255, 0.1)` |
| shadow-md | `0 8px 32px rgba(0, 0, 0, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.15)` |
| shadow-lg | `0 12px 40px rgba(0, 0, 0, 0.12), inset 0 1px 0 rgba(255, 255, 255, 0.2)` |
| shadow-xl | `0 20px 50px rgba(0, 0, 0, 0.15), inset 0 1px 0 rgba(255, 255, 255, 0.25)` |
| shadow-2xl | `0 25px 60px rgba(0, 0, 0, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.3)` |

## Glass Shadow

For glassmorphism surfaces (cards, modals, sidebars, navbars), use the glass-shadow token from `colors.md` instead of standard shadow tokens. The glass shadow combines a soft outer shadow with inset top and bottom edge highlights to simulate light refraction through frosted glass.

## Component Mapping

| Component type | Token |
|---|---|
| Subtle separators, tiny UI details | shadow-2xs or shadow-xs |
| Inputs, buttons, small controls, lightweight cards | shadow-xs or shadow-sm |
| Standard cards, popovers, dropdowns | shadow-md or glass-shadow |
| Prominent cards, sticky surfaces | shadow-lg or glass-shadow |
| Modals, high-priority overlays | shadow-xl or glass-shadow |
| Hero overlays, top-level emphasis (sparingly) | shadow-2xl |

## Rules

- Use only these tokens — no custom box-shadow values
- Keep elevation steps intentional; avoid jumping multiple levels
- Components in the same family share the same baseline elevation
- Hover/focus on interactive elevated elements: step up by one level
- Never stack multiple shadow tokens on one element
- Never use shadow-xl/shadow-2xl for dense list items or body containers
- Glass surfaces prefer glass-shadow over standard tokens for the characteristic frosted-glass depth
