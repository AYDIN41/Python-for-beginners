#with ile dosya okuma ile işlemi yapıldıgında dosya kendi kendine kapanıyor
with open("C:/Users/asus/Desktop/ea.txt","r") as dosya:
    okuma = dosya.read()
    print(okuma)
with open("C:/Users/asus/Desktop/ea.txt","r") as dosya:
    dosya.seek(17)
    okuma = dosya.read(11)
    print(okuma)
    dosya.seek(0)
    okuma2 = dosya.read(23)
    print(okuma2)

"""
#dosyanın içindeki envanterlerin içinde gezinmemizi sağlayan fonksiyon 
with open("C:/Users/asus/Desktop/ea.txt","r") as dosya:
    okuma = dosya.read()
    print(dosya.tell())
    dosya.seek(23)
    print(dosya.tell())
    print(okuma)

"""



