print("""
*****************************************************
Asal Sayi Programi
*****************************************************
""")
sayi = float(input("Lutfen asal olup olmadıgını kontrol etmek istediginiz sayiyi yaziniz: "))
def asalKontrol(sayii):
    i = 2
    sayi = sayii / 2
    for i in sayi:
        if(sayi % i != 0):
            print("Sayiniz",sayii,"Asal sayidir")
            break
        else:
            print("Sayiniz",sayii,"Asal sayi degildir")
            break
asalKontrol(sayi)

"""

liste1 = [1,2,3,4,5,6]
liste2 = [i * 2 for i in liste1]
print(liste2)

ikiyleCarp = lambda x : x * 2
print(ikiyleCarp(5))
terstenYazdırma = lambda isim : isim[::-1]
print(terstenYazdırma("Emirhan Aydın"))

def ciftmiTekmi(sayi):
    return sayi % 2 == 0
print(ciftmiTekmi(4))
tekmiCiftmi = lambda sayii : sayii % 2 == 0
print(tekmiCiftmi(4))


b = 10
def globalKullanimi():
    b = 2
    print(b)
globalKullanimi()
print(b)
b = 10
def globallKullanimi():
    global b
    b = 2
    print(b)
globallKullanimi()
print(b)

def teksayiileCokislem(*a):
    toplam = 0
    for i in a:
        toplam += i
    print(toplam)
teksayiileCokislem(1,2,3,4,5,6,7,77,7,7,94,7,7,7,7)


def isimBilgi(isim="Bilgi Yok",soyisim="Bilgi Yok",Numara="Bilgi Yok"):
    print("İsim = {} Soyisim = {}  Numara = {}".format(isim,soyisim,Numara))
isimBilgi("1453")
isimBilgi(Numara = "1453")

def toplama(a,b,c):
    return  a+b+c
def carpma(a):
    return a*2
toplam = toplama(3,4,5)
print(carpma(toplam))



def faktoriyel(sayi):
    a = sayi
    if(sayi == 0 or sayi == 1):
        sayi = 1
    for i in range(1,sayi):
        sayi *= i
    print("Girmiş oldugunuz deger: {}\nDegerinizin faktoriyeli: {}".format(a,sayi))
sayii = int(input("Lutfen faktoriyelini bulmak istediginiz degeri giriniz: "))
faktoriyel(sayii)

i = 0
while(i<10):
    i += 1
    if(i == 5):
        continue
    print(i)
    
liste = [1,2,3,4,5]
liste2 = [i*2 for i in liste]
print(liste2)

liste = [[1,2,3],[4,5,6,7,8],[15,78]]
liste2 = [j for i in liste for j in i]
print(liste2)
"""
    