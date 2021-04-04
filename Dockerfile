FROM python:3.9.2-slim
WORKDIR /code
RUN apt-get -y update && \
    apt-get -y install sudo git make curl xz-utils file wget && \
    apt-get -y install mecab libmecab-dev mecab-ipadic-utf8 swig && \
    apt-get -y install python-dev gcc g++ && \
    git clone https://github.com/neologd/mecab-ipadic-neologd.git && \
    cd mecab-ipadic-neologd && \
    ./bin/install-mecab-ipadic-neologd -n -y && \
    echo `mecab-config --dicdir`"/mecab-ipadic-neologd" && \
    cd .. && \
    rm -rf mecab-ipadic-neologd && \
    apt-get autoremove -y &&\
    apt-get clean
ENV LANG en_US.utf8
ADD pyproject.toml /code
ADD poetry.lock /code
RUN pip install -U pip &&\
    pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install && \
    rm pyproject.toml poetry.lock
