import pandas as pd
import numpy as np

nba = pd.read_csv('./data/nba.csv').dropna(how='all')
nba.Salary.fillna(0, inplace=True)
nba.College.fillna('None', inplace=True)
nba.Salary = nba.Salary.astype('int')
nba.Age = nba.Age.astype('float')

# ----------------------------------------------------------
# pandas astype category can help  reduce a memory by a lot
# when you have only few category for the whole data
# -----------------------------------------------------------

nba.Position = nba.Position.astype('category')

# get the unique value for any particular column
print(nba.Position.nunique())

# Sort
nba.sort_values(by=['Age'], ascending=True, inplace=True)
nba.sort_values(by=['Salary'], ascending=False, na_position='last')

# by default NA values are sorted to the end after highest values
nba.sort_values(by=['Team', 'Name'], ascending=True, inplace=True)
nba.sort_values(by=['Team', 'Name'], ascending=False, inplace=True)
# provide a list of booleans if you want to sort one by ascending and
# other by descending
nba.sort_values(by=['Team', 'Name'], ascending=[True, False], inplace=True)
# to sort by index
nba.sort_index(inplace=True)



