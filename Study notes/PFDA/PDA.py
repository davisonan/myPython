# PDA.py
# Python for Data Analysis

# 1. Run Python 2.7 to use all packages
# /usr/local/bin/python2.7

import pandas as pd

path = '/Users/xutian/Documents/3_Codes/PYTHON/usagov_bitly_data2013-05-17-1368814203'

open(path).readline()

import json

records = [json.loads(line) for line in open(path)]

# u'America/Chicago': u stands for unicode, a standard form of string encoding.
records[0]['tz']
print records[0]['tz']
