toplam = 0
while(True):
    sayi = int(input("Lutfen bir sayi giriniz: "))
    toplam += sayi
    decision = input("Cıkmak isterseniz 'e' ye basınız: ")
    if(decision=="e"):
        break
print("Toplam sonucu: ",toplam)