# Pandas Practice Questions 🐼

Welcome to **Practice Questions** of my Pandas learning and practice journey.

After completing the first 10 days of Pandas practice, I am now focusing on solving problems independently. This practice set contains **50 questions**, starting from basic DataFrame operations and gradually moving toward filtering, sorting, creating new columns, GroupBy, statistical analysis, and challenge-level problems.

The main goal of this day is not only to write code, but also to understand **how to read a problem, identify the required Pandas operation, and solve it step by step.**

---

## 🎯 Objectives

* Practice Pandas fundamentals
* Improve DataFrame manipulation skills
* Understand DataFrame selection and indexing
* Strengthen filtering and conditional operations
* Practice sorting and ranking
* Learn how to create new columns
* Understand `groupby()` operations
* Practice statistical functions
* Work with missing values
* Improve logical thinking and problem-solving skills
* Build confidence in solving Pandas problems independently

---

# 📚 How I Approach a Pandas Problem

When solving a Pandas question, I follow these basic steps:

### Step 1 – Understand the question

First, I identify **what the question is asking for**.

For example:

> Find students whose marks are greater than 80.

Here, the important information is:

* Column → `Marks`
* Condition → `> 80`
* Required result → Matching rows

---

### Step 2 – Identify the Pandas operation

Different questions require different operations.

| Requirement    | Pandas Operation |
| -------------- | ---------------- |
| First rows     | `head()`         |
| Last rows      | `tail()`         |
| Rows & columns | `shape`          |
| Column names   | `columns`        |
| Data types     | `dtypes`         |
| Select column  | `df["Column"]`   |
| Filter rows    | `df[condition]`  |
| Sort data      | `sort_values()`  |
| Group data     | `groupby()`      |
| Average        | `mean()`         |
| Maximum        | `max()`          |
| Minimum        | `min()`          |
| Total          | `sum()`          |
| Unique values  | `unique()`       |
| Frequency      | `value_counts()` |
| Statistics     | `describe()`     |

---

### Step 3 – Write the simplest solution

I first try to solve the problem using basic Pandas operations instead of making the code unnecessarily complicated.

### Step 4 – Check the output

After running the code, I check whether the output matches what the question asked.

### Step 5 – Understand the logic

I try to remember **why** the code works instead of only memorizing the syntax.

---

# 🟢 Level 1 — Basic Pandas

### Q1.

Extract the first 5 rows of the DataFrame.

### Q2.

Extract the last 3 rows of the DataFrame.

### Q3.

Find the total number of rows and columns in the DataFrame.

### Q4.

Extract only the `Name` column.

### Q5.

Extract the `Name` and `Marks` columns.

### Q6.

Display the column names of the DataFrame.

### Q7.

Check the data types of the DataFrame columns.

### Q8.

Find the average of the `Age` column.

### Q9.

Find the maximum value in the `Marks` column.

### Q10.

Find the minimum value in the `Marks` column.

---

# 🟡 Level 2 — Filtering ⭐

### Q11.

Extract the complete records of students whose marks are **greater than 80**.

### Q12.

Extract only the `Name` and `Marks` of students whose marks are **greater than or equal to 60**.

### Q13.

Find the students whose age is **20**.

### Q14.

Find the students who are from **Nagpur**.

### Q15.

Extract the `Name` and `Marks` of students who are from **Pune**.

### Q16.

Find the students whose marks are **between 70 and 90**.

### Q17.

Find the students whose age is **greater than 20**.

### Q18.

Find all **female students**.

### Q19.

Extract the `Name`, `City`, and `Marks` of all **male students**.

### Q20.

Extract only the `Name` and `Marks` of students whose marks are **greater than 90**. ⭐

---

# 🔵 Level 3 — Sorting ⭐

### Q21.

Sort the students by `Marks` in **ascending order**.

### Q22.

Sort the students by `Marks` in **descending order**.

### Q23.

Sort the students by `Age` in **ascending order**.

### Q24.

