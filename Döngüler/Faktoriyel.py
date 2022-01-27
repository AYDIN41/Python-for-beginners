sayi = int(input("Lutfen Faktoriyelini bulmak istediginiz degeri giriniz: "))
faktoriyel = 1
for i in range(1,sayi+1):
    faktoriyel = faktoriyel * i
print("Girmiş oldugunuz sayinin: {} faktoriyeli: {}".format(sayi,faktoriyel))