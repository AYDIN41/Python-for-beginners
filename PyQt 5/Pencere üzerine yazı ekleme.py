import sys
from PyQt5 import QtWidgets,QtGui

def Pencere():
    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle("ABC")
    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    etiket1.setText("Deneme Yazisi...")
    etiket2.setPixmap(QtGui.QPixmap("download.jpg"))
    #etiket1 pencerenin içine yazi atmak için kullanılır
    pencere.setGeometry(50,50,400,400)
    etiket1.move(150,50)
    etiket2.move(300,50)
    #yazılan yazının nerede varolacağını gösterir
    pencere.show()

    sys.exit(app.exec_())
Pencere()















