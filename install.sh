#!/usr/bin/env bash
set -euo pipefail
REPO="farishan-labs/flowview"
BRANCH="main"
echo "Installing flowview (requires vocus)..."
TMPDIR="$(mktemp -d)"
git clone "https://github.com/${REPO}.git" "$TMPDIR/flowview"
cd "$TMPDIR/flowview"
pip install --user -e .
echo "flowview installed. Run: flowview <flow>"