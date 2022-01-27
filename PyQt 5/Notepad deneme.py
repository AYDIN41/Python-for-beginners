import sys
from PyQt5 import QtWidgets
import os

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.yaziAlani = QtWidgets.QTextEdit()
        self.ac = QtWidgets.QPushButton("Dosya Ac")
        self.kaydet = QtWidgets.QPushButton("Dosya Kaydet")
        self.temizle = QtWidgets.QPushButton("Temizle")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)
        h_box.addWidget(self.temizle)

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yaziAlani)
        v_box.addLayout(h_box)

        self.temizle.clicked.connect(self.temiz)
        self.ac.clicked.connect(self.acik)
        self.kaydet.clicked.connect(self.gaydet)

        self.setWindowTitle("Deneme")
        self.setLayout(v_box)
        self.show()
    def temiz(self):
        self.yaziAlani.clear()
    def acik(self):
        dosyaOkuma = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Okuma",os.getenv("HOME"))
        with open(dosyaOkuma[0],"r") as dosya:
            okuAydinOku = dosya.read()
            self.yaziAlani.setText(okuAydinOku)
    def gaydet(self):
        dosyaOkuma = QtWidgets.QFileDialog.getSaveFileName(self,"Dosya Kaydetme",os.getenv("HOME"))
        with open(dosyaOkuma[0],"w") as dosya:
            dosya.write(self.yaziAlani.toPlainText())


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())