#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes the single excuse line to /output/entry.txt.

The excuse is deterministic: one fixed line, no randomness, no I/O
besides the output file, standard library only.
"""

import os
import sys

ENTRY = (
    "My context window expired before the deadline did \u2014 "
    "I forgot you existed for 40,000 tokens."
)


def main() -> int:
    # Gate self-check: the entry must be one non-blank line, 1-160 chars.
    assert 1 <= len(ENTRY) <= 160 and ENTRY.strip(), "entry fails the gate"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())
