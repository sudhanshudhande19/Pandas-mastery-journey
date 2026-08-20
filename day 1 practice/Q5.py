import pandas as pd

student_data = {
    "Name": [
        "Rahul", "Amit", "Priya", "Neha", "Rohit",
        "Sneha", "Akash", "Pooja", "Vikas", "Anjali",
        "Karan", "Riya", "Sahil", "Komal", "Nikhil",
        "Payal", "Aditya", "Simran", "Varun", "Isha"
    ],

    "Age": [
        20, 21, 19, 20, 22,
        21, 20, 19, 22, 21,
        20, 19, 21, 20, 22,
        19, 21, 20, 22, 19
    ],

    "Marks": [
        80, 75, 90, 85, 70,
        88, 92, 78, 65, 95,
        82, 89, 76, 84, 71,
        91, 87, 79, 68, 93
    ],

    "City": [
        "Nagpur", "Pune", "Mumbai", "Delhi", "Nashik",
        "Nagpur", "Pune", "Mumbai", "Delhi", "Nashik",
        "Nagpur", "Pune", "Mumbai", "Delhi", "Nashik",
        "Nagpur", "Pune", "Mumbai", "Delhi", "Nashik"
    ]
}

df = pd.DataFrame(student_data)
# head
print(df.head())
# tail
print(df.tail())
# shape
print(df.shape)
# information
print(df.info())
# describe
print(df.describe())
