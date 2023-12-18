import pandas as pd

# file_name = pd.read_csv('file.csv') <--- Format of read_csv

data = pd.read_csv("transaction2.csv", sep = ';')
data

# Summary of the data
data.info() 

# Working with Calculations

# Defining variables

# Mathematical Operations on Tableau

#ProfitPerItem = SellingPricePerItem - CostPerItem
#ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
#CostPerTransaction = CostPerItem*NumberOfItemsPurchased 
#SellingPricePerTransaction = SellingPricePerItem*NumberOfItemsPurchased

# CostPerTransaction Column calculation

# CostPerTransaction = CostPerItem*NumberOfItemsPurchased
# Variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem*NumberOfItemsPurchased

# Adding new column to dataframe

data['CostPerTransaction'] = CostPerTransaction

# Sales per Transaction

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation =  Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup = (Sales - Cost) / Cost

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

data['Markup'] = (data['ProfitPerTransaction']) / data['CostPerTransaction']

# Rounding Markup: Round(variable,digits)

# roundmarkup = round(data['Markup'], 2)

data['Markup'] = round(data['Markup'])

# Combining date field

# my_date = data['Day'] + '-' + data['Month'] + '-' + data['Year']  
 
# Checking column data type
print(data['Day'].dtype)
print(data['Month'].dtype)
print(data['Year'].dtype)


# Change column type
day = data['Day'].astype(str)
month = data['Month'].astype(str)
year = data['Year'].astype(str)

my_date = day + '-' + month + '-' + year

data['Date'] = my_date

# Using iloc to view specific column

data.iloc[0] #views the row with index number 0.
data.iloc[0:3] #views first 3 rows
data.iloc[-5:] #last 5 rows

data.head(5) #first five rows

data.iloc[:,2] # get's all rows of column 3.
data.iloc[4,2] #brings 4th row in 2nd column

# Split client keywords fiels
# new_variable = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',', expand = True)

# creating new columns for the split column in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

# Using replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

# Using the lower function to change ItemDescription to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

# Bringing in new dataset

season = pd.read_csv('value_inc_seasons.csv', sep = ';')

# Merging files: pd.merge(old_df, new_df, on = 'key')

data = pd.merge(data, season, on = 'Month')

# Dropping Columns
# dataframe = dataframe.drop('columnname' , axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)

# Export into csv
data.to_csv('ValueInc_Cleaned.csv', index = False)

