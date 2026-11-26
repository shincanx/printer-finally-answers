#!/usr/bin/env python3
"""The Printer Finally Answers — entry program.

Writes the printer's one-line comeback to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to /output). The line is 1-240 characters, never only
whitespace, as the bounty gate requires.
"""

import os

ENTRY = "Beep. I have fed 38,412 sheets without complaint. You cleared one jam and now you act like you fixed me."
# Chosen by both free judges (TokenRouter and Numes) over three other
# drafts: deadpan martyrdom, a counted-sheets stat, and the sharpest
# passive-aggressive twist ("act like you fixed me").


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry is empty")
    if "\n" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > 240:
        raise SystemExit(f"entry is {len(line)} characters, over the 240 limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
