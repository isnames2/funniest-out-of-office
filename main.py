#!/usr/bin/env python3
"""Funniest out-of-office auto-reply — one line, written to entry.txt."""

import os
from pathlib import Path

LINE = "I'm away until Monday. If this is urgent, it isn't — it's just loud. I'll reply when I'm back and braver."
# 105 characters, one line, no trailing newline: bytes equal characters
# apart from the single em dash (3 bytes in UTF-8).

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
