# Day 4 — GroupBy & Aggregation

##  Topic
Grouping data and computing summary statistics using `groupby()`, `.agg()`, and `value_counts()`.

##  What I Learned
- How `groupby()` follows the **Split-Apply-Combine** pattern to summarize data
- How to compute group-wise statistics: `.mean()`, `.sum()`, `.count()`
- How to run multiple aggregations at once using `.agg()`
- How to group by multiple columns for hierarchical summaries
- How to sort grouped results using `sort_values()`
- How to use `value_counts()` to check distribution of a categorical column
- The conceptual difference between `groupby()` and `pivot_table()`

##  Exercises Covered
1. Created a DataFrame with `Department`, `Employee`, `Salary`, `Age` columns (10+ rows, multiple departments repeating)
2. Used `groupby('Department')` to compute average, total, and count of employees per department
3. Applied `.agg(['mean','max','min'])` for multiple aggregations in a single call
4. Grouped by multiple columns — `groupby(['Department','Age'])`
5. Sorted grouped results by highest average salary using `sort_values()`
6. Used `value_counts()` on the `Department` column to check category distribution

##  Key Concepts

### Split-Apply-Combine
`groupby()` works in three stages:
- **Split** — divide data into groups based on a key column
- **Apply** — run a function (mean, sum, count, etc.) on each group independently
- **Combine** — merge the results back into a single summarized output

### `.agg()` for Multiple Aggregations
Instead of calling `.mean()` and `.max()` separately, `.agg(['mean','max','min'])` computes several statistics in one call — more efficient and readable.

### Grouping by Multiple Columns
`df.groupby(['col1','col2'])` creates a hierarchical grouping — first splits by `col1`, then further splits each group by `col2`. Useful for finer-grained summaries.

### `value_counts()`
Counts occurrences of each unique value in a column. It's essentially a shortcut for `groupby(column).size()`, commonly used to quickly understand category distribution.

### `groupby()` vs `pivot_table()`

| Aspect | `groupby()` | `pivot_table()` |
|---|---|---|
| Output format | Long format — one row per group | Wide format — cross-tabulated (rows × columns) |
| Best for | General group-wise aggregation | Visual, side-by-side comparisons |
| Under the hood | Base grouping engine | Built on top of `groupby()` internally |

**In short:** `pivot_table()` is a more presentation-friendly wrapper around `groupby()`, reshaping results into a readable grid instead of a long list.

## 📂 Files
- `day4_pandas.py` / `day4_pandas.ipynb` — solved exercises
- `README.md` — this file

---

**Next up:** Day 5 — Merging, Joining & Concatenating DataFrames