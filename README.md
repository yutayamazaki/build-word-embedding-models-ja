# Word2Vec-ja
## How to Train Word2Vec in Japanese.
1. Donload Wikipedia corpus(jawiki-latest-pages-articles.xml.bz2) from [here](https://dumps.wikimedia.org/jawiki/latest/).
2. Download WikiExtractor.py from [here](https://github.com/attardi/wikiextractor).
3. And execute WikiExtractor.py
4. Execute clean_format.py
5. Execute get_corpus.py
6. Execute train_word2vec.py

## Training

```shell
docker build . -t w2v
docker run -it -v $PWD:/code w2v bash run.sh
```
