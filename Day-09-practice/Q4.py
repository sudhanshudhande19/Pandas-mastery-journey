import pandas as pd

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

def age_category(age):
    if age < 30:
        return 'Young'
    elif age < 45:
        return 'Middle'
    else:
        return 'Senior'


df['Age_Category'] = df['Age'].map(age_category)

print(df)