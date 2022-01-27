class isci():
    def __init__(self,isim,soyisim,maas,dil,zamMiktari,yeniDil):
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.dil = dil
        self.zamMiktari = zamMiktari
        self.yeniDil = yeniDil
    def bilgileriGoster(self):
        print("""
        
        İsim = {}
        
        Soyisim = {}
        
        Maas = {}
        
        Dil = {}
        
        
        
        """.format(self.isim,self.soyisim,self.maas,self.dil))
    def zamAlma(self,zamMiktari):
        print("Net Maasınız",self.maas + (self.maas * self.zamMiktari),"Onceki maasınız: ",self.maas,"Yapılan zam: ",self.maas * self.zamMiktari)
        self.maas = self.maas + (self.maas * self.zamMiktari)
    def dilEkleme(self,yeniDil):
        self.dil.append(yeniDil)

isim = input("Lutfen isminizi giriniz: ")
soyisim = input("Lutfen soyisim giriniz: ")
maas = float(input("Lutfen maas giriniz: "))
dil = list(input("Lutfen bildiginiz dilleri giriniz: "))
zam = float(input("Lutfen ne kadar zam istediginizi giriniz : "))
yeniDil = input("Lutfen yeni dilin girin giriniz: ")
zam = zam / 100
emekci = isci(isim,soyisim,maas,dil,zam,yeniDil)
emekci.bilgileriGoster()
emekci.zamAlma(zam)
emekci.dilEkleme(yeniDil)
emekci.bilgileriGoster()