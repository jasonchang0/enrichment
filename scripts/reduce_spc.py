import os
import sys
import glob
import timepont_mapper
from timepoint_mapper import switch_tp

'''
arguments:
[0]: script name
[1]: data directory under project

'''

db = sys.argv[1]  # /Users/jasonchang/Desktop/bior18/data

os.chdir()