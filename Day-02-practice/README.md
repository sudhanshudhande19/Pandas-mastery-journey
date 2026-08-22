# Day 2 — Indexing, Selection & Filtering

##  Topic
Selecting and filtering data in Pandas DataFrames using `loc`, `iloc`, conditional filtering, and `isin()`.

##  What I Learned
- How to select rows and columns using **label-based indexing** (`loc`)
- How to select rows and columns using **position-based indexing** (`iloc`)
- How to filter rows based on single and multiple conditions using `&` and `|`
- How to use `isin()` to filter rows against a list of values
- How to create new columns derived from existing column conditions

##  Exercises Covered
1. Created a DataFrame with columns: `Name`, `Age`, `City`, `Salary`, `Department`
2. Practiced label-based selection using `loc`
3. Practiced position-based selection using `iloc`
4. Applied single and multiple condition filtering on rows
5. Used `isin()` to filter rows matching a list of cities
6. Added a derived boolean column (`Senior`) based on an `Age` condition

##  Key Concept — `loc` vs `iloc`

| Aspect | `loc` | `iloc` |
|---|---|---|
| Basis of selection | Label / index name | Integer position |
| Example | `df.loc[2, 'Salary']` | `df.iloc[2, 3]` |
| Slicing behavior | Inclusive of end label | Exclusive of end position |
| Best used when | You know column/row **names** | You know row/column **positions** |

**In short:** `loc` works with labels (what you name things), `iloc` works with positions (where things sit numerically).

## 📂 Files
- `day2_pandas.py` / `day2_pandas.ipynb` — solved exercises
- `README.md` — this file

---

**Next up:** Day 3 — Handling Missing Data
