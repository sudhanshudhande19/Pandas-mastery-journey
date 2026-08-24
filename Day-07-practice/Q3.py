import pandas as pd


df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-15', '2024-02-10', '2024-02-20', '2024-03-05'],
    'Sales': [200, 340, 150, 400, 280]
})

df['Date'] = pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['DayName'] = df['Date'].dt.day_name()

print(df)