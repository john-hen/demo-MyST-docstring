"""Builds the documentation locally."""

from subprocess import run
from pathlib import Path

here = Path(__file__).parent
run(['sphinx-build', 'docs', 'HTML'], cwd=here)
