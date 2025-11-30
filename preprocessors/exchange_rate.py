import pandas as pd
from datetime import datetime

df = pd.read_csv("exchange_rate.txt", header=None)

df.columns = ["AUD", "GBP", "CAD", "CHF", "CNY", "JPY", "NZD", "SGD"]

# daily dates from 1990 to 2016
start_date = datetime(1990, 1, 1)
num_rows = len(df)
dates = pd.bdate_range(start=start_date, periods=num_rows)
df.insert(0, "date", dates)


# use SGD as target (OT)
df = df.rename(columns={"SGD": "OT"})

df.to_csv("exchange_rate.csv", index=False)
