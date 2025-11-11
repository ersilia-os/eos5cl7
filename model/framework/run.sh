#!/usr/bin/env bash
set -euo pipefail
: "${PYTHON:=python}"
"$PYTHON" "$1/code/main.py" "$2" "$3"
