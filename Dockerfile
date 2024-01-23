FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit==2023.9.4
RUN pip install lazyqsar==0.3
RUN pip install pandas
RUN pip install numpy
RUN pip install xgboost==2.0.3
RUN pip install joblib==1.2.0
RUN pip install lightgbm==3.3.5

WORKDIR /repo
COPY . /repo
