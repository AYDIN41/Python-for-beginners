import sqlite3

class esya():
    def __init__(self,isim,tutar,miktar,sonFiyat):
        self.isim = isim
        self.tutar = tutar
        self.miktar = miktar
        self.sonFiyat = sonFiyat
    def __str__(self):
        return "Ürün ismi: {}\nÜrün Fiyatı: {}\nAlınacak Miktar: {}\nSon Fiyat: {} Türk Lirası".format(self.isim,self.tutar,self.miktar,self.sonFiyat)
class market():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("SuperMarket")

        self.cursor = self.baglanti.cursor()

        cevap = "CREATE TABLE IF NOT EXISTS supermarket (isim TEXT,tutar INT,miktar INT,sonfiyat INT)"

        self.cursor.execute(cevap)
    def baglantiKes(self):
        self.baglanti.close()
    def urunGoster(self):
        self.cursor.execute("Select * From supermarket")
        urunler = self.cursor.fetchall()
        if(len(urunler) == 0):
            print("Urun katalogunuz boş")
        else:
            for i in urunler:
                urun = esya(i[0],i[1],i[2],i[3])
                print(urun)
    def urunEkle(self,urun):
        cevap = "Insert into supermarket Values (?,?,?,?)"

        self.cursor.execute(cevap,(urun.isim,urun.tutar,urun.miktar,urun.sonFiyat))
        self.para = urun.tutar * urun.miktar
        self.baglanti.commit()
    def urunSil(self,isim):
        self.cursor.execute("Delete From supermarket where isim = ?",(isim,))
        self.baglanti.commit()
    def fiyatGoster(self,isim):

        self.cursor.execute("Select * From supermarket where isim = ?",(isim,))
        urunler = self.cursor.fetchall()
        if(len(urunler) == 0):
            print("Urun fiyatı bulunamadı")
        else:
            urunn = urunler[0][4]
            sorgu2 = "Update supermarket set sonFiyat = ? where isim = ?"
            self.cursor.execute(sorgu2,(urunn,isim))
            print(urunn,"Türk Lirası")
            self.baglanti.commit()

























