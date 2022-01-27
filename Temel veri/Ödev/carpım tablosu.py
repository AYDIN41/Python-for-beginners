print("""
**************************************
Carpım Tablosuna Hosgeldiniz
**************************************
""")
sayi = 0
for i in range(1,11):
    sayi += 1
    for j in range(1,11):
        print("{} X {} = {}".format(sayi,j,sayi*j))