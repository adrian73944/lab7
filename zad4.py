import pandas as pd
import math
data = {
    'Id':[1,2,3,4,5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz','Michał'],
    'Nazwisko':['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko':['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja':[8000,4500,6000,5500,7000]
}
df = pd.DataFrame(data)
pracownicy_5k=df[df['Pensja']>5000]
wiek=df.sort_values('Wiek')
stanowisko =df.groupby('Stanowisko')['Pensja'].mean()

awans= {
    'Id':[2,4],
    'nowe':['Senior programista','Senior programista']
}
df_awans = pd.DataFrame(awans)
df_nowe=pd.merge(df,df_awans, on='Id', how='left')
print(df_nowe)

