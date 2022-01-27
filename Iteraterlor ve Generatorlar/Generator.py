def carpıımTablosu():
    for i in range(1,11):
        for j in range(1,11):
            yield "{} x {} = {}".format(i,j,i*j)
generate = carpıımTablosu()
inerate = iter(generate)
for i in inerate:
    print(i)





"""
generate = (i ** 3 for i in range(6))
iterasiyon = iter(generate)
for i in iterasiyon:
    print(i)



import time
def kareal():
    baslama = time.time()
    for i in range(1,100):
        yield i**2
    bitis = time.time()
    print(bitis-baslama)
generator = kareal()
inerator = iter(generator)
for i in inerator:
    print(i)
kareal()
inerator2 = iter(generator)
print(next(inerator2))

"""
