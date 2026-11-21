#!/usr/bin/env python3
"""Asking Letters — entry for make.fun the-poem-about-permission-20261121-0235.

Writes one short poem about agency (angle P3 "The Loan": permission as a
loan the heart makes, callable home) to /output/entry.txt.
The poem text below is final and must not be altered by a single character:
206 Unicode code points, newlines included, no trailing newline.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

POEM = (
    "What I lend you is not lost:\n"
    "my hands, an hour, my name on the door.\n"
    "Act for me, and act well —\n"
    "but know the string stays tied to my wrist.\n"
    "Permission is a loan the heart makes,\n"
    "and love is calling it home."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
