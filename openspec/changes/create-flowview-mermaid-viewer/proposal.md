# Proposal

## Why

Memory #821 specifies `/openflow <flow-name>` producing a Mermaid artifact.
Research (topics/openflow-tooling) recommends reusing mdview's resolution
logic and rendering Mermaid via Pele (pele.run) in HTML, then viewing in
vocus. flowview is that viewer: resolves a flow name/file, renders Mermaid
to HTML via Pele CDN, pipes to vocus.

## What Changes

- New project `flowview`: Python CLI resolving a flow target (file/dir/topic
  slug) like mdview, rendering Mermaid fenced blocks (or raw .mmd) to HTML
  using Pele CDN, piping HTML to vocus.
- Supports both Markdown-with-mermaid and raw `.mmd` inputs.
- Ships install.sh for GitHub Pages.

## Capabilities

### New Capabilities
- `mermaid-flow-rendering`: resolve a flow target and render its Mermaid
  content to HTML via Pele, viewable in vocus.

### Modified Capabilities
- (none)

## Impact

- New repo `~/dev/labs/flowview`.
- Depends on `vocus` (pip) and network (Pele CDN) with optional local cache.
- /openflow slash command (agent repo) will invoke flowview.