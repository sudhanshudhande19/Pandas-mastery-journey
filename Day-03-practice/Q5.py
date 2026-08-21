import pandas as pd


df = pd.read_csv("employee_missing_values.csv")
print(df.isnull().sum())