import pandas as pd

fone = pd.read_csv('./data/fortune1000.csv', index_col=('Rank'))

sec = fone.groupby('Sector')

# group by extractions
sec.first()
sec.size()
sec.last()
sec.get_group('Energy')
sec.get_group('Technology')
sec.max()
sec.min()
sec["Revenue"].sum()

# agg method
sec.agg({"Revenue": "sum", "Profits": "sum", 'Employees': "mean"})
sec.agg(["size", "sum", "mean"])

sec.agg({"Revenue": ["sum","mean"], "Profits": "sum", 'Employees': "mean"})

# customer data
w1 = pd.read_csv('./data/Restaurant - Week 1 Sales.csv')
w2 = pd.read_csv('./data/Restaurant - Week 2 Sales.csv')
cu = pd.read_csv('./data/Restaurant - Customers.csv')
foods = pd.read_csv('./data/Restaurant - Foods.csv')

w1_w2 =  pd.concat([w1, w2], ignore_index=False)
w1_w2 =  pd.concat([w1, w2], ignore_index=True)
w1_w2 =  w1.append(w2, ignore_index=True)
pd.concat([w1, w2], keys=['week_1','week_2'])

# inner join
w1.merge(w2, how='inner', on='Customer ID', suffixes=['_w1', '_w2'])

w1.merge(w2, how='inner', on=['Customer ID','Food ID'], suffixes=['_w1', '_w2'])

# outer is interesting 
w1.merge(w2, how="outer",on="Customer ID", suffixes=['_w1', '_w2'], indicator=True)
#left
w1.merge(foods, how='left', on='Food ID', sort=True)

w2.merge(cu, how='left', left_on='Food ID', right_on='ID').drop('ID', axis=1)
# use join method if you need to concatenate data frame by index
w2.columns = ['check1', 'check2']
w1.join(w2)









