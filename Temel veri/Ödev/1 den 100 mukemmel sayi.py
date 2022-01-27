def mukemmel(sayı):
    toplam = 0

    for i in range(1, sayı):

        if (sayı % i == 0):
            toplam += i

    return toplam == sayı


for i in range(1, 1001):
    if (mukemmel(i)):
        print("Mükemmel Sayı:", i)



"""
def mukemmelSayi(sayi):
    toplam = 0
    for i in range(1,sayi):
        if (sayi % i == 0):
            toplam = toplam + i
    if (toplam == sayi):
        print(i+1)
for i in range(1,1001):
    mukemmelSayi(i)


"""


