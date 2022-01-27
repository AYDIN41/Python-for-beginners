liste1 = ["EA","Aydın","41","EFSANE"]
sonuc = []
for i in range(0,len(liste1)):
    sonuc.append((i,liste1[i]))
print(sonuc)
print(list(enumerate(liste1)))
for i,j in enumerate(liste1):
    print(i,j)
#bir biri ile eşleşen listeleri yaziyor