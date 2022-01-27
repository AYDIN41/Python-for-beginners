import requests
from bs4 import BeautifulSoup
import sys

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
        self.show()
        """self.temizle.clicked.connect(self.temiz)
        self.ac.clicked.connect(self.dosyaAC)
        self.kaydet.clicked.connect(self.kaydett)"""


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()



response = requests.get("https://www.doviz.com/")

html_icerik = response.content
doviz = input("Turk lirası karşısında degerini görmek istediginiz birimi giriniz: ")
soup = BeautifulSoup(html_icerik,"html.parser")
turkLirasi = 1
dolar = soup.find_all("td",{"class":"text-bold"})
paraIsmi = soup.find_all("td",{"href":"https://kur.doviz.com/serbest-piyasa/euro"})
for i in dolar:
    i = i.text
    i = i.strip()
    i = i.replace("\n",",")
    if(not(i.startswith("%"))):
        if(doviz=="Dolar"):
            if(i.startswith("8")):
                pencere.yaziAlani.setText(str(i  + " Dolar"))

sys.exit(app.exec_())



