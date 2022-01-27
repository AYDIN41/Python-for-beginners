import sys
from PyQt5 import QtWidgets
def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Deneme Deneme")
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText("Hey Hey Dağcı Komando")
    etiket.move(250,75)
    tamam = QtWidgets.QPushButton("Tamam")
    iptal = QtWidgets.QPushButton("Hayır")

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(tamam)
    h_box.addWidget(iptal)
    v_box = QtWidgets.QVBoxLayout()
    v_box.addLayout(h_box)
    v_box.addStretch()
    pencere.setLayout(v_box)
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
Pencere()







