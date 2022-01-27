def ekstraOzellik(func):
    def wrapped(sayilar):
        ciftsayilarToplami = 0
        ciftSayilar = 0
        teksayilarToplami = 0
        tekSayilar = 0
        for i in sayilar:
            if(i % 2 == 0):
                ciftSayilar += 1
                ciftsayilarToplami += i
            else:
                tekSayilar += 1
                teksayilarToplami += i
        print("\nTeklerin ortalaması: ",teksayilarToplami/tekSayilar,"\nÇift sayılar ortalaması: ",ciftsayilarToplami/ciftSayilar)
        func(sayilar)
    return wrapped

@ekstraOzellik
def ortalamaBul(sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    print("Ortalamanız: ",toplam/len(sayilar))
ortalamaBul(list([1,2,3,4,5,77,94,41]))



"""
def ekstraOzellik(func):
    def wrapped(sayilar):
        ciftsayilarToplami = 0
        ciftSayilar = 0
        teksayilarToplami = 0
        tekSayilar = 0
        for i in sayilar:
            if(i % 2 == 0):
                ciftSayilar += 1
                ciftsayilarToplami += i
            else:
                tekSayilar += 1
                teksayilarToplami += i
        print(func.__name__,"tek sayilar: ",tekSayilar,"Toplam: ",teksayilarToplami,"çift sayilar: ",ciftSayilar,"Toplam: ",ciftsayilarToplami)
        print("\nTeklerin ortalaması: ",teksayilarToplami/tekSayilar,"\nÇift sayılar ortalaması: ",ciftsayilarToplami/ciftSayilar)
        return sayilar
    return wrapped

@ekstraOzellik
def ortalamaBul(sayilar):
    toplam = 0
    for i in sayilar:
        toplam += i
    print("Ortalamanız: ",toplam/len(sayilar))
ortalamaBul(list([1,2,3,4,5,77,94,41]))




"""








