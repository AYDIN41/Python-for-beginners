import numpy as np
import pandas as pd
from numpy.random import randn
print(randn(3,3))
df = pd.DataFrame(data=randn(3,3),index=["A","B","C"],columns=["Colums1","Colums2","Colums3"])
print(df)
print(df["Colums3"])
print(df["Colums1"])
print(df.loc["C"])
print(df.loc["B"])
print(df[["Colums1","Colums3"]])
df["Colums4"] = pd.Series(randn(3),index=["A","B","C"])
print(df)
df["Colums5"] = df["Colums1"] + df["Colums2"] + df["Colums3"] + df["Colums4"]
print(df)
print(df.drop("Colums4",axis=1))
df.drop("Colums4",axis=1,inplace=True)
print(df)
print(df.loc["A"])
print(df.iloc[2])
print(df.loc["A","Colums5"])
print(df.iloc[0][3])
print(df.loc["B","Colums2"])
print(df.loc[["A","C"],["Colums2","Colums5"]])