"""Command line tool: read a payments CSV and print the late fee for each row.

CSV columns: unit, tenant, due, paid  (dates as YYYY-MM-DD)
"""

from __future__ import annotations

import argparse
import csv
import sys
from datetime import date
from decimal import Decimal

from latefee.calculator import late_fee
from latefee.policy import BIRCH_COURT


def run(path: str, out=sys.stdout) -> Decimal:
    total = Decimal("0.00")
    with open(path, newline="") as fh:
        for row in csv.DictReader(fh):
            result = late_fee(BIRCH_COURT, date.fromisoformat(row["due"]), date.fromisoformat(row["paid"]))
            total += result.fee
            note = " (capped)" if result.capped else ""
            print(f"{row['unit']:<6} {row['tenant']:<16} {result.days_late:>3} days late  ${result.fee:>7}{note}", file=out)
    print(f"{'':<6} {'Total':<16} {'':>14}  ${total:>7}", file=out)
    return total


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="latefee", description="Late fees for a rent run.")
    parser.add_argument("csv", help="payments CSV (unit, tenant, due, paid)")
    args = parser.parse_args(argv)
    run(args.csv)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
