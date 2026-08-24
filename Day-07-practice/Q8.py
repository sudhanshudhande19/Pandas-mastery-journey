import pandas as pd

df = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=10, freq='D'),
    'Sales': [100, 120, 90, 150, 130, 170, 160, 140, 180, 200]
})
df.set_index('Date', inplace=True)

df['MA_3'] = df['Sales'].rolling(window=3).mean()
print(df)