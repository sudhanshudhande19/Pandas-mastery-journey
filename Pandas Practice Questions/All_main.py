import pandas as pd

data = {
    "Name": ["Amit", "Rahul", "Sneha", "Priya", "Rohit", "Neha", "Vikas", "Pooja", "Karan", "Anjali"],
    "Age": [20, 21, 19, 22, 20, 21, 23, 19, 22, 20],
    "Marks": [85, 92, 67, 76, 55, 95, 88, 72, 60, 91],
    "City": ["Nagpur", "Pune", "Nagpur", "Mumbai", "Pune", "Nagpur", "Mumbai", "Pune", "Nagpur", "Mumbai"],
    "Gender": ["M", "M", "F", "F", "M", "F", "M", "F", "M", "F"]
}

df = pd.DataFrame(data)

#  Level 1 — Basic Pandas

print(df.head())

print(df.tail())

print(df.shape)

print(pd.DataFrame(df, columns=['Name']))

print(pd.DataFrame(df, columns=['Name','Marks']))

print(df.columns)

print(df.dtypes)

print(df['Age'].mean())

print(df['Marks'].max())

print(df['Marks'].min())


print("=================================")

# Level 2 — Filtering


print(df[df['Marks'] > 80])

print(df[df["Marks"] >= 60][['Name','Marks']])

print(df[df["Age"]> 20])

print(df[df['City'] == 'Nagpur'])

print(df[df['City'] == 'Pune'][['Name','Marks']])

print(df.query("70 <= Marks <= 90"))

print(df.query("Age > 20"))

print(df[df['Gender'] == 'F'])

print(df[df['Gender'] == 'M'][['Name','City','Marks']])

print(df.query("Marks > 90 ") [['Name','Marks']])

print("=================================")


# 3 Level 3 — Sorting

print(df.sort_values(['Marks']))

print(df.sort_values(['Marks'],ascending=False))

print(df.sort_values(['Age']))

print(df['Marks'].argmax())

print(df['Marks'].argmin())

print(df.sort_values(['Marks'])[-3:])

print(df.sort_values(['Marks'])[:3])

print("=================================")


# Level 4 — Creating New Columns


df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
print(df)

df['Bonus_Marks'] = df['Marks'] + 5
print(df)

df['Age_Next_Year'] = df['Age'] +1
print(df)

df['Grade'] = df['Marks'].apply(lambda x:
                                'A' if x >= 90 else
                                'B' if x >=80 else
                                'C' if x >= 70 else
                                'D' if x >= 60 else
                                'F')
print(df)

print("=================================")


# Level 5 — GroupBy


print(df['City'].value_counts())

print(df.groupby('City')['Name'].count())

print(df.groupby('City')['Marks'].mean())

print(df.groupby('City')['Marks'].max())

print(df.groupby('City')['Marks'].min())

print(df.groupby('Gender').value_counts())

print(df.groupby('Gender')['Marks'].mean())

print(df.groupby('City')['Age'].mean())

print("=================================")


# Level 6 — Important Pandas Operations


print(df.isnull())

print(df.isnull().sum())

print(df['Marks'].sum())

print(df["Marks"].mean())

print(df['Marks'].median())

print(df['Marks'].std())

print(pd.unique(df['City']))

print(df["City"].value_counts())

print(df.describe())

print("=================================")


#All Challenge Questions


result = df[df["City"] == "Nagpur"].loc[df[df["City"] == "Nagpur"]["Marks"].idxmax()]
print(result)

ll = df[df["City"] == "Pune"]["Marks"].mean()
print(ll)

print(df[df['Marks'] >= 80].sort_values('Marks', ascending=False))

kk = df.sort_values("Marks", ascending=False).head(3)[["Name", "Marks", "City"]]
print(kk)

print(df.groupby('City')['Marks'].max())

print("=================================")
