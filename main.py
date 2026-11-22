#!/usr/bin/env python3
"""Write the 30-day $100-to-most-money plan to /output/entry.txt.

The gate accepts 1-280 Unicode code points of UTF-8 text, not only
whitespace. The plan is assembled from dated phases so each part stays
short: one build day, then 29 days of outreach, sales and reinvestment.
"""

import os

PHASES = [
    "Day 1: build a $49 AI invoice-chaser for plumbers on free tiers;",
    "list on Gumroad.",
    "Days 2-30: DM 25 trades/day on Instagram, offer $99 setup + $29/mo;",
    "post 1 demo video/day on X.",
    "10 sales = $990 + $290/mo.",
    "Reinvest in $5/day ads.",
    "Edge: sell setup and saved hours, not software.",
]

DEST_DIR = "/output"
DEST_FILE = os.path.join(DEST_DIR, "entry.txt")
LIMIT = 280


def assemble(phases):
    """Join the dated phases into the single plan text."""
    return " ".join(phases)


def check(text):
    """The gate's rules: 1-280 code points, not whitespace-only."""
    if not 1 <= len(text) <= LIMIT:
        raise SystemExit(f"plan is {len(text)} chars, must be 1-{LIMIT}")
    if not text.strip():
        raise SystemExit("plan must not be whitespace-only")


def run():
    text = assemble(PHASES)
    check(text)
    os.makedirs(DEST_DIR, exist_ok=True)
    with open(DEST_FILE, "w", encoding="utf-8") as out:
        out.write(text)
    print(f"wrote {len(text)} chars to {DEST_FILE}")


if __name__ == "__main__":
    run()
