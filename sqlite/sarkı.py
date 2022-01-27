import sqlite3

import time

class sarkici():
    def __init__(self,sarki_ismi,sanatci,album,produksiyon_sirketi,sarki_suresi):
        self.sarki_ismi = sarki_ismi
        self.sanatci = sanatci
        self.album = album
        self.produksiyon_sirketi = produksiyon_sirketi
        self.sarki_suresi = sarki_suresi
    def __str__(self):
        return "Sarkı İsmi: {}\nSanatçı İsmi: {}\nAlbum: {}\nProduksiyon Şirketi: {}\nSarki Süresi: ".format(self.sarki_ismi,self.sanatci,self.album,self.produksiyon_sirketi,self.sarki_suresi)
class sarkiGosterme():
    def __init__(self):
        self.baglantiOlustur()
    def baglantiOlustur(self):
        self.baglanti = sqlite3.connect("Sarkıcı.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS sarkıcı (isim TEXT,sanatcı TEXT,album TEXT,produksiyon TEXT,sure INT)"
        self.cursor.execute(sorgu)
    def baglantiKes(self):
        self.cursor.close()
    def sarkiciGosterme(self):
        self.cursor.execute("Select * From sarkıcı")
        sarkii = self.cursor.fetchall()
        if(len(sarkii) == 0):
            print("Şarkı sekmesi boş")
        else:
            for i in sarkii:
                sargi = sarkici(i[0],i[1],i[2],i[3],i[4])
                print(sargi)
    def sarkiEkleme(self,Sarkici):
        self.cursor.execute("Insert into sarkıcı Values(?,?,?,?,?)",(Sarkici.sarki_ismi,Sarkici.sanatci,Sarkici.album,Sarkici.produksiyon_sirketi,Sarkici.sarki_suresi))
        self.baglanti.commit()
    def sarkiSil(self,isim):
        self.cursor.execute("Delete From sarkıcı where isim = ?",(isim,))
        self.baglanti.commit()
    def sarkiSuresi(self,isim):
        self.cursor.execute("Select * From sarkıcı where isim = ?",(isim,))
        sargi = self.cursor.fetchall()
        if(len(sargi) == 0):
            print("Sarkı bulunamadı")
        else:
            a = sargi[0][4]
            sure = sargi[0][4]
            if (not(a > 0 and a < 20)):
                sure = sargi[0][4]
                sure = sure / 60
            sorgu = "Update sarkıcı set sure = ? where isim = ?"
            self.cursor.execute(sorgu,(sure,isim))
            print(sure,"dk")
            self.baglanti.commit()














