def mukemmelSayi(func):
    print("Mukemmel Sayilar")
    def wrapper():
        for sayi in range(1,1001):
            toplam = 0
            i = 1
            while(i < sayi):
                if ( sayi % i == 0):
                    toplam = toplam + i
                i += 1
            if (toplam == sayi):
                print("Mukemmel Sayi",i)
        func()
    return wrapper()






@mukemmelSayi
def asal_sayilar():
    print("Asal Sayılar...")
    for sayi in range(2,1001):
        i = 2
        say = 0
        while (i < sayi):
            if (sayi % i == 0):
                say += 1
            i += 1
        if (say == 0):
            print(sayi)


asal_sayilar()
