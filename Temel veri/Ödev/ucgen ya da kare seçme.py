print("********************\nHosgeldiniz\n********************")
print("Geometrik şeklin kosesi 4 mü yoksa 3 mü olacak?")
kose = int(input("Lutfen istediginiz kose sayisini giriniz: "))
if(kose == 4):
    dikKose = float(input("Birinci koseyi giriniz: "))
    dikKose2 = float(input("İkinci koseyi giriniz: "))
    dikKose3 = float(input("Üçüncü koseyi giriniz: "))
    dikKose4 = float(input("Dördüncü koseyi giriniz: "))
    while(dikKose+dikKose2+dikKose3+dikKose4!=360):
        print("Girmis oldugunuz degerler 360'a eşit degildir yeniden giriniz")
        dikKose = float(input("Birinci koseyi giriniz: "))
        dikKose2 = float(input("İkinci koseyi giriniz: "))
        dikKose3 = float(input("Üçüncü koseyi giriniz: "))
        dikKose4 = float(input("Dördüncü koseyi giriniz: "))
    if(dikKose == dikKose2 and dikKose == dikKose3 and dikKose== dikKose4):
        print("Kare")
    elif(dikKose == dikKose3 and dikKose2 == dikKose4)
    else:
        print("Dörtgen")
elif(kose == 3):
    ucKose = float(input("Birinci koseyi giriniz: "))
    ucKose2 = float(input("İkinci koseyi giriniz: "))
    ucKose3 = float(input("Üçüncü koseyi giriniz: "))
    while (ucKose + ucKose2 + ucKose3 != 180):
        print("Girmis oldugunuz degerler 180'e eşit degildir yeniden giriniz")
        ucKose = float(input("Birinci koseyi giriniz: "))
        ucKose2 = float(input("İkinci koseyi giriniz: "))
        ucKose3 = float(input("Üçüncü koseyi giriniz: "))
    if(ucKose == ucKose2 and ucKose== ucKose3):
        print("Eşkenar üçgen")
    elif(ucKose == ucKose2 or ucKose == ucKose3 or ucKose2 == ucKose3):
        print("İkizkenar ucgen")
    else:
        print("Normal ucgen")
else:
    print("Girdiginiz deger geçerli degildir")
