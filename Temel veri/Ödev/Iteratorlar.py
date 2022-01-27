class Kareler():
    def __init__(self,max = 0):
        self.max = max
        self.kuvvet = 0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.kuvvet < self.max):
            self.kuvvet += 1
            sonuc = self.kuvvet ** 2
            return sonuc
        else:
            raise StopIteration
inetarasyon = iter(Kareler(5))
print(next(inetarasyon))
print(next(inetarasyon))
print(next(inetarasyon))
print(next(inetarasyon))
print(next(inetarasyon))
print(next(inetarasyon))
