class calisan():
    def __init__(self, isim, departman, maas, yil):
        self.isim = isim
        self.departman = departman
        self.maas = maas
        self.yil = yil

    def getInformation(self):
        print("""
        Bilgiler{}
        
        İsim: {}
        
        Departman: {}
        
        Maas: {}
        
        Yıl: {}
        
        """.format("\n", self.isim, self.departman, self.maas, self.yil))

class yonetici(calisan):
    def zam(self,zam):
        self.maas += zam

dir(yonetici)
isim = input("Lutfen bir isim giriniz: ")
departman = input("Lutfen departmanınızı giriniz: ")
maas = int(input("Lutfen maaşınızı giriniz: "))
yil = input("Lutfen kaç yıl çalıştıgınızı giriniz: ")
zama = int(input("Lutfen istediginiz zammı giriniz: "))
burjuva = yonetici(isim, departman, maas, yil)
burjuva.getInformation()
burjuva.zam(zama)
burjuva.getInformation()

"""
isim = input("Lutfen bir isim giriniz: ")
departman = input("Lutfen departmanınızı giriniz: ")
maas = input("Lutfen maaşınızı giriniz: ")
yil = input("Lutfen kaç yıl çalıştıgınızı giriniz: ")
emekci = calisan(isim,departman,maas,yil)
emekci.getInformation()
makam = input("Lutfen Makamınızı giriniz: ")
burjuva = calisan.yonetici(makam)
burjuva.takeinfo()

"""
