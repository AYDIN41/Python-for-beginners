def asalSayi():
    for sayi in range(2,1001):
        i = 2
        say = 0
        while (i < sayi):
            if (sayi % i == 0):
                say += 1
            i += 1
        if (say == 0):
            yield sayi
generator = asalSayi()
iterasyon = iter(generator)
for i in iterasyon:
    print(i)