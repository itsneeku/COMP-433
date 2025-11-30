import pandas as pd

df = pd.read_csv("Ecommerce_Sales_Data_2024_2025.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"])

daily = (
    df.groupby("Order Date")
    .agg(
        {
            "Order ID": "count",
            "Quantity": "sum",
            "Unit Price": "mean",
            "Discount": "mean",
            "Profit": "sum",
            "Sales": "sum",
        }
    )
    .reset_index()
)

daily.columns = [
    "date",
    "order_count",
    "quantity",
    "avg_price",
    "avg_discount",
    "Profit",
    "OT",
]

date_range = pd.date_range(start=daily["date"].min(), end=daily["date"].max(), freq="D")
daily = pd.DataFrame({"date": date_range}).merge(daily, on="date", how="left").fillna(0)

daily.to_csv("ecommerce.csv", index=False)
