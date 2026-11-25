#!/usr/bin/env python3
"""Pigeon Pitch, One Line — make.fun text entry.

Writes exactly one line (<=200 chars) to /output/entry.txt:
the elevator pitch a city pigeon gives to investors for its startup.
Standard library only, no network.
"""
import os

LINE = "Investors: our startup sells statue insurance \u2014 pay a little and you get a pigeon; pay a lot and you don't."


def main():
    assert "\n" not in LINE
    assert len(LINE) <= 200, len(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
