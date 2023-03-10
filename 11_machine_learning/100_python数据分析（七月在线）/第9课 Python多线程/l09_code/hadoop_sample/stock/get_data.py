import math
import numpy as np
import pandas as pd
import tushare as ts

df = ts.get_hist_data('300340', start = '2016-01-01', end = '2016-12-31')
for k, v in df['p_change'].iteritems():
    v = math.floor(float(v))
    print('%s,%d' % (k, v))
