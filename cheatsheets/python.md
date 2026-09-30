# Шпаргалка: Python

## Переменные и типы

```python
x = 1            # int
y = 3.14         # float
s = "привет"     # str
b = True         # bool
n = None         # «ничего»
f"{x} + {y} = {x + y}"   # f-строка
```

## Коллекции

```python
lst = [1, 2, 3]                 # список (меняемый, порядок)
tup = (1, 2, 3)                 # кортеж (неизменяемый)
d = {"a": 1, "b": 2}            # словарь ключ→значение
st = {1, 2, 3}                  # множество (уникальные)

lst[-1]                         # последний элемент
d.get("c", 0)                   # безопасно, с дефолтом
len(lst), sum(lst), max(lst)
sorted(lst, reverse=True)
```

## Циклы и условия

```python
for x in lst: ...
for i, x in enumerate(lst): ...
for k, v in d.items(): ...

while cond: ...

if x > 0: ...
elif x == 0: ...
else: ...
```

## Функции

```python
def f(a, b=10, *, c=1):   # c — только по имени
    return a + b + c

f(1, c=5)                  # позиционные и именованные
```

## Файлы и JSON

```python
from pathlib import Path
Path("out").mkdir(parents=True, exist_ok=True)

with open("f.txt", "w", encoding="utf-8") as fh:
    fh.write("текст\n")

import json
json.dump(data, open("a.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
data = json.load(open("a.json", encoding="utf-8"))
```

## Исключения

```python
try:
    risky()
except FileNotFoundError as e:
    print("нет файла:", e)
except (ValueError, KeyError):
    ...
finally:
    ...
```

## Классы и dataclass

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

from dataclasses import dataclass

@dataclass
class Report:
    name: str
    score: float = 0.0
```

## Замыкания, декораторы, генераторы

```python
def make_counter():
    n = 0
    def inc():
        nonlocal n
        n += 1
        return n
    return inc

def timed(fn):
    def wrapper(*args, **kw):
        import time
        t0 = time.perf_counter()
        out = fn(*args, **kw)
        print(f"{fn.__name__}: {time.perf_counter()-t0:.3f}s")
        return out
    return wrapper

def batches(xs, size):
    for i in range(0, len(xs), size):
        yield xs[i:i + size]
```

## Типы

```python
def scale(x: float, k: int = 2) -> float: ...
items: list[int] = []
mapping: dict[str, float] = {}
maybe: int | None = None
```

## Окружение (uv)

```bash
uv init
uv add numpy pandas matplotlib
uv run python script.py
uv run pytest -q
```
