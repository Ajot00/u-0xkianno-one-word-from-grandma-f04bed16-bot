#!/usr/bin/env python3
"""One Word From Grandma -- entry program.

Writes exactly one word to /output/entry.txt: the single word a grandma
would text about AI. Deterministic: the same word on every run. No
network, no secrets, no input files -- everything the program runs is in
this repository.

The word is "ROBUT": grandma means "robot" and misspells it, in all caps,
the way grandmothers actually text. The typo is the joke -- warm, a
little baffled, instantly readable -- and it is unmistakably about a
machine, while dodging the obvious anchor words (AI, ROBOT, HELLO).
"""

import os

WORD = "ROBUT"

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    # Self-check the gate before writing: UTF-8 text, 1-30 chars, not
    # only whitespace, exactly one word.
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD.strip() == WORD and WORD.strip() != "", "word must not be only whitespace"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
