from functools import reduce

def ciftmi(sayi):
    if(sayi % 2 == 0):
        return True
    else:
        return False
def a(sayi,sayi2):
    return sayi+sayi2
liste1 = [1,2,3,4,5,6,7,8,9,10]
liste2 = (list(filter(ciftmi,liste1)))
print(reduce(a,liste2))
