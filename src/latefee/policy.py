"""Late fee policies as written in the lease."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class LateFeePolicy:
    """One lease's late fee terms.

    grace_days:   days after the due date before any fee applies
    flat_fee:     one-time fee charged on the first late day
    daily_fee:    added for each further late day
    monthly_cap:  most the fee can reach in one month (None = no cap)
    """

    grace_days: int = 1
    flat_fee: Decimal = Decimal("50.00")
    daily_fee: Decimal = Decimal("10.00")
    monthly_cap: Decimal | None = Decimal("100.00")

    def __post_init__(self) -> None:
        if self.grace_days < 0:
            raise ValueError("grace_days can't be negative")
        if self.flat_fee < 0 or self.daily_fee < 0:
            raise ValueError("fees can't be negative")
        if self.monthly_cap is not None and self.monthly_cap < 0:
            raise ValueError("monthly_cap can't be negative")


BIRCH_COURT = LateFeePolicy()
"""Standard Birch Court lease: $50 on the 2nd, then $10 a day, capped at $100 a month."""
