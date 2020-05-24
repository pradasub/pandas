import pandas as pd
from pandas_datareader import data
import datetime as dt
import matplotlib.pyplot as plt


stocks = data.DataReader(name='MSFT',data_source='yahoo', start="2010-01-01", end="2020-12-31")

stocks.loc[pd.to_datetime('2010-01-04')]
stocks.iloc[500]
stocks.iloc[-2]

stocks.index.day_name()
stocks.insert(0, 'Day_of_week', stocks.index.day_name())

# dateoffset add 5 days or subtract 5 days

stocks.index + pd.DateOffset(days = 5)
stocks.index - pd.DateOffset(days = 5)
# add or subtract 3 weeks
stocks.index + pd.DateOffset(weeks = 3)
stocks.index - pd.DateOffset(weeks = 3)
# add or subtract 3 weeks
stocks.index - pd.DateOffset(months = 3)
stocks.index + pd.DateOffset(months = 3)
# you can also add days months, hours etc.
stocks.index + pd.DateOffset(years = 1, months = 3, days = 5, hours=10, minutes=10, seconds=50)

# make all days last day of months in date
stocks.index + pd.tseries.offsets.MonthEnd()

# Time deltas
ec = pd.read_csv('./data/ecommerce.csv', parse_dates=['order_date', 'delivery_date'])
# subtract oder_date and delivery date
ec['delivery_time'] = ec.delivery_date - ec.order_date
# use time delta
pd.read_csv()
ec.sort_values( )
