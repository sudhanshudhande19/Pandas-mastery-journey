import pandas as pd

d1 = pd.Timestamp('2024-01-15')
d2 = pd.Timestamp('2024-02-20')

diff = d2 - d1
print(diff)        
print(type(diff))  
print(diff.days)  