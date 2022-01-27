import sys
from PyQt5 import QtWidgets
import os
class Notepad(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.yazi_Alani = QtWidgets.QTextEdit()

        self.temizle = QtWidgets.QPushButton("Temizle")
        self.ac = QtWidgets.QPushButton("Ac")
        self.kaydet = QtWidgets.QPushButton("Kaydet")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi_Alani)
        v_box.addLayout(h_box)
        self.setWindowTitle("Note Pad")
        self.setLayout(v_box)
        self.temizle.clicked.connect(self.temizlik)
        self.ac.clicked.connect(self.acc)
        self.kaydet.clicked.connect(self.kaydetme)
    def temizlik(self):
        self.yazi_Alani.clear()
    def acc(self):
        self.ac = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
        with open(self.ac[0],"r") as dosya:
            self.yazi_Alani.setText(dosya.read())
    def kaydetme(self):
        self.kaydet = QtWidgets.QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        with open(self.kaydet[0],"w") as dosya:
            dosya.write(self.yazi_Alani.toPlainText())
class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.pencere = Notepad()

        self.setCentralWidget(self.pencere)

        self.menu_olustur()

    def menu_olustur(self):
        menubar = self.menuBar()
        dosya = menubar.addMenu("Dosya")
        self.setWindowTitle("Menuler")

        dosya_ac = QtWidgets.QAction("Dosya Aç",self)
        dosya_ac.setShortcut("Ctrl+Z")

        dosya_kaydet = QtWidgets.QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("Ctrl+A")

        temizle = QtWidgets.QAction("Temizle",self)
        temizle.setShortcut("Ctrl+W")

        cikis = QtWidgets.QAction("Çıkış",self)
        cikis.setShortcut("Ctrl+Q")

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)
        dosya.triggered.connect(self.cevap)
        self.show()
    def cevap(self,action):
        if action.text() == "Dosya Aç":
            self.pencere.acc()
        elif action.text() == "Dosya Kaydet":
            self.pencere.kaydetme()
        elif action.text() == "Temizle":
            self.pencere.temizlik()
        elif action.text() == "Çıkış":
            QtWidgets.qApp.quit()
app = QtWidgets.QApplication(sys.argv)

menu = Menu()

sys.exit(app.exec_())