import os
import sys
import math
import numpy as np
import pandas as pd

'''
arguments:
[0]: script name
[1]: data directory under project

'''

db = sys.argv[1]  # /Users/jasonchang/Desktop/bior18/data

os.chdir(db)

# print(glob.glob('*.csv'))

'''
Experimental data for molar attenuation coefficients (kg/[mol * cm]) 
referenced from https://eprints.soton.ac.uk/365473/
'''
EPSILON_L1_HI = 18190 / 0.981
EPSILON_L1_I = 2280 / 0.981
EPSILON_L2_HI = 368.2 / 0.981
EPSILON_L2_I = 43200 / 0.981

'''
negative base-10 logarithm of the acid dissociation constant (Ka) of
bromocresol green
'''
KA = 4.0738e-05
PK2 = -math.log10(KA)

'''
Target peak wavelengths for bromocresol green
'''
L1 = 442
L2 = 616

df = pd.read_csv('ph_meta.csv')
df.rename({'WL/nm': 'wl'}, axis=1, inplace=True)

df_count = df.groupby(['timepoint', 'sample','rep'], as_index=False).size().reset_index().rename(columns={0: 'count'})

new_df = pd.DataFrame(columns=['timepoint', 'sample', 'pH1', 'pH2', 'pH3'])

new_df_dict = {}
for key in new_df.columns:
    new_df_dict[key] = []

for t in df_count['timepoint'].unique():
    for s in df_count['sample'].unique():
        pH_array = [0] * 3

        for r in df_count['rep'].unique():
            sub_df = df[(df['timepoint'] == t) & (df['sample'] == s) & (df['rep'] == r)]

            wl_range1 = sub_df[(L1 - 3 <= sub_df['wl']) & (sub_df['wl'] <= L1 + 3)]
            wl_range2 = sub_df[(L2 - 3 <= sub_df['wl']) & (sub_df['wl'] <= L2 + 3)]

            wl_agg1 = wl_range1.agg({'Abs': ['min', 'max', 'mean', 'median']}).T
            wl_agg2 = wl_range2.agg({'Abs': ['min', 'max', 'mean', 'median']}).T

            wl_abs1 = wl_agg1['mean']
            wl_abs2 = wl_agg2['mean']

            R = wl_abs2 / wl_abs1

            e1 = EPSILON_L2_HI / EPSILON_L1_HI
            e2 = EPSILON_L2_I / EPSILON_L1_HI
            e3 = EPSILON_L1_I / EPSILON_L1_HI

            pH = PK2 + math.log10((R - e1) / (e2 - e3 * R))

            pH_array[int(r) - 1] = pH

        '''
        Fill in values in the case replicates are missing
        '''
        print(pH_array)
        if any([math.isnan(_) for _ in pH_array]):
            pH_array = [pH_array[0]] * 3

        new_df_dict['timepoint'] += [t]
        new_df_dict['sample'] += [s]
        new_df_dict['pH1'] += [pH_array[0]]
        new_df_dict['pH2'] += [pH_array[1]]
        new_df_dict['pH3'] += [pH_array[2]]

# Compile meta dataframe
for key in new_df_dict:
    print(key + ': ' + str(len(new_df_dict[key])))

meta_df = pd.DataFrame.from_dict(new_df_dict, orient='columns')

print(meta_df.head())
print(meta_df.shape)

# df.dropna(axis=0, how='any', inplace=True)

meta_df.to_csv('ph_measurements.csv', index=False)


