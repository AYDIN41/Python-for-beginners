import requests
from bs4 import BeautifulSoup
import sys
import os
from PyQt5 import QtWidgets



class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.yaziAlani = QtWidgets.QTextEdit()

        self.temizle = QtWidgets.QPushButton("Temizle")
        self.ac = QtWidgets.QPushButton("Dosya Aç")
        self.kaydet = QtWidgets.QPushButton("Dosyaya Veri Kaydet")

        h_box = QtWidgets.QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yaziAlani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.ac.clicked.connect(self.dosyaAc)
        self.show()
        """self.temizle.clicked.connect(self.temiz)
        self.ac.clicked.connect(self.dosyaAC)
        self.kaydet.clicked.connect(self.kaydett)"""
    def dosyaAc(self):
        dosya = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Arama",os.getenv("HOME"))
        with open(dosya[0],"r") as dosya:
            self.yaziAlani.setText(dosya.read())
app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

response = requests.get("https://www.imdb.com/chart/top/")

html_icerigi = response.content

secim = float(input("Lutfen izlemek istediginiz minumum rating'i yaziniz: "))
soup = BeautifulSoup(html_icerigi,"html.parser")
basliklar = soup.find_all("td",{"class": "titleColumn"})
ratingler = soup.find_all("td",{"class": "ratingColumn imdbRating"})
for baslik, rating in zip(basliklar,ratingler):
    baslik = baslik.text
    rating = rating.text
    baslik = baslik.strip()
    baslik = baslik.replace("\n","")
    rating = rating.strip()
    rating = rating.replace("\n","")
    if (float(rating) >= secim):
        for i in range(0,10):
            pencere.yaziAlani.setText(baslik[i] + rating[i])




sys.exit(app.exec_())
