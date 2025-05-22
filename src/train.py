import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import mlflow
import json
import yaml

# Load param
params = yaml.safe_load(open("params.yaml"))
C = params["C"]

df = pd.read_csv("data/processed/data.csv")
X = df.drop("target", axis=1)
y = df["target"]

model = LogisticRegression(C=C, max_iter=200)
model.fit(X, y)
acc = model.score(X, y)

mlflow.start_run()
mlflow.log_param("C", C)
mlflow.log_metric("accuracy", acc)
mlflow.end_run()

joblib.dump(model, "model/model.pkl")
json.dump({"accuracy": acc}, open("metrics.json", "w"))
