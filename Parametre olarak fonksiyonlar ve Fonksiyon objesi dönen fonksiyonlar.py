def anafonksiyon(islem):
    def carpma(*args):
        carp = 1
        for i in args:
            carp *= i
        return carp
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    if (islem == "carpma"):
        return carpma
    else:
        return toplama
fonk = anafonksiyon("carpma")
print(fonk(1,2,3,4,5))
fonk2 = anafonksiyon("doblama")
print(fonk2(1,2,3,4,5,67,88,99,94))
def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b
def anaFonksiyon(func1,func2,func3,func4,islem):
    if (islem== 1):
        print(func1(94,41))
    elif (islem== 2):
        print(func2(94,41))
    elif (islem== 3):
        print(func3(94,41))
    elif (islem== 4):
        print(func4(94,41))
    else:
        print("Gecersiz deger")
anaFonksiyon(toplama,cikarma,carpma,bolme,4)






