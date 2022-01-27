kilo =int(input("Lutfen Kilonuzu giriniz: "))
boy = float(input("Lutfen Boyunuzu giriniz: "))
bedenKitleIndeksi = float(kilo / (boy * boy))
if(bedenKitleIndeksi<18.5):
    print("Zayıf {}".format(bedenKitleIndeksi))
elif(bedenKitleIndeksi>=18.5 and bedenKitleIndeksi < 25):
    print("Normal {}".format(bedenKitleIndeksi))
elif(bedenKitleIndeksi>=25.5 and bedenKitleIndeksi < 30):
    print("Fazla kilolu {}".format(bedenKitleIndeksi))
else:
    print("Obez {}".format(bedenKitleIndeksi))

