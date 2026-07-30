# Cards

> Dependencies: `colors.md`, `radius.md`, `shadows.md`, `typography.md`

## Core Specs

- **Background:** glass-bg
- **Backdrop filter:** glass-blur
- **Border:** 1px, glass-border
- **Radius:** 20px (base)
- **Shadow:** glass-shadow
- **Position:** relative, overflow hidden

## Glass Edge Highlights

- **Top edge (::before):** absolute, top 0, left 0, right 0, height 1px, glass-edge-top gradient
- **Left edge (::after):** absolute, top 0, left 0, width 1px, full height, glass-edge-left gradient

## Card Heading

- Desktop: 20px, medium weight, heading color
- Mobile: 16px, medium weight, heading color
- Never skip heading levels — the page hierarchy must logically arrive at the card heading level.

## States

### Static Card (no interactivity)
- Background: glass-bg
- Backdrop filter: glass-blur
- Border: 1px, glass-border
- Radius: 20px
- Shadow: glass-shadow
- No hover styles. Non-interactive cards must NOT have hover background changes.

### Interactive Card (clickable)
- Same base styles as static card
- Hover: glass-bg-hover background
- Transition: all properties, 200ms
- Cursor: pointer

## Rules

- Background: glass-bg
- Backdrop filter: glass-blur
- Border: 1px, glass-border
- Radius: 20px
- Shadow: glass-shadow
- Interactive hover: glass-bg-hover background
- Non-interactive: no hover styles
- All cards must have `position: relative; overflow: hidden` for edge highlights
