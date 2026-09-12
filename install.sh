#!/bin/sh
set -eu
OG_REPO_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec python3 "$OG_REPO_DIR/scripts/install_skills.py" "$@"
