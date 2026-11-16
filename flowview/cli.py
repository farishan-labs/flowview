"""CLI entry point for flowview."""

import argparse
import subprocess
import sys

from .render import resolve_target, build_html


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="flowview", description="Native Mermaid/flow viewer (Pele + vocus)."
    )
    parser.add_argument("target", nargs="?", default="", help="file, dir, or topic slug")
    args = parser.parse_args(argv)

    target = resolve_target(args.target)
    if target is None:
        print(f"flowview: no flow found for: {args.target!r}", file=sys.stderr)
        sys.exit(2)
    try:
        source = target.read_text(encoding="utf-8")
    except OSError as e:
        print(f"flowview: cannot read {target}: {e}", file=sys.stderr)
        sys.exit(2)
    title = target.stem
    is_raw = target.suffix.lower() == ".mmd"
    html = build_html(source, title, is_raw_mmd=is_raw)
    try:
        subprocess.run(["vocus", "--title", title], input=html, text=True, check=False)
    except FileNotFoundError:
        print("flowview: 'vocus' not found on PATH; install vocus first", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"flowview: failed to start viewer: {e}", file=sys.stderr)
        sys.exit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())