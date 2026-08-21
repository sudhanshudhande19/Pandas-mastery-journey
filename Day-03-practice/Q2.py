import pandas as pd
import numpy as np

data = {
    'Name': ['Amit', 'Riya', 'Karan', 'Sneha', 'Vikas', 'Pooja', 'Rahul'],
    'Age': [25, np.nan, 30, 28, np.nan, 22, 35],
    'City': ['Mumbai', 'Pune', np.nan, 'Delhi', 'Nagpur', 'Pune', np.nan],
    'Salary': [50000, 45000, np.nan, 60000, 55000, np.nan, 48000],
    'Department': ['IT', 'HR', 'IT', np.nan, 'Sales', 'HR', 'IT']
}

df = pd.DataFrame(data)
# 1
print(df.isnull())      # isnull ---> True
print("--------------")
# 2
print(df.notnull())     # notnull---> Flase
# 3
print(df.isnull().sum())    # sum of all null value 


