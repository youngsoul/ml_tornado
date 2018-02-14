# fscale_dummies.py

# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to
import pandas as pd


# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1=None, dataframe2=None):
    # create F-Scale encoding
    # One Hot Encoding
    # Represent categorical variables as binary vectors
    dataframe1 = pd.concat(
        [dataframe1['F-Scale'], pd.get_dummies(dataframe1, prefix=['F-Scale'], columns=['F-Scale'], sparse=False)],
        axis=1)

    # Return value must be of a sequence of pandas.DataFrame
    return dataframe1,
