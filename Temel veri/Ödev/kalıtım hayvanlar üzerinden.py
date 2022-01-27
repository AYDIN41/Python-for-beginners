class hayvan():
    def __init__(self,tur="Bilgi Yok",bacak_sayisi = 0,tuyluMu="Bilgi Yok",Yas=0):
        self.tur = tur
        self.bacak_sayisi = bacak_sayisi
        self.tuyluMu = tuyluMu
        self.Yas = Yas
    def __str__(self):
        return "Tur: {}\nBacak Sayısı: {}\nTuylu mu? {}\nYas: {}".format(self.tur,self.bacak_sayisi,self.tuyluMu,self.Yas)
class kopek(hayvan):
    def __init__(self,tur="Bilgi Yok",bacak_sayisi = 0,tuyluMu="Bilgi Yok",Yas= 0,isim="Bilgi Yok",renk="Bilgi Yok"):
        self.tur = tur
        self.bacak_sayisi = bacak_sayisi
        self.tuyluMu = tuyluMu
        self.Yas = Yas
        self.isim = isim
        self.renk = renk

    def takeInfo(self):
        print("Tur: {}\nBacak Sayısı: {}\nTuylu mu? {}\nYas: {}\nİsim: {}\nRenk: {}".format(self.tur, self.bacak_sayisi, self.tuyluMu,self.Yas,self.isim,self.renk))
class kus(hayvan):
    def __init__(self,tur="Bilgi Yok",bacak_sayisi = 0,tuyluMu="Bilgi Yok",Yas=0,ad="Bilgi Yok",renk="Bilgi Yok"):
        self.tur = tur
        self.bacak_sayisi = bacak_sayisi
        self.tuyluMu = tuyluMu
        self.Yas = Yas
        self.ad = ad
        self.renk = renk
    def __str__(self):
        return "Tur: {}\nBacak Sayısı: {}\nTuylu mu? {}\nYas: {}\nİsim: {}\nRenk: {}".format(self.tur, self.bacak_sayisi, self.tuyluMu,self.Yas,self.ad,self.renk)
class at(hayvan):
    def __init__(self,tur="Bilgi Yok",bacak_sayisi = 0,tuyluMu="Bilgi Yok",Yas=0,yaris=0,renk="Bilgi Yok"):
        self.tur = tur
        self.bacak_sayisi = bacak_sayisi
        self.tuyluMu = tuyluMu
        self.Yas = Yas
        self.yaris = yaris
        self.renk = renk
    def __str__(self):
        return "Tur: {}\nBacak Sayısı: {}\nTuylu mu? {}\nYas: {}\nİsim: {}\nRenk: {}".format(self.tur, self.bacak_sayisi, self.tuyluMu,self.Yas,self.yaris,self.renk)

print("""
Hayvan Özellikleri Belirleme

1-Köpek

2-Kus

3-At

""")
while(1):
    decision = int(input("İşlem yapmak istediginiz hayvanı deneyin: "))

    if(decision==1):
        tur = input("Lutfen hayvanın türünü giriniz: ")
        bacakSayisi = int(input("Lutfen bacak sayisini giriniz: "))
        tuy = input("Lutfen Tüylü mü değil mi giriniz: ")
        yas = int(input("Lutfen hayvanın yaşını giriniz: "))
        isim = input("Lutfen hayvanın ismini giriniz: ")
        renk = input("Lutfen hayvanın rengini giriniz: ")
        kopekk = kopek(tur,bacakSayisi,tuy,yas,isim,renk)
        kopekk.takeInfo()
    elif(decision==2):
        tur = input("Lutfen hayvanın türünü giriniz: ")
        bacakSayisi = int(input("Lutfen bacak sayisini giriniz: "))
        tuy = input("Lutfen Tüylü mü değil mi giriniz: ")
        yas = input("Lutfen hayvanın yaşını giriniz: ")
        isim = input("Lutfen hayvanın ismini giriniz: ")
        renk = input("Lutfen hayvanın rengini giriniz: ")
        kuss = kus(tur, bacakSayisi, tuy,yas,isim,renk)
        print(kuss)
    elif(decision==3):
        tur = input("Lutfen hayvanın türünü giriniz: ")
        bacakSayisi = int(input("Lutfen bacak sayisini giriniz: "))
        tuy = input("Lutfen Tüylü mü değil mi giriniz: ")
        yas = input("Lutfen hayvanın yaşını giriniz: ")
        yaris = input("Lutfen hayvanın katıldıgı yariş adetini giriniz: ")
        renk = input("Lutfen hayvanın rengini giriniz: ")
        att = at(tur, bacakSayisi, tuy, yas,yaris,renk)
        print(at)
    else:
        print("Yanlıs Girdiginiz")
        break















