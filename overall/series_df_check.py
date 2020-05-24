import pandas as pd
import numpy as np
# CREATE A DATAFRAME

# different ways of getting numbers
x1 = np.arange(100)
x2 = np.array([1,100])
x3 = np.linspace(1, 100, 100)

# creating a data frame
x4 = np.arange(10)
x5 = np.linspace(1,20,10)
x6 = np.linspace(1,100,10)
y1 = pd.DataFrame({'a': x4, 'b': x5, 'c':x6})
s1 = y1.get('a')
y1.insert(0, 'das2', y1.c.apply(lambda x: x/100))
# Series
y2 = pd.Series(x4)
# Series from dict
z1 = pd.Series({'a':1, 'b':2, 'c':3})
z1.sort_values(ascending=False, inplace=True)
z1.sort_index(ascending=True, inplace=True)
# Apply
z1 = z1.apply(lambda x: 2*x)
