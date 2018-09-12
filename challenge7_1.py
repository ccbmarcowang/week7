# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
def co2():
    df_climate=pd.read_excel('ClimateChange.xlsx',sheet_name='Data')
    df_co2=df_climate[df_climate['Series code']=='EN.ATM.CO2E.KT']
    df_country=pd.read_excel('ClimateChange.xlsx',sheet_name='Country')
    df_country1=df_country[['Country name','Income group']]
    df=pd.merge(df_country1,df_co2)
    df=df.replace({'..':np.nan})
    df=df.dropna(thresh=8)
    df=df.fillna(method='bfill',axis=1).fillna(method='ffill',axis=1)
    df['Sum emissions']=df.iloc[:,7:29].sum(axis=1)
    df_new=df[['Country name','Income group','Sum emissions']]
    df_last=df_new.groupby('Income group').sum().sort_values('Income group')
    df_last[['Highest emission country','Highest emissions']]=df_new.groupby('Income group').max().sort_values('Income group')
    df_last[['Lowest emission country','Lowest emissions']]=df_new.groupby('Income group').min().sort_values('Income group')
    return df_last
if __name__=='__main__':
    print(co2())