# Day 3 — Handling Missing Data

##  Topic
Detecting, handling, and cleaning missing values in Pandas DataFrames.

##  What I Learned
- How to detect missing values using `isnull()` and `notnull()`
- How to count missing values per column using `isnull().sum()`
- How to drop rows/columns containing missing values using `dropna()`
- How to fill missing values using `fillna()` with constants, mean, forward fill, and backward fill
- How to apply missing-value handling on a real-world dataset

##  Exercises Covered
1. Created a DataFrame with intentional `NaN` values across multiple columns
2. Detected missing values using `isnull()` and `notnull()`
3. Counted missing values per column using `isnull().sum()`
4. Practiced dropping missing data:
   - `dropna()` — drop rows with any NaN
   - `dropna(how='all')` — drop rows where all values are NaN
   - `dropna(subset=['column_name'])` — drop based on a specific column
5. Practiced filling missing data:
   - `fillna(0)` — replace NaN with a constant
   - `fillna(df['column'].mean())` — fill numeric columns with the mean
   - `fillna(method='ffill')` and `fillna(method='bfill')` — forward/backward fill
6. Loaded a real dataset (Titanic CSV), checked missing values with `isnull().sum()`, and handled them using an appropriate strategy

##  Key Concept — `dropna()` vs `fillna()`

| Aspect | `dropna()` | `fillna()` |
|---|---|---|
| What it does | Removes rows/columns with missing data | Replaces missing data with a value |
| Data loss | Yes — reduces dataset size | No — dataset size stays the same |
| Best used when | Missing data is minimal / not important | Missing data needs to be preserved (e.g., small dataset, important rows) |
| Risk | Losing valuable rows/columns | Introducing bias if fill value isn't representative |

**In short:** Use `dropna()` when missing data is negligible and won't hurt the analysis. Use `fillna()` when every row matters and you can reasonably estimate the missing value (mean, median, forward/backward fill, etc.).

## 📂 Files
- `day3_pandas.py` / `day3_pandas.ipynb` — solved exercises
- `README.md` — this file

---

**Next up:** Day 4 — Data Aggregation & Grouping (`groupby`)