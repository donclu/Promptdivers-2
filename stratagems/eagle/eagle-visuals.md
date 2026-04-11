# Eagle Visuals — Eagle

## Code: `EVS`

> "A picture says a thousand tokens. Make it count."

---

## When to call

- You need to **generate, edit, or direct visual assets**: images, diagrams, mockups, thumbnails.
- Creating **architecture diagrams**, flowcharts, or system maps.
- Designing **UI mockups** or wireframes before implementation.
- Producing **marketing visuals**, social media assets, or presentation graphics.
- Generating **data visualizations**: choosing chart types, describing visualizations.

---

## Inputs

1. **Type** — diagram / mockup / illustration / chart / icon / photo-style.
2. **Purpose** — what is this visual for? (Technical docs / presentation / marketing / UI)
3. **Specifications** — dimensions, colors, style guide, brand constraints.
4. **Content** — what should be shown? Text, data, relationships, layout.
5. **Tool** — what generation/editing tool is available? (IDE image tool, Mermaid, draw.io, Figma, AI image gen)

---

## Steps

1. **Define the visual brief:**
   ```markdown
   ## VISUAL BRIEF
   Type: [diagram / mockup / illustration / chart]
   Purpose: [doc / presentation / marketing / UI]
   Audience: [developers / leadership / public]
   Style: [technical / clean / playful / brand-aligned]
   Dimensions: [web banner / slide / social / custom]
   ```

2. **Choose the tool and format:**

   | Visual type | Recommended tool | Format |
   |-------------|-----------------|--------|
   | Architecture diagram | Mermaid in Markdown | `.md` with mermaid block |
   | Flowchart / sequence | Mermaid | `.md` |
   | UI mockup | IDE image gen or description | `.png` / `.webp` |
   | Data chart | Describe chart type + axes | Description for human/tool to implement |
   | Illustration / marketing | AI image generation tool | `.png` / `.webp` |
   | Icon set | SVG description or tool | `.svg` |

3. **For diagrams (Mermaid):**
   ```mermaid
   graph LR
     A[Input] --> B{Decision}
     B -->|Yes| C[Action]
     B -->|No| D[Alternative]
   ```
   - Produce the Mermaid code
   - Verify it renders correctly
   - Include in documentation

4. **For mockups and illustrations:**
   - Write a detailed visual description / prompt
   - If AI image gen is available: generate and iterate
   - If not: produce the spec for a designer
   - Note: pair with `ui-design-expert` for UI-specific work

5. **For data visualizations:**
   - Recommend chart type based on data relationship:
     - Comparison → bar chart
     - Trend over time → line chart
     - Composition → pie/donut chart
     - Distribution → histogram
     - Correlation → scatter plot
   - Describe axes, labels, colors, key insights to highlight
   - Produce the chart with available tools or describe for implementation

6. **Quality check:**
   - Does the visual communicate the intended message at a glance?
   - Is text readable? Colors accessible? Labels clear?
   - Does it match the project's style/brand?

7. **Log:** `Stratagem: EVS — Visual: [type] for [purpose]. Tool: [what was used]`

---

## Outputs

- Visual assets (images, Mermaid diagrams, chart specs)
- Visual brief document (if handing off to a designer)
- Alternative options (if the human wants to choose)

---

## Cooldown / limits

- No cooldown for diagrams and specifications.
- AI-generated images: iterate max 3 times before asking human for direction.
- **Never use copyrighted content** as source material for image generation.
- For UI mockups: always pair with `ui-design-expert` skill for production-quality work.
- Mermaid diagrams: test rendering before including in docs.

---

*"Eagle Visuals — Super Earth's propaganda division, at your service."*
