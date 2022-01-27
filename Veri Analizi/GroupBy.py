import numpy as np
import pandas as pd
dataset = {"Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],"Çalışan":["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],"Maaş":[3000,3500,2500,4500,4000,2000]}
df = pd.DataFrame(dataset)
print(df)
dataGroup = df.groupby("Departman")
print(dataGroup.sum())
print(df.groupby("Departman").sum())
print(dataGroup.sum().loc["Bilişim"])
#sadece maaş değeri almak istersek eğer başına int ya da float değeri getirebiliriz
print(float(dataGroup.sum().loc["Bilişim"]))
print(int(dataGroup.sum().loc["Bilişim"]))
print(df.groupby("Departman").count())
print(df.groupby("Departman").max())
print(df.groupby("Departman").min())
print(df.groupby("Departman").min()["Maaş"])
print(df.groupby("Departman").min()["Maaş"]["Bilişim"])
#ortalama almak için ise mean fonksiyonunu kullanıyoruz
print(df.groupby("Departman").mean())
print(df.groupby("Departman").mean()["Maaş"]["Üretim"])
print(df.groupby("Departman").mean()["Maaş"]["Bilişim"])
