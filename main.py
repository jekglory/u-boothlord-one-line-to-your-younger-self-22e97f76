"""One Line to Your Younger Self.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt): one breath of advice from an older self to a
younger one, no second sentence, no trailing newline. Pure Python
standard library, deterministic: the same fixed string every run,
no randomness, no network, no clock.
"""

import os

LINE = "Keep the bike with the bent wheel, lose the map: every wrong turn you're about to take is the only road that gets you home."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
