#!/usr/bin/env python3

"""Generate static pages from .py files"""

from __future__ import annotations

import shutil
from collections import defaultdict
from pathlib import Path
from typing import Optional, Sequence

from jinja2 import Environment, FileSystemLoader, select_autoescape
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer

env = Environment(loader=FileSystemLoader("site-src/templates"), autoescape=False)
day_template = env.get_template("day.j2.html")
index_template = env.get_template("index.j2.html")

OUTPUT_DIR = "site-dist/"


def main(argv: Optional[Sequence[str]] = None) -> int:

    # generate the pygments html
    pygments_css = HtmlFormatter().get_style_defs(".highlight")
    with open("site-dist/pygments.css", "w") as fh:
        fh.write(pygments_css)

    days = defaultdict(list)
    for year in sorted(Path("./").glob("20*")):
        year_str = str(year)
        for day_path in sorted(Path(year).glob("**/*.py")):
            day_num = day_path.parts[-2].strip("day")

            # store the day/part strings for index.html
            days[(year_str, day_num)].append(day_path.stem)

            # load the code
            code = day_path.read_text()

            formatted_code = highlight(code, PythonLexer(), HtmlFormatter())

            # render the template
            html_output = day_template.render(
                {
                    "year": year_str,
                    "part": day_path.stem,
                    "day_num": day_num,
                    "day_code": formatted_code,
                    "code_str": code,
                }
            )

            # save the output
            outpath = Path(
                f"{OUTPUT_DIR}/{year_str}/{day_path.parts[-2]}/{day_path.stem}.html"
            )
            outpath.parents[0].mkdir(parents=True, exist_ok=True)
            with open(outpath, "w") as fh:
                fh.write(html_output)

        for data_path in sorted(Path(year).glob("**/*.txt")):
            # copy the data.txt into the dist path
            shutil.copy(
                data_path,
                Path(f"{OUTPUT_DIR}/{year_str}/{data_path.parts[-2]}/{data_path.name}"),
            )

            data_path

    # create index.html
    index_html = index_template.render({"days": days})
    with open(f"{OUTPUT_DIR}/index.html", "w") as fh:
        fh.write(index_html)

    return 0


if __name__ == "__main__":
    exit(main())
