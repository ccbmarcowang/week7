import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def co2_gdp_plot():
    df_climate=pd.read_excel('ClimateChange.xlsx',sheetname='Data')
    data1=df_climate[df_climate['Series code']=='NY.GDP.MKTP.CD'].set_index('Country code')
    data2=df_climate[df_climate['Series code']=='EN.ATM.CO2E.KT'].set_index('Country code')
    data1.drop(data1.columns[:5],axis=1,inplace=True)
    data2.drop(data2.columns[:5],axis=1,inplace=True)
    data1.replace({'..':pd.np.nan},inplace=True)
    data2.replace({'..':pd.np.nan},inplace=True)
    data1=data1.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).fillna(0)
    data2=data2.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1).fillna(0)
    data=pd.concat([data1.sum(axis=1),data2.sum(axis=1)],axis=1)
    f=lambda x:(x.values-x.min())/(x.max()-x.min())
    data=data.apply(f)
    data.columns=['GDP-SUM','CO2-SUM']
    data=data.reset_index()
    l=data[data['Country code']=='CHN'].values
    china=[float("{:.3f}".format(l[0,2])),float("{:.3f}".format(l[0,1]))]
    fig=plt.subplot()
    fig.set_title('GDP-CO2')
    fig.plot(data['CO2-SUM'],label='CO2-SUM')
    fig.plot(data['GDP-SUM'],label='GDP-SUM')
    fig.set_xlabel('Countries')
    fig.set_ylabel('Values')
    plt.xticks([data[data['Country code']=='CHN'].index[0],data[data['Country code']=='USA'].index[0],data[data['Country code']=='GBR'].index[0],data[data['Country code']=='FRA'].index[0],data[data['Country code']=='RUS'].index[0]],['CHN','USA','GBR','FRA','RUS'],rotation=90)
    plt.legend(loc='upper left')
    return fig,china
if __name__=='__main__':
    fig,china=co2_gdp_plot()
    print(china)