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
def verileriGuncelle(eskiYayinevi,yeniYayinevi):
    cursor.execute("Update kitaplık set SAYFA_SAYİSİ = ? where SAYFA_SAYİSİ = ?",(yeniYayinevi,eskiYayinevi))
    con.commit()
def verileriSilme(silmeImleci):
    cursor.execute("Delete From kitaplık where YAZAR = ?",(silmeImleci,))
    con.commit()
yeniSayfa = input("Lutfen degiştirilecek imleci yaziniz: ")
verileriSilme(yeniSayfa)
#IstekVeri(isim,yazar,yayinevi,sayfaSayisi)
#veriAl()
con.close() # Bağlantıyı koparıyoruz.