import pandas as pd

data = {
    'Date' : ['19/8/2026','20/8/2026','21/8/2026','22/8/2026','23/8/2026'],
    'City' : ['Pune','Mumbai','NAgpur','Pune','Nagpur'],
    'Product' : ['IPhone15','IPhone16','IPhone17','IPhone15','IPhone16'],
    'Sales' : [60000,70000,50000,90000,100000]
}  
df = pd.DataFrame(data)

df_multi = df.set_index(['City', 'Product'])
print(df_multi)

df_back = df_multi.reset_index()
print(df_back)