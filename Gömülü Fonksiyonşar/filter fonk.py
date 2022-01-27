print(list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6] )))
def asalMı(x):
    if(x==1):
        return False
    elif(x==2):
        return True
    else:
        for i in range(2,x):
            if(x % i == 0 ):
                return False
        return True
print(list(filter(asalMı,range(1,100))))
#filter fonksiyonu gönderilen satiların True olanını döndürür

