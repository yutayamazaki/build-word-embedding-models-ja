import os
import glob
import unicodedata
from typing import List

import neologdn
from bs4 import BeautifulSoup


def remove_tag(text: str) -> str:
    soup = BeautifulSoup(text, "html.parser")
    text = soup.get_text()
    return text


def get_sentences(text: str) -> List[str]:
    sentence_list: List[str] = []
    for s in text.split("\n"):
        if s == "":
            continue
        sentence_list.append(s)
    return sentence_list


if __name__ == "__main__":
    ROOT: str = "extracted"
    OUT_TEXT: str = "sentences.txt"

    text_dirs: List[str] = glob.glob(os.path.join(ROOT, "*"))
    text_paths: List[str] = []
    for text_dir in text_dirs:
        text_paths += glob.glob(os.path.join(text_dir, "*"))

    for idx, t in enumerate(text_paths):
        with open(t, "r", encoding="utf-8") as f:
            text: str = f.read()

        text = unicodedata.normalize(u"NFKD", text)
        text = remove_tag(text)
        text = neologdn.normalize(text)
        sentences: List[str] = get_sentences(text)

        with open(OUT_TEXT, "a", encoding="utf-8") as f:
            for s in sentences:
                f.write(s + "\n")
