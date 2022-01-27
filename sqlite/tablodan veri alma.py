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
def veriAl():
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall()
    for i in liste:
        print(i)
def verial2():
    cursor.execute("Select İSİM,YAZAR From kitaplık")
    listee = cursor.fetchall()
    for i in listee:
        print(i)
def verial3(yayinevi):
    cursor.execute("Select * From kitaplık where YAYIN_EVİ = ?",(yayinevi,))
    lis = cursor.fetchall()
    for i in lis:
        print(i)
veriAl()
verial2()
yayinevi = input("Lutfen görmek istediginiz yayinevini giriniz: ")
verial3(yayinevi)
con.close() # Bağlantıyı koparıyoruz.