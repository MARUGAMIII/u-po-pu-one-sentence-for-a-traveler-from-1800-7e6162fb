"""One Sentence for a Traveler from 1800.

Writes a single sentence explaining the modern internet to someone
arriving from the year 1800, using only words and pictures from their
own world: roads, houses, letters, doors, libraries, tables.

Pure Python standard library, deterministic, no network access, and it
reads no file outside this repository. The sentence is a constant
embedded below; the program only writes it to /output/entry.txt.
"""

import os
import re

ENTRY = (
    "Imagine a road joining every house on earth, carrying your letters "
    "to any door in a breath and laying a thousand libraries open upon "
    "your table."
)

# Words coined after 1800 that the entry must never use.
MODERN_WORDS = {
    "internet", "wifi", "wi-fi", "smartphone", "email", "e-mail",
    "website", "digital", "online", "computer", "phone", "network",
    "screen", "app", "data", "cloud", "server", "software", "web",
    "modem", "router", "browser", "download", "upload", "video",
    "television", "radio", "electric", "electricity",
}

OUTPUT_PATH = "/output/entry.txt"


def validate(entry: str) -> None:
    """Check the entry against the competition gate and the judge brief."""
    if not 1 <= len(entry) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(entry)}")
    entry.encode("ascii")  # no em dash or other non-ASCII
    if entry.strip() != entry or not entry.strip():
        raise ValueError("entry must not be blank or padded with whitespace")
    if len(re.findall(r"[.!?]", entry)) != 1 or not entry.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    words = set(re.findall(r"[a-z]+", entry.lower()))
    banned = words & MODERN_WORDS
    if banned:
        raise ValueError(f"entry uses modern words: {sorted(banned)}")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="ascii", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
