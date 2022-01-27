print("Boy kilo endeksi programına hosgeldiniz")
kilo = float(input("Lutfen kilonuzu giriniz: "))
boy = float(input("Lutfen boyunuzu giriniz: "))
endeks = float(kilo/(boy**2))
print("Vucut kile endeksiniz: {}".format(endeks))
if(endeks<19):
    print("Zayıfsınız")
elif(endeks>=19 and endeks< 26):
    print("Normal kiloya sahipsiniz")
else:
    print("Kilonuz aşırı")