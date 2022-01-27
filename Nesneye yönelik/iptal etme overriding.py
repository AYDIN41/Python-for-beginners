class calisan():
    def __init__(self,isim,departman,maas,yil):
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
    def __init__(self,isim,departman,maas,yil,makam):
        self.isim = isim
        self.departman = departman
        self.maas = maas
        self.yil = yil
        self.makam = makam

    def takeInformation(self):
        print("""
        Bilgiler{}

        İsim: {}

        Departman: {}

        Maas: {}

        Yıl: {}
        
        Makam: {}
            
        """.format("\n", self.isim, self.departman, self.maas, self.yil,self.makam))


    def zam(self,zam):
        self.maas += zam
isim = input("Lutfen bir isim giriniz: ")
departman = input("Lutfen departmanınızı giriniz: ")
maas = int(input("Lutfen maaşınızı giriniz: "))
yil = input("Lutfen kaç yıl çalıştıgınızı giriniz: ")
zama = int(input("Lutfen istediginiz zammı giriniz: "))
makam = input("Lutfen mevcut pozisyonunuzu giriniz: ")
burjuva = yonetici(isim, departman, maas, yil,makam)
burjuva.getInformation()
burjuva.zam(zama)
burjuva.getInformation()
burjuva.takeInformation()