import streamlit as st
import pandas as pd
from data_loader import load_inventory_data
from forecasting import generate_inventory_forecast
from utils import plot_inventory_forecast

st.set_page_config(page_title="Warehouse Inventory Forecast Tool", layout="wide")
st.title("📦 Warehouse Inventory Forecast Tool")

uploaded_file = st.file_uploader(
    "Upload Inventory CSV / Excel", type=["csv", "xlsx"]
)

def style_risk_rows_html(df, height=400):
    """
    Returns an HTML table with bold headers, colored rows based on risk level,
    and wrapped in a scrollable div.
    """
    color_map = {"High": "#ffcccc", "Medium": "#fff2cc", "Low": "#d9ead3"}
    
    # Table header
    headers = "".join([f"<th style='padding:5px;text-align:center;'><b>{col}</b></th>" for col in df.columns])
    
    # Start table HTML
    html = f"<div style='overflow:auto; max-height:{height}px; width:100%;'><table style='border-collapse: collapse; width:100%;' border='1'><thead><tr>{headers}</tr></thead><tbody>"
    
    # Table rows
    for _, row in df.iterrows():
        color = color_map.get(row["Risk Level"], "white")
        row_html = "".join([f"<td style='padding:5px;text-align:center;'>{val}</td>" for val in row])
        html += f"<tr style='background-color:{color};'>{row_html}</tr>"
    
    html += "</tbody></table></div>"
    return html

if uploaded_file:
    # Load and forecast
    df = load_inventory_data(uploaded_file)
    forecast_df = generate_inventory_forecast(df)

    # Select and rename columns to display
    display_df = forecast_df[
        [
            "item_name",
            "current_stock",
            "avg_daily_sales",
            "days_until_stock_out",
            "reorder_date",
            "lead_time_days",
            "risk_level",
        ]
    ].copy()

    # Capitalize column names for display
    display_df.columns = [
        "Item Name",
        "Current Stock",
        "Average Daily Sales",
        "Days Until Stock-Out",
        "Reorder Date",
        "Lead Time (Days)",
        "Risk Level",
    ]

    # Display scrollable, styled table
    st.subheader("📊 Inventory Summary")
    st.markdown(style_risk_rows_html(display_df, height=400), unsafe_allow_html=True)

    # Item-level analysis
    st.subheader("🔍 Item-Level Analysis")
    selected_item = st.selectbox(
        "Select Item",
        forecast_df["item_name"].unique()
    )

    item_data = forecast_df[forecast_df["item_name"] == selected_item].iloc[0]
    sales_cols = [c for c in df.columns if c.startswith("day_")]
    sales_history = item_data[sales_cols].values

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Average Daily Demand", item_data["avg_daily_sales"])
        st.metric("Days Left", item_data["days_until_stock_out"])
        st.metric("Risk Level", item_data["risk_level"])

    with col2:
        fig = plot_inventory_forecast(selected_item, sales_history)
        st.pyplot(fig)
