import sqlite3

con = sqlite3.connect("Library.db") # sqlite3 ile baglanti olusturduk, library.db olusturduk
cursor = con.cursor() # bir tane kursor yaratdik, veriler uzerinde gezinebilmek icin

def tablo ():
    cursor.execute("CREATE TABLE IF NOT EXISTS books (Isim TEXT, Yazar TEXT, Yayinevi TEXT,Sayfa INT)") #sorgu yaziyoruz
    con.commit() #sorguyu calistiriyoruz

def veri_ekle(): # tablomuza veri ekleme fonksiyonu
    cursor.execute("Insert into books Values('Olu evinden anilar','Fyodor Dostoyevski','Dorlion',480)")
    con.commit()
def veri_ekle2(isim,yazar,yayinevi,sayfa): #kullanicidan veri alarak tabloya ekleyecegiz
    cursor.execute("Insert into books Values(?,?,?,?)",(isim,yazar,yayinevi,sayfa))
    con.commit()
def veri_al():
    cursor.execute("Select *From books") # tum bilgileri getirir
    data=cursor.fetchall()
    for i in data:
        print(i)
def verial2():
    cursor.execute("Select Isim,Yazar From books") # sadece isim ve yazari dondurur
    data=cursor.fetchall()
    for i in data:
        print(i)
def verial3 (yayinevi): # yayinevi verip bilgileri aliyoruz
    cursor.execute("Select *From books where Yayinevi=?",(yayinevi,))
    data=cursor.fetchall()
    for i in data:
        print(i)
def veri_gunceller(eski_yayinevi,yeni_yayinevi):
    cursor.execute("Update books set Yayinevi=? where Yayinevi=?",(yeni_yayinevi,eski_yayinevi))
    con.commit()

def veri_sil(yazar):
    cursor.execute("Delete From books where Yazar=?",(yazar,))
    con.commit()

veri_sil("Maksim Gorki")
veri_al()
# veri_gunceller("Dorlion","Qanun")
# veri_al()

#yayinevi=input("Yayinevi: ")
#verial3(yayinevi)
# isim=input("Kitap ismi: ")
# yazar=input("Kitabin yazari: ")
#
# sayfa=input("Sayfa sayisi: ")
# veri_ekle2(isim,yazar,yayinevi,sayfa)
#veri_ekle()

con.close()





