import numpy as np
import pandas as pd

data = np.arange(15, 30).reshape(5, 3)
dfx = pd.DataFrame(
    data, 
    index=['apple', 'banana', 'kiwi', 'grapes', 'mango'], 
    columns=['store1', 'store2', 'store3']
)

dfx['store4'] = np.nan
dfx.loc['watermelon'] = np.arange(15, 19)
dfx.loc['oranges'] = np.nan
dfx['store5'] = np.nan

dfx.loc['apple', 'store4'] = 20.0

dfx.isnull()
dfx.notnull()
dfx.isnull().sum()
dfx.isnull().sum().sum()
dfx.count()

dfx.store4[dfx.store4.notnull()]
dfx.store4.dropna()
dfx.dropna()
dfx.dropna(how='all')
dfx.dropna(how='all', axis=1)
dfx.dropna(thresh=5, axis=1)

ar1 = np.array([100, 200, np.nan, 300])
ser1 = pd.Series(ar1)
ar1.mean()
ser1.mean()

ser2 = dfx.store4
ser2.sum()
ser2.mean()
ser2.cumsum()

filledDf = dfx.fillna(0)
dfx.mean()
filledDf.mean()

dfx.store4.ffill()
dfx.store4.bfill()
