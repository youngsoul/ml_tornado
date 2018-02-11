import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from sklearn.preprocessing import OneHotEncoder, PolynomialFeatures
from sklearn.linear_model import Ridge

df = pd.read_excel('./data/TornadoData.xlsx', 'Tornado_MinData')

# Drop the na rows
df.dropna(subset=['F-Scale','Damage Factor'], how='any', inplace=True)

# convert the data type of F-Scale to integer
df['F-Scale'] = df['F-Scale'].astype(np.int64)


def calculate_property_damage(row):
    multiplier = 1000
    if row['Damage Factor'] == 'M':
        multiplier = 1000000
    return row['Property_DMG'] * multiplier

# for each row, call the calculate_property_damage function.
# axis=1 means start at the top of the dataframe and go does, (row by row)
# and pass the row to the function.
df['Property_Damage'] = df.apply(calculate_property_damage, axis=1)
df['Property_Damage_Mil'] = df['Property_Damage'].apply(lambda x: x/1000000.0)



df_year_month = df.groupby([df['Date'].dt.year, df['Date'].dt.month], axis=0)['Property_Damage_Mil'].agg(['sum', 'mean', 'max', 'count'])

# convert multilevel index (Date-Year => Date-Month) to two columns of Year and Month
df_year_month.index = df_year_month.index.set_names(['Year','Month'])
df_year_month.reset_index(inplace=True)


import time
def year_month_ts(row, min_datetime):
    year = int(row['Year'])
    month = int(row['Month'])
    day = 1

    ts = (dt.datetime(year,month,day) - min_datetime).total_seconds()
    return ts

    # (dt.datetime(year,month,day) - dt.datetime(1900,1,1)).total_seconds()

min_dt = dt.datetime(df_year_month['Year'].min(), df_year_month['Month'].min(), 1)

df_year_month['Year_Month_TS'] = df_year_month.apply(year_month_ts, axis=1, min_datetime = min_dt)





print(len(df_year_month))

y = df_year_month['count']

X = df_year_month['Year_Month_TS']

print(X)


show_plot= False

if show_plot:
    fig, axes = plt.subplots(1, 1, figsize=(16, 9), dpi=100)

    x = range(len(X))
    axes.plot(x, y)

    axes.set_xlabel('Year / Month')
    axes.set_ylabel('Number of tornados')
    axes.set_xticks(x)
    #axes.set_xticklabels(x_labels, rotation=90)
    axes.set_title('Number of Tornados by month')

    # add a trend line
    z = np.polyfit(x, y, 1)
    p = np.poly1d(z)
    plt.plot(x,p(x),"r--")
    # the line equation:
    print("y=%.6fx+(%.6f)"%(z[0],z[1]))
    plt.show()



# use the first 184 data points for training, the rest for testing
n_train = int(746 * 0.7)

xticks = pd.date_range(start=df_year_month.index.min(),
                       end=df_year_month.index.max(),
                       freq='D')

# function to evaluate and plot a regressor on a given feature set
def eval_on_features(features, target, regressor):
    # split the given features into a training and a test set
    X_train, X_test = features[:n_train], features[n_train:]
    # also split the target array
    y_train, y_test = target[:n_train], target[n_train:]
    regressor.fit(X_train, y_train)
    print("Test-set R^2: {:.2f}".format(regressor.score(X_test, y_test)))
    y_pred = regressor.predict(X_test)
    y_pred_train = regressor.predict(X_train)
    plt.figure(figsize=(10, 3))

    plt.xticks(range(0, len(X), 8), xticks.strftime("%a %m-%d"), rotation=90,
               ha="left")

    plt.plot(range(n_train), y_train, label="train")
    plt.plot(range(n_train, len(y_test) + n_train), y_test, '-', label="test")
    plt.plot(range(n_train), y_pred_train, '--', label="prediction train")

    plt.plot(range(n_train, len(y_test) + n_train), y_pred, '--',
             label="prediction test")
    plt.legend(loc=(1.01, 0))
    plt.xlabel("Date")
    plt.ylabel("Number of Tornados")

    plt.show()






X_year_month = np.hstack([df_year_month['Year'].values.reshape(-1,1), df_year_month['Month'].values.reshape(-1,1)])


enc = OneHotEncoder()
X_year_month_onehot = enc.fit_transform(X_year_month).toarray()

poly_transformer = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)

X_year_month_onehot_poly=poly_transformer.fit_transform(X_year_month_onehot)

lr = Ridge()
eval_on_features(X_year_month_onehot_poly, y, lr)

print("")


