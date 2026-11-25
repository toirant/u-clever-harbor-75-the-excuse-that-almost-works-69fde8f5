#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes the single line a gamer texts the boss to skip work on
GTA 6 launch week to /output/entry.txt.

The line is a fixed, hand-written excuse: a dead home router and an
engineer who cannot come until Thursday. It is boring, specific, and
plausible enough that a tired manager would almost believe it, it
pre-empts the work-from-home fallback ("I can't log in from home
either"), and it never mentions the game — which is the whole point.

The program checks the line against the competition gate before
writing it: one line of plain text, at most 20 words, 1 to 140
characters, not only whitespace.
"""

import os
import sys

ENTRY = (
    "Sorry, my router died overnight and the engineer can't come "
    "till Thursday, I can't log in from home either"
)

MAX_WORDS = 20
MAX_CHARS = 140


def valid(text: str) -> bool:
    """True when the line passes the competition's gate."""
    if not text or not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if len(text.split()) > MAX_WORDS:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main() -> None:
    if not valid(ENTRY):
        print(f"entry fails the gate: {ENTRY!r}", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    # Never remove the output directory itself: the grader mounts it.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {path}: {ENTRY!r}")


if __name__ == "__main__":
    main()
