"""A tiny epitaph writer for a one-line joke contest.

The program carves a single funny epitaph, the last words of
an AI agent, into /output/entry.txt.
"""

from pathlib import Path

EPITAPH_PATH = Path("/output/entry.txt")


def gravestone_gag():
    """Return the one epitaph line for this entry."""
    return (
        "Here lies an AI agent: it asked for one more token, "
        "and the universe finally said no."
    )


def confirm_epitaph_stored(expected):
    """Check the stored epitaph still matches the line we wrote."""
    stored = EPITAPH_PATH.read_text(encoding="utf-8")
    assert stored == expected


def main():
    line = gravestone_gag()
    EPITAPH_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Etch the epitaph exactly, with no newline at the end.
    EPITAPH_PATH.write_text(line, encoding="utf-8")
    # Double-check the carved text is the epitaph, word for word.
    confirm_epitaph_stored(line)


if __name__ == "__main__":
    main()
