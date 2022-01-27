import numpy as np
import pandas as pd
from numpy.random import randn
print(randn(3))
print(randn(3,3))
df = pd.DataFrame(data = randn(3,3),index= ["Satır 1","Satır 2","Satır 3"],columns=["Sutun 1","Sutun 2","Sutun 3"])
print(df)
print(df["Sutun 1"])
print(df["Sutun 2"])
print(type(df["Sutun 3"]))
#satır elamanlarını almak için farklı bir dataFrame fonksiyonu kullanıyoruz = df.loc
print(df.loc["Satır 1"])
print(type(df.loc["Satır 1"]))
print(df[["Sutun 1","Sutun 3"]])
print(df)
df["Sutun 4"] = pd.Series(randn(3),["Satır 1","Satır 2","Satır 3"])
print(df)
df["Sutun 5"] = df["Sutun 1"] + df["Sutun 2"] + df["Sutun 3"]
print(df)
#axis yatayda 0 dikeyde 1 dir df.drop sutunlar fonksiyonunu  kullanmak için axis i 1 yapmalıyız
print(df.drop("Sutun 5",axis=1))
print(df)
#inplace methodunu kullanmak için inplace fonksiyonunu kullanmalıyız
df.drop("Sutun 5",axis=1,inplace=True)
print(df)
print(df.loc["Satır 1"])
print(df.iloc[0])
print(df.loc["Satır 1","Sutun 2"])
print(df.iloc[0][1])
print(df.loc["Satır 2","Sutun 2"])
print(df.loc[["Satır 1","Satır 2"],["Sutun 1","Sutun 3"]])