#!/bin/bash
set -eu

cd src
wget https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2
python -m wikiextractor.WikiExtractor -o extracted jawiki-latest-pages-articles.xml.bz2
python clean_format.py
python get_corpus.py
python train_word2vec.py
