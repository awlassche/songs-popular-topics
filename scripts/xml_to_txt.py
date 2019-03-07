import os

import lxml.etree

if __name__ == '__main__':

    for doc in os.scandir('/Users/alielassche/documents/github/meertens-song-collection-master/xml'):
        tree = lxml.etree.parse(doc.path)
        songid = tree.find('//id')
        fname = songid.text
        text = tree.find('//text')
        lyrics = ''.join(text.itertext())
        with open(str(fname) + '.txt', 'w') as f:
            f.write(lyrics)