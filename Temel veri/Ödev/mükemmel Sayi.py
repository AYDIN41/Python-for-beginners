sayi = int(input("Lutfen sayi giriniz: "))
toplam = 0
for i in range(1,sayi):
    if(sayi % i == 0):
        toplam = toplam + i
if(toplam==sayi):
    print("Mukemmel Sayi")
else:
    print("Mukemmel Sayi Degil")



