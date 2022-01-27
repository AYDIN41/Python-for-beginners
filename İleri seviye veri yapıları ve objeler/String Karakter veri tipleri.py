print("python".upper())
print("PYTHON".lower())
print("PyTHon".upper())
print("PyTHon".lower())
#upper fonksiyonu ya da lower fonksiyonu string leri büyük veya küçük yaparlar
print("Emirhan Aydın AAAAAAYdın AAAAAAAAAAAAAAAydın".replace("A","BABA"))
print("Emirhan Aydın AAAAAAYdın AAAAAAAAAAAAAAAydın".replace(" ","BABA"))
print("Emirhan Aydın AAAAAAYdın AAAAAAAAAAAAAAAydın".replace("Emirhan","BABA"))
#replace fonksiyonu seçilen string in yerine başka bir string yazar
print("EA".startswith("EA"))
print("EA".endswith("ds"))
print("EA".startswith("as"))
print("EA".endswith("EA"))
print(list("Emirhan Aydın BABA".split("a")))
print(list("Emirhan Aydın BABA".split(" ")))
print(list("Emirhan Aydın BABA".split("r")))
#split fonksiyonu istenilen eleman yazılarak yazılan elemana göre ayırım yapar
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEMİRHANAYDİNAAAAAAAAAAAAAAAAAAAAAAAAAAA".strip("A"))
print("                               EMİRHANAYDİN                               ".strip())
print("                               EMİRHANAYDİN                               ".lstrip())
print("                               EMİRHANAYDİN                               ".rstrip())
#strip fonksiyonu elemanın girildiği yeri yok eder lstrip left girersek sol tarafı right girersek sağ tarafı yok eder
liste1 = ["18","06","2000"]
print("/".join(liste1))
liste1 = ["T","B","M","M"]
print(".".join(liste1))
#join fonksiyonu atanmış elemana göre araları tamamlar

print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEMİRHANAYDİNAAAAAAAAAAAAAAAAAAAAAAAAAAA".count("A"))
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEMİRHANAYDİNAAAAAAAAAAAAAAAAAAAAAAAAAAA".count("A",21))
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEMİRHANAYDİNAAAAAAAAAAAAAAAAAAAAAAAAAAA".count("AYDİN"))
#count fonksiyon istenen striingi sayar
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEMİRHANAYDİNAAAAAAAAAAAAAAAAAAAAAAAAAAA".find("E"))
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEMİRHANAYDİNAAAAAAAAAAAAAAAAAAAAAAAAAAA".rfind("M"))
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEMİRHANAYDİNAAAAAAAAAAAAAAAAAAAAAAAAAAA".rfind("as"))
print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEMİRHANAYDİNAAAAAAAAAAAAAAAAAAAAAAAAAAA".find("EMİRHAN"))
#find fonksiyonu yazilan string in dizisini bulur ve yazar rfind bize göre sağ taraftan başlar istenilen deger bulunmaz ise -1 yazar
print("                               EMİRHANAYDİN                               ".lstrip())
print("                               EMİRHANAYDİN                               ".rstrip())
print("                               EMİRHANAYDİN                               ".strip())