# damage_bins.py

# The script MUST contain a function named azureml_main
# which is the entry point for this module.

# imports up here can be used to
import pandas as pd

"""
Create Damage Factor Bins to use for categorical classification
"""
#Binning:
def binning(col, cut_points, labels=None):
  #Define min and max values:
  minval = col.min()
  maxval = col.max()

  #create list by adding min and max to cut_points
  break_points = [minval] + cut_points + [maxval]

  #if no labels provided, use default labels 0 ... (n-1)
  if not labels:
    labels = range(len(cut_points)+1)

  #Binning using cut function of pandas
  colBin = pd.cut(col,bins=break_points,labels=labels,include_lowest=True)
  return colBin


# The entry point function can contain up to two input arguments:
#   Param<dataframe1>: a pandas.DataFrame
#   Param<dataframe2>: a pandas.DataFrame
def azureml_main(dataframe1 = None, dataframe2 = None):

    cut_points = list(range(100000,50000000, 100000))
    bin_labels = ["damage_bin_{}".format(i) for i in cut_points]
    dataframe1["Damage_Bin"] = binning(dataframe1["Property_Damage"], cut_points[0:-1], bin_labels)
    # Return value must be of a sequence of pandas.DataFrame
    return dataframe1,
