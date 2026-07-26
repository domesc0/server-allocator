FROM python:3.11-slim

WORKDIR /app

# Függőségek telepítése
RUN pip install --no-cache-dir fastapi uvicorn jinja2

# Alkalmazásfájlok másolása
COPY app.py .
COPY templates/ templates/
COPY config.json .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]