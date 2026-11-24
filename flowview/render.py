"""Resolve flow targets and render Mermaid to HTML via Pele."""

import html as _html
import re
import pathlib

RESEARCH_TOPICS = "/home/faris/dev/labs/research/topics"

PELE_CDN = "https://cdn.jsdelivr.net/npm/pele@1/dist/pele.global.js"


def resolve_target(arg: str) -> pathlib.Path | None:
    if not arg:
        return None
    p = pathlib.Path(arg).expanduser()
    if p.is_file():
        return p
    if p.is_dir():
        for name in ("README.md", "readme.md", "flow.mmd", "flow.md"):
            cand = p / name
            if cand.is_file():
                return cand
        mds = sorted(list(p.glob("*.mmd")) + list(p.glob("*.md")))
        if mds:
            return mds[0]
        return None
    cand = pathlib.Path(RESEARCH_TOPICS) / arg
    if cand.is_dir():
        return resolve_target(str(cand))
    for ext in (".md", ".mmd"):
        if (pathlib.Path(RESEARCH_TOPICS) / (arg + ext)).is_file():
            return pathlib.Path(RESEARCH_TOPICS) / (arg + ext)
    return None


def _fences_to_pre(source: str) -> str:
    # convert ```mermaid ... ``` fences to <pre class="mermaid">
    def repl(m):
        body = m.group(1)
        return f'<pre class="mermaid">{_html.escape(body.strip())}</pre>'
    out = re.sub(r"```mermaid\s*\n(.*?)```", repl, source, flags=re.S)
    # also handle ```mmd
    out = re.sub(r"```mmd\s*\n(.*?)```", repl, out, flags=re.S)
    return out


def build_html(source: str, title: str, is_raw_mmd: bool = False) -> str:
    if is_raw_mmd:
        body = f'<pre class="mermaid">{_html.escape(source.strip())}</pre>'
    else:
        converted = _fences_to_pre(source)
        # if no mermaid fences found, treat entire source as one diagram
        if "<pre class=\"mermaid\">" not in converted:
            body = f'<pre class="mermaid">{_html.escape(source.strip())}</pre>'
        else:
            # keep any surrounding markdown as text? For v0, render only diagrams
            body = converted
            # strip non-pre content? keep simple: extract pre blocks
            pres = re.findall(r'<pre class="mermaid">.*?</pre>', body, flags=re.S)
            body = "\n".join(pres) if pres else body
    template = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{_html.escape(title)}</title>
<style>
  :root {{
    --pele-bg: #fff; --pele-fg: #1f1f1f; --pele-line: #1f1f1f;
    --pele-muted: #6e6e6e; --pele-surface: #f3f3f3;
    --pele-surface-alt: #e6e6e6; --pele-border: #8a8a8a;
  }}
  body {{ font-family: system-ui, sans-serif; margin: 2rem; background: #fafafa; color: #222; }}
  @media (prefers-color-scheme: dark) {{
    :root {{
      --pele-bg: #2a2a3e; --pele-fg: #e0e0e0; --pele-line: #e0e0e0;
      --pele-muted: #a0a0a0; --pele-surface: #3a3a4e;
      --pele-surface-alt: #2a2a3e; --pele-border: #5a5a6e;
    }}
    body {{ background: #1e1e2e; color: #e0e0e0; }}
  }}
  .mermaid {{ background: var(--pele-bg); padding: 1rem; border-radius: 8px; text-align: center; }}
  .mermaid svg {{ margin: 0 auto; display: block; }}
  h1 {{ font-size: 1.2rem; opacity: .7; }}
</style>
</head>
<body>
<h1>{_html.escape(title)}</h1>
{body}
<script src="{PELE_CDN}"></script>
<script>
  (function() {{
    function mountAll() {{
      if (!window.pele) return setTimeout(mountAll, 50);
      document.querySelectorAll('pre.mermaid').forEach(function (el) {{
        try {{ window.pele.mount(el, el.textContent); }}
        catch (e) {{ el.textContent = 'PeleError: ' + e.message; }}
      }});
    }}
    mountAll();
  }})();
</script>
</body>
</html>"""
    return template