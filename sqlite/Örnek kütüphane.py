import sqlite3

import time

class Kitap():

    def __init__(self,isim,yazar,yayinevi,tür,baskı):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tür = tür
        self.baskı = baskı
    def __str__(self):
        return "Kitap ismi: {}\nYazar : {}\nYayinevi: {}\nTür= {}\nBaskı = {}".format(self.isim,self.yazar,self.yayinevi,self.tür,self.baskı)
class Kutuphane():
    def __init__(self):

        self.baglanti_olustur()

    def  baglantiOlustur(self):
        self.baglanti = sqlite3.connect("Kütüphane.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT,yazar TEXT,yayinevi TEXT,tür TEXT,baskı INT)"

        self.cursor.execute(sorgu)


    def baglantiyiKes(self):
        self.baglanti.close()

    def kitaplariGoster(self):
        sorgu = "Select * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("Kütüphaneniz boş")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
    def kitapSorgula(self,isim):
        sorgu = "Select * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()
        if(len(kitaplar) == 0):
            print("Kitap bulunmamaktadır")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)
    def kitapEkle(self,kitap):

        sorgu = "Insert into kitaplar Values(?,?,?,?)"

        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tür,kitap.baskı))

        self.baglanti.commit()
    def kitapSil(self,isim):

        sorgu = "Delete From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        self.baglanti.commit()
    def BaskıYükselt(self,isim):

        sorgu = "Select * From kitaplar where isim = ?"

        self.cursor.execute(sorgu,(isim,))

        kitaplar = self.cursor.fetchall()

        if(len(kitaplar) == 0):
            print("Kitap bulunamadı")
        else:
            baskı = kitaplar[0][4]
            baskı += 1
            sorgu2 = "Update kitaplar set baskı = ? where isim = ?"
            self.cursor.execute(sorgu2,(baskı,isim))
            self.baglanti.commit()












