FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=10000

CMD ["gunicorn", "skm_service.wsgi:application", "--bind", "0.0.0.0:10000"]
