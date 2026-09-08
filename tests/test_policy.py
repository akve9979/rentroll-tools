import unittest
from decimal import Decimal

from latefee import LateFeePolicy


class PolicyTest(unittest.TestCase):
    def test_negative_grace_days_rejected(self):
        with self.assertRaises(ValueError):
            LateFeePolicy(grace_days=-1)

    def test_negative_fee_rejected(self):
        with self.assertRaises(ValueError):
            LateFeePolicy(flat_fee=Decimal("-5"))


if __name__ == "__main__":
    unittest.main()
