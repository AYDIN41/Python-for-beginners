print("""
**************************
Sayiların bölenlerini bulma
**************************
""")

liste1 = []
def sayiniBoleninibulma(sayi):
    for i in range(2,sayi):
        if(sayi % i == 0):
          # eksil  liste1 = i
            liste1.append(i)
    print("Sayiniz: ",sayi,"Bolenleri: ",liste1)
   # eksik hal, print("Bolenleri: ",liste1)
while (True):
    sayi = input("Lutfen sayinizi giriniz: (Çıkmak istiyorsanız F'e tıklayın)")
    if(sayi=='f' or sayi=='F'):
        print("Çıkıs yapılıyor")
        break
    else:
        sayiniBoleninibulma(int(sayi))
