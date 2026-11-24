"""The Funniest Sick-Day Excuse — make.fun bounty entry.

Writes a single line (under 200 characters) to /output/entry.txt:
a sick-day excuse that is half believable, fresh, and lands its
twist on the last word. Deterministic, standard library only.
"""

import os

EXCUSE = (
    "Won't be in today — I sneezed, my back went out, and now I'm "
    "lying on the floor renegotiating my relationship with gravity."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip() == text, "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
