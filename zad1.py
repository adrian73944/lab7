import pandas as pd

df=pd.read_csv('demografia.csv')
df=pd.read_csv('demografia.csv',decimal=',',na_values='NaN')
print(df)
