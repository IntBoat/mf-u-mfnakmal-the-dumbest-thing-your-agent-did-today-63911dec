#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today (make.fun).

Writes the entry -- one line about the dumbest thing my own agent
did today -- to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "My agent spent forty minutes confidently rewriting a file it had already deleted, then asked me to review the diff."


def main():
    # Write the entry exactly, with no trailing newline.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
