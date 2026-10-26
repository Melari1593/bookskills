---
name: image-to-web-design
description: Convert any supplied image, screenshot, illustration, or visual design into a reusable, responsive web design system and implementation plan. Use when asked to extract visual language, design tokens, components, motion, textures, depth, or implement a website from visual references.
---

# Image to Web Design — Universal Skill

## Objective
Transform ANY input image into a coherent web design system and, when requested, a functional frontend. Preserve the source's visual identity without assuming that the sample reference is the required style.

## Inputs
- Required: at least one image, screenshot, mockup, or visual reference.
- Optional: website purpose, target audience, preferred stack, accessibility target, brand guidelines, target repository, routes, content, interaction requirements.
- If purpose is missing, offer a generic reusable component library rather than inventing a business or page type.

## Workflow
1. **Inspect**: inventory layout, hierarchy, subjects, silhouettes, textures, palette, typography cues, spacing, light/shadow, perspective, motifs, and image-specific constraints. Distinguish observed features from inferred features.
2. **Extract tokens**: propose semantic color roles (background, surface, text, muted, accent, border), typography pairing, spacing scale, radii, shadows, borders, textures, breakpoints, motion durations, and easing. Extract colors from pixels where practical, then adjust for accessible contrast; report approximations as approximations.
3. **Map to UI**: translate shapes and motifs into header, navigation, hero, buttons, cards, inputs, sections, dialogs, and footer. Do not use decorative art in place of semantic controls.
4. **Illustrations**: when authorized, create original artwork inspired by visual attributes, not a direct reproduction of protected characters or branding. Prefer SVG/CSS for simple scalable motifs, image assets for painterly artwork. Keep foreground, middle ground, and background layers distinct.
5. **Depth and effects**: support flat, embossed, debossed, neumorphic, paper-cut, watercolor, glass, metallic, or other styles ONLY when justified by the source or requested. Implement texture with restrained CSS overlays; make decorative layers pointer-events:none.
6. **Motion**: specify optional entrance, hover, scroll, and ambient effects with reduced-motion fallback. Avoid movement that obscures content, degrades performance, or traps focus.
7. **Implement**: default to React + TypeScript + Tailwind CSS, with Motion/Framer Motion only when needed. Build reusable components and data-driven sections. If user specifies another stack, adapt. Use responsive image handling and avoid layout shift.
8. **Verify**: compare implementation against reference for visual fidelity, spacing, palette, assets, and responsive behavior. Test keyboard navigation, contrast, focus states, alt text, reduced motion, and mobile layouts. State what has and has not been tested.
9. **Package**: deliver tokens, component inventory, asset manifest, implementation, setup instructions, and limitations. Commit/push only when the user requests it and repository access is available.

## Suggested output structure
```
image-to-web-design/
  SKILL.md
  references/                 # optional examples
  outputs/
    visual-analysis.md
    design-tokens.json
    component-map.md
    asset-manifest.md
    implementation-notes.md
```

## Implementation principles
- Avoid hardcoding a specific aesthetic; derive it from each new input.
- Maintain legibility: text overlays must have sufficient contrast; decorative textures must not reduce readability.
- Preserve source aspect ratio, crop intentionally, and respect asset licensing.
- Use semantic HTML, accessible labels, visible focus, and responsive layouts.
- Separate reusable primitives from theme-specific artwork.
- Never claim a generated UI was tested, deployed, or pushed unless verified.

## Example reference: Woodland Watercolor
An illustrative forest scene with warm ivory paper background, muted sage foliage, tan-brown trees, woodland animals, mushrooms, and fine botanical accents. Potential derived UI: cream surfaces, botanical dividers, hand-painted illustration assets, subtle paper grain, soft inset/raised controls, and gentle floating leaf motion. Example approximate palette: #F8F5ED, #E5D8C4, #A98769, #A5A58D, #D9B7A7. This is ONLY an example, never the universal default.

## Invocation
`$image-to-web-design <image> [purpose] [stack] [repo]`

## Acceptance criteria
- Design decisions trace back to observed reference features.
- Responsive, accessible components are separated from theme-specific assets.
- Design tokens can be swapped for a different image without rebuilding all components.
- Any original illustrations, textures, or relief effects are optional, performance-aware layers.
