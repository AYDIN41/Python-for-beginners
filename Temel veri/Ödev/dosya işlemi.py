def not_hesapla(satir):


    satir = satir[:-1]

    liste = satir.split(",")

    isim = liste[0]

    not1 = int(liste[1])

    not2 = int(liste[2])

    not3 = int(liste[3])

    son_not = not1 * (3/10) + not2 * (3/10) + not3 * (4/10)

    if (son_not >= 90):

        harf = "AA"
    elif (son_not >= 85):
        harf = "BA"
    elif (son_not >= 80):
        harf = "BB"
    elif (son_not >= 75):
        harf = "CB"
    elif (son_not >= 70):
        harf = "CC"
    elif (son_not >= 65):
        harf = "DC"
    elif (son_not >= 60):
        harf = "DD"
    elif (son_not >= 55):
        harf = "FD"
    else:
        harf = "FF"

    return isim + "------------------> " + harf + "\n"

with open("C:/Users/asus/Desktop/dosya.txt","r",encoding= "utf-8") as file:

    eklenecekler_listesi = []
    kalanlar = []
    gecenler = []

    for satir in file:
        eklenecekler_listesi.append(not_hesapla(satir))
        satir = satir[:-1]
        satireleman = satir.split(",")
        satireleman = satireleman[2]
        for i in satireleman:

            if(i == "AA" or i == "BA" or i == "BB" or i == "CB" or i == "CC" ):
                print("GG")
                gecenler.append(satir + "\n")
            else:
                print("a")
                kalanlar.append("\n" + satir + "\n")
    with open("C:/Users/asus/Desktop/gecenler.txt.txt", "w", encoding="utf-8") as file2:
        for i in gecenler:
            file2.write(i)
    with open("C:/Users/asus/Desktop/kalanlar.txt.txt", "w", encoding="utf-8") as file3:
        for i in kalanlar:
            file3.write(i)







