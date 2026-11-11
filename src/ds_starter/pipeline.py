"""The orchestrator: decides which helpers run, and in what order."""

import pandas as pd

from ds_starter.helpers import add_revenue, clean_sales, summarise_by_region


def run_pipeline(raw_sales: pd.DataFrame) -> pd.DataFrame:
    """Turn raw sales data into a summary table for each region.

    Takes a DataFrame and returns a DataFrame. Reading and saving files
    happens outside this function (see scripts/run_pipeline.py).
    """
    cleaned = clean_sales(raw_sales)
    with_revenue = add_revenue(cleaned)
    summary = summarise_by_region(with_revenue)
    return summary
