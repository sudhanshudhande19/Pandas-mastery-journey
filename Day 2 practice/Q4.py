import pandas as pd

data = {
    "Name" :         ["Amit","priya","rahul","sneha","vikas","anjali","roshan","meera"],
    "Age" :          [28,32,25,29,35,27,31,30],
    "City" :         ["mumbai","delhi","pune","nagpur","banglaore","hyderabad","chennai","kolka"],
    "Salary" :       [55000,62000,48000,51000,75000,46000,68000,53000],
    "Department" :   ["IT","HR","Finance","Marketing","IT","sales","Finance","HR"],
    "Experience" :   [3,5,2,4,8,2,6,4]

}
df = pd.DataFrame(data)
# 1
print(df[df["Salary"] > 50000])

print("---------------------------")
# 2
print([df[df["Age"] > 25]] and [df[df["Department"]=='IT']])