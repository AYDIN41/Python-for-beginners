import sys

from PyQt5 import QtWidgets,QtGui
def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("Cemoliber")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("Dünyanın en yakışıklısı kimdir ")
    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("pp.jfif"))
    pencere.setGeometry(200,200,500,500)
    buton = QtWidgets.QPushButton(pencere)
    buton2 = QtWidgets.QPushButton(pencere)
    buton3 = QtWidgets.QPushButton(pencere)
    buton4 = QtWidgets.QPushButton(pencere)
    #butonu cağırmak için kullanılan metod
    buton.setText("A)Cemoliber")
    buton2.setText("B)Cemoliber")
    buton3.setText("C)Cemoliber")
    buton4.setText("D)Cemoliber")
    #cagrılan butonu isimlendirmek için
    buton.setGeometry(75,75,200,50)
    buton2.setGeometry(75,150,200,50)
    buton3.setGeometry(75,225,200,50)
    buton4.setGeometry(75,300,200,50)
    etiket1.move(110,50)
    etiket2.move(75,375)
    pencere.show()

    sys.exit(app.exec_())

Pencere()






