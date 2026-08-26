# Day 9 — Advanced Functions: apply, map, lambda

##  Topic
Applying custom logic and transformations to Pandas Series and DataFrames using `apply()`, `map()`, `applymap()`, `lambda` functions, and `np.where()`.

##  Overview

When built-in Pandas operations aren't enough to transform data the way you need, you write your own logic and "apply" it across a Series or DataFrame. This is one of the most powerful and frequently used skills in real-world data work — cleaning messy columns, creating derived features, applying business rules, and reshaping values row by row.

Today's practice covers four closely related but distinct tools:

- **`apply()`** — runs a function across an entire Series, or across rows/columns of a DataFrame
- **`map()`** — runs a function or maps values using a dictionary, but only on a single Series
- **`applymap()`** (or `.map()` on a DataFrame in newer Pandas) — runs a function element-wise across every cell of a DataFrame
- **`lambda`** — a short, throwaway function defined inline, often used inside `apply()`/`map()` instead of writing a full `def`

##  Concept 1: `apply()` on a Series

`Series.apply(func)` runs a function on every value in a column. Useful when you need to transform a single column with custom logic that plain arithmetic or built-in methods can't handle.

```python
def add_bonus(x):
    return x * 1.1

df['Salary'] = df['Salary'].apply(add_bonus)
```

This multiplies every value in the `Salary` column by 1.1 — effectively adding a 10% bonus to everyone.

##  Concept 2: `apply()` with `lambda`

A `lambda` lets you write the same logic in a single line, without defining a separate function. It's most useful for short, one-off transformations.

```python
df['Salary'] = df['Salary'].apply(lambda x: x * 1.1)
```

This does exactly the same thing as `add_bonus`, just written inline. As a rule of thumb: use `lambda` for simple one-liners, and a proper `def` function when the logic has multiple steps or needs to be reused.

##  Concept 3: `map()` for value substitution

`map()` works only on a Series (a single column), and it's ideal for two situations:
1. Replacing values using a dictionary
2. Applying a simple function element-wise

```python
def categorize_age(age):
    if age < 30:
        return 'Young'
    elif age < 50:
        return 'Middle'
    else:
        return 'Senior'

df['AgeGroup'] = df['Age'].map(categorize_age)
```

Or using a dictionary directly:

```python
mapping = {25: 'Young', 45: 'Middle', 60: 'Senior'}
df['AgeGroup'] = df['Age'].map(mapping)
```

`map()` is generally faster and more readable than `apply()` when you're just doing a lookup or a simple transformation on one column.

##  Concept 4: Row-wise `apply()` with `axis=1`

When a transformation needs values from **multiple columns** at once, `apply()` is called on the whole DataFrame with `axis=1`, which passes each row (as a Series) into the function.

```python
def combine_info(row):
    return f"{row['Name']} earns {row['Salary']} at age {row['Age']}"

df['Summary'] = df.apply(combine_info, axis=1)
```

Here, `row` behaves like a dictionary/Series where you can access any column by name — this is the key difference from column-wise `apply()`, which only sees one column's values at a time.

##  Concept 5: `applymap()` — element-wise across the whole DataFrame

`applymap()` (or `.map()` on a DataFrame in newer Pandas versions) applies a function to **every single cell** in the DataFrame, regardless of column.

```python
df_numeric = df[['Age', 'Salary']].applymap(lambda x: round(x, 2))
```

This is useful for blanket formatting operations — like rounding every number, or stripping whitespace from every string — across an entire DataFrame at once.

##  Concept 6: `np.where()` for vectorized conditionals

`np.where()` is not part of `apply()`/`map()` family, but it's commonly used alongside them for fast conditional column creation without writing a custom function at all.

```python
df['SalaryLevel'] = np.where(df['Salary'] > 50000, 'High', 'Low')
```

This is much faster than `apply()` for simple if/else logic because it's vectorized (runs in C under the hood) rather than looping row by row in Python.

##  Concept 7: Returning multiple values from `apply()`

Sometimes a single row-wise function needs to produce **two or more new columns** at once. This is done by returning a list/tuple/Series from the function and using `result_type='expand'`.

```python
def split_info(row):
    return [row['Salary'] * 0.1, row['Age'] + 1]

df[['Bonus', 'NextAge']] = df.apply(split_info, axis=1, result_type='expand')
```

This avoids having to call `apply()` twice for two related derived columns.

##  Key Differences Summary

| Function | Works On | Best For | Speed |
|---|---|---|---|
| `apply()` (Series) | One column | Custom row-by-row logic on a single column | Slower than vectorized ops |
| `apply()` (DataFrame, `axis=1`) | Whole rows | Logic that needs multiple columns together | Slower — loops row by row |
| `map()` | One column only | Dictionary lookups or simple value transforms | Fast, simple |
| `applymap()` | Every cell in DataFrame | Blanket formatting across all columns | Slower for large DataFrames |
| `np.where()` | Whole column (vectorized) | Simple if/else conditions | Fastest |

**Rule of thumb:**
- Use `np.where()` first if the logic is a simple condition.
- Use `map()` for single-column lookups or substitutions.
- Use `apply()` when you need custom logic that `map()` or vectorized functions can't express.
- Use `applymap()` only when the same transformation truly applies to every cell in the DataFrame.

##  Exercises Covered

1. Built a DataFrame with `Name`, `Age`, `Salary` columns.
2. Added a 10% bonus to `Salary` using `.apply()` with a named function.
3. Repeated the same bonus calculation using `.apply()` with a `lambda`.
4. Converted `Age` into categories (`Young`/`Middle`/`Senior`) using `.map()`.
5. Wrote a row-wise function combining `Age` and `Salary` using `df.apply(func, axis=1)`.
6. Rounded all numeric values across the DataFrame using `.applymap()`.
7. Created a `High`/`Low` salary column using `np.where()`.
8. Wrote a function that returns two values at once, expanded into two new columns using `result_type='expand'`.
9. Combined `.apply()` with `sorted()` to sort a column by custom logic (like string length).
10. Documented the differences between `apply()`, `map()`, and `applymap()`.

##  Files
- `day9_pandas.py` / `day9_pandas.ipynb` — solved exercises
- `README.md` — this file

---

**Next up:** Day 10 — Mini Project (combining everything learned so far)