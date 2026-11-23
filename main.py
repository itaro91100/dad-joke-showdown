#!/usr/bin/env python3
"""Dad Joke Showdown entry — one original dad joke, at most 200 characters.

The whole entry is a single dad joke: a straight-faced setup, a groan-worthy
pun, and a delivery that lands exactly like a dad telling it at the dinner
table.
"""

import os

JOKE = "I told my plants a joke about photosynthesis. They didn't laugh \u2014 they just stood there, soaking it in."


def main() -> None:
    """Write exactly the joke text to /output/entry.txt.

    No trailing newline, no extra text — the file holds the joke and
    nothing else, so the judge reads the joke exactly as written.
    """
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
