import pandas as pd

nba = pd.read_csv('./data/nba.csv').dropna(how='all')
nba.Salary = nba.Salary.fillna(0).astype(float)
nba['Rank'] = nba.Salary.rank(ascending=False).astype(int)
nba.sort_values(by=['Salary'], inplace=True, ascending=False)