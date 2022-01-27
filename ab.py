def mukemmelSayi(func):
    def wrapped(sayilar):
        for sayi in sayilar:
            toplam = 0
            i = 1
            while (i < sayi):
                if (sayi % i == 0):
                    toplam = toplam + i
                i += 1
            if (toplam == sayi):
                print("Mukemmel Sayi",i)
        func(sayilar)
    return wrapped




@mukemmelSayi
def asal_sayilar(sayilar):
    print("Asal Sayılar...")

    for sayi in sayilar:
        i = 2
        say = 0
        while (i < sayi):
            if (sayi % i == 0):
                say += 1
            i += 1
        if (sayi == 0 or sayi == 1):
            say += 1
        if (say == 0):
            print(sayi)

asal_sayilar(range(1000))