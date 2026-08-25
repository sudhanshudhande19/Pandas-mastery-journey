import pandas as pd

data = {
    "Name": [
        "  Amit Sharma ", 
        "priya  Singh", 
        "RAHUL   Verma", 
        " sneha kapoor", 
        "Vikas   ", 
        "ANJALI Mehta", 
        " rohan   ", 
        "MEERA  Joshi", 
        "   Suresh ", 
        "Kavita   "
    ],
    "Email": [
        "  amit.sharma@Gmail.Com ", 
        "PRIYA_singh@ yahoo.com", 
        "rahul.verma@outlook.COM", 
        " sneha.kapoor@GMAIL.com", 
        "vikas123 @hotmail.com ", 
        "anjali.mehta@YAHOO.Com", 
        " rohan.kumar@ gmail.com", 
        "MEERA.joshi@outlook.com ", 
        " suresh@GMAIL.Com", 
        "kavita@ yahoo.com "
    ],
    "Phone": [
        "  98765 43210", 
        "91- 8765432109", 
        " +91 9988776655 ", 
        "9876-543-210", 
        "  9123456789", 
        "91  9876543210", 
        " +91- 9090909090", 
        " 98765-43211 ", 
        "91- 9123456780", 
        "  90000 11111 "
    ]
}

df = pd.DataFrame(data)

print(df['Name'].str.lower())
print(df['Name'].str.upper())
