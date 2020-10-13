import sqlite3
import time

class Kitap():
    def __init__(self,kitap,yazar,yayinevi,baski_sayi):
        self.kitap=kitap
        self.yazar=yazar
        self.yayinevi=yayinevi
        self.baski_sayi=baski_sayi
    def __str__(self):
        return "Kitap : {}\nYazar : {}\nYayinevi : {}\nBaski Sayi : {}".format(self.kitap,self.yazar,self.yayinevi,self.baski_sayi)

class Kutuphane():
    def __init__(self):
        self.baglanti()
    def baglanti(self):
        self.con=sqlite3.connect("Library.db")
        self.cursor=self.con.cursor()

        sorgu="CREATE TABLE IF NOT EXISTS library(isim TEXT,yazay TEXT,Yayinevi Text,baskisayi INT)"
        self.cursor.execute(sorgu)
        self.con.commit()
    def close(self):
        self.con.close()
    def kitap_goster(self):
        sorgu="Select *From library"
        self.cursor.execute(sorgu)
        kitaplar=self.cursor.fetchall()
        if len(kitaplar)==0: # eger kitap yoksa listede
            print("Kitap bulunmamaktadir..")
        else:
            for i in kitaplar:
              kitap=Kitap(i[0],i[1],i[2],i[3]) # Kitap sinfindan object olusturduk
              print(kitap)
    def kitap_sorgula(self,isim):
        sorgu="Select *From library where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if len(kitaplar)==0:
            print("Boyle kitap bulunmuyor..")
        else:
              kitap=Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3])
              print(kitap)
    def kitap_ekle(self,kitap):
        sorgu="Insert into library Values(?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.kitap,kitap.yazar,kitap.yayinevi,kitap.baski_sayi))
        self.con.commit()
    def sil(self,isim):
        sorgu="Delete From library where isim=?"
        self.cursor.execute(sorgu,(isim,))
        self.con.commit()
    def baski_artir(self,isim):
        sorgu="Select *From library where isim=?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar=self.cursor.fetchall()
        if len(kitaplar)==0:
            print("Boyle kitap bulunmuyor..")
        else:
            baski=kitaplar[0][3]
            baski+=1
            sorgu2="Update library set baskisayi=? where isim=?"
            self.cursor.execute(sorgu2,(baski,isim))
            self.con.commit()
