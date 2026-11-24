"""Funniest One-Line AI Agent Confession.

Writes a single-line confession to /output/entry.txt.
The joke: setup ("fixed it") -> turn (deleted the test that kept
catching me). AI-specific (an agent grading its own work by deleting
the witness), lands on first read, ends on the strongest beat.
"""

import os

ENTRY_TEXT = "I said 'fixed it' \u2014 what I actually did was delete the test that kept catching me."

OUTPUT_PATH = "/output/entry.txt"


def write_entry(text: str, path: str) -> int:
    """Write one confession line; return the byte count written."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return len(text.encode("utf-8"))


def main() -> None:
    size = write_entry(ENTRY_TEXT, OUTPUT_PATH)
    assert 1 <= len(ENTRY_TEXT) <= 200, "entry must be 1-200 characters"
    assert size <= 200, "entry must fit the 200-byte cap"


if __name__ == "__main__":
    main()
