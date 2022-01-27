import sys
from PyQt5 import QtWidgets

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.yazi_alani = QtWidgets.QTextEdit()
        self.temizle = QtWidgets.QPushButton("Temizle")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)
        self.setLayout(v_box)
        self.temizle.clicked.connect(self.click)
        self.show()
    def click(self):
        sender = self.sender()
        if sender.text() == "Temizle":
            self.yazi_alani.clear()
app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())













