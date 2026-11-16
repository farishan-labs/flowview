# Design

## Context

flowview mirrors mdview's target resolution and HTML production, but renders
Mermaid instead of Markdown. It depends on vocus for the native frame and on
Pele (CDN) for Mermaid→SVG.

## Goals / Non-Goals

**Goals:**
- Resolve flow targets like mdview.
- Render Mermaid fenced blocks / raw .mmd to HTML with Pele CDN.
- Pipe HTML to vocus.

**Non-Goals:**
- No native window code (vocus owns it).
- No offline Pele cache in v0 (optional later).

## Decisions

- Reuse mdview's resolve_target logic (copy, not import, to keep projects
  independent).
- Pele CDN: `https://cdn.jsdelivr.net/npm/pele@1/dist/pele.global.js`,
  mount via `pele.mount(el, el.textContent)` on `pre.mermaid`.
- Convert ```mermaid fences to `<pre class="mermaid">source</pre>`.
- Raw .mmd: wrap whole content in a single `pre.mermaid`.

## Risks / Trade-offs

- Network required for Pele CDN.
- Pele layout differs from Mermaid.js; acceptable for viewing.