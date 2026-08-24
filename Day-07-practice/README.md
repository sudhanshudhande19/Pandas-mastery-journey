# Day 7 — Working with Dates & Time Series

##  Overview
Day 7 of the **Pandas Mastery Journey** focuses on one of the most practical and widely-used areas of data analysis: handling **dates and time series data**. Real-world datasets almost always contain a time dimension — sales logs, sensor readings, stock prices, attendance records — and Pandas provides a powerful, purpose-built toolkit for working with them efficiently.

This day covers converting raw strings into proper datetime objects, extracting date components, building date ranges, resampling data across time periods, and applying rolling/lag operations commonly used in time series analysis.

##  Learning Objectives
By the end of this day's practice, the goal is to be comfortable with:
- Converting string dates into native Pandas `datetime64` objects
- Extracting year, month, day, and weekday information from dates
- Generating custom date ranges programmatically
- Setting a datetime column as the DataFrame index for time-aware operations
- Resampling time series data across different frequencies (daily → monthly, etc.)
- Creating lag features using `.shift()`
- Computing moving averages using `.rolling()`
- Performing arithmetic between dates using `Timedelta`

##  Exercises Covered

| # | Concept | Method(s) Used |
|---|---------|-----------------|
| 1 | Creating a DataFrame with date + sales data | `pd.DataFrame()` |
| 2 | Converting string dates to datetime | `pd.to_datetime()` |
| 3 | Extracting date components | `.dt.year`, `.dt.month`, `.dt.day`, `.dt.day_name()` |
| 4 | Generating a date range | `pd.date_range()` |
| 5 | Setting date column as index | `.set_index()` |
| 6 | Resampling to monthly totals | `.resample('M').sum()` |
| 7 | Creating lag features | `.shift()` |
| 8 | Computing rolling average | `.rolling(window=3).mean()` |
| 9 | Date arithmetic | `Timestamp` subtraction, `Timedelta` |
| 10 | Understanding the `.dt` accessor | Conceptual (README write-up) |

##  Key Concept — Why the `.dt` Accessor Matters

Once a column is converted to `datetime64` type using `pd.to_datetime()`, Pandas unlocks a special accessor: `.dt`. This accessor gives direct access to date/time properties and methods (`.dt.year`, `.dt.month`, `.dt.weekday`, `.dt.day_name()`, etc.) without needing to manually parse strings.

**Why it's better than string operations:**
- **Correctness** — string slicing on dates (e.g., `date_str[:4]` for year) is fragile and breaks with inconsistent formats. `.dt` works off the actual underlying date value.
- **Performance** — `.dt` operations are vectorized and optimized in C, making them significantly faster than looping through strings.
- **Built-in intelligence** — `.dt` understands calendar logic (leap years, month lengths, weekdays) automatically, which string manipulation does not.

##  Summary of Time Series Operations

| Operation | Purpose |
|---|---|
| `resample()` | Aggregate data across a new time frequency (e.g., daily → monthly) |
| `shift()` | Create lagged/leading values — useful for comparing periods |
| `rolling()` | Compute moving statistics (average, sum, etc.) over a window |
| `Timedelta` | Represent and calculate differences between two dates |

##  Files
- `day7_pandas.py` / `day7_pandas.ipynb` — solved exercises
- `README.md` — this file

##  Series Progress
- ✅ Day 1 — Pandas Basics: Series & DataFrame
- ✅ Day 2 — Indexing, Selection & Filtering
- ✅ Day 3 — Handling Missing Data
- ✅ Day 4 — GroupBy & Aggregation
- ✅ Day 5 — Merging, Joining & Concatenation
- ✅ Day 6 — Pivot Tables & Reshaping
- ✅ Day 7 — Working with Dates & Time Series

---

**Next up:** Day 8 — String Operations & Text Data