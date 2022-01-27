liste1 = [1,2,3,4,5,6]
liste2 = [7,8,9,10,11,12,13,14]
i = 0
sonuç = []
while(i<len(liste1) and i<len(liste2)):
    sonuç.append((liste1[i],liste2[i]))
print(sonuç)