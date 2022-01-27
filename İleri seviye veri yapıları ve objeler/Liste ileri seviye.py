liste1 = [1,2,3,4,5,6]
liste2 = [21,94,41]
liste1.extend(liste2)
print(liste1)
# extend metodu bir listenin içine başka bir listeyi atamayı saglar
liste1.insert(2,"EMİRHAN")
print(liste1)
liste1.insert(0,"AYDIN")
print(liste1)
#insert metodu istenilen indise istenilen degeri atar
print(liste1.pop(3))
print(liste1)
print(liste1.pop())
print(liste1)
#pop methodu istenilen diziden istenilen değeri siler içerisine deger atılmazsa en sondaki degeri siler
liste1.remove(21)
print(liste1)
liste1.remove("AYDIN")
print(liste1)
#remove methodu içine yazılan degeri siler yanlıs deger yazarsanız hatalı döndürür
print(liste1.index(94))
liste1 = [1,8,8,8,2,3,4,5,6,7,8,94]
print(liste1.index(8,4))
#index methodu degerin kaçıncı indeks de oldugunu gösterir
print(liste1.count(1))
print(liste1.count(10))
print(liste1.count(8))
#count methodu degerin kaç kere yazıldıgını gösterir istenilen deger yoksa 0 yazar
liste1.sort()
print(liste1)
liste1.sort(reverse=True)
print(liste1)
liste1 = ["A","B","C","D","E","F"]
liste1.sort()
print(liste1)
liste1.sort(reverse=True)
print(liste1)
#sort methodu küçükten büyüğe ya da tam tersi sekilde sıralr reserve= True büyükten küçüğe içi boş işe küçükten büyüğe sıralar

