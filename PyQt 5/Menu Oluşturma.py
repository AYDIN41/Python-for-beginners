import sys
from PyQt5 import QtWidgets

class Menu(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        menubar = self.menuBar()

        dosya = menubar.addMenu("Dosya")
        duzenle = menubar.addMenu("Düzenle")


        dosya_Ac = QtWidgets.QAction("Dosya Aç",self)
        dosya_Ac.setShortcut("Ctrl+O")

        dosya_kaydet = QtWidgets.QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+S")

        cikis = QtWidgets.QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_Ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)

        araVedegistir = duzenle.addMenu("Ara ve Degistir")

        ara = QtWidgets.QAction("Ara",self)
        ara.setShortcut("Ctrl+T")
        degistir = QtWidgets.QAction("Değiştir",self)
        degistir.setShortcut("Ctrl+A")
        araVedegistir.addAction(ara)
        araVedegistir.addAction(degistir)
        temizle = QtWidgets.QAction("Temizle",self)
        duzenle.addAction(temizle)
        self.setWindowTitle("Menüler")
        cikis.triggered.connect(self.cikisYap)
        dosya.triggered.connect(self.cevap)

        self.show()
    def cikisYap(self):
        QtWidgets.qApp.quit()
    def cevap(self,action):
        if action.text() == "Dosya Aç":
            print("Dosya Aç'a bastınız")
        elif action.text() == "Dosya Kaydet":
            print("Dosya Kaydet'e bastınız")
        else:
            print("Çıkıyorsunuz")

app = QtWidgets.QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())





















