import argparse
import csv
import os

import lxml.etree
import nltk
from nltk import FreqDist
import pandas as pd
from utils import is_punct

TOKENIZER = nltk.tokenize.word_tokenize

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="The directory to operate on")
    args = parser.parse_args()
    words = []

    for doc in os.scandir(args.path):
        tree = lxml.etree.parse(doc.path)
        fname = tree.find('//id')
        year = tree.find('//year-start')
        year = int(year.text)
        text = tree.find('//text')
        chars = ''.join(text.itertext())
        if year >= 1550 and year <= 1750:
            for sentence in TOKENIZER(chars, language="dutch"):
                words.extend([w.lower() for w in sentence.split() if not is_punct(w)])

    fd = FreqDist(words)
    mfw = fd.most_common(200)
    MFW = csv.writer(open('mfw.csv', 'w'))
    for key, count in mfw:
        MFW.writerow([key, count])
