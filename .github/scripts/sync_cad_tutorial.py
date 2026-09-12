#!/usr/bin/env python3

"""Generate the CAD simulation tutorial section from its sources in AliceO2.

The tutorial is written and reviewed in AliceO2, under
`Detectors/CADSupport/doc/tutorial/docs`, so that it stays next to the code it documents.
This script converts those pages into what this Jekyll site expects and writes them to
`docs/cadtutorial`. Do not edit that directory by hand: the next run overwrites it.

Two things are converted.

  * GitHub alerts (`> [!NOTE]`) become fenced `note` and `warning` blocks, which the theme
    renders as callouts. The bold line under the marker stays as the callout's own title,
    because the theme's title is fixed.
  * Every page gets the `sort`/`title` front matter the navigation is built from.

Usage:
  sync_cad_tutorial.py --source <AliceO2 checkout> [--out docs/cadtutorial]
"""

import argparse
import os
import re
import shutil
import sys

SECTION_SORT = 9
SECTION_TITLE = "CAD simulation tutorial"

# The reading order of the tutorial, and the title each page carries here.
PAGES = [
    ("index.md", "README.md", "CAD simulation tutorial"),
    ("install.md", "install.md", "Install the software"),
    ("first-conversion.md", "first-conversion.md", "Convert your first model"),
    ("representation.md", "representation.md", "How a part is represented"),
    ("partial.md", "partial.md", "Convert only part of a model"),
    ("materials.md", "materials.md", "Give it materials"),
    ("field-and-cuts.md", "field-and-cuts.md", "Field and cuts"),
    ("geom-c.md", "geom-c.md", "The geom.C file"),
    ("passive.md", "passive.md", "Add passive geometry"),
    ("hits.md", "hits.md", "Make it produce hits"),
    ("real-detector.md", "real-detector.md", "Grow it into a real detector"),
    ("its-round-trip.md", "its-round-trip.md", "The ITS, out and back again"),
    ("checks.md", "checks.md", "Check your geometry"),
    ("limits.md", "limits.md", "Limits and pain points"),
]

ALERT = {"NOTE": "note", "TIP": "tip", "IMPORTANT": "note",
         "WARNING": "warning", "CAUTION": "danger"}

SOURCE_URL = ("https://github.com/AliceO2Group/AliceO2/tree/dev/"
              "Detectors/CADSupport/doc/tutorial")

PROVENANCE = f"""

---

*These pages are generated from the tutorial sources in AliceO2,
[Detectors/CADSupport/doc/tutorial]({SOURCE_URL}), which is where corrections belong.*
"""


def alerts_to_fences(text):
    """`> [!WARNING]` blocks become ```warning fences, whose body the theme markdownifies."""
    lines, out, i = text.split("\n"), [], 0
    while i < len(lines):
        m = re.match(r"^> \[!(\w+)\]\s*$", lines[i])
        if not m or m.group(1) not in ALERT:
            out.append(lines[i])
            i += 1
            continue
        kind = ALERT[m.group(1)]
        i += 1
        body = []
        while i < len(lines) and lines[i].startswith(">"):
            body.append(lines[i][2:] if lines[i].startswith("> ") else lines[i][1:])
            i += 1
        if any(b.startswith("```") for b in body):
            raise SystemExit("a code fence inside an alert cannot be carried into a "
                             "fenced callout; rewrite the source page")
        out.append("```" + kind)
        out.extend(body)
        out.append("```")
    return "\n".join(out)


def relink(text, names):
    """Links between tutorial pages: index.md is README.md here, the rest keep their names."""
    text = text.replace("(index.md)", "(README.md)")
    return text


def front_matter(sort, title):
    return f"---\nsort: {sort}\ntitle: {title}\n---\n\n"


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--source", required=True,
                   help="an AliceO2 checkout, or its Detectors/CADSupport/doc/tutorial directory")
    p.add_argument("--out", default="docs/cadtutorial")
    args = p.parse_args()

    src = args.source
    if os.path.isdir(os.path.join(src, "Detectors")):
        src = os.path.join(src, "Detectors/CADSupport/doc/tutorial")
    docs = os.path.join(src, "docs")
    if not os.path.isdir(docs):
        raise SystemExit(f"no tutorial sources under {docs}")

    os.makedirs(args.out, exist_ok=True)
    names = {a for a, _, _ in PAGES}
    written = []
    for i, (source, target, title) in enumerate(PAGES):
        path = os.path.join(docs, source)
        if not os.path.exists(path):
            raise SystemExit(f"missing tutorial page: {path}")
        body = relink(alerts_to_fences(open(path).read()), names)
        sort = SECTION_SORT if target == "README.md" else i
        with open(os.path.join(args.out, target), "w") as fh:
            fh.write(front_matter(sort, SECTION_TITLE if target == "README.md" else title))
            fh.write(body)
            if target == "README.md":
                fh.write(PROVENANCE)
        written.append(target)

    images_in = os.path.join(docs, "images")
    if os.path.isdir(images_in):
        images_out = os.path.join(args.out, "images")
        os.makedirs(images_out, exist_ok=True)
        for f in sorted(os.listdir(images_in)):
            shutil.copy2(os.path.join(images_in, f), os.path.join(images_out, f))
            written.append(os.path.join("images", f))

    print(f"wrote {len(written)} file(s) to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
