import pandas as pd

df=pd.read_csv('demografia.csv')
df=pd.read_csv('demografia.csv',decimal=',',na_values='NaN')

max_przyrost_index=df['2022'].idxmax(skipna=True)
kraj=df.loc[max_przyrost_index, 'KRAJE']
print(max_przyrost_index)
print(kraj)