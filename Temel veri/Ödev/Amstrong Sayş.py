sayi = int(input("Lutfen bir sayi giriniz: "))
birincikuvvet = int
ikincikuvvet = int
ucuncukuvvet = int
dorduncukuvvet = int
ust1= int
ust2 = int
ust3 = int
ust4 = int
if(sayi>999):
    birincikuvvet = sayi % 10
    ikincikuvvet = sayi % 100
    ikincikuvvet = int(ikincikuvvet / 10)
    ucuncukuvvet = sayi % 1000
    ucuncukuvvet = int(ucuncukuvvet / 100)
    dorduncukuvvet = sayi % 10000
    dorduncukuvvet = int(sayi / 1000)
    ust4 = dorduncukuvvet ** 4
    ust3 = ucuncukuvvet ** 4
    ust2 = ikincikuvvet ** 4
    ust1 = birincikuvvet ** 4
    if(ust4+ust1+ust2+ust3==sayi):
        print("You did it")

    print(birincikuvvet,ikincikuvvet,ucuncukuvvet,dorduncukuvvet)
elif(sayi>99 and sayi<1000):
    birincikuvvet = sayi % 10
    ikincikuvvet = sayi % 100
    ikincikuvvet = int(ikincikuvvet / 10)
    ucuncukuvvet = sayi
    ucuncukuvvet = int(ucuncukuvvet / 100)

    ust3 = ucuncukuvvet ** 3
    ust2 = ikincikuvvet ** 3
    ust1 = birincikuvvet ** 3
    if ( + ust1 + ust2 + ust3 == sayi):
        print("You did it")