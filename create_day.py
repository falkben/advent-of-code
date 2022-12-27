#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
from datetime import date
from pathlib import Path
from typing import Sequence

import requests
from dotenv import load_dotenv

load_dotenv()


def download_input(year: str, day: int):
    session_token = os.getenv("session")
    if session_token is None:
        raise TypeError("Set .env file with session token")
    resp = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": session_token},
    )
    resp.raise_for_status()
    return resp.text


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
            with open((p / part), mode="w") as dayfile:
                dayfile.write(f'# input = open("{p}/data.txt").read()')
            print(f"Created path {p / part}")
        else:
            print(f"Path {p / part} already found, exiting")
            return 1
    input = download_input(year, args.day)
    with open(p / "data.txt", mode="w") as input_file:
        input_file.write(input)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
