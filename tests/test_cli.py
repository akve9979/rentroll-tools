import io
import pathlib
import unittest
from decimal import Decimal

from latefee.cli import run

EXAMPLE = pathlib.Path(__file__).resolve().parents[1] / "examples" / "september-payments.csv"


class CliTest(unittest.TestCase):
    def test_example_run_total(self):
        out = io.StringIO()
        self.assertEqual(run(str(EXAMPLE), out=out), Decimal("220.00"))
        self.assertIn("Total", out.getvalue())


if __name__ == "__main__":
    unittest.main()
