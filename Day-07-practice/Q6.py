import pandas as pd
import numpy as np

# Step 1: Month-spanning data  (60 days, Jan-Feb-Mar 2024)
dates = pd.date_range(start='2024-01-01', periods=60, freq='D')
sales = np.random.randint(100, 1000, size=60)

df = pd.DataFrame({'Date': dates, 'Sales': sales})

# Step 2: Date convert to  index 
df.set_index('Date', inplace=True)

# Step 3: Monthly sum 
monthly_sales = df.resample('M').sum()

print(monthly_sales)