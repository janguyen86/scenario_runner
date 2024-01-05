FROM hangqiu/carla:0.9.13
LABEL authors="janice"
ARG CARLA_VERSION=0.9.13
ARG PYTHON_VERSION=3.7

USER root

RUN apt-get update
RUN apt-get install -y git

USER carla

