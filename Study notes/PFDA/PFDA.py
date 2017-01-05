# PFDA.py
# Python for Data Analysis

################################ Chapter 3 IPython ###############################
import numpy as np
data = {i : randn() for i in range(7)}

%run ipython_script_test.py

a = np.random.randn(100,100)
%timeit np.dot(a, a)

%reset

class Message(object):
    def __init__(self, msg):
        self._msg = msg
    def __repr__(self):
        return "Message: %s" % self._msg
    def __str__(self):
        return "Message: %s" % self._msg

msg1 = Message("I have a secret!")
msg1

#' In short, the goal of __repr__ is to be unambiguous and __str__ is to be readable.
#' Here is a good example:
import datetime
today = datetime.datetime.now()
str(today)
repr(today)

np.zeros(3)
np.zeros((3, 4))  # Tuple to indicate the shape although [3, 4] works as well.
np.arange(15)
np.empty((2, 3))

arr = np.array([1, 2, 3, 4, 5])
arr.dtype
float_arr = arr.astype(np.float64)

arr = np.arange(10)
arr[5]
arr[5:8]
arr[5:8] = 12  # Notice the difference with list

lst = list(np.arange(10))
lst[5:8] = 12  # TypeError: can only assign an iterable

#' Slices of numpy array are only views of the original array.
arr_slice = arr[5:8]
arr_slice[1] = 12345
arr
arr_slice[:] = 64
arr

arr[5:8].copy()

# Chapter 4 NumPy
# Chapter 5 Pandas
# Chapter 6 Data loading, storage, and File Formats
# Chapter 7 Data Wrangling
# Chapter 8 Plotting and Visualization
# Chapter 9 Data Aggregation and Group Operations
# Chapter 10 Time Series
# Chapter 11 Financial and Economic Data Applications
# Chapter 12 Advanced NumPy

############################### Chapter 2 Introductory Examples ###############################
path = '/Users/hanya/Github/PfDA/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

open(path).readline()

import json
records = [json.loads(line) for line in open(path)]

# The u here in front stands for unicode
records[0]
records[0]['tz']
print records[0]['tz']

time_zones = [rec['tz'] for rec in records if 'tz' in rec]

time_zones[:10]

# need to use the %paste trick to copy the following function into iPython
# 1. Copy the lines you want to copy into IPython into the clipboard
# 2. Enter %paste into IPython
# 3. Press enter
# 4. Profit!
def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

counts = get_counts(time_zones)

## Using pandas
from pandas import DataFrame, Series
import pandas as pd
import numpy as np

frame = DataFrame(records)

frame

frame['tz'].value_counts()

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz==''] = 'Unknown'
tz_counts = clean_tz.value_counts()
tz_counts[:10].plot(kind='barh', rot=0)

results = Series([x.split()[0] for x in frame.a.dropna()])
results.value_counts()

cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('windows'), 'Windows', 'Not Windows')
by_tz_os = cframe.groupby('tz', by=operating_system)

## MovieLens 1M Data Set
import pandas as pd
import os as os
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
os.getcwd()
os.chdir('/Users/hanya/Documents/3_Codes/Python/PFDA/')
users = pd.read_table('ml-1m/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ml-1m/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('ml-1m/movies.dat', sep='::', header=None, names=mnames)

data = pd.merge(pd.merge(ratings, users), movies)

mean_ratings = data.pivot_table(values='rating', index='title', columns='gender', aggfunc=mean) # this is different from the book

ratings_by_title = data.groupby('title').size()

ratings_by_title[:10]

active_titles = ratings_by_title.index[ratings_by_title >= 250]

active_titles

mean_ratings = mean_ratings.ix[active_titles]

mean_ratings

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)

############################### Chapter 1 Preliminaries ###############################
ipython --pylab

import pandas

plot(arange(10))

############################### Chapter 1 Preliminaries ###############################



