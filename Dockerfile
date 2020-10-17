FROM python:3.7-slim

RUN apt-get update && apt-get install -y libpq-dev gcc

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV PORT=5050

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

ENV MUTATIONS_ENABLED=1
CMD gunicorn -w 4 "strawapp.app:create_app()" -b 0.0.0.0:$PORT

