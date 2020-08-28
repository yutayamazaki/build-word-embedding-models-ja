import os
import random

import MeCab
from tqdm import tqdm

IN_TEXT = 'sentences.txt'
OUT_TEXT = 'tokenized_with_mecab-ipadic-neologd.txt'
MAX_FILE_SIZE = 1e9

tagger = MeCab.Tagger(
    # '-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd'
    '-Owakati -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd'
)

with open(IN_TEXT, 'r', encoding='utf-8') as f:
    sentences = f.readlines()

random.shuffle(sentences)

with open(OUT_TEXT,'a', encoding='utf-8') as f:
    for s in tqdm(sentences):
        cleaned_s = tagger.parse(s).strip()
        f.write(cleaned_s)

        # file_size = os.path.getsize(OUT_TEXT)
        # if file_size > MAX_FILE_SIZE:
        #     exit()
