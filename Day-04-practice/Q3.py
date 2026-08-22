import pandas as pd

data = {
    "Department": ["IT", "HR", "Sales", "Finance", "IT","Marketing", "HR", "Sales", "Finance", "IT"],
    "Employee": ["Amit", "Priya", "Rahul", "Sneha", "Vikas","Anjali", "Rohan", "Meera", "Karan", "Neha"],
    "Salary": [55000, 62000, 48000, 51000, 75000,46000, 68000, 53000, 72000, 60000],
    "Age": [28, 32, 25, 29, 35,27, 31, 30, 33, 26]
}

df = pd.DataFrame(data)

print(df.groupby('Department')['Salary'].agg(['mean','max','min']))
