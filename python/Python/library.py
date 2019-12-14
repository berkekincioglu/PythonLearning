import sqlite3
import time
class Kitap():
    def __init__(self,isim,yazar,yayinevi,tur,baski,sayfa):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski
        self.sayfa = sayfa
    def __str__(self):
        return "Kitap ismi: {}\n Yazar: {}\n Yayinevi: {}\n Tur: {}\n Baski: {}\n Sayfa Sayisi: {}".format(self.isim,self.yazar,self.yayinevi,self.tur,self.baski,self.sayfa)

class Kutuphane():
    def __init__(self):
        self.baglanti_olustur()
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("kutuphane.db")
        self.cursor = self.baglanti.cursor()
        sorgu = 'Create Table if not exists kitaplar (isim TEXT,yazar TEXT,yayinevi TEXT,tur TEXT,baski INT,sayfa INT)'
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def baglanti_kes(self):
        self.baglanti.close()
    def kitaplari_goster(self):
        sorgu = 'Select * From kitaplar '
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if (len(kitaplar)==0):
            print("Gosterilecek kitap bulunamadi")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4],i[5])
                print(kitap)
    def kitap_sorgula(self,isim):
        sorgu = 'Select * From kitaplar where isim =?'
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()
        if (len(kitaplar)==0):
            print('Hata meydana geldi.')
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4],kitaplar[0][5])
            print(kitap)
    def kitap_ekle(self,kitap):
        sorgu = 'Insert into kitaplar Values(?,?,?,?,?,?)'
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tur,kitap.baski,kitap.sayfa))
        self.baglanti.commit()
    def kitap_sil(self,isim):
        sorgu = 'Delete From kitapler where isim = ?'
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()
    def kitap_sayfa(self,isim):
        sorgu='Select * From kitaplar where isim = ?'
        self.cursor.execute(sorgu,(isim,))
        kitap_=self.cursor.fetchall()
        if(len(kitap_)==0):
            print('Hata')
        else:
            x = kitap_[0][5]
            print(x)