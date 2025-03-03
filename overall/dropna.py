import pandas as pd
import numpy as np

nba = pd.read_csv('./data/nba.csv')
# dropna.py everywhere
no_na_nba = nba.dropna()
# subset drop
nba.dropna(subset=['College'], inplace=True)
nba.dropna(subset=['College', 'Salary'], inplace=True)
# remove when all rows have NA
nba.dropna(how='all', inplace=True)
# remove any columns that have null values
nba.dropna(axis=1)

# FIll na
# fillna for the whole dataframe
nba.fillna(0, inplace=True)
# fillna for a particular column
nba['Salary'].fillna(0, inplace=True)
nba.College.fillna('prada', inplace=True)


