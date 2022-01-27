#dosyanın herhangi bir yerine isim gönderme fonksiyonu
with open("C:/Users/asus/Desktop/ea.txt","r+") as dosya:
    liste = dosya.readlines()
    print(liste)
with open("C:/Users/asus/Desktop/ea.txt","r+") as dosya:
    liste.insert(6,"AYDIN\n")
    print(liste)
    dosya.seek(0)
    for i in liste:
        dosya.write(i)
    #for dongusu yerine dosya.writelines()da yazılabilir
with open("C:/Users/asus/Desktop/ea.txt","r+") as dosya:
    print(dosya.read())

"""
#dosyanın basına ekleme yapabilen dosya işlemi
with open("C:/Users/asus/Desktop/ea.txt","r+") as dosya:
    print(dosya.read())
with open("C:/Users/asus/Desktop/ea.txt","r+") as dosya:
    icerik = dosya.read()
    icerik = "Aydin94\n" + icerik
    dosya.seek(0)
    dosya.write(icerik)
with open("C:/Users/asus/Desktop/ea.txt","r+") as dosya:
    print(dosya.read())



#dosyanın sonu isim yazıdıran fonksiyon
with open("C:/Users/asus/Desktop/ea.txt","r+") as dosya:
    print(dosya.read())
with open("C:/Users/asus/Desktop/ea.txt","a") as dosya:
    dosya.write("\nEmirhan AYDIN4194")
with open("C:/Users/asus/Desktop/ea.txt","r+") as dosya:
    print(dosya.read())




#dosya arası işlemler yapma üstüne yazdırma
with open("C:/Users/asus/Desktop/ea.txt","r+") as dosya:
    dosya.seek(13)
    dosya.write("EFSANE")

with open("C:/Users/asus/Desktop/ea.txt","r+") as dosya:
    print(dosya.read())



"""