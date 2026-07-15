import pandas as pd

df = pd.read_csv("superstore.csv")
print(df.columns.tolist())
print(df.shape)