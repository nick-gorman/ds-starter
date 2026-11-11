"""Tests for the orchestrator: does the whole pipeline fit together?"""

import pandas as pd

from ds_starter.config import RAW_SALES_PATH
from ds_starter.pipeline import run_pipeline


def test_run_pipeline_returns_one_row_per_region():
    raw_sales = pd.read_csv(RAW_SALES_PATH)

    summary = run_pipeline(raw_sales)

    assert sorted(summary["region"]) == ["East", "North", "South", "West"]


def test_run_pipeline_returns_expected_columns():
    raw_sales = pd.read_csv(RAW_SALES_PATH)

    summary = run_pipeline(raw_sales)

    assert summary.columns.tolist() == [
        "region",
        "orders",
        "total_units",
        "total_revenue",
        "average_order_value",
    ]
