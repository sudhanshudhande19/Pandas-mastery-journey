import pandas as pd

data = {
    "Department": ["IT", "HR", "Sales", "Finance", "IT","Marketing", "HR", "Sales", "Finance", "IT"],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vikas","Anjali", "Rohan", "Meera", "Karan", "Neha"],
    "EmployeeID": [1011,1012,1013,1014,1015,1016,1017,1018,1019,1020],
}

data1 = {
    "EmployeeID":  [1011,1012,1088,1014,1099,1091,1070,1018,1055,1020],
    "Salary": [55000, 62000, 48000, 51000, 75000,46000, 68000, 53000, 72000, 60000],
    "JointYear": [28, 32, 25, 29, 30,27, 20, 21, 22, 26]
}

df = pd.DataFrame(data)
df2 = pd.DataFrame(data1)

print(pd.merge(df,df2,on='EmployeeID',how='right'))
print(pd.merge(df,df2,on='EmployeeID',how='left'))
print(pd.merge(df,df2,on='EmployeeID',how='outer'))
