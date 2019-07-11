import os
import glob

from bs4 import BeautifulSoup


def remove_tag(text: str) -> str:
    soup = BeautifulSoup(text)
    text = soup.get_text()
    return text


def get_sentences(text: str) -> list:
    sentence_list = []
    for s in text.split('\n'):
        if s == '':
            continue
        sentence_list.append(s)
    return sentence_list


ROOT = 'extracted'
OUT_TEXT = 'sentences.txt'

text_dirs = glob.glob(os.path.join(ROOT, '*'))
text_paths = []
for text_dir in text_dirs:
    text_paths += glob.glob(os.path.join(text_dir, '*'))


for idx, t in enumerate(text_paths):
    with open(t, 'r', encoding='utf-8') as f:
        text = f.read()
    
    text = remove_tag(text)
    sentences = get_sentences(text)
    
    with open(OUT_TEXT, 'a', encoding='utf-8') as f:
        for s in sentences:
            f.write(s + '\n')