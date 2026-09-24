# late-fee-calc

[![CI](https://github.com/akve9979/late-fee-calc/actions/workflows/ci.yml/badge.svg)](https://github.com/akve9979/late-fee-calc/actions/workflows/ci.yml)

Works out late fees for residential leases, so the rent run and the lease terms always agree. We use it for the monthly late fee pass before charges go into the property management system.

## What it does
- Applies each lease's late fee terms: grace days, a one-time flat fee, a daily fee, and a monthly cap
- Reads a payments CSV and prints the fee per unit, plus a total
- Keeps money in `Decimal`, rounded to cents

## Install
```bash
python -m pip install -e .
```

## Use it
```bash
latefee examples/september-payments.csv
```
```
A1     Priya Shah         0 days late  $   0.00
A2     Tom Adeyemi        1 days late  $  50.00
B1     Rosa Delgado       3 days late  $  70.00
B2     Sam Whitfield     18 days late  $ 100.00 (capped)
       Total                            $ 220.00
```

From Python:
```python
from datetime import date
from latefee import LateFeePolicy, late_fee

policy = LateFeePolicy(grace_days=1, flat_fee=50, daily_fee=10, monthly_cap=100)
late_fee(policy, due=date(2026, 9, 1), paid=date(2026, 9, 4)).fee   # Decimal('70.00')
```

## Policies
See [docs/policies.md](docs/policies.md) for how each setting works and the default Birch Court terms.

## Contributing
Branch off `main`, open a pull request, and wait for CI and one review. Details in [CONTRIBUTING.md](CONTRIBUTING.md).

## License
MIT
