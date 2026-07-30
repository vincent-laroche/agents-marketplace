# Color Tokens


## Background Tokens

### Neutral
| Token | Light | Dark |
|---|---|---|
| neutral-primary-soft | #FFFFFF | #0B0F19 |
| neutral-primary | #FFFFFF | #060A12 |
| neutral-primary-medium | #FFFFFF | #141C2E |
| neutral-primary-strong | #FFFFFF | #1E293B |
| neutral-secondary-soft | #F8FAFB | #0B0F19 |
| neutral-secondary | #F8FAFB | #060A12 |
| neutral-secondary-medium | #F8FAFB | #141C2E |
| neutral-secondary-strong | #F8FAFB | #1E293B |
| neutral-tertiary-soft | #F0F3F5 | #0B0F19 |
| neutral-tertiary | #F0F3F5 | #141C2E |
| neutral-tertiary-medium | #F0F3F5 | #1E293B |
| neutral-quaternary | #E2E7EC | #1E293B |
| quaternary-medium | #E2E7EC | #2A3650 |
| gray | #CAD1D8 | #2A3650 |

### Brand
| Token | Light | Dark |
|---|---|---|
| brand-softer | #E6FFF3 | #071F16 |
| brand-soft | #B8FFD9 | #0C3927 |
| brand | #0EA66D | #8AFFC4 |
| brand-medium | #B8FFD9 | #0C3927 |
| brand-strong | #087A4E | #6BEFAB |

### Status
| Token | Light | Dark |
|---|---|---|
| success-soft | #ECFDF5 | #002C22 |
| success | #007A55 | #009966 |
| success-medium | #D0FAE5 | #004F3B |
| success-strong | #006045 | #007A55 |
| danger-soft | #FEF0F2 | #4D0218 |
| danger | #C70036 | #C70036 |
| danger-medium | #FFE4E6 | #8B0836 |
| danger-strong | #A50036 | #A50036 |
| warning-soft | #FFF7ED | #7C2D12 |
| warning | #F97316 | #F97316 |
| warning-medium | #FFEDD5 | #7C2D12 |
| warning-strong | #C2410C | #C2410C |

### Button Glint (CSS custom properties, used for the glint box-shadow effect)
| Variable | Light | Dark |
|---|---|---|
| `--color-1-400` | rgba(255,255,255,0.30) | rgba(255,255,255,0.15) |
| `--color-1-700` | rgba(0,0,0,0.08) | rgba(0,0,0,0.20) |

### Utility
| Token | Light | Dark |
|---|---|---|
| dark | #0F172A | #0F172A |
| dark-strong | #0B0F19 | #1E293B |
| disabled | #F0F3F5 | #0F172A |

### Accent
| Token | Value (same both modes) |
|---|---|
| purple | #A78BFA |
| sky | #38BDF8 |
| teal | #2DD4BF |
| pink | #F472B6 |
| cyan | #22D3EE |
| fuchsia | #D946EF |
| indigo | #818CF8 |
| orange | #FB923C |

## Text Color Tokens

### Base
| Token | Light | Dark |
|---|---|---|
| white | #FFFFFF | #FFFFFF |
| black | #0F172A | #0F172A |
| heading | #0F172A | #F0F6FC |
| body | #475569 | #94A3B8 |
| body-subtle | #64748B | #94A3B8 |

### Brand
| Token | Light | Dark |
|---|---|---|
| fg-brand-subtle | #B8FFD9 | #0C3927 |
| fg-brand | #0EA66D | #8AFFC4 |
| fg-brand-strong | #087A4E | #B8FFD9 |

### Status
| Token | Light | Dark |
|---|---|---|
| fg-success | #047857 | #065F46 |
| fg-success-strong | #065F46 | #10B981 |
| fg-danger | #BE123C | #F43F5E |
| fg-danger-strong | #881337 | #F87171 |
| fg-warning-subtle | #EA580C | #F97316 |
| fg-warning | #7C2D12 | #FBBF24 |
| fg-disabled | #94A3B8 | #64748B |

