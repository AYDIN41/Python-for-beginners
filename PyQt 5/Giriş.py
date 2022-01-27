import sys

from PyQt5 import QtWidgets

def Pencere():
    app = QtWidgets.QApplication(sys.argv)
    #applikasyon olusturup alınmak istenilen argumanları alıyor app uygulaması açmak zorunlu
    pencere = QtWidgets.QWidget()
    #pencere olusturmak için gereken işlem QtWidgets.QWidget()
    pencere.setWindowTitle("Giriş Dersi")
    #olusturulan pencereye baslık koyuluyor
    pencere.setGeometry(41,94,700,700)
    #set geometry ile boyutlar ayarlanabilir ilk iki secenek nereden baslayacagı son isi ise boyutları
    pencere.show()
    #açılan pencereyi gösteriyor
    sys.exit(app.exec_())
    #carpı tusuna basılmadıkça programın çalışırlılıgını sürdürür
Pencere()
