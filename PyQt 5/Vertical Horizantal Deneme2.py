import sys
from PyQt5 import QtWidgets
def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Aydın41")
    hey = QtWidgets.QPushButton("Hey Hey")
    asker = QtWidgets.QPushButton("Komando")
    h_box = QtWidgets.QHBoxLayout()
    h_box.addWidget(hey)
    h_box.addStretch()
    h_box.addWidget(asker)
    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)

    pencere.setLayout(v_box)
    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
Pencere()








