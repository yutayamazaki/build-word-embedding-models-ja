# Word2Vec-ja
## How to Train Word2Vec in Japanese.
1. Donload Wikipedia corpus(jawiki-latest-pages-articles.xml.bz2) from [here](https://dumps.wikimedia.org/jawiki/latest/).
2. Download WikiExtractor.py from [here](https://github.com/attardi/wikiextractor).
3. And execute WikiExtractor.py
4. Execute clean_format.py
5. Execute get_corpus.py
6. Execute train_word2vec.py

```shell
python3 -m venv venv
pip install -r requirements.txt
wget https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2
python -m wikiextractor -o extracted jawiki-latest-pages-articles.xml.bz2
python clean_format.py
python get_corpus.py
```
