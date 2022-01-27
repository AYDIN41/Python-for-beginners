from functools import reduce
def toplama(x,z):
    return x*z
def buyukMu(x,z):
    if(x>z):
        return x
    else:
        return z
list2 = []
for i in range(1,6):
    ass = int(input())
    list2.append(ass)

print(reduce(toplama,[1,2,5,3,6,7]))
print(reduce(buyukMu,list2))
#reduce fonksiyonu fibonacci sayiları gibi çalışır bu sayede aralardaki enbüyük sayiları bulabiliriz ya da faktoriyel olarak kullanabiliriz



