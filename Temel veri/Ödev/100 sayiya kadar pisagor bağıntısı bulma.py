def pisagorBulma():
    liste = list()
    for i in range(1,101):
        for j in range(1,101):
            c = ((i*i) + (j*j)) ** 0.5
            if(c == int(c)):
                liste.append((i,j,int(c)))
    return liste
for i in pisagorBulma():
    print(i)