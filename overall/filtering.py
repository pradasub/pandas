import pandas as pd

emp = pd.read_csv('./data/employees.csv')
emp.columns = [i.replace(" ", "_").lower() for i in emp.columns]
emp.start_date = pd.to_datetime(emp.start_date)
emp.senior_management = emp.senior_management.astype(bool)
emp.gender = emp.gender.astype('category')

emp = emp[emp.salary > 1000]

# check nulls
x1 = emp[emp.team.isnull()]
x2 = emp[emp.gender.notnull()]

# between
x3 = emp[emp.salary.between(60000, 70000)]
emp = emp.sort_values(by=['first_name'])
first = emp.first_name.duplicated(keep='first')
last = emp.first_name.duplicated(keep='first')

# keep either only duplicates or only uniques
only_duplicates = emp[emp.first_name.duplicated(keep=False)]
only_uniques = emp[~emp.first_name.duplicated(keep=False)]
drop_dups = emp.drop_duplicates(keep='first')
drop_dups = emp.drop_duplicates(keep='last')
drop_dups = emp.drop_duplicates(keep=False)
drop_dups = emp.drop_duplicates(subset=['first_name'])

emp.drop_duplicates(inplace=True)

# unique genders for emp
print(emp.gender.unique())
print(emp.gender.nunique(dropna=False)) # does not use na values


