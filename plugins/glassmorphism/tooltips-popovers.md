# Tooltips & Popovers

> Dependencies: `colors.md`, `radius.md`, `shadows.md`

## Tooltips

### Core Specs
- Padding: 12px horizontal, 8px vertical
- Font: 14px, medium weight
- Radius: 12px (default)
- Shadow: shadow-xs
- Transition: opacity, 300ms

### Dark (Default)
- Background: dark
- Text: white
- Border: transparent

### Light
- Background: glass-bg
- Backdrop filter: glass-blur
- Text: heading color
- Border: 1px, glass-border

## Popovers

### Core Specs
- Background: glass-bg
- Backdrop filter: glass-blur
- Radius: 20px (base)
- Shadow: glass-shadow
- Border: 1px, glass-border
- Transition: opacity, 300ms
- Position: relative, overflow hidden

### Glass Edge Highlights
- Top edge (::before): absolute, top 0, left 0, right 0, height 1px, glass-edge-top gradient
- Left edge (::after): absolute, top 0, left 0, width 1px, full height, glass-edge-left gradient

### Header / Title
- Padding: 12px horizontal, 8px vertical
- Background: transparent
- Bottom border: glass-border-subtle
- Font: 14px, medium weight, heading color

### Body / Content
- Standard: 12px horizontal, 8px vertical padding; 14px, body color
- Rich: 16px padding; 14px, body color

## Arrows

- Size: 8x8px rotated 45deg
- Color must match the background of the tooltip/popover variant

## Rules

- Tooltips: 12px radius
- Popovers: 20px radius
- Dark tooltips: dark background, white text
- Light tooltips/popovers: glass-bg + glass-blur + glass-border tokens
- Arrows match parent background color
- Popovers must have `position: relative; overflow: hidden` for edge highlights
