import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.radyoYazisi = QtWidgets.QLabel("Hangi Dili Kullanıyorsun")
        self.java = QtWidgets.QRadioButton("Java")
        self.python = QtWidgets.QRadioButton("Python")
        self.php = QtWidgets.QRadioButton("Php")
        self.yaziAlani = QtWidgets.QLabel("")
        self.button = QtWidgets.QPushButton("Tıkla Gönder")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.radyoYazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.php)
        v_box.addWidget(self.button)
        v_box.addWidget(self.yaziAlani)
        v_box.addStretch()

        self.setWindowTitle("Radio Button")

        self.setLayout(v_box)
        self.button.clicked.connect(lambda : self.click(self.java.isChecked(),self.python.isChecked(),self.php.isChecked(),self.yaziAlani))
        self.show()
    def click(self,java,python,php,yazi):
        if java:
            yazi.setText("Java")
        if python:
            yazi.setText("Python")
        if php:
            yazi.setText("Php")
        if not(java or python or php):
            yazi.setText("Birini seçiniz...")



app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())










