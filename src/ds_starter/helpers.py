"""Helper functions: each one does a single, small job on a DataFrame.

Each helper takes a DataFrame and returns a new DataFrame. None of them
read or write files, which makes them easy to test and reuse.
"""

import pandas as pd


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """Fix data types, tidy text and drop rows we cannot use."""
    return (
        df.assign(
            order_date=pd.to_datetime(df["order_date"]),
            region=df["region"].str.strip().str.title(),
        )
        .dropna(subset=["units", "unit_price"])
        .drop_duplicates(subset="order_id")
        .reset_index(drop=True)
    )


def add_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Add a revenue column (units x unit price)."""
    return df.assign(revenue=df["units"] * df["unit_price"])


def summarise_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """Summarise orders, units and revenue for each region."""
    return (
        df.groupby("region", as_index=False)
        .agg(
            orders=("order_id", "count"),
            total_units=("units", "sum"),
            total_revenue=("revenue", "sum"),
        )
        .assign(
            total_units=lambda d: d["total_units"].astype(int),
            total_revenue=lambda d: d["total_revenue"].round(2),
            average_order_value=lambda d: (d["total_revenue"] / d["orders"]).round(2),
        )
        .sort_values("total_revenue", ascending=False)
        .reset_index(drop=True)
    )
