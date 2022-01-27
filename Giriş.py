def selam(isim):
    print("SELAM",isim)
selam("Aydın")
merhaba = selam
merhaba("ALi")
del selam
print(type(merhaba))

def fonksiyonn():
    def fonksiyon2():
        print("Kucuk fonksiyondan selamlar")
    fonksiyon2()
    print("Hey Hey Dağcı Komando")
fonksiyonn()
def toplama(*args):
    def doplama(args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    return  doplama(args)
print(toplama(0,1,2,3,4,5,94))



def fonksiyon (*args):
    for i in args:
        print(i)
fonksiyon(1,2,3,4)
def isimliFonksiyon(isim,*args):
    print("İsminiz: ",isim)
    print("*******************")
    for i in args:
        print(i)
isimliFonksiyon("Aydın",1,2,3,4,5,6,7,94)
#*args fonksiyonu ile istenilen sayıda sayiyi gönderip demet şekline sokabiliriz
def yeniFonksiyon (**kwargs):
    print(kwargs)
yeniFonksiyon(isim = "Emirhan",soyisim = "Aydın",numara = 191005026)
def fonk(**kwargs):
    for i,j in kwargs.items():
        print("Arguman: ",i,"Deger: ",j)
fonk(isim = "Emirhan",soyisim = "Aydın",numara = 154)
def fonk(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
#kwargs fonksiyonu ile istenilen isimleri veya objeleri gönderebiliriz bunun sayesinde sözlük gibi kullanım  edinmiş oluruz
fonk(İsim = "Emirhan",Soyisim = "Aydın",Numara = 154)
def birlesikFonk(*args,**kwargs):
    for i in args:
        print(i)
    print("---------------------")
    for i,j in kwargs.items():
        print(i,j)
liste = []
boyut = int(input("Lutfen kaç tane sayi yazmak istiyorsaniz girin: "))
for i in range(1,boyut+1):
    a = int(input("Lutfen sayilari girin: "))
    liste.append(a)
isim = input("Lutfen bir isim girin: ")
Soyisim = input("Lutfen bir Soyisim girin: ")
Numara = int(input("Lutfen bir Numara girin: "))
birlesikFonk(liste,İsim = isim,Soyisim = Soyisim,Numara = Numara)





