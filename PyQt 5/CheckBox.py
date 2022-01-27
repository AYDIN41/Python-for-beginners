import sys
from PyQt5.QtWidgets import QWidget,QApplication,QCheckBox,QLabel,QPushButton,QVBoxLayout

class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):

        self.checkBox = QCheckBox("Python'ı seviyormusun?")
        self.yaziAlani = QLabel("")
        self.buton = QPushButton("Bana Tıkla")

        v_box = QVBoxLayout()

        v_box.addWidget(self.checkBox)
        v_box.addWidget(self.yaziAlani)
        v_box.addWidget(self.buton)

        self.setWindowTitle("Check Box")
        self.setLayout(v_box)
        self.checkBox.clicked.connect(lambda : self.click(self.checkBox.isChecked(),self.yaziAlani))
        self.buton.clicked.connect(self.abc)
        self.show()
    def click(self,checkBox,yazialani):
        if checkBox:
            yazialani.setText("Pek iyi çok güzel")
        else:
            yazialani.setText("Neden?")
    def abc(self):
        self.buton.setText("Tıkladın")

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())











