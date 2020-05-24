import pandas as pd

df = pd.read_csv('./data/chicago.csv').dropna(how='all')
df.columns = [i.replace(" ","_").lower() for i in df.columns]
df.department = df.department.astype('category')
print(df.nunique())

# whenver calling lower and upper use str
df.name.str.lower()
df.name.str.title()
df.name.str.upper()
df.name.str.len() # length of string
# when using replace use str
df.department.str.replace('MGMNT','Management')
df.name.str.replace('AARON','Roberts')
df.employee_annual_salary.str.replace('$','').astype(float)
# check where water is present
x1 = df[df.position_title.str.lower().str.contains('water')]
x2 = df[df.position_title.str.lower().str.startswith('water')]
x2 = df[df.position_title.str.lower().str.endswith('ist')]

# remove whitespace from string
df.name = df.name.str.lstrip().str.rstrip()
df.position_title = df.position_title.str.strip()
# you can do this to index or columns
df.columns = df.columns.str.strip()
df.set_index(keys='name', drop=True, inplace=True)
df.index = df.index.str.strip()
# split method
df = df.reset_index()
df['first_name'] = df.name.str.split(',').str.get(0).str.title()
# split and assign it back to the dataframe
df[['first_name', 'last_name']] = df.name.str.split(',', expand=True)
df[['pt1', 'pt2']] = df.position_title.str.split(' ', expand=True, n= 1)


