import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tvAcik(self):
        if (self.tv_durum=="Açık"):
            print("Televiyonunuz açılıyor")
            self.tv_durum = "Açık"
        else:
            print("Televizyon kapalı")
    def tv_sesDegistirme(self):
        while(True):
            cevap = input("Sesinizi artırmak için '>' e basiniz\nAzaltmak  için '<' e basiniz\nÇıkmak için exit'e basin: ")
            if(cevap=='>'):
                if(self.tv_ses < 32):
                    self.tv_ses += 1
                    print("Yeni sesiniz: ",self.tv_ses)
            elif (cevap == '<'):
                if (self.tv_ses > 0):
                    self.tv_ses -= 1
                    print("Yeni sesiniz: ", self.tv_ses)
            elif (cevap == "exit"):
                if self.tv_ses <= 0 and self.tv_ses >= 32:
                    pass
                else:
                    print("Sonuc sesi: ", self.tv_ses)
                    break
            else:
                print("Yanlıs tusladınız bir daha deneyin")


    def kanalEkleme(self,kanal_listesi):
        if(self.kanal_listesi == "Trt"):
            print("Bu kanala mevcutsunuz")

        else:
            self.kanal_listesi.append(kanal_listesi)
    def kanalAcma(self,kanal):
        if(self.kanal==kanal):
            print("Kanalınız: ",self.kanal)
        else:
            print("Kanal Mevcut Degil")
tvdurum = input("Lutfen TV durumunu yaziniz: ")
tvses = int(input("Lutfen TV sesini yaziniz: "))
kanalListesi = list(input("Lutfen TV kanal/kanallarini yaziniz: "))
kanall = input("Lutfen seçmek istediginiz kanalı yaziniz: ")
kumada = Kumanda(tvdurum,tvses,kanalListesi,kanall)
kumada.tvAcik()
kumada.tv_sesDegistirme()
kumada.kanalEkleme(kanalListesi)
kumada.kanalAcma(kanall)











