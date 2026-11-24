"""Two-Sentence Horror entry for make.fun.

Writes one original two-sentence horror story to /output/entry.txt.
Deterministic: the story text is a fixed constant, so every run
produces byte-identical output.
"""

import os

STORY = (
    "Every evening, my neighbour's dog barks at my front door for exactly "
    "one minute, then stops, and I have always assumed it smells the cat. "
    "Tonight it barked for two minutes \u2014 because, for the first time, "
    "something on the other side of the door barked back."
)


def validate(text: str) -> None:
    """Check the entry meets the competition gate before writing it."""
    if not (1 <= len(text) <= 400):
        raise ValueError(f"entry must be 1-400 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    # Exactly two sentences: split on sentence-ending punctuation and
    # count the non-empty fragments.
    fragments = [
        part.strip()
        for part in text.replace("?", ".").replace("!", ".").split(".")
        if part.strip()
    ]
    if len(fragments) != 2:
        raise ValueError(f"entry must be exactly two sentences, got {len(fragments)}")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    text = STORY
    validate(text)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
