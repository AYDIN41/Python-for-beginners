def ucegatla(func):
    def wrapped(sayi):
        lisde = []
        for i in sayi:
            lisde.append(i*3)
        print(lisde)
        return func(sayi)
    return wrapped


@ucegatla
def ikiyeKatla(sayilar):
    liste = []
    for i in sayilar:
        liste.append(i*2)
    return liste
print(ikiyeKatla(range(1000)))