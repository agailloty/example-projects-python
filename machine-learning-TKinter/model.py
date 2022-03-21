from joblib import dump
import pickle
from sklearn.linear_model import LinearRegression
import pandas as pd
data = pd.read_csv("salary_data.csv")
X, y = data.drop(columns=["salary"]), data["salary"]

lin_model = LinearRegression()
lin_model.fit(X, y)


# Save the model on disk for later use
dump(lin_model, "model.joblib")
