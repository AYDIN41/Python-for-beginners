import numpy as np
arr = np.arange(0,10)
print(arr)
print(arr[3])
print(arr[1:7])
print(arr[:6])
print(arr[::2])
print(arr[:3])
arr[:3] = 94
print(arr)
arr = np.arange(1,10)
print(arr)
arr2 = arr
print(arr2)
arr2[:3] =91
print(arr2)
print(arr)
#arr den alınan bir sayi değişince arr de deişiryor nedeni iki değişkenin tek bir belleğe bağlanmasıdır
arr[:3] = 94
print(arr2)
print(arr)
arr = np.arange(1,10)
arr2 = arr.copy()
print(arr2)
arr2[:4] = 94
print(arr2)
print(arr)
#copy methodu kullanıldığında değişkenler ayrı belleklere bağlanıyor
newArray = np.arange(1,21)
print(newArray)
newArray = newArray.reshape(5,4)
print(newArray)
print(newArray[0,0])
#istenilen satırdan istenilen kadar sayi çekme methodu
print(newArray[:,:2])
print(newArray[:3,:3])
#istenilen satırdan tüm sayıların çekilmesşi
print(newArray[:3,:])
print(newArray[:3])
arr = np.arange(1,11)
print(arr)
print(arr > 3 )
booleanArray = arr > 3
print(arr[booleanArray])
print(arr[arr>7])
print(newArray)
print(newArray[:3,:3])
print(newArray[:,:2])