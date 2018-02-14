# damage_factor.py

# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# Only keep those rows where the Damage Factor is 'K', or 'M' or 'B'

# imports up here can be used to
import pandas as pd


# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1=None, dataframe2=None):
    dataframe1 = dataframe1[(dataframe1['Damage Factor'] == 'K') | (dataframe1['Damage Factor'] == 'M') | (
                dataframe1['Damage Factor'] == 'B')]
    # Return value must be of a sequence of pandas.DataFrame
    return dataframe1,
