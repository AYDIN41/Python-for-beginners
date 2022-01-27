import numpy as np
import pandas as pd
arr = np.array([[94,41,np.nan],[11,np.nan,np.nan],[55,77,np.nan]])
print(arr)
df = pd.DataFrame(arr,index=["Index1","Index2","Index3"],columns=["Column1","Column2","Column3"])
print(df)
#dropna fonksiyonu sayesinde nan sayılar not a number olanlar yazılmıyor
print(df.dropna())
#axis 0 yatay 1 dikey olarak alınıyor
print(df.dropna(axis=1))
#thresh değer verme methodunda ise kullanılan yöntem yazılan sayıya göre kaç tane nan sayı gösterileceğini belirliyor
print(df.dropna(thresh=2))
print(df.fillna(0))
print(df.sum())
print(df.sum().sum())
print(df.size)
print(df.isnull().sum())
print(df.isnull().sum().sum())
def meanCalculate(df):
    totalSum = df.sum().sum()
    totalNumbers = df.size - df.isnull().sum().sum()
    totalMunis = totalSum / totalNumbers
    return totalMunis
print(df.fillna(meanCalculate(df),inplace=True))
print(df)
print(df)