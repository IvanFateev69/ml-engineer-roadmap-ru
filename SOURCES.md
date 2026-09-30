# Источники

Курированная подборка. Обязательные материалы — на русском (или с русской
инструкцией); англоязычные идут как «глубже». Символы: ✔ — ссылка проверена,
○ — канонический адрес. У каждого источника своя лицензия — соблюдайте её.
Этот список — указатель, а не копия: тексты роадмапа авторские.

---

## Язык, SWE, окружение (М1–М5, М9)

- Мэтиз «Изучаем Python», 3-е издание (RU) — главы 2–11, 15–16. Основа языка.
- ✔ MIT Missing Semester — https://missing.csail.mit.edu (структура тем shell/git;
  лицензия NC — только «почитать»).
- ○ Русский перевод — https://missing-semester-rus.github.io
- ✔ Python Packaging User Guide — https://packaging.python.org
- ○ uv (менеджер окружений) — https://docs.astral.sh/uv/
- ○ ruff (линтер/форматтер) — https://docs.astral.sh/ruff/
- ○ mypy (типы) — https://mypy.readthedocs.io
- ✔ calmcode (короткие уроки, в т.ч. pytest) — https://calmcode.io
- ○ Python docs: sqlite3, threading, asyncio, re, json, logging —
  https://docs.python.org/3/library/ (частично есть RU: https://docs.python.org/ru/3/)
- ✔ Exercism Python (практика, репозитории трека MIT) — https://github.com/exercism/python
- ✔ letpy.com (RU-тренажёр Python, опционально) — https://letpy.com
- ✔ deep-ml (задачи по ML-математике) — https://www.deep-ml.com

## Классический ML и математика (М3–М5, М11)

- Berkeley Data 100 textbook (BSD-3) — https://ds100.org/course-notes/ — pandas,
  EDA, регрессия, CV, bootstrap, проверка гипотез.
- «Машинное обучение» (RU) — логрег, деревья, ансамбли, метрики.
- Хьюен «Проектирование систем машинного обучения» (RU) — главы 3–9.
- ✔ Google ML Crash Course — https://developers.google.com/machine-learning/crash-course
- ✔ Google Rules of ML — https://developers.google.com/machine-learning/guides/rules-of-ml
- ✔ CS229 main notes / summer2019 — https://cs229.stanford.edu/main_notes.pdf ,
  https://cs229.stanford.edu/summer2019/
- ✔ cs231n notes — https://cs231n.github.io (NumPy, backprop, CNN, transfer learning)
- ○ MIT 6.390 open notes — https://introml.mit.edu/notes/ (только чтение)
- Kaggle Learn: Intro/Intermediate ML, Pandas, Data Cleaning, Intro to SQL —
  https://www.kaggle.com/learn/
- ○ «Грокаем алгоритмы» (RU) — хеш-таблицы, сложность.

## Данные, пайплайны, версионирование (М3)

- ○ pandera (валидация схем) — https://pandera.readthedocs.io
- ○ DVC (версионирование данных) — https://dvc.org/doc
- ✔ MLOps Zoomcamp (EN, глубже) — https://github.com/DataTalksClub/mlops-zoomcamp
- ✔ Made With ML (SWE-дисциплина для ML) — https://madewithml.com ,
  https://github.com/GokuMohandas/Made-With-ML

## DL-основы и внутренности (М6–М8)

- ✔ Karpathy «Neural Networks: Zero to Hero» — https://karpathy.ai/zero-to-hero.html
  (micrograd, makemore, GPT; код MIT) — ключевой источник М6–М8.
- ○ Karpathy micrograd — https://github.com/karpathy/micrograd
- ○ Karpathy build-nanogpt — https://github.com/karpathy/build-nanogpt
  («коммит = шаг» — образец ведения проекта).
- ○ Karpathy «A Recipe for Training Neural Networks» —
  https://karpathy.github.io/2019/04/25/recipe/
- ✔ Stanford CS336 «Language Modeling from Scratch» — https://cs336.stanford.edu/
  (задания MIT; лучший бесплатный курс по LLM с нуля).
- ✔ Raschka LLMs-from-scratch — https://github.com/rasbt/LLMs-from-scratch (код MIT).
- ✔ CMU 10-714 Deep Learning Systems — https://dlsyscourse.org/ (видео/слайды).
- ✔ Harvard mlsysbook / TinyTorch / StaffML — https://mlsysbook.ai ,
  https://mlsysbook.ai/staffml/ (идеи и методика; лицензия CC — проверяйте).
