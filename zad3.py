import pandas as pd

df=pd.read_csv('demografia.csv')
df=pd.read_csv('demografia.csv',decimal=',',na_values='NaN')

df_bez=df.drop(columns=['KRAJE'])
max_przyrost=df_bez.max().max()
rok=df_bez.max().idxmax()
index=df_bez.idxmax()
kraj=df.loc[index, 'KRAJE']

print(kraj)
