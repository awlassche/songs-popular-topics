import argparse
import csv
import glob
import os
import re
import string

import nltk
from nltk import FreqDist
import pandas as pd

TOKENIZER = nltk.tokenize.word_tokenize

def is_punct(t):
    return re.match(f'[{string.punctuation}]+$', t) is not None

if __name__ == '__main__':

    os.chdir("/Users/alielassche/documents/github/songs-popular-topics/Corpus") #pad naar de map waar je txt-documenten staan, beginnend met /Users
    words = []

    for doc in glob.glob("*.txt"):
        text = open(doc, "r", encoding="utf-8").read()
        for sentence in TOKENIZER(text, language="dutch"):
            words.extend([w.lower() for w in sentence.split() if not is_punct(w)])

    fd = FreqDist(words)
    mfw = fd.most_common(150)
    MFW = csv.writer(open('mfw.csv', 'w'))
    for key, count in mfw:
        MFW.writerow([key, count])