- ✔ stas00/ml-engineering (CC-BY-SA) — https://github.com/stas00/ml-engineering
- ✔ How to Scale Your Model (Roofline, масштабирование) — https://jax-ml.github.io/scaling-book/
- ✔ LLM Inference Handbook (CC BY) — https://handbook.modular.com/
- ✔ LLM Engineer's Toolkit (карта библиотек LLM-стека) —
  https://github.com/KalyanKS-NLP/llm-engineer-toolkit

## Обучение и железо (facts)

- ✔ NVIDIA Pascal Tuning Guide (FP16 на cc 6.1) —
  https://docs.nvidia.com/cuda/pascal-tuning-guide/index.html
- ○ Kaggle kernels metadata (выбор GPU, `machine_shape`) —
  https://github.com/Kaggle/kaggle-api/blob/main/docs/kernels_metadata.md
- ○ Colab FAQ — https://research.google.com/colaboratory/faq.html
- ○ PyTorch install matrices — https://pytorch.org/get-started/locally/

## Serving, MLOps, инференс (М9, М12)

- ✔ CMU 17-645 «Machine Learning in Production» — https://mlip-cmu.github.io/ ,
  книга https://mlip-cmu.github.io/book/ (CC BY-NC-ND — только чтение; структура
  лабораторных — ориентир).
- ✔ Full Stack Deep Learning 2022 (архив) — https://fullstackdeeplearning.com/course/2022/
- ○ ONNX Runtime — https://onnxruntime.ai/docs/
- ○ MLflow — https://mlflow.org/docs/latest/
- ✔ Evidently (наблюдаемость, дрейф) — https://www.evidentlyai.com/ml-observability-course
- ○ Streamlit — https://docs.streamlit.io
- ✔ Google MLOps levels / ML Test Score / Hidden Technical Debt —
  https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
- ✔ Chip Huyen — https://github.com/chiphuyen/dmls-book , https://github.com/chiphuyen/aie-book

## LLM / AI engineering (М10, М11)

- ✔ Hugging Face Learn (12 курсов) — https://huggingface.co/learn
- ✔ anthropics/courses (MIT) — https://github.com/anthropics/courses
- ✔ LangChain Academy (MIT) — https://academy.langchain.com/courses/intro-to-langgraph
- ✔ RAG from scratch — https://github.com/langchain-ai/rag-from-scratch
- ✔ mlabonne/llm-course — https://github.com/mlabonne/llm-course
- ○ LLM Zoomcamp — https://github.com/DataTalksClub/llm-zoomcamp
- ✔ W&B AI Academy — https://wandb.ai/site/courses
- ○ sentence-transformers — https://www.sbert.net
- ○ multilingual-e5-small (RU-эмбеддинги) — https://huggingface.co/intfloat/multilingual-e5-small
- ○ Gemini API — https://ai.google.dev/gemini-api/docs
- «Промт-инжиниринг для LLM» (RU); Huyen «AI Engineering» (EN, глубже).

## Ответственный AI

- ✔ fairmlbook — https://fairmlbook.org
- ○ Model Cards (Mitchell et al., 2019) — https://arxiv.org/abs/1810.03993
- NIST AI RMF / EU AI Act — читать первоисточники (бэклог).

## Практика и тренажёры

- ✔ Kaggle Learn — https://www.kaggle.com/learn/
- ✔ Exercism — https://github.com/exercism/python
- ✔ letpy — https://letpy.com
- ✔ labex Linux Journey (основы Linux) — https://labex.io/linuxjourney
- ✔ build-your-own-x (список «собери X сам») — https://github.com/codecrafters-io/build-your-own-x
- ✔ deep-ml — https://www.deep-ml.com
- ✔ tensorgym — https://tensorgym.com

## Книги из личной библиотеки (только ссылки на главы)

- Мэтиз «Изучаем Python» (RU) — язык, pytest (гл. 11 в 3-м изд.), matplotlib.
- «Машинное обучение» (RU) — М4, М6.
- Хьюен «Проектирование систем МО» (RU) — М3, М4, М7, М9, М12.
- «Промт-инжиниринг для LLM» (RU) — М7, М10.
- Huyen «AI Engineering» (EN) — М10–М11, глубже.
