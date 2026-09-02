FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN playwright install --with-deps chromium

COPY . .

ENV PORT=5000
EXPOSE 5000

CMD gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 120