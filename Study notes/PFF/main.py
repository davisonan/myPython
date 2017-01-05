import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
from pandas_datareader.data import Options

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2013, 1, 27)
goog = web.DataReader('GOOG', 'yahoo', start, end)
goog.ix['2010-01-04']

goog_o = Options('GOOG', 'yahoo')
goog_o.get_options_data(expiry=goog_o.expiry_dates[0])

