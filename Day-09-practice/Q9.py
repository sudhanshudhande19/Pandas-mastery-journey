import pandas as pd
import numpy as np

data = {
    "Name": [
        "Amit Sharma",
        "Priya Singh",
        "Rahul Verma",
        "Sneha Kapoor",
        "Vikas Mehta",
        "Anjali Joshi",
        "Rohan Kumar",
        "Meera Desai",
        "Suresh Patil",
        "Kavita Rao"
    ],
    "Age": [
        28,
        32,
        25,
        29,
        35,
        27,
        31,
        30,
        33,
        26
    ],
    "Salary": [
        55000,
        62000,
        48000,
        51000,
        75000,
        46000,
        68000,
        53000,
        70000,
        47000
    ]
}

df = pd.DataFrame(data)

def age_salary_features(row):
    age_group = "Young" if row["Age"] < 30 else "Experienced"
    salary_in_lakhs = row["Salary"] / 100000  
    return age_group, salary_in_lakhs

df[["AgeGroup", "SalaryLakhs"]] = df.apply(age_salary_features, axis=1, result_type='expand')

print(df)