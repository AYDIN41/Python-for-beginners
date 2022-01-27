print("""
********************************
Kullanıcı Giriş Programı
********************************
""")
sys_kullanici_ismi = "Aydın41"

sys_parola = "1071"


i = 0
while (i<3):
    kullaniciAdi = input("Lutfen isminizi giriniz: ")

    parolaa = input("Lutfen parolananızı giriniz: ")
    if(kullaniciAdi != sys_kullanici_ismi and parolaa == sys_parola):
        print("Kullanici adini yanlıs girdiniz")
        i += 1
        print("İsminizimi unuttunuz?")
        decision = input("İsminizi unuttuysanız 'e' e tıklayın: ")
        if(decision=="e"):
            print("Yeni isminizi giriniz...")
            sys_kullanici_ismi = input("Yeni isminizi giriniz")
            i -=1
    elif(kullaniciAdi == sys_kullanici_ismi and parolaa != sys_parola ):
        print("Parolanizi yanlıs girdiniz")
        i += 1
        print("Şifrenizimi unuttunuz?")
        decision = input("Şifrenizi unuttuysanız 'e' e tıklayın: ")
        if(decision=="e"):
            print("Yeni şifre giriniz...")
            sys_parola = input("Yeni şifrenizi giriniz")
            i -=1
    elif(kullaniciAdi != sys_kullanici_ismi and parolaa != sys_parola):
        print("Her ikiside yanlış")
        i += 1
    else:
        print("Dogru Girdiniz")
        break
    if(i==3):
        print("Hakkınız tükendi")


