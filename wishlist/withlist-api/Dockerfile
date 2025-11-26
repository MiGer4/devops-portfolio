# --- ЕТАП 1: Builder (Збір залежностей) ---
FROM python:3.11-slim AS builder

# Оновлення безпеки та встановлення інструментів збірки
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libc-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /install
COPY requirements.txt .

# Встановлюємо пакети: gunicorn додано для продакшен-сервера
RUN echo "\ngunicorn" >> requirements.txt && \
    pip install --no-cache-dir --prefix=/usr/local -r requirements.txt

# --- ЕТАП 2: Final (Оптимізований образ) ---
FROM python:3.11-slim

# Копіюємо встановлені пакети та встановлюємо non-root user
COPY --from=builder /usr/local /usr/local

# Створення non-root користувача для безпеки
RUN groupadd --gid 1000 appuser && \
    useradd --uid 1000 --gid appuser --shell /bin/sh --create-home appuser

WORKDIR /app
COPY . .
RUN chown -R appuser:appuser /app

USER appuser
EXPOSE 8000

# Використовуємо Gunicorn як продакшен-сервер (4 воркери)
# command: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]