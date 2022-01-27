class uceKatla():
    def __init__(self,max = 0):
        self.max = max
        self.kuvvet = 0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.kuvvet <= self.max):
            sonuc = 3 ** self.kuvvet
            self.kuvvet += 1
            return sonuc
        else:
            self.kuvvet = 0
            raise StopIteration
uc = uceKatla(3)
iterasyon = iter(uc)
for i in iterasyon:
    print(i)












"""class ucekatla():
    def __init__(self,sayilar):
        self.sayilar = sayilar
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if(self.index < len(self.sayilar)):
            return self.sayilar[self.index]**3
        else:
            self.index = -1
            raise StopIteration
ucegatla = ucekatla(range(100))
interasyon = ucegatla
for i in interasyon:
    print(i)
"""