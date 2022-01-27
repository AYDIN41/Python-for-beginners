vize1 = float(input("Lutfen 1.vizenizi notunuzu giriniz: "))
while(vize1<0 or vize1>100):
    print("Yazdıgınız not kapsam içerisinde değildir...\nTekrar deneyiniz")
    vize1 = float(input("Lutfen 1.vizenizi notunuzu giriniz: "))
vize2 = float(input("Lutfen 2.vizenizi notunuzu giriniz: "))
while(vize2<0 or vize2>100):
    print("Yazdıgınız not kapsam içerisinde değildir...\nTekrar deneyiniz")
    vize2 = float(input("Lutfen 2.vizenizi notunuzu giriniz: "))
final = float(input("Lutfen final notunuzu giriniz: "))
while(final<0 or final>100):
    print("Yazdıgınız not kapsam içerisinde değildir...\nTekrar deneyiniz")
    final = float(input("Lutfen final notunuzu giriniz: "))
toplamNot = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)
print("Ortalama notunuz: ",toplamNot)
if(toplamNot >= 90 and toplamNot<=100):
    print("AA")
elif(toplamNot >= 85):
    print("BA")
elif(toplamNot >= 80):
    print("BB")
elif(toplamNot >= 75):
    print("CB")
elif(toplamNot >= 70):
    print("CC")
elif(toplamNot >= 65):
    print("DC")
elif(toplamNot >= 60):
    print("DD")
elif(toplamNot >= 55):
    print("FD")
elif(toplamNot < 55 and toplamNot >=0):
    print("FF")
else:
    print("Yazdıgınız not kapsam içerisinde değildir...")
