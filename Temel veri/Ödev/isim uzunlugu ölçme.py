def isimDegistirme(isim):
    a = dict()
    for i in isim:
        if(i in a):
            a[i] += 1
        else:
            a[i] = 1
    for isim,sayi in a.items():
        print("Harf:",isim,"Sayi",sayi)
isimDegistirme("ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb")
