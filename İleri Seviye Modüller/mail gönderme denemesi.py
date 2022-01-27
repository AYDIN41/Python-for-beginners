import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

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

    print("Mailinizi Basarıyla Gönderdiniz...")

    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu")
    sys.stderr.flush()