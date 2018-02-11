import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_excel('./data/TornadoData.xlsx', 'Tornado_MinData')
print(df.head())

print(df.isnull().sum())

print(df[df['F-Scale'].isnull()].head())

print(df[df['Damage Factor'].isnull()].head())

# drop rows with null F-Scale, and null Damage Factor
# note that County_Name has two missing values, but those rows have F-Scale, and Damage Factor
# so I do not want to dro the County_Name
print(df.shape)

# if either F-Scale or Damage Factor has a missing value, then drop it.
print(df.dropna(subset=['F-Scale','Damage Factor'], how='any').shape)

# Drop the na rows
df.dropna(subset=['F-Scale','Damage Factor'], how='any', inplace=True)

# convert the data type of F-Scale to integer
df['F-Scale'] = df['F-Scale'].astype(np.int64)

# create a column with an actual numeric property damage value include factor:
# e.g. 25.0. K = 25000
def calculate_property_damage(row):
    multiplier = 1000
    if row['Damage Factor'] == 'M':
        multiplier = 1000000
    return row['Property_DMG'] * multiplier


# for each row, call the calculate_property_damage function.
# axis=1 means start at the top of the dataframe and go does, (row by row)
# and pass the row to the function.
df['Property_Damage'] = df.apply(calculate_property_damage, axis=1)

print(df.head())

# create F-Scale encoding
# One Hot Encoding
# Represent categorical variables as binary vectors
df2 = pd.get_dummies(df, prefix=['F-Level'], columns=['F-Scale'],sparse=False)

print(df2.head())


plt.scatter(df['F-Scale'],df['Property_Damage'])
plt.xlabel('F-Scale')
plt.ylabel('Property Damage')
plt.title('Damage by F Scale')

plt.show()