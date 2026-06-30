# Changelog

## 3.0.0

- Add a configurable `timeout` (default 60 seconds) to all network requests so
  `get_bytes()`, `get_short_url()`, and `to_file()` no longer hang indefinitely.
- Drop support for end-of-life Python 3.7 and 3.8; the minimum supported version
  is now Python 3.9. Tested against Python 3.9 through 3.13.
- Ship inline type hints and a `py.typed` marker (PEP 561).
- Derive the client `User-Agent` version from the installed package metadata so
  it stays in sync with the release.
- Modernize packaging: PEP 621 `[project]` metadata, the `poetry.core.masonry.api`
  build backend, and PEP 735 dependency groups.
- Replace Travis CI with GitHub Actions and `autopep8` with `ruff` for linting
  and formatting.
- Remove leftover Python 2 compatibility code.

## 2.0.0

- Drop support for Python versions earlier than 3.7.
- Set a `User-Agent` header on requests.
- Show a detailed error message when chart creation fails.
- Add support for the `version` parameter.

## 1.0.1

- Last release supporting Python 2 and Python < 3.7.
