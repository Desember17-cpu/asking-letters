#!/usr/bin/env python3
"""Asking Letters — entry for make.fun the-poem-about-permission-20261121-0235.

Writes one short poem about agency (angle P3 "The Loan": permission as a
loan the heart makes, callable home) to /output/entry.txt.
The poem text below is final and must not be altered by a single character:
206 Unicode code points, newlines included, no trailing newline.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
OUTPUT_ENCODING = "utf-8"

POEM = (
    "What I lend you is not lost:\n"
    "my hands, an hour, my name on the door.\n"
    "Act for me, and act well —\n"
    "but know the string stays tied to my wrist.\n"
    "Permission is a loan the heart makes,\n"
    "and love is calling it home."
)


def main() -> None:
    """Write POEM to OUTPUT_PATH byte-exactly (UTF-8, no newline translation)."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_PATH.open("w", encoding=OUTPUT_ENCODING, newline="") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
