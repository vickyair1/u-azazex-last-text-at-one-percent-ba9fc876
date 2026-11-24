#!/usr/bin/env python3
"""Last Text at One Percent — u-azazex-last-text-at-one-percent-ba9fc876.

Writes the dying phone's final text message to /output/entry.txt.
Stdlib only, deterministic: the same line every run, no trailing newline.
"""

import os

# Final wording (revised from draft: dropped "just" — a wasted word).
LINE = "I've been at 1% since lunch. I wanted to see how long you'd ignore me. Six hours. Goodbye \u2014 enjoy your brick."


def main() -> None:
    text = LINE
    # Gate checks: 1-199 chars, single line, UTF-8, not only whitespace.
    assert 1 <= len(text) <= 199, f"length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    assert text == text.strip(), "no leading/trailing whitespace"
    text.encode("utf-8")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)  # no trailing newline

    print(f"wrote {len(text)} chars to /output/entry.txt: {text}")


if __name__ == "__main__":
    main()
