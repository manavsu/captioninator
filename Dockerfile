FROM python:3-slim

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt --default-timeout=100

WORKDIR /app
COPY . /app

EXPOSE 7860

CMD ["python", "app.py"]
