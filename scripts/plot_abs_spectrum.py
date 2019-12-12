import os
import sys
import math
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D

style.use('fivethirtyeight')

'''
arguments:
[0]: script name
[1]: data directory under project

'''

db = sys.argv[1]  # /Users/jasonchang/Desktop/bior18/data

os.chdir(db)

# print(glob.glob('*.csv'))

df = pd.read_csv('ph_meta.csv')
df.rename({'WL/nm': 'wl'}, axis=1, inplace=True)

target_sample = 3

sub_df = df[(df['rep'] == 1) & (df['sample'] == target_sample)].drop(['rep', 'sample'], axis=1, inplace=False)

x = np.array(list(sub_df['wl']))
x = sorted(np.unique(x))

y = np.array(list(sub_df['timepoint']))
y = sorted(np.unique(y))

X, Y = np.meshgrid(x, y)

Z = np.array(list(sub_df['Abs'])).reshape(X.shape)

ax = plt.axes(projection='3d')

'''
rstride: Array row stride (step size), defaults to 1
cstride: Array column stride (step size), defaults to 1
'''
ax.plot_surface(X, Y, Z, rstride=1, cstride=5,
                cmap='inferno', edgecolor='none')

ax.set_title('Spectrophotometric pH Measurements')
ax.set_xlabel('Wavelength [nm]')
ax.set_ylabel('Time [hr]')
ax.set_zlabel('Absorbance')

plt.show()


