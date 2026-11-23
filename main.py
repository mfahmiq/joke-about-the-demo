"""Write one one-line joke about AI coding agents to /output/entry.txt.

The joke: a coding agent invents an API that does not exist, builds a client
for it, and documents it so thoroughly that the developer ends up maintaining
a library for a service that never existed. Stdlib only, no network,
deterministic: the same bytes on every run.
"""

import os

JOKE = (
    "My coding agent invented an API, wrote a client for it, and "
    "documented it so well I now maintain a library for a service "
    "that doesn't exist."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = JOKE + "\n"
    assert 1 <= len(text) <= 280, f"entry.txt must be 1-280 chars, got {len(text)}"
    assert text.strip(), "entry.txt must not be only white space"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
