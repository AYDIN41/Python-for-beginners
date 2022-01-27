def ortakBolen(sayi1,sayi2):
    ebob = 1
    enbuyuk = 0
    if(sayi1<sayi2):
        enbuyuk = sayi1
    else:
        enbuyuk = sayi2
    for i in range(1,enbuyuk+1):
        if(sayi1 % i == 0 and sayi2 % i == 0 ):
            ebob = i
    print("En buyuk ortak bolen",ebob)
saui1 = int(input("Lutfen bir sayi giriniz: "))
saui2 = int(input("Lutfen bir sayi giriniz: "))
ortakBolen(saui1,saui2)


