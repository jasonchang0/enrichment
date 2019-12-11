import os
import sys
import glob
import pandas as pd
import timepoint_mapper
from timepoint_mapper import switch_tp

'''
arguments:
[0]: script name
[1]: data directory under project

'''

db = sys.argv[1]  # /Users/jasonchang/Desktop/bior18/data

os.chdir(db)

# print(glob.glob('*.csv'))

'''
Parse PH spectrum files

Example: 'PHT04S61.csv'
'''
df = pd.DataFrame(columns=['timepoint', 'sample', 'rep', 'WL/nm', 'Abs'])

df_dict = {}
for key in df.columns:
    df_dict[key] = []

for file in glob.glob('PH*.csv'):
    time_ind = int(file[3:5])
    sample = int(file[6])
    rep = int(file[7])

    timepoint = switch_tp(time_ind)

    df = pd.read_csv(file)

    df.reset_index(drop=False, inplace=True)
    df.columns = df.iloc[0]

    df.drop(0, axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)

    num_WL = len(df['WL/nm'])
    # num_WL = len(df.index)

    if num_WL != 1401:
        print(file)
        print(num_WL)
        print(df.head())

    df_dict['timepoint'] += [timepoint] * num_WL
    df_dict['sample'] += [sample] * num_WL
    df_dict['rep'] += [rep] * num_WL
    df_dict['WL/nm'] += list(df['WL/nm'])
    df_dict['Abs'] += list(df['Abs'])

# Compile meta dataframe
for key in df_dict:
    print(key + ': ' + str(len(df_dict[key])))

meta_df = pd.DataFrame.from_dict(df_dict, orient='columns')

print(meta_df.head())
print(meta_df.shape)

# df.dropna(axis=0, how='any', inplace=True)

meta_df.to_csv('ph_meta.csv', index=False)







