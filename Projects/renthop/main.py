# main.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from itertools import product
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import StratifiedKFold

path = '/Users/hanya/Documents/01_Work/01_Projects/Kaggle/07_TwoSigmaJob/'

d_train = pd.read_json(path + 'train.json')

d_train.head()

[key for key, val in df_train['building_id'].items() if val == '53a5b119ba8f7b61d4e010512e0dfc85']
sorted(d_train.index)

d_train[d_train['building_id'] == '53a5b119ba8f7b61d4e010512e0dfc85']

def add_features(df):
    fmt = lambda s: s.replace("\u00a0", "").strip().lower()
    df["photo_count"] = df["photos"].apply(len)
    df["street_address"] = df['street_address'].apply(fmt)
    df["display_address"] = df["display_address"].apply(fmt)
    df["desc_wordcount"] = df["description"].apply(len)
    df["pricePerBed"] = df['price'] / df['bedrooms']
    df["pricePerBath"] = df['price'] / df['bathrooms']
    df["pricePerRoom"] = df['price'] / (df['bedrooms'] + df['bathrooms'])
    df["bedPerBath"] = df['bedrooms'] / df['bathrooms']
    df["bedBathDiff"] = df['bedrooms'] - df['bathrooms']
    df["bedBathSum"] = df["bedrooms"] + df['bathrooms']
    df["bedsPerc"] = df["bedrooms"] / (df['bedrooms'] + df['bathrooms'])

    df = df.fillna(-1).replace(np.inf, -1)
    return df

# The first finding is the index in d_train is the building_id
#

# 1. Extract the words in the feature column and create more features based on
# this column.
# 2. Closeness to subways
# 3. The agents' photo
# 4. The other information on the webpage
# 5. Need to do web-scrapping to get additional information on the webpage.
# 6. Figure out the way of generating the link for the page.
# 7. Lightening of the photos. Convolutional neural networks.

features = Counter(word.strip(' ,.*;&').lower() for line in d_train['features'] for words in line for word in words.split())
features.most_common(100)

descs = Counter(word.strip(' ,.*;&?!-').lower() for line in d_train['description'] for word in line.split())
descs.most_common(100)

# features = Counter(word.lower() for line in d_train['features'] for word in line if 'war' in word.lower())

features['luxury']
['prewar', 'pre-war', 'laundry', 'dishwasher', 'doorman']

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

# Condition: new, renovated, etc

# Color of hardwood floors.

## Need to find better ways to summarize the above information.
# Neighborhood convenience: Transportation
# Neighborhood comfort
# Neighborhood enjoyment:

# The distribution of prices sorted by frequencies in a descending order.
d = Counter(d_train['price']).most_common(200)
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

d_train.iloc[2]['features']
d_train.iloc[2]['description']


iFeatures = [1 if i else 0 for i in d_train['features']]
iDescriptions = [1 if i else 0 for i in d_train['description']]

d_train['iFeature'] = iFeatures
d_train['iDesc'] = iDescriptions

a = d_train.groupby(['interest_level', 'iFeature', 'iDesc']).apply(f).reset_index()
b = d_train.groupby(['interest_level']).agg(['count'])['description'].reset_index()
c = pd.merge(a, b, on='interest_level')
c['pct%'] = c['n']/c['count'] * 100


d_train[['building_id', 'listing_id', 'manager_id']].T.apply(lambda x: x.nunique(), axis=1)


features = pd.DataFrame({'feature': [j for i in d_train.features.values for j in i]})
features['dummy'] = 1
features.groupby('feature').count().sort_values('dummy', ascending=False)




# Use Google API to plot apartments on GPS
import json
import pandas as pd
import gpxpy as gpx
import gpxpy.gpx
gpx = gpxpy.gpx.GPX()

for index, row in d_train.iterrows():
    if row['interest_level'] == 'high':
        gps_waypoint = gpxpy.gpx.GPXWaypoint(row['latitude'], row['longitude'], elevation=10)
        gpx.waypoints.append(gps_waypoint)

filename = "test.gpx"
FILE = open(filename,"w")
FILE.writelines(gpx.to_xml())
FILE.close()
print ('Created GPX:')


#' # Clustering apartments based on their lat and lons
#' See this [post](https://www.kaggle.com/luisblanche/two-sigma-connect-rental-listing-inquiries/neighborhoods-instead-of-lat-long).
