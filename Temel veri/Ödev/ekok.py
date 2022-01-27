def ortakEnkucuk(sayi1,sayi2):
    i=2
    ekok = 1
    sa= sayi2
    asa = sayi1
    while(True):
        if(sayi1 % i == 0 and sayi2 % i == 0):
            ekok *= i
            sayi1 //= i
            sayi2 //= i
        elif(sayi1 % i  != 0 and sayi2 % i  == 0):
            ekok*=i
            sayi2 //= i
        elif (sayi1 % i == 0 and sayi2 % i != 0):
            ekok *= i
            sayi1 //= i
        else:
            i+=1
        if(sayi1 == 1 and sayi2 == 1):
            break
    sayi1 = asa
    sayi2 = sa
    print("Girdiginiz 1. {} ile 2.sayi {} Ekok'u = {}".format(sayi1,sayi2,ekok))
say1 = int(input("Lutfen ilk sayiyi giriniz: "))
say2 = int(input("Lutfen ikinci sayiyi giriniz: "))
ortakEnkucuk(say1,say2)