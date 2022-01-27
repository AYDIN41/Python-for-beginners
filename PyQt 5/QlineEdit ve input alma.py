import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()


    def init_ui(self):
        self.yaziAlani = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdır = QtWidgets.QPushButton("Yazdır")
        self.yaziAlani2 = QtWidgets.QLabel("")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yaziAlani)
        v_box.addWidget(self.yaziAlani2)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdır)
        v_box.addStretch()
        self.setLayout(v_box)

        self.temizle.clicked.connect(self.click)
        self.yazdır.clicked.connect(self.click)


        self.show()
    def click(self):
        sender = self.sender()

        if (sender.text() == "Temizle"):
            self.yaziAlani.clear()
        else:
            self.yaziAlani2.setText(self.yaziAlani.text())
            if(self.yaziAlani.text() == "Cemoliber"):
                self.yaziAlani2.setText("Dünyanın en yakışıklısı mı demek istedin?")







app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())

















