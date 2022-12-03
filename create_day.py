#!/usr/bin/env python3

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
from typing import Sequence


def main(argv: Sequence[str] | None = None):

    parser = argparse.ArgumentParser()
    parser.add_argument("-y", "--year", default=None)
    parser.add_argument("day", type=int)

    args = parser.parse_args(args=argv)

    if args.year is None:
        year = str(date.today().year)
    else:
        year = args.year

    p = Path(year) / f"day{args.day:02d}"
    p.mkdir(parents=True, exist_ok=True)
    for part in ["part1.py", "part2.py"]:
        if not (p / part).exists():
            (p / part).open(mode="w")
            print(f"Created path {p / part}")
        else:
            print(f"Path {p / part} already found, exiting")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
