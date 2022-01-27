liste1 = [1,2,3,4,5,6,7,8,9,10]

liste2 = list()

for i in liste1:
    if(i % 2 == 0):
        liste2.append(i)
print(liste2)

liste = [x for x in range(1,101) if x % 2 == 0]
print(liste)