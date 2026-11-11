"""Run the full pipeline: read data -> process it -> save the result.

Run from the project folder with:

    uv run scripts/run_pipeline.py
"""

import pandas as pd

from ds_starter.config import PROCESSED_DATA_DIR, RAW_SALES_PATH, SALES_SUMMARY_PATH
from ds_starter.pipeline import run_pipeline


def main() -> None:
    # 1. Read the raw data with pandas
    raw_sales = pd.read_csv(RAW_SALES_PATH)
    print(f"Read {len(raw_sales)} rows from {RAW_SALES_PATH}")

    # 2. Hand it to the orchestrator, which calls the helpers
    summary = run_pipeline(raw_sales)

    # 3. Save the result with pandas
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
    summary.to_csv(SALES_SUMMARY_PATH, index=False)
    print(f"Saved {len(summary)} rows to {SALES_SUMMARY_PATH}")

    print()
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()
