import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

with open ("C:/Users/asus/Desktop/ac.txt","r+",encoding = "utf-8") as dosya:
    dosya.seek(22)
    okuma = dosya.read(20)

    dosya.seek(0)
    okuma2 = dosya.read((20))
    dosya.seek(65)
    okuma3 = dosya.read()


mesaj = MIMEMultipart()
mesaj["From"] = okuma
mesaj["To"] = okuma
mesaj["Subject"] = "Deneme Odevi"
yazi = okuma2
mesaj_govdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

mesaj2 = MIMEMultipart()
mesaj2["From"] = okuma
mesaj2["To"] = okuma3
mesaj2["Subject"] = "Deneme Odevi"
mesaj2_govdesi = MIMEText(yazi,"plain")
mesaj2.attach(mesaj2_govdesi)
try:
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(okuma,"E14531453")
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    mail2 = smtplib.SMTP("smtp.gmail.com",587)
    mail2.ehlo()
    mail2.starttls()
    mail2.login(okuma,"E14531453")
    mail2.sendmail(mesaj2["From"],mesaj2["To"],mesaj.as_string())
    print("Mailiniz basarı ile gönderildi")
except:
    sys.stderr.write("Hatalı Bir Mail")
    sys.stderr.flush()
