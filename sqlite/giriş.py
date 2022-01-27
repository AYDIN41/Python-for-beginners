import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.
def tabloYapma():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık(İSİM TEXT,YAZAR TEXT,YAYIN_EVİ TEXT,SAYFA_SAYİSİ INT)")
    con.commit()
tabloYapma()


con.close() # Bağlantıyı koparıyoruz.


"""
import sqlite3 # Sqlite'yı dahil ediyoruz

con = sqlite3.connect("kütüphane.db") # Tabloya bağlanıyoruz.

cursor = con.cursor() # cursor isimli değişken veritabanı üzerinde işlem yapmak için kullanacağımız imleç olacak.

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (İsim TEXT, Yazar TEXT, Yayınevi TEXT, Sayfa_Sayısı INT)") # Sorguyu çalıştırıyoruz.
    con.commit() # Sorgunun veritabanı üzerinde geçerli olması için commit işlemi gerekli.
tablo_oluştur()
con.close() # Bağlantıyı koparıyoruz.


"""