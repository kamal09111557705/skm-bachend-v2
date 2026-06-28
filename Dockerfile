FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=10000

CMD ["sh", "-c", "python manage.py makemigrations accounts && python manage.py migrate && python manage.py collectstatic --noinput && gunicorn skm_service.wsgi:application --bind 0.0.0.0:$PORT"]
