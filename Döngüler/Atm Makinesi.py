print("""
*******************************************
Atm Makinesine Hosgeldiniz

1.İşlem: Bakiye Sorgulama

2.İşlem: Para Çekme

3.İşlem: Para Yatırma

4.İşlem: Çıkış 
*******************************************
""")
anaPara = 10000
while(True):
    islem = int(input("Lutfen işleminizi giriniz: "))
    if(islem==1):
        print("Bakiyeniz... {}".format(anaPara))
    elif(islem==2):
        paracekme = int(input("Lutfen çekmek istediginiz parayi yaziniz: "))
        while(paracekme>anaPara):
            paracekme = int(input(" '-' Bakiyeyi göremezsiniz tekrar deneyin: "))
        print("Çektiginiz Para: {}\nKalan Tutar: {}".format(paracekme,anaPara-paracekme))
        anaPara = anaPara - paracekme
    elif(islem==3):
        paraYatirma = int(input("Lutfen yatirmak istediginiz parayi yaziniz: "))
        print("Yatirdiginiz Para: {}\nKalan Tutar: {}".format(paraYatirma,anaPara+paraYatirma))
        anaPara = anaPara+paraYatirma
    elif(islem==4):
        print("Çıkıs Yapiliyor...\nYine Bekleriz")
        break
    else:
        print("Yanlıs Girdiniz")
