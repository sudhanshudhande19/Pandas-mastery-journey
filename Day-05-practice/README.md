# Day 5 — Merging, Joining & Concatenation

##  Topic
Combining multiple DataFrames using `merge()`, `concat()`, and `join()` in Pandas.

##  What I Learned
- How to perform an **inner join** between two DataFrames using a common key
- The difference between `left`, `right`, `outer`, and `inner` joins
- How to concatenate DataFrames **row-wise** and **column-wise** using `concat()`
- How to use `join()` to combine DataFrames on their index, including handling overlapping column names with suffixes
- How to merge on differently-named key columns using `left_on` and `right_on`
- How to trace the origin of each row after a merge using the `indicator=True` parameter
- How merging behaves with duplicate keys (many-to-one relationships)

##  Exercises Covered
1. Created two DataFrames — `df1` (`EmployeeID`, `Name`, `Department`) and `df2` (`EmployeeID`, `Salary`, `JoiningYear`) and Performed an inner join using `pd.merge(df1, df2, on='EmployeeID')`
2. Compared `left`, `right`, and `outer` joins on mismatched keys
3. Performed row-wise concatenation using `pd.concat([df1, df2])`
4. Performed column-wise concatenation using `pd.concat([df1, df2], axis=1)`
5. Used `df1.join(df2, lsuffix='_left', rsuffix='_right')` for overlapping column names
6. Tested merge behavior with duplicate `EmployeeID` values
7. Merged DataFrames with differently named key columns using `left_on` / `right_on`
8. Used `indicator=True` to inspect the `_merge` column and understand row origin


##  Key Concept — `merge()` vs `concat()` vs `join()`

| Method | Purpose | Best used when |
|---|---|---|
| `merge()` | Combines DataFrames based on common column(s)/keys, like a SQL join | You need to match rows using a specific key column |
| `concat()` | Stacks DataFrames together, either row-wise or column-wise | You want to simply append/stack data without matching on a key |
| `join()` | Combines DataFrames based on their index | You want to combine data using index alignment rather than a column |

**In short:** `merge()` is key-based (like SQL joins), `concat()` is stacking-based, and `join()` is index-based.

## 📂 Files
- `day5_pandas.py` / `day5_pandas.ipynb` — solved exercises
- `README.md` — this file

---

**Next up:** Day 6 — Reshaping Data (Pivot Tables & Melt)