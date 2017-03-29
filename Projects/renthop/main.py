# main.py

import json
import numpy as np
import pandas as pd
import xgboost as xgb
import scikit_learn as sklearn
import matplotlib.pyplot as plt
from pprint import pprint

path = '/Users/hanya/Documents/01_Work/01_Projects/Kaggle/07_TwoSigmaJob/'

with open(path + 'train.json') as df:
    df_train = json.load(df)

df_train.keys()

df_train['description']
df_train['building_id']
df_train['photos']
df_train['latitude']
df_train['longitude']
df_train['street_address']
df_train['listing_id']
df_train['interest_level']
df_train['display_address']
df_train['bedrooms']
df_train['bathrooms']
df_train['manager_id']
df_train['price']
df_train['created']
df_train['features']


d_train = pd.read_json(path + 'train.json')


[key for key, val in df_train['building_id'].items() if val == '53a5b119ba8f7b61d4e010512e0dfc85']
sorted(d_train.index)

d_train[d_train['building_id'] == '53a5b119ba8f7b61d4e010512e0dfc85']

# The first finding is the index in d_train is the building_id
#

# 1. Extract the words in the feature column and create more features based on
# this column.
# 2. Closeness to subways
# 3. The agents' photo
# 4. The other information on the webpage
# 5. Need to do web-scrapping to get additional information on the webpage.
# 6. Figure out the way of generating the link for the page.

from collections import Counter
features = Counter(word.strip(' ,.*;&').lower() for line in d_train['features'] for words in line for word in words.split())
features.most_common(100)

features = Counter(word.lower() for line in d_train['features'] for word in line if 'war' in word.lower())

features['luxury']
['prewar', 'pre-war', 'laundry', 'dishwasher', 'doorman', ]

# Age: prewar, pre-war, new,
# Transportation: subway, garage, train, walk, bicycle, bike,
# Furniture: furnished,
# Material: marble, brick, wood,
# Appliances: dishwasher, dish, washer, laundry, wifi, internet, steel, stainless, hardwood
# Neighborhood: doorman, parking, elevator, fitness (center), swimming pool, pool, outdoor, highrise, lowrise, patio, balcony, roottop, roof, deck, terrace, loft, garden/patio
# Pets: cats, dogs,
# Fees: 'no fee' mentioned or not.
# Floors: hardwood or not.
# Wheelchair: wheelchair access, ramp
# Views: Can be extracted from photos.

# Color of hardwood floors.

## Need to find better ways to summarize the above information.
# Neighborhood convenience: Transportation
# Neighborhood comfort
# Neighborhood enjoyment:

# The distribution of prices sorted by frequencies in a descending order.
d = Counter(d_train['price']).most_common(200)
import matplotlib.pyplot as plt
plt.figure()
plt.bar(range(len(d)), [i[1] for i in d], align='center')
plt.xticks(range(len(d)), [i[0] for i in d])
plt.show()

# Given the locations, find the cloest distance to subways etc, convenience stores.



# List key words in descriptions
d_train['description']

# Counter({'high': 3839, 'low': 34284, 'medium': 11229})
Counter(d_train['interest_level'])

def f(x):
    return pd.Series({'avgPrice': np.mean(x['price']), 'n': len(x['price'])})
d_train.groupby(['interest_level']).apply(f)

#                    avgPrice        n
# interest_level
# high            2700.293045   3839.0
# low             4176.599142  34284.0
# medium          3158.767388  11229.0
# Price is a big driver in determining the interest. People basically look for
# the best price-to-quality ratio properties.


d_train.groupby(['interest_level', 'bathrooms', 'bedrooms']).apply(f).reset_index()
