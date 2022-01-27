class araba():
    def __init__(self,marka,model,seri,renk):
        self.marka = marka
        self.model = model
        self.seri = seri
        self.renk = renk


marka1 = input("Lutfen Almak istediginiz markayı giriniz: ")
model = input("Lutfen Almak istediginiz modeli giriniz: ")
seri = input("Lutfen Almak istediginiz seriyi giriniz: ")
renkk  = input("Lutfen Almak istediginiz rengi giriniz: ")
araba1 = araba(marka1,model,seri,renkk)
print(araba1.marka,"\n",araba1.model,"\n",araba1.seri,"\n",araba1.renk)
marka2 = input("Lutfen Almak istediginiz markayı giriniz: ")
model2 = input("Lutfen Almak istediginiz modeli giriniz: ")
seri2 = input("Lutfen Almak istediginiz seriyi giriniz: ")
renkk2  = input("Lutfen Almak istediginiz rengi giriniz: ")
araba2 = araba(marka2,model2,seri2,renkk2)
print(araba2.marka,"\n",araba2.model,"\n",araba2.seri,"\n",araba2.renk)


"""
class araba():
    marka = "Mercedes"
    model = 2020
    seri = "Benz"
    renk = "Siyah"
araba1 = araba
print("Arabanın Markası {}\nModeli {}\nSeri {}\nRenk {}".format(araba1.marka,araba1.model,araba1.seri,araba1.renk))
print(dir(araba))


"""