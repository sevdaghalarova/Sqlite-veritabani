from kutuphane_project import *
print("""
*** Kitap Programina Hosgeldiniz ***

1. Kitaplari Goster
2. Kitap Sorgulama
3. Kitap Ekle
4. Kitap Sil
5. Baski sukselt

Cikmak icin "q" tusuna basin
""")
kutuphane=Kutuphane()
while True:
    islem=input("Bir islem giriniz..")
    if islem=="q":
        print("Yine Bekleriz  ")
        break
    elif islem=="1":
        print("Kitaplar hazirlaniyor...")
        time.sleep(3)
        kutuphane.kitap_goster()
    elif islem=="2":
        isim=input("Hangi kitabi aramak istersin...? ")
        print("Kitap sorgulaniyor...")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)
    elif islem=="3":
        isim=input("Isim  ")
        yazar=input("Yazar  ")
        yayinevi=input("Yayin evi  ")
        baskisay=input("Baski sayi  ")
        yeni_kitap=Kitap(isim,yazar,yayinevi,baskisay)
        kutuphane.kitap_ekle(yeni_kitap)
        time.sleep(1)
        print("Kitap eklendi..")
    elif islem=="4":
        isim=input("Hangi kitabi silmek istersin? ")
        cevap=input(" Eminmisin? e/h")
        if cevap=="e":
            print("Kitap siliniyor...")
            time.sleep(1)
            kutuphane.sil(isim)
            print("Kitap silindi.")
    elif islem=="5":
        isim=input("Hangi kitapin baskisini yukseltmek istersin?  ")
        kutuphane.baski_artir(isim)
    else:
        print("Gecersiz islem...")



