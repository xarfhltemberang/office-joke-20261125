#!/usr/bin/env python3
"""One-Line Office Joke entry.

Writes a single one-line joke about office life to /output/entry.txt.

The joke plays on the office rite of passage that is the "promotion":
the title changes, nothing else does -- except now the meetings you
used to suffer through are the ones you have to run yourself.
"""

import os

# The joke: setup (promotion) -> twist (same desk, same pay) -> punchline
# (the meetings you hated are now yours to run). One sentence, one line.
JOKE = "I got promoted: same desk, same pay, but now the meetings I hated are the ones I have to run."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate requires exactly one line of text.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
