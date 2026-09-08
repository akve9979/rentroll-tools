"""Work out the late fee for a single rent payment."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from latefee.policy import LateFeePolicy


@dataclass(frozen=True)
class FeeResult:
    days_late: int
    fee: Decimal
    capped: bool


def late_fee(policy: LateFeePolicy, due: date, paid: date) -> FeeResult:
    """Return the late fee for rent due on `due` and paid on `paid`."""
    days_late = (paid - due).days - policy.grace_days + 1
    if days_late <= 0:
        return FeeResult(days_late=0, fee=Decimal("0.00"), capped=False)

    fee = policy.flat_fee + policy.daily_fee * (days_late - 1)
    capped = policy.monthly_cap is not None and fee > policy.monthly_cap
    if capped:
        fee = policy.monthly_cap
    return FeeResult(days_late=days_late, fee=fee.quantize(Decimal("0.01")), capped=capped)
