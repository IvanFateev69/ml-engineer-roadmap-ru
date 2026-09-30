# Шпаргалка: NumPy

```python
import numpy as np

a = np.array([1, 2, 3])            # вектор, shape (3,)
M = np.array([[1, 2], [3, 4]])     # матрица, shape (2, 2)

a.shape, a.dtype, a.ndim
np.zeros((2, 3)), np.ones((2, 3)), np.arange(5)
np.random.default_rng(seed=42).normal(size=(2, 3))
```

## Векторные операции (без циклов)

```python
a + a          # поэлементно
a * 2          # масштаб
M @ a          # матричное умножение
a @ a          # скалярное произведение (сумма произведений)
np.sum(a), a.mean(), a.std()
np.sqrt(a), np.exp(a), np.log(a)
```

## Индексация и маски

```python
a[0], a[-1]
M[0, 1]                # элемент: строка 0, столбец 1
M[:, 0]                # весь столбец 0
a[a > 1]               # булева маска
a[[0, 2]]              # выбор по индексам
```

## Формы

```python
a.reshape(3, 1)        # (3,) -> (3, 1)
M.T                    # транспонирование
a[:, None]             # добавить ось
X.shape                # ОСНОВНОЕ: печатайте shape при каждой ошибке
```

## Broadcasting

```python
X = np.random.randn(100, 3)   # 100 примеров, 3 признака
mean = X.mean(axis=0)         # (3,) — по каждому признаку
Xc = X - mean                 # (100,3) - (3,) → (100,3)

# axis = ось, которая ИСЧЕЗАЕТ
X.sum(axis=0)   # -> (3,)
X.sum(axis=1)   # -> (100,)
```

## Копия vs представление

```python
b = a            # ссылка на тот же массив
b = a.copy()     # независимая копия
```

## Обратная матрица и линейная алгебра

```python
np.linalg.inv(M)              # обратная (осторожно с вырожденными)
np.linalg.solve(A, b)         # решить A x = b (устойчивее)
np.linalg.svd(X)              # сингулярное разложение (PCA)
w = np.linalg.lstsq(X, y, rcond=None)[0]   # МНК
```

## Численная производная (проверка аналитики)

```python
def numeric_grad(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)
```

## Нормализация (параметры — только по train!)

```python
mu, sigma = X_train.mean(0), X_train.std(0)
X_train_n = (X_train - mu) / (sigma + 1e-8)
X_val_n   = (X_val   - mu) / (sigma + 1e-8)   # те же mu/sigma
```
