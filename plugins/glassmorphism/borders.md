# Borders

## Width Scale

| Context | Width |
|---|---|
| Default (inputs, buttons, cards) | 1px |
| Emphasis / focus | 2px |

## Rules

- Use solid borders by default
- Glass surfaces use translucent borders: `1px solid glass-border` token from `colors.md`
- Dashed borders only for special cases like file dropzones
- Components in the same family must use matching border widths
- Never mix 1px and 2px borders within a single component

## Usage

| Context | Width |
|---|---|
| Inputs / selects / textareas | 1px default; 2px on focus or error |
| Buttons | 1px for variants that require outlining |
| Cards / containers | 1px glass-border; avoid stacked heavy borders |
| Glass surfaces (cards, modals, sidebars) | 1px glass-border with translucent rgba values |

## Glass Edge Highlights

Glass surfaces use pseudo-elements for subtle edge highlights that simulate light refraction:

- **Top edge (::before):** 1px height, full width, glass-edge-top gradient from `colors.md`
- **Left edge (::after):** 1px width, full height, glass-edge-left gradient from `colors.md`
- Both pseudo-elements are absolutely positioned within the glass container (requires `position: relative; overflow: hidden` on the parent)
