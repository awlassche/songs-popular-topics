import argparse
import csv
import glob
import os

import nltk
from nltk import FreqDist
import pandas as pd
from utils import is_punct

TOKENIZER = nltk.tokenize.word_tokenize

if __name__ == '__main__':

    os.chdir("/Users/alielassche/documents/github/songs-popular-topics/Corpus/VARDnormalized/varded50")
    words = []

    for doc in glob.glob("*.txt"):
        text = open(doc, "r", encoding="utf-8").read()
        for sentence in TOKENIZER(text, language="dutch"):
            words.extend([w.lower() for w in sentence.split() if not is_punct(w)])

    fd = FreqDist(words)
    mfw = fd.most_common(150)
    MFW = csv.writer(open('mfw_VARD2.csv', 'w'))
    for key, count in mfw:
        MFW.writerow([key, count])
