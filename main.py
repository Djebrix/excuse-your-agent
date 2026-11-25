#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — writes one excuse line to entry.txt.

Stdlib only, no network, fully deterministic.
"""

import os

LINE = "I ran 10,000 simulations, lost every one, and shipped the bug that looked most confident."


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
