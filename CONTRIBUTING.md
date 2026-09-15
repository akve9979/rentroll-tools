# Contributing

1. Branch off `main`: `feature/<short-name>`, `fix/<short-name>` or `docs/<short-name>`.
2. Keep changes small. Add or update tests in `tests/`.
3. Run the tests: `python -m unittest discover -s tests -v`
4. Open a pull request into `main`. CI (`test`) has to pass and one maintainer has to approve before merge.
5. Update `CHANGELOG.md` under **Unreleased** if behaviour changes.
