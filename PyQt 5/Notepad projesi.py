import sys
from PyQt5 import QtWidgets
import os
class Pencere(QtWidgets.QWidget):
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
        self.show()
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
app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

















