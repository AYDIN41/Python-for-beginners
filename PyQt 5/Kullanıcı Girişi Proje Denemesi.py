import sys
from PyQt5 import QtWidgets
import sqlite3
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.baglanti_olustur()
        self.init_ui()
    def baglanti_olustur(self):
        baglanti = sqlite3.connect("database.db")
        self.cursor = baglanti.cursor()

        sorgu = "Create Table If not exists üyeler(kullanıcı_adı TEXT,parola TEXT)"
        self.cursor.execute(sorgu)

        baglanti.commit()

    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yapınız")
        self.yazi_alani = QtWidgets.QLabel("")
        self.setWindowTitle("Kullanıcı İsmi")
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.giris)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.giris.clicked.connect(self.login)


        self.show()
    def login(self):
        ad = self.kullanici_adi.text()
        sifre = self.parola.text()
        sorgu = "Select * From üyeler where kullanıcı_adı = ? and parola = ?"
        self.cursor.execute(sorgu,(ad,sifre))

        hesap = self.cursor.fetchall()

        if (len(hesap) == 0):
            self.yazi_alani.setText("Bu tür bir hesap yok lutfen yeniden deneyin\nLütfen")
        else:
            self.yazi_alani.setText("Hosgeldiniz " + ad)




app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())






















