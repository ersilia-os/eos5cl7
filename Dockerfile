FROM bentoml/model-server:0.11.0-py311
MAINTAINER ersilia

RUN apt-get update && apt-get install -y libgomp1 && rm -rf /var/lib/apt/lists/*
RUN pip install rdkit==2023.9.4
RUN pip install lazyqsar==1.0
RUN pip install pandas==2.2.3
RUN pip install numpy==1.26.4
RUN pip install xgboost==2.0.3
RUN pip install joblib==1.2.0
RUN pip install lightgbm==3.3.5
RUN pip install chemprop==2.2.0
RUN pip install matplotlib==3.10.3
RUN pip install seaborn==0.13.2

WORKDIR /repo
COPY . /repo
