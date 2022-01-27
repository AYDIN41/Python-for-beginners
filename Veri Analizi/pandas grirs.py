import numpy as np
import pandas as pd
labels_list = ["Mustafa","Kemal","Murat","Kadir","Aydın"]
data_list = [10,20,30,40,50]
"""pd = pd.Series(data=data_list,index=labels_list)
print(pd)"""
"""pd = pd.Series(data_list)
print(pd)"""
npArray = np.array([10,20,30,40,50])
"""pd = pd.Series(npArray,labels_list)"""
"""pd = pd.Series(data=data_list,index=["Emirhan","BABA","Aydın","AKA","94"])"""
dataDict = {"Aydın":100,"Salih":101,"BlaBla":23}
"""pd = pd.Series(dataDict)"""
seri2017 = pd.Series([5,10,15,20],["Buğday","Mısır","Erik","Ceviz"])
print(seri2017)
seri2018 = pd.Series([8,19,33,40],["Buğday","Mısır","Çilek","Ceviz"])
print(seri2018)
print(seri2018+seri2017)
total = seri2018+seri2017
print(total["Ceviz"])
