import time
import random
print("""
*************************
Sayı Tahmin etme programı
*************************
""")
def sayiTahmin(sayi):
    sayi2 = random.randint(1, 20)
    while(True):
        if (sayi == sayi2):
            return sayi2
        elif (sayi > sayi2):
            return sayi2
        elif (sayi < sayi2):
            return sayi2


tahminHakki = 3
while(tahminHakki>=0):
    if (tahminHakki == 0):
        print("Hakkınız bitti")
        break
    sayiGirin = int(input("Lutfen tahmin için bir sayi girin: "))
    sayiTahmin(sayiGirin)
    sayi3 = int(sayiTahmin(sayiGirin))
    if(sayiGirin>sayi3):
        print("Bilgiler sorgulanıyor...")
        time.sleep(2)
        print("Sayiniz büyük lutfen daha küçüğünü giriniz ")
        tahminHakki -=1
    elif(sayiGirin<sayi3):
        print("Bilgiler sorgulanıyor...")
        time.sleep(2)
        print("Sayiniz küçük lutfen daha büyüğünü giriniz ")
        tahminHakki -=1
    else:
        print("Bilgiler sorgulanıyor...")
        time.sleep(3)
        print("Tebrikler!!!")
        break
