FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install lazyqsar==0.3
RUN pip install pandas
RUN pip install numpy

WORKDIR /repo
COPY . /repo
