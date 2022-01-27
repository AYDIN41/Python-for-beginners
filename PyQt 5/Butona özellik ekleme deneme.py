import sys
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ozellikEkleme()
    def ozellikEkleme(self):
        self.yaziAlani = QtWidgets.QLabel("Henüz dokunulmadı")
        self.yaziAlani2 = QtWidgets.QLabel("Tıkladıkça 2 ile çarpacak")
        self.buton = QtWidgets.QPushButton("Tıkla")
        self.say = 1

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yaziAlani)
        v_box.addWidget(self.yaziAlani2)
        v_box.addWidget(self.buton)
        v_box.addStretch()
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.buton.clicked.connect(self.click)
        self.show()
    def click(self):
        self.say *= 2
        self.yaziAlani.setText("Yeni Sayiniz: {}".format(self.say))

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
