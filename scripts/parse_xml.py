import argparse
import os
import re

import lxml.etree
import nltk
import pandas as pd

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="The directory to operate on")
    args = parser.parse_args()
    Rows = []

    for doc in os.scandir(args.path):
        d_dict = {}
        tree = lxml.etree.parse(doc.path)
        fname = tree.find('//id')
        d_dict['id'] = fname.text
        year = tree.find('//year-start')
        year = int(year.text)
        d_dict['year'] = year
        lon = tree.find('//lat') # these are exchanged in the xml-file
        lat = tree.find('//lon') # these are exchanged in the xml-file
        if lon is None:
            d_dict['lon'] = 'None'
        if lon is not None:
            d_dict['lon'] = lon.text
        if lat is None:
            d_dict['lat'] = 'None'
        if lat is not None:
            d_dict['lat'] = lat.text
        # root = tree.getroot()
        # root.attrib['translation']
        # if root.attrib['translation'] is None:
        #     d_dict['genre'] = None
        # if root.attrib['translation'] is not None:
        #     d_dict['genre'] = root.attrib['translation']
        category = tree.find('//category')
        if category is None:
            d_dict['category'] = 'None'
        if category is not None:
            d_dict['category'] = category.attrib['translation']
        place = tree.find('//standard-name')
        if place is None:
            d_dict['location'] = 'None'
        if place is not None:
            d_dict['location'] = place.text
        Rows.append(d_dict)
    
    df = pd.DataFrame(Rows)
    df.to_csv('songs.csv', sep='\t')
