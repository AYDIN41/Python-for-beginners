liste1 = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5]
print(liste1)
x = set(liste1)
print(x)
x = {"JAVA","JAVA","PYTHON"}
print(x)
x = {"Ali","Mehmed","Salih","Veli"}
for i in x:
    print(i)
x = {1,2,3,4}
print(x)
x.add(5)
print(x)
x = {"Ali","Mehmed","Salih","Veli"}
x.add("EMİRHAN")
print(x)
#add kümeye yeni sayi/string ekliyor
x = {1,2,3,4,5}
y = {1,3,5,7,9}
print(x.difference(y))
print(y.difference(x))
print(x.difference_update(y))
print(x)
#difference kümeler arasında farkları gösterir difference_update ise var olan farkı istenilen kümeye aktarır
print(y.discard(9))
print(y)
x = {1,2,3,4}
print(x.intersection(y))
x.intersection_update(y)
print(x)
#intersection kumelerin keşisim noktalarını yazar
x = {10,20,30,40}
z = {10,20}
print(x.isdisjoint(y))
print(x.isdisjoint(z))
#isdisjoint kümelerin ortak noktası yoksa True varsa False döner
print(z.issubset(x))
print(x.issubset(y))
#issurbet atanan deger alt küme ise True döner değilse False
print(x.union(y))
x.update(y)
print(x)
#union ve update 2 kümeyi birleştiriyor

