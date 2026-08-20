import pandas as pd

df_dict = {
    "Name" : ["sudhanshu","Adity","Kunal","Rohit","Kulbhushan","Raju","Ayush"],
    "Age" : [22,22,23,22,20,21,20],
    "Gender":["M","M","M","M","M","M","M"],
    "College" : ["KCEM","KCEM","KCEM","KCEM","KCEM","KCEM","KCEM"]
}

df = pd.Series(df_dict)
print(df)