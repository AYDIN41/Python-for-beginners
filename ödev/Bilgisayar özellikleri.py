import random
import time
import msvcrt
class bilgisayar():
    def __init__(self,bilgisayarDurum="Açık",bilgisayarSes = 0,uygulamalar = ["Windows"],uygulama = "Windows"):
        print("Bilgisayar Açılıyor")
        self.bilgisayarDurum = bilgisayarDurum
        self.bilgisayarSes = bilgisayarSes
        self.uygulamalar = uygulamalar
        self.uygulama = uygulama
    def sesAyari(self):
        while(True):
            sesDeneme = input("Sesi artırmak istiyorsanız '+' kısmak istiyorsanız '-' çıkmak istiyorsanız 'e' e basınız: ")
            if(sesDeneme == '+'):
                if(self.bilgisayarSes<100):
                    self.bilgisayarSes += 1
                    print("Mevcut Sesiniz: ",self.bilgisayarSes)
                else:
                    print("Bundan daha fazla artıramazsınız")
            elif(sesDeneme == '-'):
                if(self.bilgisayarSes>0):
                    self.bilgisayarSes -= 1
                    print("Mevcut Sesiniz: ", self.bilgisayarSes)
                else:
                    print("Bundan daha fazla kısamazsınız")
            elif(sesDeneme == 'e'):
                print("Ses ayarınız en son hali: ",self.bilgisayarSes)
                break
            else:
                print("Girdiginiz deger kabul edilmemektedir")
    def bilgisayaracma(self):
        print("Bilgisayarınız açıktır")
        self.bilgisayarDurum = "Açık"
    def bilgisayarKapatma(self):
        print("Bilgisayar kapanıyor")
        self.bilgisayarDurum = "Kapalı"
    def uygulamaEkle(self,kanal):
        print("Uygulumanız eklendi")
        self.uygulamalar.append(kanal)
    def __len__(self):
        return len(self.uygulamalar)
    def uygulumaSecme(self):
        rastgele = random.randint(0,len(self.uygulamalar)-1)
        self.uygulama = self.uygulamalar[rastgele]
    def __str__(self):
        return  "Bilgisayar Durumu: {}\nBilgisayar Sesi: {}\nUygulamalar: {}\nMevcut Uygulama: {}\n".format(self.bilgisayarDurum,self.bilgisayarSes,self.uygulamalar,self.uygulama)
laptop = bilgisayar()
print("""
Bilgisayar Durumuna Hosgeldiniz

1.İşlem Çıkmak 

2.İşlem Bilgisayarı açma

3.İşlem Bilgisayarı kapatma

4.İşlem Ses ayarı yapma

5.İşlem Uygulama ekleme

6.İşlem Rastgele Uygulama Açma

7.İşlem Mevcut Bilgileri gösterme

""")
while(True):
    karar = int(input("Lutfen işleminizi seçiniz: "))
    if(karar == 1):
        print("Bilgisayardan Çıkıyorsunuz")
        break
    elif(karar == 2):
        laptop.bilgisayaracma()
    elif(karar == 3):
        laptop.bilgisayarKapatma()
    elif(karar == 4):
        laptop.sesAyari()
    elif(karar == 5):
        uygulamalar = input("Lutfen eklemek istediginiz uygulamaları ',' koyarak yaziniz: ")
        eklenecekler = uygulamalar.split(",")
        for i in eklenecekler:
            laptop.uygulamaEkle(i)
        print("Başarılı bir şekilde uygulamanız yüklendi")
    elif(karar == 6):
        laptop.uygulumaSecme()
    elif(karar == 7):
        print(laptop)
    else:
        print("Seçtiğiniz deger kabul edilmemektedir")






































