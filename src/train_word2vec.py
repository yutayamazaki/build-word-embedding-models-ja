import logging

import yaml
from gensim.models import word2vec


with open('config.yaml', 'r') as f:
    config = yaml.load(f, Loader=yaml.SafeLoader)

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO
)

sentences = word2vec.Text8Corpus(config['corpus'])
model = word2vec.Word2Vec(sentences, vector_size=config['size'])

model.save(config['model_name'])
