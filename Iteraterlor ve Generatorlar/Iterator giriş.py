class alisverisListesi():
    def __init__(self,alinacaklar):
        self.alinacaklar = alinacaklar
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if(self.index < len(self.alinacaklar)):
            return self.alinacaklar[self.index]
        else:
            self.index = -1
            raise StopIteration
sepet = alisverisListesi(["Elma","Et","Su","Kitap","Soda"])
iterasyonnn = iter(sepet)
print(next(iterasyonnn))
print(next(iterasyonnn))
print(next(iterasyonnn))


for i in iterasyonnn:
    print(i)


"""













class Kumanda():
    def __init__(self,kanal_listesi):
        self.kanal_listesi = kanal_listesi
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        self.index += 1
        if(self.index < len(self.kanal_listesi)):
            return self.kanal_listesi[self.index]
        else:
            self.index = -1
            raise StopIteration
kumanda = Kumanda(["Trt1","Atv","Show Tv","Fox","Cartoon Network"])
iteratison = iter(kumanda)
print(next(iteratison))
for i in iteratison:
    print(i)









liste = [1,2,3,4,5]
iteration = iter(liste)
#print(next(iteration))
for i in iteration:
    print(i)
"""









