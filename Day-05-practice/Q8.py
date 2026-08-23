import pandas as pd


df1 = pd.DataFrame({
    'EmployeeID': [101, 102, 103],
    'Name': ['Amit', 'Riya', 'Karan']
})

df2 = pd.DataFrame({
    'EmployeeID': [101, 101, 102, 102, 103],
    'Month': ['Jan', 'Feb', 'Jan', 'Feb', 'Jan'],
    'Salary': [50000, 51000, 60000, 61000, 45000]
})

result = pd.merge(df1,df2, indicator= True)
print(result)