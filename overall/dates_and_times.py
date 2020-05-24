import pandas as pd
import numpy as np
import datetime as dt

# python native timestamp examples
print(dt.date.today())
someday = dt.date(2010, 1, 20)
print(someday.month); print(someday.day); print(someday.year)

somedaytime = dt.datetime(2010, 1, 20, 8, 13, 57)
str(somedaytime)

# pandas timestamp
pd.Timestamp("2105-03-15")
pd.Timestamp("2105/03/15")
pd.Timestamp("1/1/2015")
pd.Timestamp("2015-03-08 6:13:19 PM")
pd.Timestamp(dt.date(2015,1,2))
pd.read_csv('./data/')

dates = ["2016-01-01", "2016-04-12", "2009/09/07"]
dates = ["2016/01/01", "2016/04/12", "2009/09/07"]
dtIndex = pd.DatetimeIndex(dates)

values = [100,200,300]
pd.Series(data=values, index = dtIndex)

# pd.to_datetime()

pd.to_datetime("2001-04-19")
pd.to_datetime(dt.date(2015,1,1))
pd.to_datetime(["2015", "2015-01", "2016-09-29"])
times = pd.Series(["2015-03-03", "2014-02-08", "2016", "July 4th, 1996"])
pd.to_datetime(times)
times2 = pd.Series(["2015/03/03", "2014-02-08", "2016", "July 4th, 1996", "Hello", "Prada"])
pd.to_datetime(times2, errors='coerce')

# pd.date_range
times3 = pd.date_range(start="2016-01-01", end="2019-01-24", freq="D")
times3 = pd.date_range(start="2016-01-01", end="2019-01-24", freq="5D")
times3 = pd.date_range(start="2016-01-01", end="2019-01-24", freq="B")
times3 = pd.date_range(start="2016-01-01", end="2019-01-24", freq="W")
times3 = pd.date_range(start="2016-01-01", end="2019-01-24", freq="H")
times3 = pd.date_range(start="2016-01-01", end="2019-01-24", freq="M")
times3 = pd.date_range(start="2016-01-01", end="2019-01-24", freq="MS")
times3 = pd.date_range(start="2016-01-01", periods=25, freq="MS")
print(times3)

# check .dt
bunch_of_dates =pd.date_range(start="2000-01-01", end="2010-12-13", freq="24D")
s = pd.Series(bunch_of_dates)
d = s.dt.day
m = s.dt.month
y = s.dt.year
wd = s.dt.weekday_name
qs = s.dt.is_quarter_start
s[qs]






