FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /newsapp

ADD . /newsapp

COPY ./requirements.txt /newsapp/requirements.txt

RUN pip install -r  requirements.txt

COPY . /newsapp/