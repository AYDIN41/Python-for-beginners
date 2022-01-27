def terscevir(isim):
    if(type(isim)!= str):
        raise ValueError("Deger hatası vardır lutfen kontrol ediniz...")
    else:
        print(isim[::-1])
aydin = str(input("Lutfen isim giriniz: "))
terscevir(aydin)
try:
    print(terscevir(aydin))
except ValueError:
    print("Deger eksik")




"""

try:
    a = int(input("Lutfen bir sayi girin: "))
    b = int(input("Lutfen bir sayi girin: "))
    print(a / b)
except (ValueError,ZeroDivisionError):
    print("Deger hatası var")
finally:
    print("Program sonlanıyor")



try:
    a = int(input("Lutfen bir sayi girin: "))
    b = int(input("Lutfen bir sayi girin: "))
    print(a / b)
except ValueError:
    print("Deger hatası var")
except ZeroDivisionError:
    print("0 bölüm yapılmaz")



"""

