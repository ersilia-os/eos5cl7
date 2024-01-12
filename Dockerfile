FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN pip install rdkit==2022.9.2
RUN pip install lazyqsar==0.3
RUN pip install pandas
RUN pip install numpy
RUN pip install xgboost == 2.0.3
RUN pip install joblib == 1.2.0

WORKDIR /repo
COPY . /repo
