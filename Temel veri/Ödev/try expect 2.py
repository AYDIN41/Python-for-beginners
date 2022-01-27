def ciftTek(sayi):
    if(sayi%2==0):
        return sayi
    else:
        raise ValueError("2'ye bölünenleri giriniz lütfen")

sayii = [1,2,3,4,5,6,3,7,8,5,9,555,22,23]
for i in sayii:
    try:
        print(ciftTek(i))
    except ValueError:
        pass



"""

def ciftTek(sayi):
    if(sayi%2==0):
        return sayi
    else:
        raise ValueError("2'ye bölünenleri giriniz lütfen")

sayii = int(input("Lutfen bir sayi giriniz: "))
ciftTek(sayii)
try:
    print(ciftTek(sayii))
except ValueError:
    print("2'ye bölünenleri giriniz...")

"""
