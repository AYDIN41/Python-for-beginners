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
        dosya2 = dosya[0],dosya[1]
        with open(dosya2,"r") as dosya:
            self.yaziAlani.setText(dosya.read())

app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

response =requests.get("https://www.imdb.com/chart/top/")

html_icerigi = response.content


soup = BeautifulSoup(html_icerigi,"html.parser")
baslıklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})
for baslık,rating in zip(baslıklar,ratingler):
    baslık = baslık.text
    rating = rating.text
    baslık = baslık.strip()
    baslık = baslık.replace("\n","")
    rating = rating.strip()
    rating = rating.replace("\n","")
    pencere.yaziAlani.setText(str(baslık + rating))
sys.exit(app.exec_())