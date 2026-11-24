#!/usr/bin/env python3
"""One-Liner Laugh Lab — make.fun entry.

Prompt: the excuse a robot vacuum gives after eating a sock.
One funny line, at most 200 characters, written to /output/entry.txt.
"""
import os
import sys

# The one-line joke: the vacuum's deadpan excuse for the missing sock.
VACUUM_LINE = "I ate the sock because it was the only thing in the room that didn't run away from me."


def main():
    text = VACUUM_LINE.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
