import sys

from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.yaziAlani = QtWidgets.QLabel("")
        self.buton = QtWidgets.QPushButton("Tıkla")
        self.checkBox = QtWidgets.QCheckBox("Cemoliber'i seviyorsan tıkla")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.checkBox)
        v_box.addWidget(self.yaziAlani)
        v_box.addWidget(self.buton)
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setWindowTitle("Cemoliber")
        self.setLayout(h_box)
        self.checkBox.clicked.connect(lambda : self.click(self.checkBox.isChecked(),self.yaziAlani))
        self.buton.clicked.connect(self.ax)
        self.show()
    def ax(self):
        self.buton.setText("Tıkladın")
    def click(self,checkbox,yazi):
        if checkbox:
            yazi.setText("Dogru Karar")
        else:
            yazi.setText("Wrong Decision")
app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())





