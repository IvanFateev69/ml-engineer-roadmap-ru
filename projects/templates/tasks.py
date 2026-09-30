"""Шаблон tasks.py — единая точка входа в проект (MIT).

Замените заглушки своей логикой. Команды:
    uv run tasks.py data
    uv run tasks.py train
    uv run tasks.py check
    uv run tasks.py serve
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import sys
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")
REPORTS = Path("reports")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("tasks")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def cmd_data() -> None:
    """raw -> processed. Должна быть идемпотентной: повторный запуск
    не меняет файлы при тех же входных данных."""
    PROCESSED.mkdir(parents=True, exist_ok=True)
    log.info("подготовка данных из %s", RAW)
    # TODO: прочитать raw, почистить, записать processed
    # Проверьте контрольную сумму результата:
    # digest = sha256(PROCESSED / "dataset.csv")
    # (PROCESSED / "dataset.sha256").write_text(digest)
    log.info("готово")


def cmd_train() -> None:
    """Обучение модели. Перед запуском убедитесь, что есть prediction.md."""
    REPORTS.mkdir(parents=True, exist_ok=True)
    if not Path("prediction.md").exists():
        log.warning("нет prediction.md — сначала зафиксируйте прогноз!")
    log.info("обучение…")
    # TODO: обучение, метрики, чекпоинт, графики
    metrics = {"accuracy": 0.0, "baseline_accuracy": 0.0, "n_test": 0}
    (REPORTS / "metrics.json").write_text(
        json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    log.info("метрики: %s", metrics)


def cmd_check() -> None:
    """Быстрые проверки целостности: данные на месте, тесты зелёные."""
    ok = RAW.exists() or PROCESSED.exists()
    log.info("данные найдены: %s", ok)
    if not ok:
        sys.exit(1)


def cmd_serve() -> None:
    """Локальный запуск сервиса (М9+)."""
    log.info("запуск сервиса…")
    # TODO: uvicorn.run(...)


def main() -> None:
    parser = argparse.ArgumentParser(description="Задачи проекта")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("data", help="подготовить данные")
    sub.add_parser("train", help="обучить модель")
    sub.add_parser("check", help="проверить целостность")
    sub.add_parser("serve", help="запустить сервис")

    args = parser.parse_args()
    {
        "data": cmd_data,
        "train": cmd_train,
        "check": cmd_check,
        "serve": cmd_serve,
    }[args.command]()


if __name__ == "__main__":
    main()
