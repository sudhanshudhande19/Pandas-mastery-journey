# Day 6 — Pivot Tables & Reshaping

##  Overview
Day 6 of the **Pandas Mastery Journey** covers how to reshape data between different layouts — a critical skill for reporting, visualization, and preparing data for machine learning. Data often needs to move between "wide" formats (one row per entity, values spread across columns) and "long" formats (one row per observation), depending on the task at hand.

This day explores pivot tables for summarizing data, `melt()` for unpivoting, and `stack()`/`unstack()` for working with multi-level indexes.

##  Learning Objectives
By the end of this day's practice, the goal is to be comfortable with:
- Building a pivot table with `pivot_table()`
- Applying different aggregation functions within a pivot table
- Handling missing combinations with `fill_value`
- Understanding the difference between `pivot()` and `pivot_table()`
- Converting wide-format data to long format using `melt()`
- Using `stack()` and `unstack()` on multi-index DataFrames
- Adding row/column totals with `margins=True`
- Working with multi-level indexes and resetting them

##  Exercises Covered

| # | Concept | Method(s) Used |
|---|---------|-----------------|
| 1 | Creating a DataFrame with categorical + numeric data | `pd.DataFrame()` |
| 2 | Building a pivot table | `pd.pivot_table(values, index, columns, aggfunc)` |
| 3 | Changing aggregation function | `aggfunc='mean'/'count'` |
| 4 | Filling missing pivot cells | `fill_value=0` |
| 5 | Plain pivot without aggregation | `df.pivot()` |
| 6 | Unpivoting wide to long format | `pd.melt()` |
| 7 | Stacking a multi-index DataFrame | `df.stack()` |
| 8 | Unstacking a multi-index DataFrame | `df.unstack()` |
| 9 | Adding totals to a pivot table | `margins=True` |
| 10 | Setting and resetting multi-level index | `set_index([...])`, `reset_index()` |

##  Key Concept — `pivot()` vs `pivot_table()` vs `melt()`

**`pivot()`** reshapes data without any aggregation — it assumes each index/column combination has exactly one value, and will raise an error if duplicates exist.

**`pivot_table()`** is a more flexible version of `pivot()` that supports aggregation (mean, sum, count, etc.), making it suitable for datasets with duplicate index/column combinations.

**`melt()`** does the opposite of pivoting — it converts wide-format data (many columns) into long-format data (fewer columns, more rows), which is often the required shape for plotting libraries and statistical models.

**In short:** use `pivot()` for simple, unique reshaping, `pivot_table()` when aggregation is needed, and `melt()` to unpivot data back into a long format.

##  Files
- `day6_pandas.py` / `day6_pandas.ipynb` — solved exercises
- `README.md` — this file

##  Series Progress
- ✅ Day 1 — Pandas Basics: Series & DataFrame
- ✅ Day 2 — Indexing, Selection & Filtering
- ✅ Day 3 — Handling Missing Data
- ✅ Day 4 — GroupBy & Aggregation
- ✅ Day 5 — Merging, Joining & Concatenation
- ✅ Day 6 — Pivot Tables & Reshaping

---

**Next up:** Day 7 — Working with Dates & Time Series