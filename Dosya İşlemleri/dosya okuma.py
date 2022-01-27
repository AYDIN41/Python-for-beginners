
dosya = open("C:/Users/asus/Desktop/aydin41.txt","r")


aydin41 = dosya.readlines()
print(aydin41)
#redlines dosyadaki bulunan bütün satırları okuyor
dosya.close()












"""
dosya = open("C:/Users/asus/Desktop/aydin41.txt","r")
#redline ilk satırdar başlayarak teker teker okuyor yazıldıkça +1 şekilde gider

print(dosya.readline())
print(dosya.readline())
print(dosya.readline())

dosya.close()

dosya = open("C:/Users/asus/Desktop/aydin41.txt","r")

okuma = dosya.read()
# kolay şekilde yazdıklarımızı okumak için
print("Dosyaniz: ",okuma,sep="")


dosya.close()



dosya = open("C:/Users/asus/Desktop/aydin41.txt","r")
for i in dosya:
    print(i, end = "")
dosya.close()


"""