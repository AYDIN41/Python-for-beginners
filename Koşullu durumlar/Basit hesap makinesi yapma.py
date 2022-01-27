print("""*******************************
Hesap Makinesi Programı

1.İşlem: Toplama

2.İşlem: Çıkarma

3.İşlem: Çarpma

4.İşlem: Bölme

*******************************
""")
sayi = float(input("Lutfen 1.sayiyi giriniz: "))
sayi2 = float(input("Lutfen 2.sayiyi giriniz: "))
decision = input("Lutfen seçmek istediginiz işlemi giriniz: ")
while(True):
    if (decision == "1"):
        print("{} + {} = {}".format(sayi, sayi2, sayi+sayi2))
    elif (decision == "2"):
        print("{} - {} = {}".format(sayi, sayi2, sayi - sayi2))
    elif (decision == "3"):
        print("{} x {} = {}".format(sayi,sayi2 ,sayi * sayi2))
    elif (decision == "4"):
        print("{} - {} = {}".format(sayi, sayi2, sayi / sayi2))
    else:
        print("Cıkış yapılıyor")
        break
    decision = input("Lutfen seçmek istediginiz işlemi giriniz: (Çıkmak istiyorsanız bu tuşların dışında birine tıklayin) ")
    if(decision == "1" or decision == "2" or decision == "3" or decision == "4"):
        sayi = float(input("Lutfen 1.sayiyi giriniz: "))
        sayi2 = float(input("Lutfen 2.sayiyi giriniz: "))


