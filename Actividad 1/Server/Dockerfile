FROM ubuntu:latest
MAINTAINER Nicolás Yagui "nicolas.acevedoy@sansano.usm.cl"

RUN apt-get update && apt-get install -y python3

COPY server.py /Server/

WORKDIR /Server/