# Tasks

## 1. Scaffold

- [x] 1.1 Create repo layout (pyproject.toml, flowview/__init__.py, flowview/cli.py, flowview/render.py) and verify files exist
- [x] 1.2 Add install-deps.sh and README.md

## 2. Resolution

- [x] 2.1 Implement resolve_target (file/dir/topic slug, .md/.mmd) mirroring mdview and verify with a topic slug

## 3. Rendering

- [x] 3.1 Implement Mermaid fence → pre.mermaid conversion and Pele CDN injection; verify HTML output
- [x] 3.2 Implement raw .mmd wrapping; verify output
- [x] 3.3 Wrap HTML in a minimal template (title, styling) and verify

## 4. CLI & packaging

- [x] 4.1 Add argparse CLI (--html/--title not needed; target arg) and verify `flowview --help`
- [x] 4.2 Add pyproject console script `flowview`; verify pip install -e and PATH
- [x] 4.3 Pipe rendered HTML to vocus and verify diagram opens

## 5. Integration

- [x] 5.1 Verify flowview on a sample .mmd opens in vocus and renders via Pele
- [x] 5.2 Verify flowview on a Markdown file with ```mermaid fence

## Workflow follow-up

- Archive the change after review.
- Add /openflow slash command in agent repo invoking flowview.