import sys
from PyQt5 import  QtWidgets
def Pencere():

    add = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Vertical Yazı Denemesi")
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")
    h_box = QtWidgets.QHBoxLayout()

    h_box.addWidget(okay)
    h_box.addWidget(cancel)
    h_box.addStretch()
    v_box = QtWidgets.QVBoxLayout()
    v_box.addLayout(h_box)
    v_box.addStretch()
    pencere.setLayout(v_box)
    pencere.setGeometry(100,100,500,500)
    pencere.show()



    sys.exit(add.exec_())
Pencere()












