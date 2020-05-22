import pandas as pd

sm = pd.read_csv('./data/salesmen.csv', parse_dates=['Date'])
sm.Salesman = sm.Salesman.astype('category')

sm_pivot = sm.pivot(index='Date', columns='Salesman', values='Revenue')

foods = pd.read_csv('./data/foods.csv')

foods.pivot_table(values='Spend', index='Gender', aggfunc='mean')
foods.pivot_table(values='Spend', index=['Gender','Item'], columns= 'City', aggfunc='mean')
foods.pivot_table(values='Spend', index=['Gender','Item'], columns= ['City','Frequency'], aggfunc='mean')

# melt
qt = pd.read_csv('./data/quarters.csv')
qt.melt(id_vars='Salesman', var_name='Quarter', value_name='Revenue')