### Informational / Accent
| Token | Light | Dark |
|---|---|---|
| fg-yellow | #FACC15 | #FACC15 |
| fg-info | #312E81 | #93C5FD |
| fg-purple | #8B5CF6 | #A78BFA |
| fg-purple-strong | #7C3AED | #DDD6FE |
| fg-cyan | #06B6D4 | #22D3EE |
| fg-indigo | #6366F1 | #818CF8 |
| fg-pink | #EC4899 | #F472B6 |
| fg-lime | #65A30D | #84CC16 |

## Border Color Tokens

| Token | Light | Dark |
|---|---|---|
| border-dark | #0F172A | #475569 |
| border-buffer | #FFFFFF | #060A12 |
| border-buffer-medium | #FFFFFF | #0F172A |
| border-buffer-strong | #FFFFFF | #1E293B |
| border-muted | #F8FAFB | #0B0F19 |
| border-light-subtle | #F0F3F5 | #0B0F19 |
| border-light | #F0F3F5 | #0F172A |
| border-light-medium | #F0F3F5 | #1E293B |
| border-default-subtle | #E2E7EC | #0B0F19 |
| border-default | #E2E7EC | #0F172A |
| border-default-medium | #E2E7EC | #1E293B |
| border-default-strong | #E2E7EC | #475569 |
| border-success-subtle | #A7F3D0 | #064E3B |
| border-success | #047857 | #065F46 |
| border-danger-subtle | #FECDD3 | #881337 |
| border-danger | #BE123C | #BE123C |
| border-warning-subtle | #FED7AA | #7C2D12 |
| border-warning | #EA580C | #F97316 |
| border-brand-subtle | #B8FFD9 | #0C3927 |
| border-brand-light | #0EA66D | #8AFFC4 |
| border-brand | #0EA66D | #8AFFC4 |
| border-dark-subtle | #0F172A | #1E293B |
| border-purple | #A78BFA | #A78BFA |
| border-orange | #FB923C | #FB923C |

## Glassmorphism Surface Tokens

Glass surfaces use translucent backgrounds with backdrop blur instead of opaque fills. Apply these to cards, navbars, modals, sidebars, accordion, and dropdown containers.

| Token | Light | Dark |
|---|---|---|
| glass-bg | rgba(255, 255, 255, 0.45) | rgba(255, 255, 255, 0.1) |
| glass-bg-hover | rgba(255, 255, 255, 0.55) | rgba(255, 255, 255, 0.15) |
| glass-border | rgba(0, 0, 0, 0.08) | rgba(255, 255, 255, 0.12) |
| glass-border-subtle | rgba(0, 0, 0, 0.05) | rgba(255, 255, 255, 0.06) |
| glass-blur | blur(20px) | blur(20px) |
| glass-shadow | 0 8px 32px rgba(0, 0, 0, 0.06), inset 0 1px 0 rgba(255, 255, 255, 0.6), inset 0 -1px 0 rgba(255, 255, 255, 0.15) | 0 8px 32px rgba(0, 0, 0, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.5), inset 0 -1px 0 rgba(255, 255, 255, 0.1) |
| glass-edge-top | linear-gradient(90deg, transparent, rgba(255,255,255,0.5), transparent) | linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent) |
| glass-edge-left | linear-gradient(180deg, rgba(255,255,255,0.5), transparent, rgba(255,255,255,0.2)) | linear-gradient(180deg, rgba(255,255,255,0.2), transparent, rgba(255,255,255,0.05)) |

## Semantic Usage Rules

- Page/section backgrounds: neutral-primary-soft (default), neutral-secondary-soft (alternating)
- Glass surfaces (cards, navbars, modals, sidebars): glass-bg background + glass-blur + glass-border + glass-shadow
- Primary buttons: brand background
- Headings: heading text color
- Body text: body text color
- CTA links: fg-brand text color
- Default borders: border-default (opaque containers) or glass-border (glass containers)
- Status borders match intent: success → border-success, danger → border-danger, warning → border-warning
- Disabled: disabled background + fg-disabled text

## Prohibited

- No raw hex/rgb values in component code — always use design tokens
- No brand text color for long-form paragraphs
- No accent text tokens (fg-purple, etc.) for body copy or navigation
- No brand/accent backgrounds for large layout surfaces (pages, sections) unless it's a hero/campaign area
- No manual light/dark value swapping — let the CSS custom properties handle it
