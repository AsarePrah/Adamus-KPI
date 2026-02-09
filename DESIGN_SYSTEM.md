# Visual Design Guide - Professional Color & Component System

## Color Palette

### Primary Colors
```
🟦 Primary: #6366f1 (Indigo)
🟦 Primary Dark: #4f46e5 (Darker Indigo)
🟦 Primary Light: #818cf8 (Lighter Indigo)
```

### Status Colors
```
🟢 Success: #10b981 (Green)
🔴 Danger: #ef4444 (Red)
🟡 Warning: #f59e0b (Amber)
🔵 Info: #0ea5e9 (Sky Blue)
```

### Background Colors
```
⬜ Primary: #f8fafc (Light Slate)
⬜ Secondary: #f1f5f9 (Lighter Slate)
⬜ Cards: #ffffff (White)
```

### Text Colors
```
🔤 Primary: #1e293b (Dark Slate)
🔤 Secondary: #64748b (Slate)
🔤 Borders: #e2e8f0 (Border Gray)
```

## Typography System

### Font Stack
```
-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif
```

### Font Sizes
```
H1 (28px, 700)   - Page titles
H3 (20px, 700)   - Section titles
H4 (16px, 600)   - Subsection titles
Body (14px, 400) - Regular text
Label (13px, 600, uppercase) - Form labels
Small (13px, 500) - Secondary text
```

## Spacing Scale

```
8px  - Minimal (not used)
12px - Small gaps
16px - Standard gaps
24px - Large gaps
32px - Extra large gaps
```

## Shadow System

### shadow-sm
```
0 1px 2px 0 rgba(0, 0, 0, 0.05)
```
Use: Light hover effects

### shadow
```
0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)
```
Use: Standard cards and elements

### shadow-lg
```
0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)
```
Use: Elevated elements

### shadow-xl
```
0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)
```
Use: Modals, popovers, tooltips

## Rounded Corners

```
6px  - Input fields, small components
8px  - Standard cards, buttons
12px - Large cards, sections
999px - Pills, fully rounded
```

## Button Styles

### Primary Button (CTA)
```
Background: Linear gradient 135deg (#6366f1 → #4f46e5)
Padding: 10px 16px
Border Radius: 6px
Shadow: 0 1px 2px rgba(0,0,0,0.05)
Hover: Transform -2px, shadow upgrade
```

### Ghost Button (Secondary)
```
Background: Transparent
Border: 1px solid #e2e8f0
Color: #64748b
Padding: 10px 16px
Border Radius: 6px
Hover: Background #f1f5f9, border #6366f1, color #6366f1
```

### Success Button
```
Background: Linear gradient 135deg (#10b981 → #059669)
Color: White
Padding: 10px 16px
Border: None
```

### Danger Button
```
Background: Linear gradient 135deg (#ef4444 → #dc2626)
Color: White
Padding: 10px 16px
Border: None
```

## Form Elements

### Input Field
```
Padding: 10px 12px
Border: 1px solid #e2e8f0
Border Radius: 6px
Background: #ffffff
Font Size: 14px
```

### Input Focus State
```
Border Color: #6366f1
Box Shadow: 0 0 0 3px rgba(99, 102, 241, 0.1)
Background: #ffffff
Transition: All 0.3s cubic-bezier(0.4, 0, 0.2, 1)
```

### Label
```
Font Size: 13px
Font Weight: 600
Color: #64748b
Text Transform: uppercase
Letter Spacing: 0.5px
```

## Card Component

```
Background: #ffffff
Border: 1px solid #e2e8f0
Border Radius: 12px
Padding: 24px
Shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1)
Transition: All 0.3s cubic-bezier(0.4, 0, 0.2, 1)
Hover Shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1)
```

## Navigation Link

```
Default:
  Color: #64748b
  Padding: 10px 12px
  Border Radius: 6px
  Background: Transparent

Hover:
  Background: #f1f5f9
  Color: #6366f1
  Border Color: #6366f1
  
Transition: All 0.3s cubic-bezier(0.4, 0, 0.2, 1)
```

## Status Badge

### Pending (Warning)
```
Background: rgba(245, 158, 11, 0.1)
Border: 1px solid rgba(245, 158, 11, 0.2)
Color: #b45309
Border Radius: 8px
Padding: 12px 16px
```

### Approved (Success)
```
Background: rgba(16, 185, 129, 0.1)
Border: 1px solid rgba(16, 185, 129, 0.2)
Color: #047857
Border Radius: 8px
Padding: 12px 16px
```

### Rejected (Error)
```
Background: rgba(239, 68, 68, 0.1)
Border: 1px solid rgba(239, 68, 68, 0.2)
Color: #991b1b
Border Radius: 8px
Padding: 12px 16px
```

## Table Styling

### Header
```
Background: #f1f5f9
Font Size: 12px
Font Weight: 700
Color: #64748b
Text Transform: uppercase
Letter Spacing: 0.5px
Padding: 12px
```

### Row
```
Border Bottom: 1px solid #e2e8f0
Padding: 12px

Hover:
  Background: #f1f5f9
```

## Modal/Dialog

```
Width: 100% (max 420px)
Background: #ffffff
Border: None
Border Radius: 12px
Box Shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1)
Padding: 24px
```

## Transitions

All interactive elements use:
```
Transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)
```

This provides:
- Smooth animations
- Professional feel
- Good performance
- Consistent timing

## Responsive Breakpoints

### Large Screens (1024px+)
- 2-column layout
- Sticky sidebar
- Full width modals

### Medium Screens (768px - 1024px)
- 1-column layout
- Collapsible sidebar
- Full width modals

### Small Screens (<768px)
- 1-column layout
- Hidden sidebar (menu)
- Full width modals
- Adjusted padding

## Implementation Notes

1. **Consistency**: Use these values throughout
2. **Hierarchy**: Maintain clear visual hierarchy
3. **Spacing**: Use the spacing scale (12, 16, 24, 32px)
4. **Colors**: Use CSS variables for easy updates
5. **Typography**: Follow the font size scale
6. **Shadows**: Use the appropriate shadow level
7. **Transitions**: Always use 0.3s timing
8. **Borders**: Use #e2e8f0 for consistency
9. **Hover States**: Provide visual feedback
10. **Focus States**: Ensure accessibility

## Color Combinations Reference

| Use Case | Color | Paired With |
|----------|-------|-------------|
| Primary CTA | #6366f1 | White text |
| Success | #10b981 | White text |
| Error/Warning | #ef4444 | White text |
| Secondary Action | #64748b | White text |
| Background | #f8fafc | Any text |
| Card | #ffffff | #1e293b text |
| Border | #e2e8f0 | N/A |
| Hover | #f1f5f9 | Any text |

---

This design system ensures consistency, professionalism, and excellent user experience across the entire application.
