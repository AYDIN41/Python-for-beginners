import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.radioBaslik = QtWidgets.QLabel("En yakısıklı kimdir?")
        self.cemoliber = QtWidgets.QRadioButton("Cemoliber")
        self.osman = QtWidgets.QRadioButton("Osman")
        self.abdullah = QtWidgets.QRadioButton("Abdullah")
        self.ridvan = QtWidgets.QRadioButton("Rıdvan")
        self.button = QtWidgets.QPushButton("Seç Bakalım")
        self.yaziAlani = QtWidgets.QLabel("")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.radioBaslik)
        v_box.addWidget(self.cemoliber)
        v_box.addWidget(self.osman)
        v_box.addWidget(self.abdullah)
        v_box.addWidget(self.ridvan)
        v_box.addWidget(self.button)
        v_box.addStretch()
        v_box.addWidget(self.yaziAlani)
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.button.clicked.connect(lambda : self.click(self.cemoliber.isChecked(),self.osman.isChecked(),self.abdullah.isChecked(),self.ridvan.isChecked(),self.yaziAlani))

        self.show()
    def click(self,cemo,osman,apo,ridvan,yazi):
        if cemo:
            yazi.setText("Dogru Yanit")
        if osman:
            yazi.setText("Nope")
        if apo:
            yazi.setText("Lutfen")
        if ridvan:
            yazi.setText("Çok uzaklardasın")
        if not(cemo or osman or apo or ridvan):
            yazi.setText("Cemali seç!!!!")

app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())












