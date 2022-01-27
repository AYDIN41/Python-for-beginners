print(bin(4))
print(hex(512))
print(hex(300))
print(abs(-22))
#abs fonksiyonu mutlak deger görevi görür
print(round(3.75))
print(round(5.2))
print(round(4.1))
print(round(7.7))
print(round(7.7229,3))
#round fonksiyonu kesirli sayiyi en yakıın sayiya yollar

boyut = int(input("Kaç sayi girmek istersiniz: "))
liste1 = []
for i in range(1,boyut+1):
    a = int(input("Lutfen sayilarinizi giriniz: "))
    liste1.append(a)
print(max(liste1))
#max fonksiyonu en büyük veriyi gösterir
print(min(liste1))
#min fonksiyonu en küçük sayiyi gösterir
print(sum(liste1))
#sum fonksiyonu liste veya demet içerisindekilerinin toplamını alır tekil int veya float deger kabul edilmez
print(pow(4,3))
print(4**3)
#pow ya da iki çarpma işlemi sembolu (**) üst alma işlemi yapar

