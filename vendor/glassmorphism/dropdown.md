# Dropdown

> Dependencies: `colors.md`, `radius.md`, `shadows.md`, `inputs.md`

## Core Specs

### Chevron Icon
- Size: 16x16px
- Spacing: 6px left margin, -2px right margin
- Color: inherits from trigger button

### Menu Container
- Background: glass-bg
- Backdrop filter: glass-blur
- Border: 1px, glass-border
- Radius: 20px (base)
- Shadow: glass-shadow
- Z-index: elevated above content
- Position: relative, overflow hidden

### Glass Edge Highlights
- Top edge (::before): absolute, top 0, left 0, right 0, height 1px, glass-edge-top gradient
- Left edge (::after): absolute, top 0, left 0, width 1px, full height, glass-edge-left gradient

### Menu List
- Padding: 8px
- Font: 14px, body color, medium weight

### Menu Item
- Layout: inline-flex, vertically centered, full width
- Padding: 8px horizontal, 8px vertical
- Radius: 12px (default)
- Hover: glass-bg-hover background, heading text
- Transition: all properties, 200ms

## Trigger Sizes

| Size | Font size | Horizontal padding | Vertical padding |
|---|---|---|---|
| Small | 14px | 12px | 8px |
| Base | 14px | 16px | 10px |
| Large | 16px | 20px | 12px |

## Icon-only Trigger

- Padding: 8px
- Min size: 44x44px
- Icon: 20x20px

## Variants

### Default
- Menu width: 176px, items have 12px radius

### With Divider
- Top border (glass-border-subtle) between child groups, skip first group

### With Header
- Header padding: 16px horizontal, 12px vertical
- Bottom border: glass-border-subtle
- Name: heading color, 14px, medium weight
- Email: body-subtle color, 14px, truncated

### With Icons
- Icon before label: 16x16px, 8px right margin, body color
- On hover, icon color changes to heading

### With Checkbox / Radio
- Inputs: 16x16px, 8px radius, focus ring in brand-soft
- Helper text: 12px, body-subtle color, 2px top margin

### With Search
- Search input at top of menu following `inputs.md` specs
- Left icon: 12px left padding, input 36px left padding

### Scrollable
- Max height: 192px, vertical scroll overflow

## States

| State | Appearance |
|---|---|
| Focused trigger | no outline, 2px brand ring |
| Hover item | glass-bg-hover background, heading text |
| Active/open item | glass-bg-hover background, heading text |
| Disabled item | fg-disabled text, not-allowed cursor, no pointer events |
