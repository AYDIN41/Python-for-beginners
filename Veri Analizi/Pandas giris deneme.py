import numpy as np
import pandas as pd
labels_list = ["Şevket","Nazım","Turgut","Erdem","Sabahattin"]
data_list = [100,100,90,80,100]
#pd = pd.Series(data_list,labels_list)
np = np.array([10,10,8,5,4])
#abc = pd.Series(np,labels_list)
#print(pd)
#print(abc)
yazarIsmi = pd.Series([10,9,9,10],["Dostoyeski","Bacon","Zola","Yaşar Kemal"])
print(yazarIsmi)
yazarIsmi2 = pd.Series([94,91,90,100],["Dostoyeski","Bacon","Zola","Yaşar Kemal"])
print(yazarIsmi2)
print(yazarIsmi+yazarIsmi2)
total = yazarIsmi + yazarIsmi2
yazar = input("Lutfen bir yazar seçin: ")

print("Seçtiğiniz yazarın Puanı",total[yazar])
