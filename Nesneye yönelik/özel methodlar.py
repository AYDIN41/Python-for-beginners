class kitap():
    def __init__(self,kitap,yazar,sayfa_Sayisi,tur):
        self.kitap = kitap
        self.yazar = yazar
        self.sayfa_Sayisi = sayfa_Sayisi
        self.tur = tur

    def __str__(self):
        return "Kitap: {}\nYazar: {}\nSayfa Sayisi: {}\nTür: {}".format(self.kitap,self.yazar,self.sayfa_Sayisi,self.tur)
    def __len__(self):
        return self.sayfa_Sayisi
okuyorumBen = kitap("Ezilenler","Dostoyevski",397,"Roman")
print(okuyorumBen)
print("Sayfa Sayiniz: ",len(okuyorumBen))

