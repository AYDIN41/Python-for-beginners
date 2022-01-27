from sarkı import *
print("""
Sarkı Programı

1- Sarkı Gösterme

2- Sarkı Ekleme

3- Sarkı Silme

4- Sarkı Süresi 

5- Çıkmak

""")

sarki = sarkiGosterme()
while True:
    karar = int(input("Lutfen seçiminizi yapın: "))
    if (karar == 1):
        sarki.sarkiciGosterme()
    elif(karar == 2):
        sarkismi = input("Lutfen sarki ismini yazin: ")
        sanatci = input("Lutfen sanatci ismini yazin: ")
        album = input("Lutfen album ismini yazin: ")
        produksiyon = input("Lutfen produksiyon ismini yazin: ")
        sure = int(input("Lutfen sarki süresini yaziniz(saniye cinsinden): "))
        sarkisecimi = sarkici(sarkismi,sanatci,album,produksiyon,sure)
        sarki.sarkiEkleme(sarkisecimi)
    elif(karar == 3):
        isim = input("Lutfen sarki ismi giriniz: ")
        sarki.sarkiSil(isim)
    elif(karar == 4):
        isim = input("Lutfen süresini ogrenmek istediginiz sarkıyı girin")
        sarki.sarkiSuresi(isim)
    elif(karar == 5):
        print("Çıkış yapılıyor")
        break
























