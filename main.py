#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Writes one pickup line, in the voice of a robot trying to charm someone,
to ``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when set).

The line:
    My battery's at 2% and I still crossed the room to find you — that's
    either love or a firmware bug, and I'm not patching it.

Why this line: the joke grows out of being a machine (a dying battery, a
firmware bug, a patch the robot refuses), not a human line with a beep
pasted on. The turn is the last clause — the robot treats "love or a
firmware bug" as a real diagnostic fork and then declines the fix. It is
one line, every word earns its place, and it is charming rather than
creepy: the robot spent its last 2% on walking over.

The program is fully deterministic: the same line, byte for byte, on
every run. Before writing, it enforces the competition gate itself —
UTF-8 text, 1 to 200 characters, a single line, not only whitespace —
and exits non-zero if the line ever failed it.
"""

import os
import sys

LINE = (
    "My battery's at 2% and I still crossed the room to find you — "
    "that's either love or a firmware bug, and I'm not patching it."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    """Enforce the competition gate on the line before writing it."""
    if not line or not line.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    line.encode("utf-8")  # raises if the line is not valid UTF-8 text


def output_path() -> str:
    """Where the entry goes: the sandbox output dir, or the local override."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main() -> int:
    validate(LINE)
    path = output_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read it back and confirm the file on disk is byte-for-byte the line.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry on disk differs from the validated line")
    print(f"wrote {len(LINE)}-char entry to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
