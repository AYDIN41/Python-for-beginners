
liste1 = [(3,4),(10,3),(5,6),(1,9)]
liste = []
liste3 = []
for i,j in liste1:
    liste.append(i)
    liste3.append(j)
print(list(map(lambda x,y : x*y,liste,liste3)))
