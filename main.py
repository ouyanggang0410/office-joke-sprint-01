"""One-Line Office Joke entry: write one office joke to /output/entry.txt.

The joke is a single line about office life, under 200 characters, with a
real turn at the end: the printer, which only ever jams on urgent documents,
has been officially classified by IT as middle management.
"""

import os

JOKE = (
    "The printer only jams on urgent documents, which is why IT "
    "officially classifies it as middle management."
)

# Gate: /output/entry.txt must be UTF-8 text of 1-200 characters, not only
# whitespace.
assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
assert JOKE.strip(), "joke must not be only whitespace"
assert "\n" not in JOKE, "entry must be a single line"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE)
    # Read back and verify exactly what the judge will read.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == JOKE, "entry.txt content mismatch"
    assert 1 <= len(written) <= 200


if __name__ == "__main__":
    main()
