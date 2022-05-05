# -*- coding: utf-8 -*-
"""
Created on Wed May  4 09:58:16 2022

@author: unpat
"""

import pandas as pd

date_file = r'C:\Users\unpat\_Data\Python_and_Tableau_DA_Bootcamp_Dee\transaction.csv'
data = pd.read_csv(date_file, sep = ';')

# summary of the data
data.info()

# CostPerTransaction calculation
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# adding a new column 'CostPerTransaction' to the dataframe
data['CostPerTransaction'] = CostPerTransaction

# adding a new column 'SalesPerTransaction' to the dataframe
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit calculation and adding column 'ProfitPerTransaction'
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = (Sales - Cost) / Cost --> (Sales - Cost) = data['ProfitPerTransaction']
# Adding a new column 'Markup'

data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction']

# Rounding 'Markup'
data['Markup'] = roundmarkup = round(data['Markup'], 2)

# Combining date fields and adding 'date' field
data['date'] = data['Day'].astype(str) + '-' + data['Month'] + '-' + data['Year'].astype(str)

# Splitting 'ClientKeywords' into multiple columns
split_col = data['ClientKeywords'].str.split(',', expand = True)

# Adding new columns after splitting
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

# Replacing '[' & ']' replace function
data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')

# Change the 'ItemDescription' from upper case to lower case
data['ItemDescription'] = data['ItemDescription'].str.lower()

seasons_file = r'C:\Users\unpat\_Data\Python_and_Tableau_DA_Bootcamp_Dee\DA_PythonTableau_ValueIncSales\data\value_inc_seasons.csv'
seasons = pd.read_csv(seasons_file, sep = ';')

# Merge data & season dataframes
data = pd.merge(data, seasons, on = 'Month')

# Dropping unnecessary columns
data = data.drop(['ClientKeywords','Day','Month','Year'], axis = 1)

# Exporting the final dataframe into a csv file
data.to_csv(r'C:\Users\unpat\_Data\Python_and_Tableau_DA_Bootcamp_Dee\ValueInc_Cleaned.csv', index = False)






















