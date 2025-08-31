# Dockerfile for Django Auth Service
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000"]