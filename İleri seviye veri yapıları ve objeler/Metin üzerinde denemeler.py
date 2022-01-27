class ornek():
    def __init__(self):
        with open("C:/Users/asus/Desktop/metin.txt","r",encoding="utf-8") as dosya:
            dosyaIcerigi = dosya.read()
            kelimeler = dosyaIcerigi.split()
            self.sadekelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                self.sadekelimeler.append(i)
            """
            for i in self.sadekelimeler:
                print(i)
            """
    def tumkelimeler(self):
        butunKelimeler = set()
        for i in self.sadekelimeler:
            butunKelimeler.add(i)
        for i in butunKelimeler:
            print(i)

            print("....................................")
    def keime(self,kelime):
        self.kelime = kelime
    def kelime_Frekans(self):
        a = dict()
        for i in self.sadekelimeler:
            if(i in self.kelime):
                if(i in a):
                    a[i] += 1
                else:
                    a[i] = 1


        if (not(i in self.kelime)):
            if(True):

                print("Aradıgınız isim: ",self.kelime,"Bulunamadı")

        for ab,sayi in a.items():

                print("{} kelimesi {} kadar geçmiştir".format(ab,sayi))

                print("-------------------------------------------------")






kkelime = input("Lutfen aramak istediginiz kelimeyi giriniz: ")
dosya = ornek()
# = ornek(kkelime)
dosya.keime(kkelime)
dosya.tumkelimeler()


dosya.kelime_Frekans()