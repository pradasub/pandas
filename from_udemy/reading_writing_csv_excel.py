import pandas as pd
# if a csv link is available
baby_names = pd.read_csv('https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv')

baby_names["Child's First Name"].to_frame()
baby_names["Child's First Name"].tolist()
baby_names["Child's First Name"].to_dict()
", ".join(baby_names["Child's First Name"].str.title().drop_duplicates().sort_values())
baby_names.to_csv('./data/baby_names.csv', index=False, columns=["Year of Birth", "Child's First Name"], encoding='utf-8')

# Excel
ex_data1 = pd.read_excel('./data/Data - Single Worksheet.xlsx')
ex_data2 = pd.read_excel('./data/Data - Single Worksheet.xlsx', index=None)
ex_data3 = pd.read_excel('./data/Data - Multiple Worksheets.xlsx', sheet_name='Data 1')
ex_data4 = pd.read_excel('./data/Data - Multiple Worksheets.xlsx', sheet_name=['Data 1', 'Data 2'])
ex_data5 = pd.read_excel('./data/Data - Multiple Worksheets.xlsx', sheet_name=None)


# writing to excel file
girls = baby_names[baby_names['Gender'] == 'FEMALE'].copy()5
boys = baby_names[baby_names['Gender'] == 'MALE'].copy()5

excel_file = pd.ExcelWriter('./data/Baby_Names.xlsx')
girls.to_excel(excel_file, sheet_name='girls', index=None, columns=['Year of Birth', 'Gender'])
boys.to_excel(excel_file, sheet_name='boys', index=None, columns=['Year of Birth', 'Gender'])
excel_file.save()