Find the student with the **highest marks**. ⭐

### Q25.

Find the student with the **lowest marks**.

### Q26.

Find the **top 3 students** based on their marks. ⭐

### Q27.

Find the **bottom 3 students** based on their marks.

---

# 🟠 Level 4 — Creating New Columns ⭐

### Q28.

Create a new column called `Pass`.

Condition:

```text
Marks >= 40 → Pass
Marks < 40  → Fail
```

### Q29.

Create a new column called `Bonus_Marks` and add **5 marks** to every student's marks.

### Q30.

Create a new column called `Age_Next_Year`.

### Q31.

Create a `Grade` column based on the students' marks:

```text
90+       → A
80-89     → B
70-79     → C
60-69     → D
Below 60  → F
```

⭐ This is an important interview-level concept.

---

# 🔴 Level 5 — GroupBy ⭐⭐⭐

### Q32.

Find the number of students in each city.

### Q33.

Find the **average marks** of students in each city.

### Q34.

Find the **maximum marks** in each city.

### Q35.

Find the **minimum marks** in each city.

### Q36.

Find the number of students according to their gender.

### Q37.

Find the **average marks** of male and female students.

### Q38.

Find the **average age** of students in each city.

---

# 🟣 Level 6 — Important Pandas Operations

### Q39.

Check whether the DataFrame contains any missing values.

### Q40.

Find the number of missing values in each column.

### Q41.

Find the total sum of the `Marks` column.

### Q42.

Find the **mean, median, and standard deviation** of the `Marks` column.

### Q43.

Find the unique cities in the `City` column.

### Q44.

Count how many times each city appears.

### Q45.

Generate the statistical summary of the DataFrame.

**Hint:** `describe()`

---

# ⭐ Challenge Questions

### Q46.

Among the students from **Nagpur**, find the student with the **highest marks**.

### Q47.

Find the **average marks of students from Pune**.

### Q48.

Filter students who have **80+ marks** and sort them in **descending order of marks**.

### Q49.

Extract only the `Name`, `Marks`, and `City` of the **top 3 students**.

### Q50.

Find the **top-scoring student from each city**. 🔥

---

# 🧠 Important Concepts to Remember

While solving these questions, I focused on remembering the following Pandas operations:

```python
head()
tail()
shape
columns
dtypes

loc[]
iloc[]

sort_values()

unique()
nunique()
value_counts()

mean()
median()
sum()
max()
min()
std()

groupby()
agg()

describe()

isnull()
isna()
```

---

# 💡 My Learning Strategy

I try to solve every question **without immediately looking at the solution**.

My approach is:

1. Read the question carefully.
2. Identify the required column.
3. Identify the condition or operation.
4. Choose the appropriate Pandas function.
5. Write the code.
6. Run the code and check the output.
7. If the answer is wrong, find the mistake.
8. Rewrite the solution without copying.
9. Move to the next question.

This helps me understand the logic instead of only memorizing code.

---

# 🛠️ Tools & Technologies

* Python
* Pandas
* VS Code
* Git
* GitHub

---

# 📈 Learning Progress

```text
Day 01 → Day 10
Pandas Fundamentals & Practice

Day 11
50 Pandas Practice Questions
Problem Solving & Revision
```

---

# 🚀 Next Step

Continue practicing Pandas with:

* Real-world datasets
* Data cleaning
* Missing-value handling
* Data analysis
* Data visualization
* NumPy + Pandas projects
* Machine Learning datasets

The goal is to become comfortable with Pandas before moving deeper into **Data Analysis and Machine Learning**.

---

## ⭐ Conclusion

This Day 11 practice helped me strengthen my understanding of Pandas and improve my ability to solve DataFrame problems independently.

I will continue practicing consistently and building projects to improve my Python, Data Analysis, and Machine Learning skills.

---

### 👨‍💻 Author

**Sudhanshu Ravindra Dhande**

**B.Tech – Artificial Intelligence**
⭐
