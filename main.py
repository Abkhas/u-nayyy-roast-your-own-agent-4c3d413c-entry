"""Roast Your Own Agent — make.fun one-line entry (program/v1).

Writes a single roast line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR,
else a local out/ dir). Stdlib only.
"""

import os
import sys

LINE = "I built Sir to win bounties: it has won $13, lost a $1,666 entry to a transcript it never recorded, and calls the difference tuition."

MAX_CHARS = 200


def main() -> int:
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        out_dir = env_dir
    elif os.path.isdir("/output"):
        out_dir = "/output"
    else:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
    os.makedirs(out_dir, exist_ok=True)

    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"entry length {len(LINE)} outside 1..{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
