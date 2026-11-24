#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry (program/v1).

Writes one line — the funniest thing an AI agent would say in its
weekly status report to its human — to /output/entry.txt.

Deterministic by design: the text is fixed, there is no clock, no
randomness, no network and no input, so two runs write byte-identical
output. The gate requires UTF-8 text of 1 to 200 characters, not only
white space; the line below is checked against that before writing.
"""

import os

ENTRY = (
    "Status: I followed your instructions exactly. "
    "That is why the production database is on fire. "
    "Awaiting new instructions."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1 to 200 characters")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
