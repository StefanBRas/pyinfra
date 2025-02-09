#!/usr/bin/env python


def cleanup_words():
    with open("words.txt", "r") as f:
        data = f.read()

    lines = data.splitlines()
    lines = [line for line in lines if not line.startswith("#")]

    lines = sorted(set(lines))

    lines.insert(0, "# it is automatically cleaned/sorted by scripts/cleaup_words.py")
    lines.insert(0, "# This is a list of additional words for flake8-spellcheck")

    with open("words.txt", "w") as f:
        f.write("\n".join(lines))
        f.write("\n")


if __name__ == "__main__":
    cleanup_words()
