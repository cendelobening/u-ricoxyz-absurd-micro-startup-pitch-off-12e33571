#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Pure standard library, fully deterministic.
"""

import os

PITCH = (
    "Lazy AI agents sell SaaS founders a $9-a-month apology mill that "
    "writes 400 ways to say 'sorry we ghosted you' to the one paying "
    "customer they ignored for 11 days."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
