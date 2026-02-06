import pandas as pd
from datetime import datetime, timedelta

SALES_COLUMNS_PREFIX = "day_"

def calculate_average_daily_demand(row: pd.Series) -> float:
    sales_cols = [col for col in row.index if col.startswith(SALES_COLUMNS_PREFIX)]
    total_sales = row[sales_cols].sum()
    days_count = len(sales_cols)
    return round(total_sales / days_count, 2) if days_count > 0 else 0


def calculate_days_until_stock_out(current_stock: float, avg_demand: float) -> float:
    if avg_demand == 0:
        return float("inf")
    return round(current_stock / avg_demand, 1)


def calculate_reorder_date(days_left: float, lead_time: int) -> str:
    reorder_days = max(days_left - lead_time, 0)
    reorder_date = datetime.today() + timedelta(days=reorder_days)
    return reorder_date.strftime("%Y-%m-%d")


def calculate_risk_level(days_left: float, lead_time: int) -> str:
    if days_left < lead_time:
        return "High"
    elif lead_time <= days_left < lead_time + 3:
        return "Medium"
    return "Low"


def generate_inventory_forecast(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply forecasting logic to entire inventory dataset.
    """
    df = df.copy()

    df["avg_daily_sales"] = df.apply(calculate_average_daily_demand, axis=1)
    df["days_until_stock_out"] = df.apply(
        lambda r: calculate_days_until_stock_out(
            r["current_stock"], r["avg_daily_sales"]
        ),
        axis=1
    )

    df["reorder_date"] = df.apply(
        lambda r: calculate_reorder_date(
            r["days_until_stock_out"], r["lead_time_days"]
        ),
        axis=1
    )

    df["risk_level"] = df.apply(
        lambda r: calculate_risk_level(
            r["days_until_stock_out"], r["lead_time_days"]
        ),
        axis=1
    )

    return df
