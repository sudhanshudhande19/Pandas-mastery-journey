print("=========Mini project Putting It All Together=========")


import pandas as pd

df = pd.read_csv("Employee Dataset.csv")
print(df)
print("---------------------")
print(df.head())
print("---------------------")
print(df.info())
print("---------------------")
print(df.describe())
print("---------------------")

print("=============================")

# 2
print(df.isnull().sum())
print("----------------------")
print(df.dropna())

print("=============================")

# 3

print(df.loc[0:3])
print("---------------------")
print(df.iloc[0:3])

print("=============================")

# 4

df['Salary Gread'] = df['Salary'].apply(lambda x: 
                                 "A" if x > 80000 else
                                 "B" if x >= 70000 else
                                 "C" if x >= 60000 else 
                                 "D" if x >= 50000 else 
                                 "F")
print(df)

print("=============================")

# 5


print(df.groupby('Age')['Salary'].mean())
print("---------------------")
print(df.groupby('Salary').sum())
print("---------------------")
print(df.groupby('City')['Name'].count())

print("=============================")

# 6

print(pd.to_datetime(df['Date']))

print("==============================")

# 7

print(df.pivot_table(index='Name',columns='Department',values='Salary'))

print("=============================")

# 8

print(df['City'].str.strip())
print("--------------------------")
print(df['City'].str.upper())
print("--------------------------")
print(df['City'].str.lower())

print("=============================")

# 9

kk = pd.read_csv("Sales Dataset.csv")
print(pd.merge(df,kk , on='City'))

