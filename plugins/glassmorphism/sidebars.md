# Sidebars

> Dependencies: `colors.md`, `radius.md`, `typography.md`, `badges.md`, `alerts.md`

## Core Specs

- Background: glass-bg
- Backdrop filter: glass-blur
- Right border: 1px, glass-border (for left-sidebar); left border for right-sidebar
- Width: 256px
- Position: relative, overflow hidden

## Glass Edge Highlights

- Top edge (::before): absolute, top 0, left 0, right 0, height 1px, glass-edge-top gradient
- Left edge (::after): absolute, top 0, left 0, width 1px, full height, glass-edge-left gradient

## Anatomy

### Outer Container
Hidden on mobile, visible at small breakpoint. Needs a toggle/trigger for mobile.

### Inner Wrapper
- Full height, vertical scroll overflow
- Padding: 12px horizontal, 16px vertical

### Navigation List
- Vertical spacing: 8px between items
- Font weight: medium

### Navigation Item
- Layout: flex, vertically centered
- Padding: 8px horizontal, 8px vertical
- Text: heading color
- Radius: 20px (base)
- Hover: glass-bg-hover background
- Transition: all properties, 200ms
- Icon: 20x20px, body color, hover → heading color, 75ms transition
- Label: 12px left margin from icon

### Active Item
- Background: neutral-secondary-strong
- Text: fg-brand-strong

### Separator
- 16px top padding, 16px top margin
- Top border: glass-border-subtle
- 8px vertical spacing below

### Bottom CTA / Card
- Padding: 16px
- Top margin: 24px
- Radius: 20px (base)
- Background: brand-softer
- Can also use any alert variant from `alerts.md`

## Rules

- Responsive: hidden on mobile with a trigger mechanism
- Icons: 20x20px, body color (hover: heading color)
- Multi-level menus: indent with 44px left padding
- Spacing follows 8px grid
- Only neutral, brand, or status tokens — no arbitrary colors
- Sidebar must have `position: relative; overflow: hidden` for edge highlights
