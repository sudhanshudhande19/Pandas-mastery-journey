import pandas as pd


df_dict = {
    "Name" : ["sudhanshu","Adity","Rohit","Kulbhushan","Ayush"],
    "Age" : [22,22,23,22,20,],
    "City" : ["sakoli","sakoli","sakoli","kunghada","yekodi"]
}
df = pd.DataFrame(df_dict)
print(df)