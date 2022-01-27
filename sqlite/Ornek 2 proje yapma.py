
from kütüphane import *

print("""
Kütüphane Programı

1-Kitapları Göster

2-Kitap Sorgulama 

3-Kitap Ekleme

4-Kitap Sil

5-Baskı Yükselt

Çıkmak İçin 'a' ya basınız
""")

gidaplik = Kutuphane()
while True:
    karar = input("Yapmak istediginiz işlemi giriniz: ")
    if(karar == "a"):
        print("Çıkış yapılıyor")
        break
    elif(karar == "1"):
        gidaplik.kitaplariGoster()
    elif (karar == "2"):
        isim = input("Lütfen Kitap ismini giriniz: ")
        print("Kitap Sorgulanıyor")
        time.sleep(1)
        gidaplik.kitapSorgula(isim)
    elif (karar == "3"):
        isim = input("Lütfen Kitap ismini giriniz: ")
        yazar = input("Lutfen yazar ismini giriniz: ")
        yayinevi = input("Lutfen yayinevi ismini giriniz: ")
        tur = input("Lutfen kitabın türünü giriniz: ")
        baski = int(input("Lutfen kitabın baskısını giriniz: "))
        yeniGikap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("Yeni kitap ekleniyor")
        time.sleep(1)
        gidaplik.kitapEkle(yeniGikap)
    elif (karar == "4"):
        cevap = input("Emin misiniz if you are sure press the 'E'")
        if (cevap == 'E'):
            isim = ("Lutfen silmek istediginiz kitap ismini yaziniz: ")
            print("Kitap siliniyor...")
            time.sleep(1)
            gidaplik.kitapSil(isim)

    elif (karar == "5"):
        isim = input("Lutfen baskısını yükseltmek istediginiz kitap ismini giriniz: ")
        print("Baskı yükseltiliyor")
        time.sleep(1)
        gidaplik.BaskıYükselt(isim)
    else:
        print("Geçersiz giriş")













