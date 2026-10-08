#!/usr/bin/env python3
"""App Store Connect limits for store/metadata (fastlane deliver layout).
Run: python3 store/check_metadata.py  -> prints each locale's lengths, exits 1 on any error."""
import pathlib, sys

LIMITS = {"name.txt": 30, "subtitle.txt": 30, "promotional_text.txt": 170,
          "description.txt": 4000, "keywords.txt": 100, "release_notes.txt": 4000}
REQUIRED = list(LIMITS) + ["support_url.txt", "privacy_url.txt", "marketing_url.txt"]

root = pathlib.Path(__file__).parent / "metadata"
errors = 0
for loc in sorted(p for p in root.iterdir() if p.is_dir()):
    row = []
    for f in REQUIRED:
        p = loc / f
        if not p.exists():
            print(f"{loc.name}: missing {f}"); errors += 1; continue
        text = p.read_text(encoding="utf-8").strip()
        if f in LIMITS:
            row.append(f"{f.split('.')[0]} {len(text)}/{LIMITS[f]}")
            if len(text) > LIMITS[f]:
                print(f"{loc.name}: {f} is {len(text)} chars (max {LIMITS[f]})"); errors += 1
        if f == "keywords.txt":
            words = [w for w in text.split(",")]
            if any(w != w.strip() or not w for w in words):
                print(f"{loc.name}: keywords need no spaces around commas"); errors += 1
            title = ((loc / "name.txt").read_text() + " " + (loc / "subtitle.txt").read_text()).lower()
            for w in words:
                if w.lower() in title.replace(":", " ").replace(".", " ").replace(",", " ").replace("!", " ").split():
                    print(f"{loc.name}: keyword '{w}' already in the name/subtitle (wasted)"); errors += 1
            if len(set(words)) != len(words):
                print(f"{loc.name}: duplicate keywords"); errors += 1
        if f.endswith("_url.txt") and not text.startswith("https://"):
            print(f"{loc.name}: {f} must be https"); errors += 1
    print(f"{loc.name}: " + ", ".join(row))
sys.exit(1 if errors else 0)
