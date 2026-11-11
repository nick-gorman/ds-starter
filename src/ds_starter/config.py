"""Paths used across the project.

Keeping paths in one place means scripts, notebooks and the REPL all
read from and write to the same folders, wherever they are run from.
"""

from pathlib import Path

# src/ds_starter/config.py -> go up two folders to reach the project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

RAW_SALES_PATH = RAW_DATA_DIR / "sales.csv"
SALES_SUMMARY_PATH = PROCESSED_DATA_DIR / "sales_summary.csv"
