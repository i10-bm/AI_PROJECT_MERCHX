---
name: Deep Intelligence System
colors:
  surface: '#0b1326'
  surface-dim: '#0b1326'
  surface-bright: '#31394d'
  surface-container-lowest: '#060e20'
  surface-container-low: '#131b2e'
  surface-container: '#171f33'
  surface-container-high: '#222a3d'
  surface-container-highest: '#2d3449'
  on-surface: '#dae2fd'
  on-surface-variant: '#c7c4d7'
  inverse-surface: '#dae2fd'
  inverse-on-surface: '#283044'
  outline: '#908fa0'
  outline-variant: '#464554'
  surface-tint: '#c0c1ff'
  primary: '#c0c1ff'
  on-primary: '#1000a9'
  primary-container: '#8083ff'
  on-primary-container: '#0d0096'
  inverse-primary: '#494bd6'
  secondary: '#4edea3'
  on-secondary: '#003824'
  secondary-container: '#00a572'
  on-secondary-container: '#00311f'
  tertiary: '#ffb95f'
  on-tertiary: '#472a00'
  tertiary-container: '#ca8100'
  on-tertiary-container: '#3e2400'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffddb8'
  tertiary-fixed-dim: '#ffb95f'
  on-tertiary-fixed: '#2a1700'
  on-tertiary-fixed-variant: '#653e00'
  background: '#0b1326'
  on-background: '#dae2fd'
  surface-variant: '#2d3449'
  slate-950: '#020617'
  slate-900: '#0f172a'
  slate-800: '#1e293b'
  slate-700: '#334155'
  indigo-500: '#6366f1'
  emerald-500: '#10b981'
  rose-500: '#f43f5e'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: jetbrainsMono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: jetbrainsMono
    fontSize: 10px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  container-max-width: 1440px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
---

## Brand & Style

The design system is engineered for a technical, high-fidelity environment where AI-driven insights meet enterprise e-commerce operations. The brand personality is **authoritative, sophisticated, and precise**, designed to evoke a sense of "quiet power" and expert-level reliability. It targets data-literate merchants and growth engineers who require a clear window into complex autonomous agent activities.

The visual direction follows a **Modern Corporate** style with **Minimalist** and **Glassmorphic** influences. It rejects unnecessary fluff, focusing instead on deep backgrounds, razor-sharp typography, and structural depth. Visual interest is generated through subtle micro-interactions and the interplay of semi-transparent layers rather than heavy gradients or illustrative elements. The system feels like a high-performance terminal—instrumented, intentional, and robust.

## Colors

The palette is anchored in a professional **dark mode** foundation. The primary background uses a deep charcoal/slate (#0f172a) to reduce eye strain during long analytical sessions and provide a high-contrast base for data.

- **Primary (Indigo #6366f1):** Used for primary actions, active states, and technical branding elements. It represents the "intelligence" layer of the platform.
- **Secondary (Emerald #10b981):** Reserved for positive growth metrics, successful agent runs, and "healthy" status indicators.
- **Tertiary (Amber #f59e0b):** Utilized for warnings or pending states in agent logs.
- **Surface Strategy:** Use `slate-900` for the main canvas, `slate-800` for primary containers (cards/panels), and `slate-700` for borders and dividers. 
- **Functional Accents:** `rose-500` is strictly reserved for critical errors or negative inventory trends.

## Typography

This design system employs **Inter** for all primary interface elements due to its exceptional legibility and neutral, professional character. To emphasize the technical nature of the AI orchestration, **JetBrains Mono** is introduced for labels, status chips, and telemetry data.

- **Headlines:** Use tight letter-spacing and heavy weights (700-800) to create a strong visual anchor for page sections.
- **Body:** Standardized at 14px and 16px to maintain high information density without sacrificing readability.
- **Data Display:** All IDs, SKU numbers, and agent status labels must use the monospaced label font to differentiate "system data" from "user content."

## Layout & Spacing

The system utilizes a **12-column fluid grid** for dashboard views, allowing content to expand and contract while maintaining strict alignment. A **4px baseline grid** governs all micro-spacing (paddings, margins, and component heights).

- **Desktop:** 32px outer margins with 24px gutters. Content is typically organized in modular widgets that span 3, 4, 6, or 12 columns.
- **Tablet:** 24px margins. Layouts reflow from multi-column widgets to stacked panels where necessary.
- **Mobile:** 16px margins. Single-column vertical stack for all cards. 
- **Spacing Philosophy:** Use generous internal padding within cards (24px) to ensure that dense data-points don't feel cluttered.

## Elevation & Depth

Visual hierarchy is established through **tonal layering** and **semi-transparent surfaces** rather than dramatic shadows. This creates a sophisticated "HUD" (Heads-Up Display) aesthetic.

- **Level 0 (Background):** `slate-950` or `slate-900`. The base canvas.
- **Level 1 (Default Surface):** `slate-800` with a subtle 1px border of `slate-700`. This is the standard card container.
- **Level 2 (Active/Hover Surface):** `slate-700` or a semi-transparent Indigo tint (10% opacity) for high-focus areas.
- **Shadows:** Only used on Level 2 or 3 elements (like dropdowns and modals). Shadows should be long, soft, and extremely low opacity (0.3), using a dark blue tint instead of pure black to maintain the "dark mode" richness.
- **Transparency:** Use `backdrop-filter: blur(12px)` on navigation bars and modal overlays to maintain context of the underlying data.

## Shapes

The shape language is **sharp and professional**. By using "Soft" roundedness (4px - 8px), the UI maintains a technical edge while avoiding the aggressive sharpness of pure 0px corners.

- **Standard Components:** 4px (`rounded-sm`) for inputs, small buttons, and chips.
- **Containers:** 8px (`rounded-md`) for dashboard cards and primary panels.
- **Interactive States:** Hovering over elements should never change their radius; depth should be conveyed via border color shifts or subtle background brightening.

## Components

### Buttons
- **Primary:** Solid `indigo-500` with white text. No gradients. On hover, shift to `indigo-400`.
- **Secondary/Ghost:** `slate-800` background with a 1px `slate-700` border.
- **Size:** Maintain a 36px height for standard buttons to keep the interface compact.

### Input Fields
- Dark backgrounds (`slate-950`) with 1px `slate-700` borders. 
- Focus state: Border changes to `indigo-500` with a subtle 2px indigo outer glow (0.2 opacity).
- Labels should always use the monospaced font at 10px-12px.

### Cards & Panels
- **Container:** `slate-800` background, 1px `slate-700` border, 8px corner radius.
- **Header:** A distinct 1px bottom border separates the title area from the content.

### Chips & Status Indicators
- Use the monospaced font. 
- **Running:** `indigo-500` text with a 10% indigo background.
- **Success:** `emerald-500` text with a 10% emerald background.
- **Error:** `rose-500` text with a 10% rose background.

### Data Tables
- Row hover states should use a subtle background shift to `slate-800/50`.
- Use `slate-700` for thin horizontal dividers only; avoid vertical lines to keep the look clean.