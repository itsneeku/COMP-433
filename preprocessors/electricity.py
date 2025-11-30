import pandas as pd

df = pd.read_csv("LD2011_2014.txt", sep=";", decimal=",", index_col=0)

df = df.reset_index()
df.columns = ["date"] + list(df.columns[1:])

df["OT"] = df.iloc[:, 1:].mean(axis=1)

df.to_csv("electricity.csv", index=False)
