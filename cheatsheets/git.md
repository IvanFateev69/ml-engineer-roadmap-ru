# Шпаргалка: git

## Настройка (один раз)

```bash
git config --global user.name "Ваше Имя"
git config --global user.email "you@example.com"
```

## Базовый цикл

```bash
git init
git status
git add .            # или git add file.py
git commit -m "что сделано"
git log --oneline
```

## Удалённый репозиторий

```bash
git remote add origin https://github.com/USER/REPO.git
git branch -M main
git push -u origin main
git pull
```

## Посмотреть изменения

```bash
git diff                 # не закоммиченные изменения
git diff --staged        # то, что в индексе
git show HEAD            # последний коммит
```

## Откат

```bash
git restore file.py              # вернуть файл к последнему коммиту
git restore --staged file.py     # убрать из индекса
git revert <hash>                # новый коммит, отменяющий изменения
git reset --soft HEAD~1          # отменить коммит, оставив изменения
```

## Ветки

```bash
git branch                  # список
git switch -c feature       # новая ветка
git switch main
git merge feature
```

## .gitignore

```
.venv/
__pycache__/
data/
*.pt
.env
```

Если файл уже в индексе, а надо игнорировать:

```bash
git rm --cached file
```

## Полезное

```bash
git clone URL
git remote -v
git log --oneline --graph --all
```

## Правила хорошего коммита

- Один коммит — одно логическое изменение.
- Сообщение в повелительном наклонении: «добавить split», «исправить утечку».
- Коммитьте часто; перед рискованным изменением — коммит.
- Никогда не коммитьте секреты (`.env`), большие данные и `.venv`.
