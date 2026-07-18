FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY backend/requirements.txt .


RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt


COPY . .

WORKDIR /app/backend

EXPOSE 8000

# CMD ["uvicorn", "ap.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# for prod
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]