def carpma(x):
    return x * 3
print(list(map(carpma,[1,2,3,4,5,6,7,8,9])))
print(list(map(lambda x : x **2,[2,4,5,6,8,9,11])))
liste1 = [1,2,3,4,5]
liste2 = [6,7,8,9,10]
print(list(map(lambda x,y : x*y,liste1,liste2)))
#map fonksiyonu sayiları kendi aralarında çarpıyor veya teker teker fonskyina gönderiyor


