import pandas as pd

'''
Experimental data for molar attenuation coefficients (kg/[mol * cm]) 
referenced from https://eprints.soton.ac.uk/365473/
'''
EPSILON_L1_HI = 18190
EPSILON_L1_I = 2280
EPSILON_L2_HI = 368.2
EPSILON_L2_I = 43200


'''
Target peak wavelengths for bromocresol green
'''
L1 = 442
L2 = 616

df = pd.read_csv('ph_meta.csv')
df.rename({'WL/nm': 'wl'}, axis=1, inplace=True)

df_count = df.groupby(['timepoint', 'sample','rep'], as_index=False).size().reset_index().rename(columns={0: 'count'})


for t in df_count['timepoint'].unique():
    for s in df_count['sample'].unique():
        for r in df_count['rep'].unique():
            sub_df = df[(df['timepoint'] == t) & (df['sample'] == s) & (df['rep'] == r)]


