#!/bin/bash -e

# Format and autofix lint issues across the package, examples, and tests.
poetry run ruff format .
poetry run ruff check --fix .
