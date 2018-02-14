# property_month_year.py


# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to
import pandas as pd


# create a column with an actual numeric property damage value include factor:
# e.g. 25.0. K = 25000
def calculate_property_damage(row):
    multiplier = 1000
    if row['Damage Factor'] == 'M':
        multiplier = 1000000
    elif row['Damage Factor'] == 'B':
        multiplier = 10000000

    return row['Property_DMG'] * multiplier


# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1=None, dataframe2=None):
    # for each row, call the calculate_property_damage function.
    # axis=1 means start at the top of the dataframe and go does, (row by row)
    # and pass the row to the function.
    dataframe1['Property_Damage'] = dataframe1.apply(calculate_property_damage, axis=1)
    dataframe1['Property_Damage_Mil'] = dataframe1['Property_Damage'].apply(
        lambda x: x / 1000000.0)  # Return value must be of a sequence of pandas.DataFrame

    # add a month column to the data set
    dataframe1['Month'] = dataframe1['Date'].apply(lambda d: d.month)
    dataframe1['Year'] = dataframe1['Date'].apply(lambda d: d.year)
    return dataframe1,
