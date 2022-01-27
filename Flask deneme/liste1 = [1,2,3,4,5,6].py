liste1 = [1,2,3,4,5,6]
liste2 = [7,8,9,10,11,12,13,14]
liste3 = ["Python","C","C++","Java"]
i = 0
sonuç = []
while(i<len(liste1) and i<len(liste2)):
    sonuç.append((liste1[i],liste2[i]))
    i += 1
print(sonuç)

print(list(zip(liste1,liste2,liste3)))
for i,j in zip(liste1,liste3):
    print(i," ",j)
