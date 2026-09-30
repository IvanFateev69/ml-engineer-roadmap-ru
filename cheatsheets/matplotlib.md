# Шпаргалка: matplotlib

```python
import matplotlib
matplotlib.use("Agg")  # без графического окна (для скриптов/CI)
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(x, y, label="train")
ax.plot(x, y2, label="val")
ax.set_xlabel("эпоха")
ax.set_ylabel("потеря")
ax.set_title("Кривые обучения")
ax.legend()
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig("loss.png", dpi=120)
plt.close(fig)
```

## Частые графики

```python
# scatter: предсказание против факта
ax.scatter(y_true, y_pred, s=8, alpha=0.5)
ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], "r--")
ax.set_xlabel("факт"); ax.set_ylabel("предсказание")

# histogram: распределение
ax.hist(values, bins=30)

# bar: категории
ax.barh(labels, counts)

# изображение / матрица ошибок
ax.imshow(cm, cmap="Blues")
```

## Несколько графиков

```python
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].plot(loss); axes[0].set_title("loss")
axes[1].plot(acc);  axes[1].set_title("accuracy")
axes[2].hist(residuals); axes[2].set_title("остатки")
fig.tight_layout()
```

## Правила хорошего графика

- Подписи осей и заголовок — **всегда**.
- Легенда, если больше одной линии.
- Единицы измерения в подписи («потеря», «₽», «мс»).
- Сохраняйте в PNG (`savefig`) для отчёта; закрывайте фигуру (`plt.close`).
- Для датасета: сделайте 4 графика (распределения, пропуски, выбросы,
  корреляции) и вставьте в README.
