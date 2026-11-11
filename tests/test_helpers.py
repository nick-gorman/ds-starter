"""Tests for the helper functions.

Each test builds a tiny DataFrame, runs one helper on it, and checks
the result. Run all tests from the project folder with:

    uv run pytest
"""

import pandas as pd

from ds_starter.helpers import add_revenue, clean_sales, summarise_by_region


def make_raw_sales() -> pd.DataFrame:
    """A tiny, messy dataset that looks like data/raw/sales.csv."""
    return pd.DataFrame(
        {
            "order_id": [1, 2, 3, 3],
            "order_date": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-03"],
            "region": ["north", " South ", "North", "North"],
            "product": ["Pen Pack", "Notebook", "Notebook", "Notebook"],
            "units": [2, None, 4, 4],
            "unit_price": [3.0, 4.5, 4.5, 4.5],
        }
    )


def test_clean_sales_tidies_region_names():
    cleaned = clean_sales(make_raw_sales())

    assert cleaned["region"].tolist() == ["North", "North"]


def test_clean_sales_drops_missing_units_and_duplicates():
    cleaned = clean_sales(make_raw_sales())

    # Order 2 has no units and order 3 appears twice, so two rows remain
    assert cleaned["order_id"].tolist() == [1, 3]


def test_clean_sales_converts_order_date_to_datetime():
    cleaned = clean_sales(make_raw_sales())

    assert pd.api.types.is_datetime64_any_dtype(cleaned["order_date"])


def test_add_revenue_multiplies_units_by_unit_price():
    df = pd.DataFrame({"units": [2, 4], "unit_price": [3.0, 4.5]})

    result = add_revenue(df)

    assert result["revenue"].tolist() == [6.0, 18.0]


def test_summarise_by_region_totals_each_region():
    df = pd.DataFrame(
        {
            "order_id": [1, 2, 3],
            "region": ["North", "North", "South"],
            "units": [2, 4, 1],
            "revenue": [6.0, 18.0, 10.0],
        }
    )

    summary = summarise_by_region(df)

    expected = pd.DataFrame(
        {
            "region": ["North", "South"],
            "orders": [2, 1],
            "total_units": [6, 1],
            "total_revenue": [24.0, 10.0],
            "average_order_value": [12.0, 10.0],
        }
    )
    pd.testing.assert_frame_equal(summary, expected)
