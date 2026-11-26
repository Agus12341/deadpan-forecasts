"""Deadpan forecast for the city of Brindlewick, which does not exist."""

import os

TEXT = (
    "Cloudy in Brindlewick tonight with a high of 17, light winds, "
    "and one cloud that has been following the postman since Tuesday. "
    "It seems personal."
)


def write_entry(path, text):
    """Write the forecast text, refusing anything outside the 160-char gate."""
    if not (1 <= len(text) <= 160) or not text.strip():
        raise ValueError("entry text fails the 1-160 character gate")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry("/output/entry.txt", TEXT)


if __name__ == "__main__":
    main()
