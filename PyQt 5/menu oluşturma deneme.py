import sys

from PyQt5 import QtWidgets
import os
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
        self.temizle.clicked.connect(self.temiz)
        self.ac.clicked.connect(self.dosyaAC)
        self.kaydet.clicked.connect(self.kaydett)

    def temiz(self):
        self.yaziAlani.clear()
    def dosyaAC(self):
        """
        acilacakDosya = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Görüntüleme",os.getenv("HOME"))
        with open("C:/Users/asus/Desktop/a.txt","r") as dosya:
            self.yaziAlani.setText(dosya.read())
        :return:
        """
        acilacakDosya = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Görüntüleme",os.getenv("HOME"))
        with open(acilacakDosya[0],"r") as dosya:
            self.yaziAlani.setText(dosya.read())
    def kaydett(self):
        acilacakDosya = QtWidgets.QFileDialog.getSaveFileName(self,"Dosya Veri Aktarma",os.getenv("HOME"))
        with open(acilacakDosya[0],"w") as dosya:
            dosya.write(self.yaziAlani.toPlainText())
class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.menuPenceresi = Pencere()

        self.setCentralWidget(self.menuPenceresi)

        self.menuOlusturma()
    def menuOlusturma(self):
        menubar = self.menuBar()
        dosyaislemleri = menubar.addMenu("Dosya İşlemleri",)
        self.setWindowTitle("Menü")
        ac = QtWidgets.QAction("Dosya Veriyi Gösterme",self)
        ac.setShortcut("Ctrl+A")

        kaydet = QtWidgets.QAction("Dosya Veriyi Kaydetme",self)
        kaydet.setShortcut("Ctrl+Q")

        temizle = QtWidgets.QAction("Yazıları sil",self)
        temizle.setShortcut("Ctrl+Z")

        cikis = QtWidgets.QAction("Çıkış",self)

        dosyaislemleri.addAction(ac)
        dosyaislemleri.addAction(kaydet)
        dosyaislemleri.addAction(temizle)
        dosyaislemleri.addAction(cikis)

        dosyaislemleri.triggered.connect(self.dosya)
        self.show()
    def dosya(self,action):
        if action.text() == "Dosya Veriyi Gösterme":
            self.menuPenceresi.dosyaAC()
        elif action.text() == "Dosya Veriyi Kaydetme":
            self.menuPenceresi.kaydett()
        elif action.text() == "Yazıları sil":
            self.menuPenceresi.yaziAlani.clear()
        else:
            QtWidgets.qApp.quit()

app = QtWidgets.QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())

