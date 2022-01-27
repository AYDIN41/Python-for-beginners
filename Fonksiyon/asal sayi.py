print("""
*****************************************************
Asal Sayi Programi
*****************************************************
""")
sayi = int(input("Lutfen asal olup olmadıgını kontrol etmek istediginiz sayiyi yaziniz: "))
def asalKontrol(sayii):
    if (sayii == 1):
        print("1 Asal degildir")

    if (sayii == 2):
        print("2 Asaldır")
    for i in range(2,sayii):
        if(sayii % i != 0):
            print("Sayiniz",sayii,"Asal sayidir")
            break
        else:
            print("Sayiniz",sayii,"Asal sayi degildir")
            break
asalKontrol(sayi)
