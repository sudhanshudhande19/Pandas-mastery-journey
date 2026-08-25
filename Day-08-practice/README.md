# Day 8 — String Operations & Data Cleaning

##  Topic
Working with text (string) data in Pandas — cleaning, searching, filtering, and transforming string columns using the `.str` accessor.

##  Why This Matters
Real-world datasets almost always contain messy text — inconsistent casing, extra spaces, mixed formats in emails/phone numbers, duplicate entries, etc. Before any analysis or machine learning model can use this data, it needs to be cleaned and standardized. This is one of the most common tasks in real data science work.

##  Concepts Covered

### 1. The `.str` Accessor
Pandas provides a special `.str` accessor on Series of text data, which lets you apply string operations to an **entire column at once** — instead of looping through each value manually. It works similarly to Python's built-in string methods, but is vectorized (much faster on large datasets) and automatically handles missing values (`NaN`) without crashing.

```python
df['Name'].str.lower()
```

### 2. Case Conversion
- `.str.lower()` → converts all text in a column to lowercase
- `.str.upper()` → converts all text in a column to uppercase

Useful for standardizing text before comparisons (e.g., avoiding mismatches like `"Gmail"` vs `"gmail"`).

### 3. Whitespace Cleanup
- `.str.strip()` → removes leading and trailing spaces from each value

Important because invisible extra spaces (e.g., `" Sudhanshu "`) can silently break filtering, grouping, or merging operations.

### 4. Searching Text
- `.str.contains('gmail')` → returns `True`/`False` for whether a substring exists in each value. Commonly used with filtering: `df[df['Email'].str.contains('gmail')]`
- `.str.startswith('text')` → checks if a value **begins** with a given string
- `.str.endswith('text')` → checks if a value **ends** with a given string

### 5. Splitting & Extracting
- `.str.split('@')` → splits each string into parts based on a separator, returning a list (can be expanded into new columns using `expand=True`)
- `.str.extract()` → pulls out a specific pattern (using regex) from each value into a new column

### 6. Replacing Text
- `.str.replace('-', '')` → replaces occurrences of a substring/character with another (or removes it entirely)

Useful for standardizing formats — e.g., stripping dashes from phone numbers so `9876-543-210` becomes `9876543210`.

### 7. String Length
- `.str.len()` → returns the length of each string in the column. Useful for spotting unusually short/long entries that might indicate bad data.

### 8. Handling Duplicates
- `.duplicated()` → flags rows that are exact duplicates of an earlier row (`True`/`False`)
- `.drop_duplicates()` → removes duplicate rows from the DataFrame

##  Exercises Solved
1. Created a DataFrame with `Name`, `Email`, `Phone` columns containing messy data (extra spaces, mixed case)
2. Normalized `Name` column using `.str.lower()` / `.str.upper()`
3. Removed extra whitespace using `.str.strip()`
4. Filtered rows where `Email` contains `'gmail'`
5. Cleaned `Phone` column by removing unwanted characters with `.str.replace()`
6. Split `Email` into username and domain using `.str.split('@')`
7. Checked prefixes/suffixes using `.str.startswith()` and `.str.endswith()`
8. Measured string lengths with `.str.len()` to find shortest/longest names
9. Detected and removed duplicate rows using `.duplicated()` and `.drop_duplicates()`
10. Compared `.str` accessor behavior against plain Python string methods

##  Key Takeaway — `.str` vs Normal Python String Methods
Normal Python string methods (`.lower()`, `.strip()`, etc.) only work on a **single string** at a time — you'd need a loop to apply them to a whole column. The `.str` accessor applies the same operation to **every value in a Series in one line**, is faster (vectorized), and safely skips `NaN` values instead of throwing an error. This makes it the standard way to clean text data in Pandas.

##  Files
- `day8_pandas.py` / `day8_pandas.ipynb` — solved exercises
- `README.md` — this file

---

**Next up:** Day 9 — Data Visualization with Pandas