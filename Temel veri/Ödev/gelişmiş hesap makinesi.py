import math
def toplama(sayi,sayi2):
    print("{} + {} = {}".format(sayi,sayi2,sayi+sayi2))
def cikarma(sayi,sayi2):
    print("{} + {} = {}".format(sayi,sayi2,sayi-sayi2))
def carpma(sayi,sayi2):
    print("{} + {} = {}".format(sayi,sayi2,sayi*sayi2))
def bolme(sayi,sayi2):
    print("{} + {} = {}".format(sayi,sayi2,sayi/sayi2))
def ceil(sayi):
    print("{} = {}".format(sayi,math.ceil(sayi)))
def floor(sayi):
    print("{} = {}".format(sayi,math.floor(sayi)))
def degree(sayi):
    print("{} = {}".format(sayi,math.degrees(sayi)))
def faktoriyel(sayi):
    print("{} = {}".format(sayi,math.factorial(sayi)))
print("Gelişmiş hesap makinesi\nLütfen yapmak istediginiz hesabı seçiniz...\n1-Toplama\n2-Çıkarma\n3-Çarpma\n4-Bölme\n5-Kucuge yuvarlama\n6-Büyüğe yuvarlama\n7-Derece alma\n8-Faktöriyel alma")
decision = int(input("Lutfen yapmak istediğiniz hesabi seçiniz: "))
if(decision== 1):
    sayi = int(input("Lutfen 1.sayiyi yaziniz: "))
    sayi2 = int(input("Lutfen 2.sayiyi yaziniz: "))
    toplama(sayi,sayi2)
elif(decision == 2):
    sayi = int(input("Lutfen 1.sayiyi yaziniz: "))
    sayi2 = int(input("Lutfen 2.sayiyi yaziniz: "))
    cikarma(sayi,sayi2)
elif(decision == 3):
    sayi = int(input("Lutfen 1.sayiyi yaziniz: "))
    sayi2 = int(input("Lutfen 2.sayiyi yaziniz: "))
    carpma(sayi,sayi2)
elif(decision == 4):
    sayi = int(input("Lutfen 1.sayiyi yaziniz: "))
    sayi2 = int(input("Lutfen 2.sayiyi yaziniz: "))
    bolme(sayi,sayi2)
elif(decision == 5):
    sayi = int(input("Lutfen sayiyi yaziniz: "))
    ceil(sayi)
elif(decision == 6):
    sayi = int(input("Lutfen sayiyi yaziniz: "))
    floor(sayi)
elif(decision == 7):
    sayi = int(input("Lutfen sayiyi yaziniz: "))
    degree(sayi)
elif(decision == 8):
    sayi = int(input("Lutfen sayiyi yaziniz: "))
    faktoriyel(sayi)
else:
    print("You did write wrong")
