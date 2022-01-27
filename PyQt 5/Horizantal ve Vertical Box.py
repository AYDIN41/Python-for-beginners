import sys
from PyQt5 import QtWidgets
def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Deneme")
    okay = QtWidgets.QPushButton("Tamam")
    cancel = QtWidgets.QPushButton("İptal")
    deneme = QtWidgets.QPushButton("Deneme")

    h_box = QtWidgets.QHBoxLayout()
    #h_box.addStretch()
    #buraya addStretch koyulursa gönderilen degerleri sağa yaslar
    h_box.addWidget(okay)
    h_box.addStretch()
    
    h_box.addWidget(deneme)
    h_box.addStretch()
    #buraya addStretch koyulursa gönderilen degerleri ayırır yaslar
    h_box.addWidget(cancel)

    #h_box.addStretch()
    #buraya addStretch koyulursa gönderilen degerleri sola yaslar
    pencere.setLayout(h_box)


    pencere.setGeometry(100,100,500,500)
    pencere.show()
    sys.exit(app.exec_())
Pencere()





