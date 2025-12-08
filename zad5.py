import pandas as pd

dane= {
'Nr_albumu':[1, 2, 3, 4, 5],
'Imię':['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
'Nazwisko':['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
'Ocena':[4.5, 3.0, 5.0, 4.0, 2.5],
'WiekS': [22, 21, 24, 23, 25]
}
df=pd.DataFrame(dane)
ocena=df[df['Ocena']>4]
wiek=df.sort_values('WiekS')
srednia=df.groupby('Ocena')['WiekS'].mean()
print(srednia)
poprawa = {
    'Nr_albumu':[2, 5],
    'Poprawa':[4.5, 5.0],
}
df_poprawa = pd.DataFrame(poprawa)
df_nowe=pd.merge(df,df_poprawa, on='Nr_albumu', how='left')
print(df_nowe)
df_nowe.to_csv('poprawa.csv', index=False)
df_nowe1=pd.read_csv('poprawa.csv')
student={'Nr_albumu':6,'Imię':'Adrian','Nazwisko':'Lubas','Ocena':5.0,'WiekS':21}
df_nowe1.loc[len(df_nowe1)]=student
print(df_nowe1)
unikalne_wartosci=df_nowe1['Ocena'].unique()
print(unikalne_wartosci)
print(df_nowe1[df_nowe1.Ocena == 5])

