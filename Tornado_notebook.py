
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[65]:


df = pd.read_excel('./data/TornadoData.xlsx', 'Tornado_MinData')
df.head()


# In[66]:


df.describe()


# In[67]:


df.dtypes


# In[68]:


df.isnull().sum()


# In[69]:


df[df['F-Scale'].isnull()].head()


# In[70]:


df[df['Damage Factor'].isnull()].head()


# In[71]:


df[df['County_Name'].isnull()].head()


# In[72]:


df.shape


# In[73]:


df.dropna(subset=['F-Scale','Damage Factor'], how='any').shape


# In[74]:


df.dropna(subset=['F-Scale','Damage Factor'], how='any', inplace=True)


# In[75]:


df.shape


# In[76]:


df.dtypes


# In[77]:


df['F-Scale'] = df['F-Scale'].astype(np.int64)


# In[78]:


df.dtypes


# In[79]:


df.head()


# In[80]:


# create a column with an actual numeric property damage value include factor:
# e.g. 25.0. K = 25000
def calculate_property_damage(row):
    multiplier = 1000
    if row['Damage Factor'] == 'M':
        multiplier = 1000000
    return row['Property_DMG'] * multiplier


# In[81]:


# for each row, call the calculate_property_damage function.
# axis=1 means start at the top of the dataframe and go does, (row by row)
# and pass the row to the function.
df['Property_Damage'] = df.apply(calculate_property_damage, axis=1)
df['Property_Damage_Mil'] = df['Property_Damage'].apply(lambda x: x/1000000.0)


# In[82]:


df.head()


# In[83]:


# create F-Scale encoding
# One Hot Encoding
# Represent categorical variables as binary vectors
df = pd.concat([df['F-Scale'], pd.get_dummies(df, prefix=['F-Level'], columns=['F-Scale'],sparse=False)], axis=1)
df.head()


# ## Data Is Prepared
# 
# At this point we have performed the following:
# 
# - read in data set
# - removed na F-Scale
# - removed na Damage Factor
# - Calculated Property Damage
# - Calculated Property Damage in Millions
# - Created F-Scale encoding
# 

# In[87]:


# By state, look at aggregate loss and tornado count

df.groupby(['State'], axis=0)['Property_Damage_Mil'].agg(['sum', 'mean', 'max', 'count'])


# In[50]:


df.groupby(['State'], axis=0)['F-Scale','Property_Damage'].mean()


# In[37]:


df[df['State']=='AK']


# In[38]:


df[df['State']=='DC']


# In[40]:


plt.scatter(df['F-Scale'],df['Property_Damage'])
plt.xlabel('F-Scale')
plt.ylabel('Property Damage')
plt.title('Damage by F Scale')

plt.show()


# In[91]:


# group the data by year
df.groupby(df['Date'].dt.year, axis=0)['Property_Damage'].agg(['sum', 'mean', 'max', 'count'])


# In[48]:


# reset_index makes the Date column part of the Dataframe instead of the index
df2 = df.groupby(df['Date'].dt.year, axis=0)['Property_Damage'].agg(['sum', 'mean', 'max']).reset_index()
x = df2['Date']
y = df2['mean']
plt.scatter(x,y)
plt.xlabel('Year')
plt.ylabel('Avg Property Damage')
plt.title('Avg Damage by Year')

plt.show()


# In[88]:


# 
# reset_index makes the Date column part of the Dataframe instead of the index
df2 = df.groupby(df['Date'].dt.year, axis=0)['Property_Damage'].agg(['sum', 'mean', 'max', 'count']).reset_index()
x = df2['Date']
y = df2['count']
plt.scatter(x,y)
plt.xlabel('Year')
plt.ylabel('count')
plt.title('Avg Tornados by Year')

plt.show()


# In[115]:


# 
# reset_index makes the Date column part of the Dataframe instead of the index
df2 = df.groupby(df['Date'].dt.year, axis=0)['F-Level_0','F-Level_1','F-Level_2','F-Level_3','F-Level_4','F-Level_5'].agg(['sum', 'mean', 'max', 'count']).reset_index()
#df2.head()
x = df2['Date']
y = df2['count']
plt.scatter(x,y)
plt.xlabel('Year')
plt.ylabel('count')
plt.title('Avg Tornados by Year')

plt.show()


# In[114]:


df2 = df.groupby(df['Date'].dt.year, axis=0)['F-Level_0','F-Level_1','F-Level_2','F-Level_3','F-Level_4','F-Level_5'].sum().reset_index()


x = df2['Date']
f0 = df2['F-Level_0']
f1 = df2['F-Level_1']
f2 = df2['F-Level_2']
f3 = df2['F-Level_3']
f4 = df2['F-Level_4']
f5 = df2['F-Level_5']

plt.stackplot(x, f0,f1,f2,f3,f4,f5,colors=['m','c','r','g','b','k'])
plt.xlabel('Year')
plt.ylabel('Stacked F-Level')
plt.title('F-Level by Year')

plt.show()


# In[44]:


x = df.groupby(df['Date'].dt.year, axis=0)

