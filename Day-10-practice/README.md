# Day 10 — Mini Project: Bringing the Entire Pandas Journey Together 🎉

##  Topic
A complete, end-to-end mini data analysis project that combines everything learned across the 10-day Pandas roadmap — from basic Series/DataFrame creation to cleaning, merging, reshaping, time series handling, and custom transformations.

---

##  The Complete 10-Day Pandas Journey

This project marks the finish line of a structured, day-by-day journey through Pandas — Python's most widely used library for data analysis and manipulation. Below is a detailed walkthrough of everything covered across the 10 days, what each day built toward, and why it mattered.

### Day 1 — Pandas Basics: Series & DataFrame
The journey started with the two foundational data structures in Pandas: the **Series** (a one-dimensional labeled array) and the **DataFrame** (a two-dimensional labeled table, essentially a collection of Series sharing the same index). This day covered how to create both from lists, dictionaries, and CSV files, how indexing works by default and with custom labels, and how to get a first look at any dataset using `.head()`, `.tail()`, `.shape`, `.info()`, and `.describe()`. This is the entry point for literally everything else in Pandas — every later concept builds on top of the Series/DataFrame structure introduced here.

### Day 2 — Indexing, Selection & Filtering
Once comfortable creating DataFrames, the next skill was **extracting exactly the data you need** from them. This day covered the two core selection tools: `loc` (label-based selection — you refer to rows/columns by their names) and `iloc` (position-based selection — you refer to rows/columns by their integer position). It also covered conditional filtering (selecting rows where a column meets some condition), combining multiple conditions with `&` and `|`, and using `isin()` to filter against a list of values. This is the skill used constantly in real analysis — almost no dataset is used in full; you're always slicing it down to what matters.

### Day 3 — Handling Missing Data
Real-world data is messy, and missing values are one of the most common problems. This day focused on **detecting** missing data with `isnull()`/`notnull()`, and **handling** it in two main ways: dropping incomplete rows with `dropna()` (with variants like `how='all'` or `subset=[...]` for more control), or filling gaps with `fillna()` — using a constant, a computed value like the column mean, or forward/backward fill (`ffill`/`bfill`) to carry nearby values into the gaps. Choosing between dropping and filling is a judgment call that depends on how much data would be lost and how important that column is.

### Day 4 — GroupBy & Aggregation
This day introduced one of Pandas' most powerful features: **`groupby()`**, which splits data into groups based on a column's values, applies a calculation to each group, and combines the results back together (the "split-apply-combine" pattern). Covered aggregations included `.mean()`, `.sum()`, `.count()`, and the more flexible `.agg()` for running multiple aggregations at once. Grouping by multiple columns, sorting grouped results, and using `value_counts()` for quick category counts were also covered. This is the backbone of most summary statistics and business reporting done in Pandas.

### Day 5 — Merging, Joining & Concatenation
Real datasets rarely live in a single table — this day covered how to **combine multiple DataFrames** together. `pd.merge()` was used to join DataFrames on a common key, with different join types (`inner`, `left`, `right`, `outer`) producing different results depending on how unmatched rows should be handled. `pd.concat()` was covered for stacking DataFrames either row-wise or column-wise, and `.join()` was introduced as a shortcut for index-based joins. The `indicator=True` parameter was also used to see exactly where each merged row came from — a useful debugging tool when merges don't behave as expected.

### Day 6 — Pivot Tables & Reshaping
This day covered how to **reshape data** into different layouts depending on what's needed for analysis or visualization. `pivot_table()` was used to summarize data by grouping on two dimensions at once (rows and columns), with different aggregation functions and handling for missing combinations via `fill_value`. The simpler `pivot()` function was compared against `pivot_table()` (no aggregation, requires unique index/column combinations), and `melt()` was introduced to go the opposite direction — converting wide data into long format. `stack()`/`unstack()` for multi-index reshaping rounded out the day.

### Day 7 — Working with Dates & Time Series
Time-based data needs special handling, and this day covered Pandas' dedicated tools for it. `pd.to_datetime()` converts string dates into proper datetime objects, unlocking the `.dt` accessor for extracting year, month, day, and weekday name. `pd.date_range()` was used to generate sequences of dates, and setting a datetime column as the index turned a regular DataFrame into a proper time series. `resample()` was covered for changing the time frequency of data (like daily to monthly), along with `.shift()` for creating lag features and `.rolling()` for moving averages — both common in trend analysis and forecasting.

### Day 8 — String Operations & Data Cleaning
Text data needs its own cleaning toolkit, covered through the `.str` accessor. This included case normalization (`.str.lower()`/`.str.upper()`), whitespace removal (`.str.strip()`), pattern matching (`.str.contains()`), splitting strings into multiple parts (`.str.split()`), and checking prefixes/suffixes (`.str.startswith()`/`.str.endswith()`). Handling duplicate rows with `.duplicated()` and `.drop_duplicates()` was also covered — an essential cleaning step before any real analysis, since duplicates silently skew aggregations and counts.

### Day 9 — Advanced Functions: apply, map, lambda
This day covered how to apply **custom logic** that built-in Pandas functions can't express directly. `.apply()` was covered on both a single Series and across whole rows (`axis=1`) for logic that needs multiple columns at once. `.map()` was introduced for fast single-column lookups and substitutions, `lambda` functions for writing short inline logic, and `applymap()` for element-wise operations across an entire DataFrame. `np.where()` was covered as a faster, vectorized alternative for simple conditional logic. Together, these tools give full flexibility to transform data in ways that go beyond Pandas' built-in methods.

### Day 10 — Mini Project (today)
The final day ties every single one of the above concepts together into one real, end-to-end analysis on an actual dataset — going from raw data to cleaned data to grouped insights to a final written summary, exactly like a real-world data analysis workflow.

---

##  Day 10 Mini Project — What This Project Demonstrates

The goal of this project is to take a real dataset from start to finish and apply every major skill learned over the 10 days in one connected workflow, rather than in isolated exercises. This mirrors what actual data analysis looks like in practice — no single technique is ever used alone; they're combined depending on what the data and the questions require.

##  Exercises Covered (10 Questions)

1. Loaded a real-world dataset using `pd.read_csv()` and explored it with `.head()`, `.info()`, and `.describe()`.
2. Checked for missing values with `isnull().sum()` and handled them using `dropna()` or `fillna()`.
3. Selected a specific subset of rows/columns using `loc`/`iloc`.
4. Created a new column based on a condition using `np.where()` or `.apply()`.
5. Used `groupby()` to compute category-wise averages, sums, and counts.
6. Converted a date column with `pd.to_datetime()` and extracted year/month/day information.
7. Built a `pivot_table()` summarizing a numeric value across two categorical columns.
8. Cleaned a text/string column using `.str.strip()`, `.str.lower()`, and removed duplicates.
9. Split the dataset into two DataFrames and recombined them using `merge()`.


##  Key Takeaway

Across these 10 days, the journey moved from **understanding the basic building blocks** (Series, DataFrame) to **selecting and cleaning data** (indexing, missing values, strings) to **summarizing and reshaping it** (groupby, pivot tables) to **combining datasets and handling time** (merge, dates) and finally to **writing custom transformation logic** (apply/map/lambda). This mini project is proof that all of these pieces work together as one connected toolkit, not separate tricks — that's what makes Pandas the standard tool for real-world data analysis in Python.

##  Files
- `day10_pandas.py` / `day10_pandas.ipynb` — solved mini project
- `README.md` — this file

---

## 🏁 10-Day Pandas Mastery Journey — Complete

Made by 
# Sudhanshu Dhande