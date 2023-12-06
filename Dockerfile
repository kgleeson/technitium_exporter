FROM python:3 AS base

ARG PROMETHEUS_CLI_VER=0.11.0

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ENV TECHNITIUM_ADDRESS=http://192.168.0.1
ENV TECHNITIUM_PORT=5380
ENV TECHNITIUM_USER=admin
ENV TECHNITIUM_PASSWORD=password
ENV TECHNITIUM_TOKEN=APIKEY
ENV TECHNITIUM_WEBPORT=8080

COPY exporter/technitium-exporter.py .

EXPOSE 8080

CMD python ./technitium-exporter.py -a ${TECHNITIUM_ADDRESS} -p ${TECHNITIUM_PORT} -t ${TECHNITIUM_TOKEN}