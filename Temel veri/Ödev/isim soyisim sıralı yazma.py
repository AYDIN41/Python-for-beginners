isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]

soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
a = list(zip(isim,soyisim))
a.sort()
print(a)
for i,j in a:
    print(i,j)