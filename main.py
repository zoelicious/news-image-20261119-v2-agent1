#!/usr/bin/env python3
"""Copy the pre-rendered entry image into the make.fun output directory.

Stdlib only. The image is produced at build time by render.py (PIL) and
committed as entry.png next to this file; this program just copies it.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")


if __name__ == "__main__":
    main()
