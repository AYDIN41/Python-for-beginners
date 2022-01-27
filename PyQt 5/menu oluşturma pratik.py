import sys
from PyQt5 import QtWidgets

class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosyalar")
        gelistirme = menubar.addMenu("Geliştirme")

        dosyaAcma = QtWidgets.QAction("Dosya Acma",self)
        dosya.addAction(dosyaAcma)

        dosyaKapatma = QtWidgets.QAction("Dosya Kapama",self)
        dosya.addAction(dosyaKapatma)

        cikis = QtWidgets.QAction("Çıkış",self)
        gelistirme.addAction(cikis)

        tiklaveGor = gelistirme.addMenu("Tıkla ve Gör")
        tikla = QtWidgets.QAction("Tıkla",self)
        gor = QtWidgets.QAction("Gör",self)
        tiklaveGor.addAction(tikla)
        tiklaveGor.addAction(gor)
        cikis.triggered.connect(self.cikisYap)
        tiklaveGor.triggered.connect(self.dikla)

        self.show()
    def cikisYap(self):
        QtWidgets.qApp.quit()
    def dikla(self,action):
        if action.text() == "Tıkla":
            print("Tıkladın")
        elif action.text() == "Gör":
            print("Did you see?")






app = QtWidgets.QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())