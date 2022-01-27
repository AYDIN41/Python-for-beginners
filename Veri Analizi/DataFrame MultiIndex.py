import numpy as np
import pandas as pd
from numpy.random import randn

outerIndex = ["Group1","Group1","Group1","Group2","Group2","Group2","Group3","Group3","Group3"]
innerIndex = ["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]
print(list(zip(outerIndex,innerIndex)))
hiercahy = list(zip(outerIndex,innerIndex))
hiercahy = pd.MultiIndex.from_tuples(hiercahy)
print(hiercahy)
df = pd.DataFrame(randn(9,3),hiercahy,columns=["Column1","Column2","Column3"])
print(df)
print(df["Column1"])
print(df.loc["Group1"])
print(df.loc[["Group1","Group3"]])
print(df.loc["Group1"].loc["Index3"])
print(df.loc["Group1"].loc["Index3"]["Column1"])
print(df.index.names)
df.index.names=["Groups","Indexes"]
print(df)
print(df.loc["Group1"])
print(df.xs("Group1"))
print(df.xs("Group1").xs("Index2").xs("Column3"))
print(df.xs("Index1",level="Indexes"))


