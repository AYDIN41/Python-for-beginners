a = 25.56
print(type(a))
b = 25
print(type(a))
c = "Emirhan"
print(type(c))
print(25,45,77)
print(25,45,77,sep = "\n")
print(*"TBMM",sep = ".")
sayi1 = input("Lutfen 1.sayiyi giriniz: ")
sayi2 = input("Lutfen 2.sayiyi giriniz: ")
toplam = int(sayi2) + int(sayi1)
print("{} + {} = {} ".format(sayi1,sayi2,toplam))
print("{1} + {0} = {2} ".format(sayi1,sayi2,toplam))


print("Lutfen dogum tarihinizi giriniz\n")
yildogumTarihi = input("Lutfen Yilinizi giriniz: ")
ayDogumTarihi = input("Lutfen Ayinizi giriniz: ")
gunDogumTarihi = input ("Lutfen Gününüzü giriniz: ")
isim = input ("Lutfen isminizi giriniz: ")
gunDogumTarihi = int(gunDogumTarihi)
print(" Gun {2}  Ay {1} Yıl {0} \n İsminiz {3} ".format(yildogumTarihi,ayDogumTarihi,gunDogumTarihi,isim))
"""




#string parcalama degerleri 0  olan deger baslama 10 olan deger bitiş 2 olan deger ise atlama degeri
isim = "Python Programlama Dili"
print("isim degeriniz:\n",isim[0:10:2])
print("isim degeriniz:\n",isim[::-1])
#ismin uzunlugunu bulmak
print("isim degeriniz sayisi:\n",len(isim))
#matematik işlemleri ile string yazdırma
a = "Emirhan"
b = "Aydın"
c = "41"
print(a + " ",  b  + " ", c)
print(b * 3)
#stringleri toplayip yazma
ad = "Emirhan"
ad = ad + "Aydın41"
print(ad)




sayi = input('1.sayiyi giriniz : ')
sayi2 = input('2.sayiyi giriniz : ')
#carpma gosterimi
print("Carpma")
print( int(sayi) * int(sayi2))
#bolme
print("Bolme")
print( int(sayi) / int(sayi2))
#tamsayili bolme
print("Tam sayili Bolme")
print( int(sayi) // int(sayi2))
print("Mod alma")
print( int(sayi) % int(sayi2))
print("Üst bulma")
print( int(sayi) ** int(sayi2))
"""