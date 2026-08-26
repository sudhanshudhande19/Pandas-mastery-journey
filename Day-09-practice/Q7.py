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
df['High/Low'] = np.where (df['Salary'] > 50000, 'High','Low')
print(df)