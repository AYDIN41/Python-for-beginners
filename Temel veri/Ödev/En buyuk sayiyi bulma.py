sayi1 = int(input("Lutfen ilk sayiyi giriniz: "))
sayi2 = int(input("Lutfen ikinci sayiyi giriniz: "))
sayi3 = int(input("Lutfen üçüncü sayiyi giriniz: "))
while(True):
    if(sayi1>sayi2 and sayi1>sayi3):
        print("Yazdıgınız sayilar arasından {} {} {} en buyugu = {}".format(sayi1,sayi2,sayi3,sayi1))
    elif(sayi2>sayi1 and sayi2>sayi3):
        print("Yazdıgınız sayilar arasından {} {} {} en buyugu = {}".format(sayi1,sayi2,sayi3,sayi2))
    elif(sayi2 == sayi1 or sayi2== sayi3 or sayi3 == sayi1):
        print("İki veya daha fazla özdeş sayi var")
    else:
        print("Yazdıgınız sayilar arasından {} {} {} en buyugu = {}".format(sayi1,sayi2,sayi3,sayi3))
    print("Çıkmak isterseniz 'E'e basınız")
    decision = input("Lutfen kararınızı belirtin: ")
    if(decision == "E"):
        print("Çıkıs yapılıyor")
        break
    else:
        print("Devam ediliyor")
        sayi1 = int(input("Lutfen ilk sayiyi giriniz: "))
        sayi2 = int(input("Lutfen ikinci sayiyi giriniz: "))
        sayi3 = int(input("Lutfen üçüncü sayiyi giriniz: "))


