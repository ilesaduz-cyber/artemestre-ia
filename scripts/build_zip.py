#!/usr/bin/env python3
"""Build dist/artemestre-ia.zip with only the skill folder, for Claude.ai and
other Skills UIs that import a ZIP.

Usage: python scripts/build_zip.py
"""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'artemestre-ia'
OUT = ROOT / 'dist' / 'artemestre-ia.zip'

OUT.parent.mkdir(exist_ok=True)
files = sorted(p for p in SKILL.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in files:
        z.write(p, p.relative_to(ROOT).as_posix())
print(f'{OUT.relative_to(ROOT).as_posix()}: {len(files)} files, {OUT.stat().st_size} bytes')
