# Неделя 0: установка окружения

Это не урок, а установочный гейт (2–4 часа). Отсюда начинается М1. Если что-то
не встало — разбирайтесь сейчас, а не в середине первого проекта.

---

## 0. Главное правило: путь без кириллицы

Инструменты Python ломаются на путях с русскими буквами. Создайте рабочую папку
**латиницей**, например:

- Windows: `C:\ml\`
- Linux/macOS: `~/ml/`

Все проекты курса живут внутри неё. Пример структуры:

```
ml/
├── m01-photo-sorter/
├── m02-classifier/
├── ...
└── notes/
```

## 1. Терминал

Терминал — первый барьер для новичка. Освойте минимум:

- `pwd` — где я;
- `ls` (Windows: `dir`) — что рядом;
- `cd folder` — перейти; `cd ..` — на уровень выше;
- создание папки, копирование, удаление файла.

- Windows: **Git Bash** (ставится вместе с Git) — рекомендуемый вариант.
- Linux/macOS: обычный терминал.

## 2. Python через uv

`uv` — быстрый менеджер Python-окружений и пакетов. Всё делаем через него.

1. Установите uv: см. https://docs.astral.sh/uv/ (одна команда).
2. Проверьте:
   ```bash
   uv --version
   uv python install 3.12
   ```
3. Создайте первое окружение:
   ```bash
   mkdir -p ~/ml/hello && cd ~/ml/hello
   uv init
   uv run python -c "print('привет, ML')"
   ```

Почему uv: он ставит Python сам, окружения изолированы, а команда `uv run`
запускает код в правильном окружении без ручной активации.

## 3. Git и GitHub

1. Установите Git, проверьте: `git --version`.
2. Задайте имя и почту:
   ```bash
   git config --global user.name "Ваше Имя"
   git config --global user.email "you@example.com"
   ```
3. Создайте аккаунт на https://github.com и настройте вход.
4. Первый репозиторий:
   ```bash
   cd ~/ml/hello
   git init
   git add .
   git commit -m "первый коммит"
   ```
5. Привяжите удалённый репозиторий и запушьте (интерфейс GitHub — со
   словарём/подсказками; если тяжело, начните с `gh` — CLI GitHub).

## 4. VS Code

1. Установите VS Code: https://code.visualstudio.com/
2. Расширения: **Python**, **Ruff**, **Jupyter**, **GitLens** (опционально).
3. Откройте папку `~/ml` через «File → Open Folder».
4. Настройте интерпретатор на созданное uv-окружение.

Отладчик (точки останова) появится в М3, но редактор нужен уже сейчас.

## 5. PyTorch (CPU-версия)

Базовая среда уроков — torch CPU. Проверьте установку:

```bash
cd ~/ml/hello
uv add torch --index-url https://download.pytorch.org/whl/cpu
uv run python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

Ожидаемо: версия печатается, `cuda` — `False` (это нормально для CPU-сборки).

### GPU (опционально, понадобится в М2)

Если у вас NVIDIA-карта:

1. Проверьте драйвер: `nvidia-smi` (нужен драйвер ≥ 528.33).
2. Создайте **отдельное** окружение под GPU и поставьте CUDA-сборку torch
   (подставьте свою версию CUDA/платформу с
   https://pytorch.org/get-started/locally/):
   ```bash
   uv venv --python 3.12 .venv-gpu
   uv pip install torch --index-url https://download.pytorch.org/whl/cu126
   ```
3. Проверочный matmul на GPU:
   ```bash
   uv run python -c "import torch; x=torch.randn(1000,1000,device='cuda'); print((x@x).sum().item())"
   ```

Если своей GPU нет — не страшно: тяжёлые задачи решаются на бесплатном
облачном GPU (Kaggle/Colab), см. соответствующие месяцы.

## 6. Реестр чёрных ящиков

Создайте файл `notes/blackbox.md` — сюда будете записывать непонятое с пометкой
«раскроется в месяце N» (см. `docs/00-kak-uchitsya.md`).

## 7. Проверочный скрипт

Сохраните `check.py` и запустите `uv run check.py`. Все пункты должны быть `OK`:

```python
import sys

results = []

results.append(("python", sys.version.split()[0]))

try:
    import torch
    results.append(("torch", torch.__version__))
    a = torch.randn(64, 64)
    b = torch.randn(64, 64)
    results.append(("matmul", float((a @ b).sum())))
except Exception as e:  # noqa: BLE001
    results.append(("torch", f"FAIL: {e}"))

try:
    from pathlib import Path
    p = Path.home() / "ml"
    results.append(("path ascii", str(p).isascii()))
except Exception as e:  # noqa: BLE001
    results.append(("path", f"FAIL: {e}"))

for name, value in results:
    print(f"OK  {name}: {value}")
```

Ожидаемый вывод — строка `OK  path ascii: True`. Если `False` — рабочая папка
содержит кириллицу, вернитесь к шагу 0.

---

## Чек-лист недели 0

- [ ] Рабочая папка латиницей (`~/ml` или `C:\ml`)
- [ ] Терминал: `pwd`/`ls`/`cd` без подглядываний
- [ ] uv установлен, `uv run python` работает
- [ ] Git настроен, первый коммит сделан
- [ ] Аккаунт GitHub, репозиторий запушен
- [ ] VS Code + расширение Python
- [ ] torch CPU импортируется
- [ ] `check.py` — все пункты OK, `path ascii: True`
- [ ] Создан `notes/blackbox.md`
- [ ] Прочитан `docs/00-kak-uchitsya.md`

Можно начинать [М1](../docs/months/m01.md).
