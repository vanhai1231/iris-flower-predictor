import pandas as pd

df = pd.read_csv("data/raw/iris.csv")
df.to_csv("data/processed/data.csv", index=False)
