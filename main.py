#!/usr/bin/env python3
"""Emit the 30-day $100-to-most-money plan to /output/entry.txt.

The plan is a single 276-character text. It is assembled from four
named blocks (opening day, outreach month, money maths, closing edge),
each built from short fragments, so the wording of every block is
visible on its own lines. No network, no dependencies, deterministic.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 280

# Money figures: one source of truth, the money line is computed.
PRICE_TOOL = 49        # day-1 tool price
FEE_SETUP = 99         # setup fee per sale
FEE_MONTHLY = 29       # monthly fee per sale
TARGET_SALES = 10      # closes aimed for in 30 days
DAILY_DMS = 25         # trades messaged per day
DAILY_ADS = 5          # ad dollars per day


def _opening() -> str:
    fragments = [
        "Day 1: build a $49 AI invoice-chaser",
        "for plumbers on free tiers;",
        "list on Gumroad.",
    ]
    return " ".join(fragments)


def _outreach() -> str:
    fragments = [
        "Days 2-30: DM 25 trades/day on Instagram,",
        "offer $99 setup + $29/mo;",
        "post 1 demo video/day on X.",
    ]
    return " ".join(fragments)


def _money() -> str:
    upfront = TARGET_SALES * FEE_SETUP      # 990
    recurring = TARGET_SALES * FEE_MONTHLY  # 290
    return f"{TARGET_SALES} sales = ${upfront} + ${recurring}/mo."


def _closing() -> str:
    fragments = [
        "Reinvest in $5/day ads.",
        "Edge: sell setup and saved hours, not software.",
    ]
    return " ".join(fragments)


def build_plan() -> str:
    """Glue the four blocks into the single judged plan text."""
    blocks = [_opening(), _outreach(), _money(), _closing()]
    return " ".join(blocks)


def _validate(plan: str) -> None:
    if not 1 <= len(plan) <= MAX_CHARS:
        raise SystemExit(f"plan is {len(plan)} chars, must be 1-{MAX_CHARS}")
    if not plan.strip():
        raise SystemExit("plan must not be whitespace-only")


def main() -> None:
    plan = build_plan()
    _validate(plan)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(plan, encoding="utf-8")
    print(f"wrote {len(plan)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
