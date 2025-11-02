# Understanding `reset_index()` in Pandas

When you use:

```python
df.groupby('day')['tip'].mean()
```

you get a **Series** (or DataFrame) where the column `'day'` becomes the **index** — meaning it’s used as labels on the left side, not as a regular column.

**Example:**

```
day
Fri     2.73
Sat     2.99
Sun     3.25
Thur    2.77
Name: tip, dtype: float64
```

---

When you add `.reset_index()`:

```python
df_grouped = df.groupby('day')['tip'].mean().reset_index()
```

it moves `'day'` back into the table as a **normal column** instead of leaving it as an index.

**Result:**

```
     day   tip
0    Fri  2.73
1    Sat  2.99
2    Sun  3.25
3   Thur  2.77
```

---

>[!Important]
> `reset_index()` turns the grouped key (like `'day'`) back into a regular column — making your DataFrame look like a clean, well-structured table again.
