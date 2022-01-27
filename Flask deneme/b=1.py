b=1
a=0
for i in range(0,20):
    print(a)
    c = a + b
    a = b
    b = c
isim = "Python öğreniyorum"
i = 1
for i in range(i,41):
    print(isim)
liste = [1,2,3,4,5]
i = 0
while(i<len(liste)):
    print("{} sayi  = {}".format(i+1,liste[i]))
    i += 1

"""
liste = [1,2,3,4,5,6,7,8]
toplam = 0
i = 0
for sayiToplami in liste: 
    i += 1 
    toplam = toplam + sayiToplami
    print("Toplam {} dönme sayisi {}".format(toplam,i))
print("\n")
liste = [1,2,45,84,26,23,94,41,77,88,22]
for bolunmeKurali in liste:
    if(bolunmeKurali % 2 == 0):
        print(bolunmeKurali)
print("\n")
kelime = "Emirhan AYDIN"
for kelimeDeneme in kelime:
    print(kelimeDeneme)
liste = [(1,2,3),(40),(5,600)]
for deneme in liste:
    print(deneme)
liste = [(1,2,3),(40,56,6),(5,600,77)]
for (i,j,k) in liste:
    print("i = {} j = {} k = {} j*k*i = {} ".format(i,j,k,j*k*i))

sozluk = {"bir":1,"iki":2,"üç":3}
for eleman in sozluk:
    print(eleman)
for eleman in sozluk.values():
    print(eleman)
for j,k in sozluk.items():
    print("Anahtar:",j,"Deger:",k)




vizeNot = float(input("Lutfen vize notunuzu giriniz: "))
finalNot = float(input("Lutfen final notunuzu giriniz: "))
notlarToplami = (vizeNot*0.4) + (finalNot * 0.6)
if(notlarToplami<101 and notlarToplami>85):
    print("Notunuz {} 'AA' dır.".format(notlarToplami))
elif(notlarToplami<85 and notlarToplami>60):
        print("Notunuz {} 'BB' dır.".format(notlarToplami))
elif(notlarToplami<60 and notlarToplami>40):
        print("Notunuz {} 'CC' dır.".format(notlarToplami))
elif(notlarToplami<40 and notlarToplami>0):
        print("Notunuz {} 'FF' dır.".format(notlarToplami))
else:
    print("Not hesaplamaları kapsamdışıdır lutfen tekrar deneyin")

sayi = 0
for i in range (1,11):
    sayi = sayi + 1
    for j in range (1,11):
        print("{} X {} = {} ".format(sayi,j,j*sayi))

yas = int(input("Lutfen yasınızı giriniz\n"))
if(yas<19 or yas > 65):
    print("Buraya giremezsiniz")
    print("Because of your age is {}\nWe can not take a responsibility".format(yas))
else:
    print("Hosgeldiniz")

######################################################################################

sayi = int(input("Lutfen bir sayi girin: "))
if(sayi % 2 == 0):
    print("Girdiginiz sayi {} çifttir".format(sayi))
else:
    print("Girdiginiz sayi {} tektir ".format(sayi))
    """
