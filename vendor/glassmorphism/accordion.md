# Accordion

> Dependencies: `colors.md`, `radius.md`

## Core Specs

- **Wrapper:** full width, 1px border (glass-border), 20px radius — clips first/last item corners
- **Item separator:** 1px bottom border (glass-border-subtle) on every item except last
- **Wrapper position:** relative, overflow hidden

## Glass Effect

- **Background:** glass-bg
- **Backdrop filter:** glass-blur
- **Border:** 1px, glass-border
- **Shadow:** glass-shadow
- **Top edge (::before):** absolute, top 0, left 0, right 0, height 1px, glass-edge-top gradient
- **Left edge (::after):** absolute, top 0, left 0, width 1px, full height, glass-edge-left gradient

## Trigger (Button)

- **Layout:** flex, space-between, full width
- **Padding:** 20px horizontal, 16px vertical
- **Font:** 14px, medium weight
- **Text color:** heading
- **Background:** transparent
- **Hover:** glass-bg-hover background
- **Focus:** outline none, 2px ring in brand color
- **Transition:** all properties, 200ms
- **Open state:** glass-bg-hover background

## Panel (Content)

- **Padding:** 20px horizontal, 16px vertical
- **Background:** transparent
- **Top border:** 1px, glass-border-subtle
- **Font:** 14px, body color, 1.625 line-height

## Chevron Icon

- Size: 16x16px
- Color: body text color
- Closed: 0deg rotation
- Open: 180deg rotation
- Transition: transform, 150ms

## Variants

### Default (Collapse)
One panel open at a time. Items stacked inside a single shared glass wrapper with rounded corners.

### Separated Cards
Each item is independent — has its own glass-bg, glass-blur, glass-border, 20px radius, and glass-shadow. 8px bottom margin between items. No shared outer border.

### Always Open
Multiple panels can expand simultaneously. Same styling as Default.

### Flush
No outer border. Trigger and panel have transparent backgrounds. Only bottom border dividers between items. Use inside containers that already provide a background.

## States

| State | Trigger appearance |
|---|---|
| Closed | heading text, transparent background |
| Open | heading text, glass-bg-hover background |
| Hover | glass-bg-hover background |
| Focus | 2px brand ring, no outline |
| Disabled | fg-disabled text, not-allowed cursor, no hover/focus |
