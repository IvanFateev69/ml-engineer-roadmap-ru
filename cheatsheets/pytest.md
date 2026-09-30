# Шпаргалка: pytest

## Файлы и запуск

- файлы `test_*.py` или `*_test.py`;
- функции `test_*`;
- запуск: `uv run pytest -q`, один файл: `uv run pytest tests/test_x.py -q`.

## Базовый тест

```python
def test_add():
    assert 2 + 2 == 4
```

## Ошибки

```python
import pytest

def test_raises():
    with pytest.raises(ValueError, match="размерности"):
        matmul(a, b_wrong_shape)
```

## Приближённые числа

```python
from math import isclose

def test_metric():
    assert isclose(my_mae(y, p), sklearn_mae(y, p), rel_tol=1e-9)
```

## Параметризация

```python
@pytest.mark.parametrize("x,expected", [(1, 1), (2, 4), (3, 9)])
def test_square(x, expected):
    assert x ** 2 == expected
```

## Фикстуры

```python
import pytest

@pytest.fixture
def sample_df():
    return pd.DataFrame({"a": [1, 2], "b": [3, 4]})

def test_cols(sample_df):
    assert list(sample_df.columns) == ["a", "b"]
```

## Временные файлы

```python
def test_write(tmp_path):
    p = tmp_path / "out.csv"
    write_report([(1, "a")], p)
    assert p.exists()
```

## Полезные приёмы

```python
# 1. Тест должен падать на сломанной реализации.
# 2. Проверяйте краевые случаи: пусто, один элемент, дубликаты.
# 3. Одна проверка = одна идея; имя теста описывает поведение.
# 4. Тест данных: пересечение train/val по хешу == 0.
# 5. Мутационная проверка: намеренно сломать функцию и убедиться,
#    что тесты это поймали.
```

## Покрытие

```bash
uv add --dev pytest-cov
uv run pytest --cov=my_package --cov-report=term-missing
```

## Детерминизм

```python
import random
import numpy as np

random.seed(42)
np.random.seed(42)
```
