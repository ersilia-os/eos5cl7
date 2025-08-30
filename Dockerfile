FROM bentoml/model-server:0.11.0-py312
MAINTAINER ersilia

RUN pip install lazyqsar[descriptors]==1.0

WORKDIR /repo
COPY . /repo
