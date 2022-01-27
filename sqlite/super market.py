from supermarket import *
print("""
1-Urunleri Goster

2- Urun Ekleme

3- Urun Silme 

4- Urun Fiyatı Görüntüleme

5-Çıkış

""")
bakkal = market()
while True:
    cevap = int(input("Lutfen seciminizi yapın: "))
    if(cevap == 1):
        bakkal.urunGoster()
    elif(cevap == 2):
        isim = input("Lutfen eklemek istediginiz urunu yazınız: ")
        tutar = int(input("Lutfen urunden ne kadar alınacagını giriniz: "))
        miktar = int(input("Lutfen urunun birim fiyatını girin: "))

        yeniUrun = esya(isim,miktar,tutar,tutar*miktar)
        bakkal.urunEkle(yeniUrun)
        print("Mevcut urun hali aşşağıdaki gibidir\n")
        bakkal.urunGoster()
    elif(cevap == 3):
        isim = input("Lutfen silmek istediginiz urunu giriniz: ")
        bakkal.urunSil(isim)
        print("Kalan ürünlerim\n")
        bakkal.urunGoster()
    elif(cevap == 4):
        isim = input("Fiyatını görmek istediginiz urunu giriniz: ")
        bakkal.fiyatGoster(isim)

    elif (cevap == 5):
        print("Çıkıyorsunuz...")
        break
    else:
        print("Girdiginiz deger geçersiz...")





















