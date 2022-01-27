
import os
from PyQt5 import QtWidgets
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
    def init_ui(self):
        self.yaziAlani = QtWidgets.QTextEdit()

        self.temizle = QtWidgets.QPushButton("Temizle")
        self.ac = QtWidgets.QPushButton("Dosya Aç")
        self.kaydet = QtWidgets.QPushButton("Dosyaya Veri Kaydet")

        h_box = QtWidgets.QHBoxLayout()

        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QtWidgets.QVBoxLayout()

        v_box.addWidget(self.yaziAlani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.ac.clicked.connect(self.dosyaAc)
        self.show()
        """self.temizle.clicked.connect(self.temiz)
        self.ac.clicked.connect(self.dosyaAC)
        self.kaydet.clicked.connect(self.kaydett)"""
    def dosyaAc(self):
        dosya = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Arama",os.getenv("HOME"))
        with open(dosya[0],"r") as dosya:
            self.yaziAlani.setText(dosya.read())


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

mesaj = MIMEMultipart()
kimden = input("Lutfen mailinizi yazınız: ")
mesaj["From"] = kimden
kime = input("Lutfen mailinizi kime göndereceğinizi yazınız: ")
mesaj["To"] = kime
baslik = input("Lutfen konu baslıgınızı yaziniz: ")
mesaj["Subject"] = baslik

yazi = input("Lutfen genel mesajınızı yazınız: ")

mesaj_govdesi = MIMEText(yazi,"plain")

mesaj.attach(mesaj_govdesi)
sifre = input("Lutfen sifrenizi giriniz: ")

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login(kimden,sifre)

    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())

    pencere.yaziAlani.setText("Mailinizi Basarıyla Gönderdiniz...")

    mail.close()
except:
    """sys.stderr.write("Bir sorun oluştu")
    sys.stderr.flush()"""
    pencere.yaziAlani.setText("Bir sorun oluştu")

sys.exit(app.exec_())









