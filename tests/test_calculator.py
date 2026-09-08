import unittest
from datetime import date
from decimal import Decimal

from latefee import LateFeePolicy, late_fee
from latefee.policy import BIRCH_COURT

DUE = date(2026, 9, 1)


class LateFeeTest(unittest.TestCase):
    def test_paid_on_due_date_is_free(self):
        self.assertEqual(late_fee(BIRCH_COURT, DUE, DUE).fee, Decimal("0.00"))

    def test_first_late_day_is_flat_fee(self):
        self.assertEqual(late_fee(BIRCH_COURT, DUE, date(2026, 9, 2)).fee, Decimal("50.00"))

    def test_daily_fee_adds_up(self):
        self.assertEqual(late_fee(BIRCH_COURT, DUE, date(2026, 9, 4)).fee, Decimal("70.00"))

    def test_fee_is_capped(self):
        result = late_fee(BIRCH_COURT, DUE, date(2026, 9, 20))
        self.assertEqual(result.fee, Decimal("100.00"))
        self.assertTrue(result.capped)

    def test_grace_period_pushes_the_start(self):
        policy = LateFeePolicy(grace_days=5)
        self.assertEqual(late_fee(policy, DUE, date(2026, 9, 5)).fee, Decimal("0.00"))
        self.assertEqual(late_fee(policy, DUE, date(2026, 9, 6)).fee, Decimal("50.00"))

    def test_no_cap(self):
        policy = LateFeePolicy(monthly_cap=None)
        self.assertEqual(late_fee(policy, DUE, date(2026, 9, 20)).fee, Decimal("230.00"))


if __name__ == "__main__":
    unittest.main()
