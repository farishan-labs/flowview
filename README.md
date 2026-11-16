# flowview

Native Mermaid/flow viewer: renders Mermaid fenced blocks (or raw `.mmd`) to HTML
via Pele (pele.run) and displays in vocus.

## Requirements

- Tested on Ubuntu 22.04+ (X11). Other distros may work; open an issue if you
  need help.
- Python 3.10+
- GTK 3 + WebKit2GTK 4.0
- [vocus](https://github.com/farishan-labs/vocus) installed and on PATH

## Install

```bash
curl -fsSL https://farishan-labs.github.io/flowview/install.sh | bash
```

## Usage

```bash
flowview path/to/flow.mmd
flowview path/to/notes.md        # extracts ```mermaid fences
flowview research-topic-slug
```

Keyboard: `Esc` closes. Fullscreen, borderless. Pele renders client-side via CDN.

## Used by

- /openflow slash command (agent repo) — invokes flowview on a flow name.

## License

GPL-3.0.