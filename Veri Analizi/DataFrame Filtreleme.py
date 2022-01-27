import numpy as np
import pandas as pd
from numpy.random import randn
df = pd.DataFrame(data=randn(4,3),index=["A","B","C","D"],columns=["Colums1","Colums2","Colums3"])
print(df)
print(df > -1)
print(df[df>-1])
print(df["Colums1"])
print(df["Colums1"]>1)
#bu şekilde yapıldığında sadece decision ı sağlayan önermeleri(satırlar) alır
print(df[df["Colums1"]>0])
print(df["Colums2"]>0.4)
print(df[df["Colums2"]>0.4])
print(df[df["Colums2"]>0])
print(df[df["Colums1"]>0])
print(df[(df["Colums1"]>0) & (df["Colums2"]>0)])
print(df[(df["Colums1"]>0) | (df["Colums2"]>0)])
df["Colums4"] = randn(4)
print(df)
df["Column5"] = ["NewValue1","NewValue2","NewValue3","Aydın94"]
print(df)
print(df.index.names)
df.set_index("Column5",inplace=True)
print(df)
print(df.index.names)
