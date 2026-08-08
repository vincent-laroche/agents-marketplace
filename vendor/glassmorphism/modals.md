# Modals

> Dependencies: `colors.md`, `radius.md`, `shadows.md`, `buttons.md`, `inputs.md`

## Core Specs

### Overlay (Backdrop)
- Fixed, covers full screen
- Z-index: 40
- Background: black at 50% opacity
- Backdrop blur: 8px

### Content Container
- Background: glass-bg
- Backdrop filter: glass-blur
- Border: 1px, glass-border
- Radius: 20px (base)
- Shadow: glass-shadow
- Padding: 20px
- Position: relative, overflow hidden

### Glass Edge Highlights
- Top edge (::before): absolute, top 0, left 0, right 0, height 1px, glass-edge-top gradient
- Left edge (::after): absolute, top 0, left 0, width 1px, full height, glass-edge-left gradient

## Anatomy

### Header
- Bottom border: glass-border-subtle
- Top corners rounded (20px)
- Title: 20px, medium weight, heading color
- Close button: Ghost variant from `buttons.md`, 6px padding

### Body
- Vertical padding: 24px
- Vertical spacing between elements: 24px
- Text: 16px, 1.625 line-height, body color

### Footer
- Top border: glass-border-subtle
- Bottom corners rounded (20px)

## Variants

### Default (Information)
Standard header + body + footer with primary/secondary action buttons.

### Pop-up (Confirmation)
Centered text, prominent icon, reduced padding:
- Body: 24px padding, text centered
- Icon: centered, 16px bottom margin, 48x48px, gray color

### Form Modal
Body contains inputs following `inputs.md`. Vertical spacing between form elements: 16px.

## Rules

- Backdrop covers full screen with fixed positioning
- Content: glass-bg background, glass-blur, 20px radius, glass-shadow
- Header/Footer separated by glass-border-subtle borders
- Close button must be present and functional
- Accessibility: `role="dialog"`, implement focus trap in code
- Dark mode automatic via token system
- Container must have `position: relative; overflow: hidden` for edge highlights
