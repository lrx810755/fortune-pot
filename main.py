"""make.fun entry: Fortune in a Pot.

Writes a one-line fortune for a houseplant to entry.txt.
"""

import os
from pathlib import Path

# One line, 119 characters, within the 120 character limit.
LINE = "Soon a sunbeam will find your leaves, and you will stretch toward it like a small green victory. Grow tall, little one."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
