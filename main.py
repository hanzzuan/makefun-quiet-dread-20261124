"""Two Days of Quiet Dread — entry program.

Writes one code review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread. Deterministic: the same line on every run.
"""

import os

ENTRY = "Approved. The tests pass, the linter is happy, and the void remains unconvinced."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry must be 1-140 characters, got {len(ENTRY)}")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
