import time
def zaman_hesapla(func):
    def wrapped(sayilar):
        baslama = time.time()

        sonuc = func(sayilar)

        bitis = time.time()

        print(func.__name__+ " " + str(bitis-baslama) + "kadar sürdü")
        return sonuc
    return wrapped
@zaman_hesapla
def kareleri_hesapla(sayilar):
    sonuc = []
    for i in sayilar:
        sonuc.append(i**2)
    return sonuc
@zaman_hesapla
def kup_alma(sayilar):
    sonuc = []
    for i in sayilar:
        sonuc.append(i ** 3)
    return sonuc
print(kareleri_hesapla(range(100000)))
print(kup_alma(range(100000)))