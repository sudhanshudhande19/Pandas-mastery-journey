import pandas as pd


df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-15', '2024-02-10', '2024-02-20', '2024-03-05'],
    'Sales': [200, 340, 150, 400, 280]
})

print(pd.date_range(start='2024-01-01',periods=10,freq='D'))