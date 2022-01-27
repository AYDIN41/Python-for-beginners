import numpy as np
import pandas as pd

df = pd.DataFrame({
  "Column1":[1,2,3,4,5,6],
    "Column2":[100,100,200,300,300,100],
    "Column3":["Mustafa","Kamil","Emre","Ayşe","Murat","Zeynep"]})
print(df)
#head fonksiyonun içinbe yazılan sayıya göre sıraların içinden istenilen kadar sıra çeker
print(df.head(3))
#istenilen sutundan ne kadar farklı değerlere sahip oldugunu görmek için uniwue fonksiyonunu kulannıyoruz
print(df["Column2"].unique())
#kaç tane farklı sonucumuz oldugunu gösteriyor
print(df["Column2"].nunique())
print(df["Column2"].value_counts())
#filtreleme sayesinde veriler içerisinden istenilen veri görüntüleniyor
print(df[(df["Column1"]>= 4) & (df["Column2"] == 300)])
#apply fonksiyonu ile verilerimiz yazılan bir fonksiyona gönderebiliriz
def times2(x):
    return x*2
def times22(x):
    return x/2
print(df["Column2"].apply(times2))
print(df["Column2"].apply(times22))
print(df["Column2"].apply(lambda x : x * 2 ))
#apply fonksiyonu ile strign uzunluklarını len ile görebiliriz
print(df["Column3"].apply(len))
#drop fonksiyonunu kullanarak istediğimiz sutun veya indeksi düşürebilirz kalıcı olarak silmek istiyorsak inplace moduulunu kullanmalıyız
print(df.drop("Column3",axis=1,inplace=True))
print(df)
#kaç tane sutunumuza sahip oldugumuzu görmek için isi columns fonksiyonunu kullanıyoruz
print(df.columns)
#indexleri de görmek için index fonksiyonunu kullanıyoruz
print(df.index)
#ne kadar index imiz olduugunu öğrenmek istersek eğer len i kullanıyoruz
print(len(df.index))
#isimleri görmek için names fonksiyonunu kullanıyoruz
print(df.index.names)
#data daki sayılara göre sıralamak istersek eğer sort_values fonksiyonunu kullanıyoruz
print(df.sort_values("Column2"))
#büyükten küçüğe sıralamak için ise
print(df.sort_values("Column2",ascending=False))
df = pd.DataFrame({
        "Ay" : ["Mart","Nisan","Mayıs","Mart","Nisan","Mayıs","Mart","Nisan","Mayıs"],
        "Şehir":["Ankara","Ankara","Ankara","İstanbul","İstanbul","İstanbul","İzmir","İzmir","İzmir"],
       "Nem":[10,25,50,21,67,80,30,70,75],
    })
print(df)
print(df.pivot_table(index="Ay",columns="Şehir",values="Nem"))
print(df.pivot_table(index="Şehir",columns="Ay",values="Nem"))




