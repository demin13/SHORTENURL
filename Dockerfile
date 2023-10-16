FROM python:3.10
LABEL authors="Shekhar Anand"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/
EXPOSE 8000
EXPOSE 8443