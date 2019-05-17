import pandas as pd

col_names = ['topic', 'weight', 'words']

keys = pd.read_csv('/Users/alielassche/applications/mallet/modern_keys_50.txt', sep='\t', names=col_names_keys, index_col=0)
keys.to_csv('modern_keys_50.csv', sep='\t')
