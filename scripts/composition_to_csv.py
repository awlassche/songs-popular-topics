import pandas as pd

col_names = list(range(50)) #make this the same number as the number of topics in the composition.txt-file
col_names.insert(0, 'id')

composition = pd.read_csv('/Users/alielassche/applications/mallet/modern_composition_50.txt', sep='\t', index_col=0, names=col_names)
composition[['path', 'songid']] = composition.id.str.split('/modern.', expand=True)
composition = composition.drop(columns['id', 'path'])
composition[['id', 'txt']] = composition.songid.str.split('.', expand=True)
composition = composition.drop(columns=['songid', 'txt'])
composition = composition[col_names]
composition.to_csv('modern_composition_50.csv', sep='\t')