

import pandas as pd

import pandas as pd

# df1 - default index 0,1,2
df1 = pd.DataFrame({
    'Name': ['Amit', 'Riya', 'Karan'],
    'Department': ['IT', 'HR', 'Sales']
})

# df2 - same default index 0,1,2
df2 = pd.DataFrame({
    'Salary': [50000, 60000, 55000],
    'JoiningYear': [2020, 2019, 2021]
})
df = pd.DataFrame(df1)
dff = pd.DataFrame(df2)


result = df.join(df2)
print(result)

total = df.join(df2,lsuffix='_left',rsuffix='_right')
print(total)