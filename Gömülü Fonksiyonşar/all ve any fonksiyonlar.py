def deneme(isim):
    for i in isim:
        if not i:
            return False
    return True
liste = [True,False,True]
liste2 = [1,2,3,4,5,6,7]
print(deneme(liste))
print(deneme(liste2))

def herhan(isim):
    for i in isim:
        if i:
            return True
    return False
print(herhan(liste))

