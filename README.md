
# 🐼 Pandas Mastery Journey

A structured **10-day daily practice roadmap** to master Pandas — from basics to real-world data cleaning, aggregation, and analysis. Every day includes hands-on exercises, solved code, and a day-wise README explaining the concepts.

---

## 📅 10-Day Roadmap Overview

| Day | Topic | Focus Area |
|---|---|---|
| 1 | Pandas Basics — Series & DataFrame | Foundations |
| 2 | Indexing, Selection & Filtering | Data Access |
| 3 | Handling Missing Data | Data Cleaning |
| 4 | GroupBy & Aggregation | Data Summarization |
| 5 | Merging, Joining & Concatenation | Combining Data |
| 6 | String Operations & Text Data | Data Cleaning |
| 7 | Date & Time Handling | Time Series |
| 8 | Pivot Tables & Reshaping | Data Restructuring |
| 9 | Data Visualization with Pandas | Analysis & Plotting |
| 10 | Real-World Mini Project | Capstone / End-to-End |

---

## 📖 Detailed Day-Wise Breakdown

### 🔹 Day 1 — Pandas Basics: Series & DataFrame
**What it covers:** Introduction to the two core Pandas data structures.
- `Series` — a one-dimensional labeled array (like a single column)
- `DataFrame` — a two-dimensional labeled table (like an Excel sheet)
- Creating Series from lists and dictionaries
- Creating DataFrames from dictionaries of lists
- Exploring data with `.head()`, `.tail()`, `.shape`, `.info()`, `.describe()`
- Reading data from a CSV file using `pd.read_csv()`

**Why it matters:** Everything in Pandas builds on Series and DataFrames — this is the foundation for all future days.

---

### 🔹 Day 2 — Indexing, Selection & Filtering
**What it covers:** How to access exactly the data you need.
- `loc[]` — label-based selection (select by row/column *names*)
- `iloc[]` — position-based selection (select by row/column *index numbers*)
- Conditional filtering with comparison operators (`>`, `<`, `==`)
- Combining multiple conditions using `&` (AND) and `|` (OR)
- `isin()` for filtering against a list of values
- Creating new columns based on conditions

**Why it matters:** Real datasets are huge — you rarely need the whole thing, you need specific rows/columns based on conditions.

---

### 🔹 Day 3 — Handling Missing Data
**What it covers:** Real-world data is messy; this day teaches cleaning it.
- Detecting missing values with `isnull()` / `notnull()`
- Counting missing values per column with `isnull().sum()`
- Dropping missing data with `dropna()` (with `how='all'`, `subset=[]` options)
- Filling missing data with `fillna()` — constant value, mean, forward-fill (`ffill`), backward-fill (`bfill`)
- Applying these techniques on a real dataset (e.g., Titanic)

**Why it matters:** Missing data breaks analysis and ML models — cleaning it properly is a core data science skill.

---

### 🔹 Day 4 — GroupBy & Aggregation
**What it covers:** Summarizing data by categories.
- `groupby()` to split data into groups (e.g., by Department)
- Aggregation functions: `.mean()`, `.sum()`, `.count()`, `.max()`, `.min()`
- Multiple aggregations at once using `.agg()`
- Grouping by multiple columns simultaneously
- `value_counts()` for quick category frequency counts
- Sorting grouped results with `sort_values()`

**Why it matters:** This is how you answer questions like "average salary per department" — one of the most common real-world analysis tasks.

---

### 🔹 Day 5 — Merging, Joining & Concatenation
**What it covers:** Combining data from multiple sources/tables.
- `pd.merge()` — SQL-style joins (`inner`, `left`, `right`, `outer`)
- `pd.concat()` — stacking DataFrames row-wise or column-wise
- `.join()` — combining on index, with suffix handling for overlapping columns
- `left_on` / `right_on` for merging on differently-named key columns
- `indicator=True` to see which rows matched from which source

**Why it matters:** Real data lives across multiple tables/files — combining them correctly is essential before analysis.

---

### 🔹 Day 6 — String Operations & Text Data
**What it covers:** Cleaning and manipulating text columns.
- The `.str` accessor for string methods on a Series
- Case conversion: `.str.upper()`, `.str.lower()`
- Whitespace cleanup: `.str.strip()`
- Searching text: `.str.contains()`, `.str.startswith()`
- Splitting and extracting: `.str.split()`, `.str.extract()`
- Replacing text: `.str.replace()`

**Why it matters:** Text data (names, categories, free-text fields) is common and often needs cleaning before it's usable.

---

### 🔹 Day 7 — Date & Time Handling
**What it covers:** Working with time-based data.
- Converting text to dates with `pd.to_datetime()`
- Extracting parts of a date: year, month, day, weekday
- Date arithmetic (differences between dates, adding days)
- Setting a datetime column as the index
- Resampling time series data (e.g., daily → monthly)

**Why it matters:** Time series data (sales over time, logs, sensor data) needs special handling that plain numbers/strings don't have.

---

### 🔹 Day 8 — Pivot Tables & Reshaping
**What it covers:** Restructuring data for better analysis.
- `pivot_table()` — Excel-style pivot tables in Pandas
- `pivot()` vs `pivot_table()` — when to use which
- `melt()` — converting wide data to long format
- `stack()` / `unstack()` — reshaping hierarchical data

**Why it matters:** Data often arrives in the "wrong shape" for analysis — reshaping is a key skill for reporting and visualization.

---

### 🔹 Day 9 — Data Visualization with Pandas
**What it covers:** Quick, built-in plotting directly from DataFrames.
- `.plot()` — line charts by default
- Bar charts: `.plot(kind='bar')`
- Histograms: `.plot(kind='hist')`
- Box plots: `.plot(kind='box')`
- Customizing titles, labels, and figure size

**Why it matters:** Visualizing data reveals patterns and outliers that raw numbers hide — a critical step before drawing conclusions.

---

### 🔹 Day 10 — Real-World Mini Project (Capstone)
**What it covers:** Bringing everything together on a real dataset.
- Load a real-world dataset (e.g., Titanic, sales data, or similar)
- Clean missing/messy data (Day 3 + Day 6 skills)
- Filter and explore using `loc`/`iloc` (Day 2 skills)
- Group and summarize with `groupby()` (Day 4 skills)
- Merge with a second dataset if applicable (Day 5 skills)
- Reshape with pivot tables (Day 8 skills)
- Visualize final insights (Day 9 skills)
- Write a short summary of findings

**Why it matters:** This ties every concept from Day 1–9 into one complete, portfolio-worthy project — proof of end-to-end Pandas mastery.

---

## 📂 Repository Structure

```
Pandas-mastery-journey/
├── Day-01-practice/
├── Day-02-practice/
├── Day-03-practice/
├── Day-04-practice/
├── Day-05-practice/
├── Day-06-practice/
├── Day-07-practice/
├── Day-08-practice/
├── Day-09-practice/
├── Day-10-practice/
└── README.md
```

Each day's folder contains the solved code/notebook and a short day-wise README explaining what was learned.

---

## 🎯 Goal
Complete a solid, practical grip on Pandas in 10 days — covering data structures, cleaning, aggregation, combining datasets, text/date handling, reshaping, visualization, and a final capstone project.

---
# Created by: Sudhanshu Dhande
