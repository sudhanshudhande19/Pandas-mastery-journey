# Day 6 — Pivot Tables & Reshaping

##  Topic
Reshaping data and building pivot tables using `pivot()`, `pivot_table()`, `melt()`, `stack()`, and `unstack()`.

##  What I Learned
- How to summarize data using `pivot_table()` with different aggregation functions (`sum`, `mean`, `count`)
- The difference between `pivot()` (no aggregation) and `pivot_table()` (with aggregation)
- How to handle missing combinations in a pivot using `fill_value`
- How to add row/column totals using `margins=True`
- How to convert data from wide format to long format using `melt()`
- How to work with multi-level indexes using `stack()`, `unstack()`, and `reset_index()`

##  Exercises Covered
1. Created a DataFrame with `Date`, `City`, `Product`, `Sales` columns
2. Built a pivot table summarizing total sales by `City` and `Product`
3. Compared `aggfunc='sum'`, `'mean'`, and `'count'` outputs
4. Used `fill_value=0` to handle missing combinations
5. Compared plain `pivot()` vs `pivot_table()`
6. Converted wide-format data to long-format using `melt()`
7. Practiced `stack()` and `unstack()` on a multi-index DataFrame
8. Added totals to a pivot table using `margins=True`
9. Created and reset a multi-level index using `set_index()` and `reset_index()`

##  Key Concept — `pivot` vs `pivot_table` vs `melt`

| Function | Purpose | Handles Duplicates? |
|---|---|---|
| `pivot()` | Reshape data (no aggregation) | ❌ No — errors on duplicate entries |
| `pivot_table()` | Reshape data **with** aggregation | ✅ Yes — aggregates duplicates |
| `melt()` | Convert wide format → long format | N/A — unpivoting operation |

**In short:** Use `pivot()` when data has no duplicate index/column pairs, `pivot_table()` when you need to aggregate, and `melt()` when you want to reshape wide data into a tidy long format.

## 📂 Files
- `day6_pandas.py` / `day6_pandas.ipynb` — solved exercises
- `README.md` — this file

---

**Next up:** Day 7 — Working with Dates & Time Series