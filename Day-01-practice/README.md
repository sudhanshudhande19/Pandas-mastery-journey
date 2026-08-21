# Day 1 — Pandas Basics: Series & DataFrame

## 📅 Day 1 of 10 — Pandas Mastery Journey

###  Topics Covered
- Introduction to `pandas.Series`
- Introduction to `pandas.DataFrame`
- Creating Series from lists and dictionaries
- Creating DataFrame from dictionary of lists
- Selecting columns from a DataFrame
- Exploring data with `head()`, `tail()`, `shape`, `info()`, `describe()`
- Reading data from a CSV file with `read_csv()`
- Checking `columns` and `dtypes`

---

###  Problems Solved

1. **Series with custom index**
   Created a `Series` of 5 numbers with custom index labels (`'a', 'b', 'c', 'd', 'e'`).

2. **Series from dictionary**
   Created a `Series` from a Python dictionary and verified that dictionary keys automatically become the index.

3. **DataFrame from dictionary of lists**
   Created a `DataFrame` with 3 columns (`Name`, `Age`, `City`) and 5 rows using a dictionary of lists.

4. **Column selection**
   - Selected a single column (`Name`) → returned as a `Series`
   - Selected multiple columns (`Name`, `City`) → returned as a `DataFrame`

5. **Exploring the DataFrame**
   Used `head()`, `tail(2)`, `shape`, `info()`, and `describe()` to inspect the DataFrame and understand what each method reveals about the data.

6. **Reading a CSV file**
   Loaded a sample dataset using `pd.read_csv()` and inspected `columns` and `dtypes`.

7. **Bonus — Series vs DataFrame**
   A `Series` is a one-dimensional labeled array capable of holding any data type, similar to a single column of data with an index.
   A `DataFrame` is a two-dimensional labeled data structure — essentially a table made up of multiple Series sharing the same index, with rows and columns.

---

###  Key Learnings
- `Series` = 1D labeled array; `DataFrame` = 2D labeled table (collection of Series).
- Selecting one column with `df['col']` returns a Series; selecting multiple columns with `df[['col1','col2']]` returns a DataFrame.
- `head()`/`tail()` help preview data, `info()` shows structure & data types, `describe()` gives statistical summary of numeric columns.
- `read_csv()` is the most common way to load external data into pandas.

---

### 🔗 Progress Tracker
✅ Day 1 — Pandas Basics: Series & DataFrame
⬜ Day 2
⬜ Day 3
⬜ Day 4
⬜ Day 5
⬜ Day 6
⬜ Day 7
⬜ Day 8
⬜ Day 9
⬜ Day 10

---

*Part of the [pandas-mastery-journey](https://github.com/sudhanshudhande19) — 10-day pandas learning challenge.*
