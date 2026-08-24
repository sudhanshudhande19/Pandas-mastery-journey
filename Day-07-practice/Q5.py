import pandas as pd

# Sample data
df = pd.DataFrame({
    'Date': ['2024-01-01', '2024-01-15', '2024-02-10', '2024-02-20', '2024-03-05'],
    'Sales': [200, 340, 150, 400, 280]
})

print(df.set_index('Date'))