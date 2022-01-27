import numpy as np

data_list = [1,2,3]
arr = np.array(data_list)
print(arr)
data_list2 = [[10,20,30],[40,50,60],[70,80,90]]
arr2 = np.array(data_list2)
print(arr2)
arr3 = np.array([1,23,94,41,10])
print(arr3)
print(arr3[1],arr[0])
print(arr2[1,2])

#arrayları aralık ile alma
print(np.arange(1,21))
#sıralı şekilde arrayları geçiyoruz
print(np.arange(0,94,7))
#istenilen adet kadar 0'yazma
print(np.zeros(7))
#istenilen adet kadar 1'yazma
print(np.ones(5))
#matris şeklinde istenilen adet kadar 0'yazma
print(np.zeros((3,2)))
#matris şeklinde istenilen adet kadar 1'yazma
print(np.ones((2,3)))
# 3.olarak yazılan sayi yazılan iki sayıyı kendi değeri kadar böler
print(np.linspace(0,100,12))
print(np.linspace(0,1,2))
#yazılan değer kadar matris oluşturuluyor ve keşisen sayılar bir keşişmeyen sayılar ise 0 oluyor
print(np.eye(3))
#yazılan iki sayı arasında random sayi atiyor
"""for i in range(0,3):
    print(np.random.randint(0,101))"""
print(np.random.randint(1,100,5))
# 0 ile 1 arasında istenilen kadar sayı atar
print(np.random.rand(5))
#- değerlerinde yazdırılması için
print(np.random.randn(5))
#arange ile alınan sayıların yeniden array e alınması
abc = np.arange(16)
print(abc)
print(abc.reshape(4,4))
newArray = np.random.randint(0,101,10)
print(newArray)
print(newArray.max())
print(newArray.min())
print(newArray.sum())
print(newArray.mean())
print(newArray.argmax())
print(newArray.argmin())
detArray = np.random.randint(1,100,25)
print(detArray)
detArray = detArray.reshape(5,5)
print(detArray)
print(np.linalg.det(detArray))
detArray2 = [[1,4],[7,3]]
print(np.linalg.det(detArray2))