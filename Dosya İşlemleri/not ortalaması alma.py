def notOkuma(satir):
    satir = satir[:-1]
    liste = satir.split(",")

    isim = liste[0]
    not1 = float(liste[1])
    not2 = float(liste[2])
    not3 = float(liste[3])

    notOrtalamasi = not1 * 0.3 + not2 * 0.3 + not3 * 0.4
    if(notOrtalamasi>50):
        if(notOrtalamasi<=100 and notOrtalamasi>=90):
             return "İsim: {}\nNot Ortalamanız: {}\nHarfNotunuz= AA".format(isim,notOrtalamasi)
        elif(notOrtalamasi<90 and notOrtalamasi>80):
            return "İsim: {}\nNot Ortalamanız: {}\nHarfNotunuz= BA".format(isim, notOrtalamasi)
        elif (notOrtalamasi <= 80 and notOrtalamasi > 70):
            return "İsim: {}\nNot Ortalamanız: {}\nHarfNotunuz= BB".format(isim, notOrtalamasi)
        elif (notOrtalamasi <= 70 and notOrtalamasi > 60):
            return "İsim: {}\nNot Ortalamanız: {}\nHarfNotunuz= CB".format(isim, notOrtalamasi)
        elif (notOrtalamasi <= 60 and notOrtalamasi > 50):
            return "İsim: {}\nNot Ortalamanız: {}\nHarfNotunuz= CC".format(isim, notOrtalamasi)
    else:
        if(notOrtalamasi <= 50 and notOrtalamasi > 44):
             return "İsim: {}\nNot Ortalamanız: {}\nHarfNotunuz= DC".format(isim, notOrtalamasi)
        elif(notOrtalamasi <= 44 and notOrtalamasi > 0):
            return "İsim: {}\nNot Ortalamanız: {}\nHarfNotunuz= FF".format(isim, notOrtalamasi)
        else:
             print("Puan Sistemine yanlış harf girdiniz")
def notOrtalama(satir):
    satir = satir[:-1]
    liste = satir.split(",")

    isim = liste[0]
    not1 = float(liste[1])
    not2 = float(liste[2])
    not3 = float(liste[3])
    notOrtalamasi = not1 * 0.3 + not2 * 0.3 + not3 * 0.4
    if (notOrtalamasi > 50):
        if (notOrtalamasi <= 100 and notOrtalamasi >= 90):
            return  "AA"
        elif (notOrtalamasi < 90 and notOrtalamasi > 80):
            return "BA"
        elif (notOrtalamasi <= 80 and notOrtalamasi > 70):
            return  "BB"
        elif (notOrtalamasi <= 70 and notOrtalamasi > 60):
            return "CB"
        elif (notOrtalamasi <= 60 and notOrtalamasi > 50):
            return "CC"

    else:
        if (notOrtalamasi <= 50 and notOrtalamasi > 44):
            return  "DC"
        elif (notOrtalamasi <= 44 and notOrtalamasi > 0):
            return  "FF"

eklenecekNotlar = list()
notOrta = []
with open("C:/Users/asus/Desktop/dosya.txt","r",encoding= "utf-8") as dosya:
    for i in dosya:
        eklenecekNotlar.append(notOkuma(i))
        notOrta.append(notOrtalama(i))
for i in notOrta:
    if (i == ["AA"] or i == ["BA"] or i == ["BB"] or i == ["CB"] or i == ["CC"]):
        with open("C:/Users/asus/Desktop/gecenler.txt.txt", "w", encoding="utf-8") as a:
            for i in eklenecekNotlar:
                a.write(i)
    elif (notOrta== ["DC"] or notOrta == ["FF"]):
        with open("C:/Users/asus/Desktop/kalanlar.txt","w",encoding= "utf-8") as c:
            for i in eklenecekNotlar:
                c.write(i)






