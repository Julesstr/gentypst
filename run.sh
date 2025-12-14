#!/usr/bin/env bash
set -e

python gentypst.py
typst compile output.typ
xdg-open output.pdf
