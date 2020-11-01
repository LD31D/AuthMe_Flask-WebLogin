FROM python:3.8

MAINTAINER LD31D

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD python main.py