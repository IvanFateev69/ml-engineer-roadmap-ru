# Шпаргалка: pandas

```python
import pandas as pd

df = pd.read_csv("data.csv")
df.head(), df.info(), df.describe()
df.dtypes
df.shape
```

## Отбор

```python
df["col"]
df[["a", "b"]]
df.loc[df["age"] > 30, ["name", "age"]]     # по метке/маске
df.iloc[0:5, 0:2]                            # по позиции
df[(df["a"] > 0) & (df["b"] == "x")]
```

## Группировки

```python
df.groupby("city")["amount"].mean()
df.groupby("city").agg({"amount": ["mean", "count", "max"]})
df["city"].value_counts()
df.sort_values("amount", ascending=False)
```

## Пропуски

```python
df.isna().sum()                      # сколько пропусков по колонкам
df.dropna(subset=["price"])          # удалить строки
df["x"] = df["x"].fillna(df["x"].median())
df["was_na"] = df["x"].isna()        # флаг «было пусто»
```

## Новые колонки и типы

```python
df["total"] = df["price"] * df["qty"]
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["date"] = pd.to_datetime(df["date"])
df.sort_values... 
df = df.assign(flag=df["x"] > 0)
```

## Groupby → merge

```python
left.merge(right, on="customer_id", how="left")
# ПРОВЕРЯЙТЕ число строк: merge может размножить строки (не 1:1)!
before = len(left)
merged = left.merge(right, on="k", how="left")
assert len(merged) == before, "строки размножились!"
```

## Время

```python
df["date"] = pd.to_datetime(df["date"])
train = df[df["date"] < "2024-01-01"]
valid = df[df["date"] >= "2024-01-01"]
assert train["date"].max() < valid["date"].min()
```

## SQL из pandas

```python
import sqlite3
conn = sqlite3.connect("db.sqlite")
pd.read_sql("SELECT city, AVG(amount) FROM t GROUP BY city", conn)
```

## Полезное

```python
df.duplicated().sum()
df.drop_duplicates(subset=["text"])
df.sample(5, random_state=42)
df.describe(include="all")
df["cat"].nunique()
```
