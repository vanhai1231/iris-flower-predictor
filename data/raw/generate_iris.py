from sklearn.datasets import load_iris
import pandas as pd

df = load_iris(as_frame=True).frame
df.to_csv("data/raw/iris.csv", index=False)