# Глоссарий RU ↔ EN

Каждый термин вводится как «русский смысл (english term, произношение)».
Лимит — 15–25 новых терминов в месяц. Обязательные материалы на русском;
английские термины нужны, чтобы читать документацию и вакансии.

---

## Python / инструменты

| RU | EN | Заметка |
|----|----|---------|
| окружение | environment | изолированный набор пакетов |
| зависимость | dependency | пакет, нужный проекту |
| виртуальное окружение | virtualenv / venv | |
| линтер | linter | ruff |
| тип-аннотация | type hint | `x: int` |
| тест | test | pytest |
| утверждение | assertion | `assert` |
| коммит | commit | |
| ветка | branch | |
| слияние | merge | |
| откат | revert / restore | |

## Данные

| RU | EN | Заметка |
|----|----|---------|
| признак | feature | колонка/вход модели |
| целевая переменная | target / label | что предсказываем |
| выборка | sample / dataset | |
| обучающая выборка | train set | |
| валидационная | validation set | для настройки |
| тестовая | test set | трогаем один раз |
| утечка данных | data leakage | ответ просочился в признаки |
| пропуск | missing value | NaN |
| выброс | outlier | |
| разбиение | split | |
| масштабирование | scaling / standardization | |
| категориальный признак | categorical feature | |
| переобучение | overfitting | |
| недообучение | underfitting | |
| регуляризация | regularization | L1/L2 |
| кросс-валидация | cross-validation (CV) | |

## Классический ML

| RU | EN | Заметка |
|----|----|---------|
| логистическая регрессия | logistic regression | |
| решающее дерево | decision tree | |
| случайный лес | random forest | |
| градиентный бустинг | gradient boosting | LightGBM/CatBoost |
| эвристика | heuristic / baseline | простое правило |
| точность (доля верных) | accuracy | |
| точность (precision) | precision | TP/(TP+FP) |
| полнота | recall | TP/(TP+FN) |
| порог | threshold | |
| матрица ошибок | confusion matrix | |
| объяснимость | explainability | SHAP |
| ценность признака | feature importance | |

## Нейросети и DL

| RU | EN | Заметка |
|----|----|---------|
| нейрон | neuron | |
| слой | layer | |
| полносвязный | fully connected / dense | |
| функция активации | activation function | ReLU, softmax |
| прямой проход | forward pass | |
| обратное распространение | backpropagation | |
| автоматическое дифференцирование | autograd | |
| градиентный спуск | gradient descent | |
| скорость обучения | learning rate | |
| эпоха | epoch | |
| батч | batch | |
| переобучение/регуляризация | dropout | |
| свёртка | convolution | CNN |
| доп. обучение | fine-tuning / transfer learning | |
| гиперпараметр | hyperparameter | |

## LLM

| RU | EN | Заметка |
|----|----|---------|
| токен | token | |
| токенизатор | tokenizer | BPE |
| эмбеддинг | embedding | вектор смысла |
| векторное представление | representation | |
| внимание | attention | |
| трансформер | transformer | |
| языковая модель | language model (LM) | |
| порождающая модель | generative model | |
| дообучение (настройка) | fine-tuning | |
| параметры | parameters / weights | |
| контекст | context / context window | |
| галлюцинация | hallucination | |
| подсказка | prompt | |
| инъекция подсказки | prompt injection | |
| дополнение поиском | retrieval-augmented generation (RAG) | |
| вызов инструмента | tool/function calling | |
| оценка | evaluation (eval) | |
| судья | LLM-as-a-judge | |

## MLOps / сервис

| RU | EN | Заметка |
|----|----|---------|
| развёртывание | deployment | |
| задержка | latency | p50/p95/p99 |
| пропускная способность | throughput | запросов/с |
| пакетная обработка | batching | |
| мониторинг | monitoring | |
| дрейф данных | data drift | PSI |
| откат | rollback | |
| реестр моделей | model registry | MLflow |
| непрерывная интеграция | CI/CD | GitHub Actions |
| контейнер | container | Docker |
| постмортем | postmortem | разбор инцидента |

---

## Как пополнять

В каждом месяце добавьте в свою колоду 15–25 карточек из таблиц
соответствующих тем. Формат карточки: спереди — русский термин, сзади —
английский + смысл + пример. Проверяйте себя без подглядывания.
