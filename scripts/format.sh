#!/bin/bash -e

poetry run autopep8 --in-place examples/*.py quickchart/*.py
