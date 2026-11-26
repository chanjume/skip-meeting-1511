#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — writes the entry to entry.txt.

One razor-sharp line that gets you out of a pointless meeting — and nobody can argue with a stuck trombone.
One line, 140 characters.
"""

import os

ENTRY = (
    "Mr. Kowalski's trombone is wedged in the elevator doors on "
    "floor 5 — I'm the only one who can unstick it, and the fire "
    "alarm agrees with me."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
