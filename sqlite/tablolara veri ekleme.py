import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.
def tabloYapma():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İSİM TEXT,YAZAR TEXT,YAYIN_EVİ TEXT,SAYFA_SAYİSİ INT)")
    con.commit()
def veriEkleme():
    cursor.execute("Insert Into kitaplık Values('İsaya Göre İncil','Jose Saramago','Kırmızı Kedi',387)")
    con.commit()
def IstekVeri(isim,yazar,yayinevi,sayfaSayisi):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayinevi,sayfaSayisi))
    con.commit()

isim = input("Kitap ismi: ")
yazar = input("Yazar ismi: ")
yayinevi = input("Yayınevi ismi: ")
sayfaSayisi = int(input("Sayfa Sayisi: "))
IstekVeri(isim,yazar,yayinevi,sayfaSayisi)
con.close() # Bağlantıyı koparıyoruz.
