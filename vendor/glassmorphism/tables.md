# Tables

> Dependencies: `colors.md`, `radius.md`, `shadows.md`

## Wrapper

- Horizontal scroll overflow
- Background: glass-bg
- Backdrop filter: glass-blur
- Radius: 20px (base)
- Border: 1px, glass-border
- Shadow: glass-shadow
- Position: relative, overflow hidden

## Glass Edge Highlights

- Top edge (::before): absolute, top 0, left 0, right 0, height 1px, glass-edge-top gradient
- Left edge (::after): absolute, top 0, left 0, width 1px, full height, glass-edge-left gradient

## Table Element

- Full width, left-aligned text (right-aligned for RTL)
- Font: 14px, body color

## Table Head

- Font: 14px, body color, medium weight
- Background: transparent
- Bottom border: glass-border-subtle
- Cell padding: 24px horizontal, 12px vertical

## Table Body

- Row background: transparent
- Row bottom border: glass-border-subtle (omit on last row to avoid doubling with wrapper border)
- Row hover: glass-bg-hover background (optional)
- Row header: medium weight, heading color, no-wrap
- Cell padding: 24px horizontal, 16px vertical

## Rules

- Wrapper must have horizontal scroll overflow for responsive scrolling
- Last row: omit bottom border to avoid doubling with wrapper border
- Row headers: always `scope="row"` for semantic structure
- Hover on rows is optional
- No arbitrary hex codes — use token colors only
- Table wrapper must have `position: relative; overflow: hidden` for edge highlights
