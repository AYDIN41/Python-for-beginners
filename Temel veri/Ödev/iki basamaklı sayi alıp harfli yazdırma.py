birler = ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
yuzler = ["","Yüz","İki yüz","Üç Yüz","Dört Yüz","Beş Yüz","Altı Yüz","Yedi Yüz","Sekiz Yüz","Dokuz Yüz"]
def harfYazdirma(sayi):
    birinci = sayi % 10
    b = sayi % 100
    ikinci = b // 10
    #c = sayi
    ucuncu = sayi // 100


    print("Girmiş oldugunuz sayi: ",sayi,"Okunusu: ",yuzler[ucuncu],"",onlar[ikinci],"",birler[birinci])
harfYazdirma(764)
