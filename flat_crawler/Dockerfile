ARG PYTHON_VERSION=3.10.12
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /usr/src/app

COPY /flat_crawler/requirements.txt /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 5432

CMD scrapy crawl scrapper
