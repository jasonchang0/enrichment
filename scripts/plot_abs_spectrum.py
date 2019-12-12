import os
import sys
import math
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

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


