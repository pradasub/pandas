import pandas as pd

bond = pd.read_csv('./data/jamesbond.csv', index_col=None)  # assign any column for index_col

# reset_index set_index
bond.set_index(keys='Year', inplace=True)

bond.reset_index(drop=True, inplace=True)

bond.sort_index(inplace=True)

# To get the largest values you can use n_largest
bond.nlargest(5, columns='Box Office')
bond.nsmallest(5, columns='Box Office')

# sample dataframe
bond.sample(n=10)
bond.sample(frac=0.1)

# location
# loc can be used for row and column identifier
print(bond.loc['1962', 'Film'])
print(bond.iloc[0, 0])
print(bond.loc['1962'])
print(bond.loc['1962': '1972'])

bond2 = bond.apply(lambda x: x[1] * 2, axis="columns")
bond3 = bond.apply(lambda x: x * 2)
