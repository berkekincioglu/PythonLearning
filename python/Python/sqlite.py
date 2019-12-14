import sqlite3
con = sqlite3.connect('kitaplik.db')
cursor = con.cursor()
def tablo_olustur():
    cursor.execute('CREATE TABLE IF NOT EXISTS kitaplik(isim TEXT,Yazar TEXT,Sayfa_sayisi INT )')
    con.commit()

def veri_ekle(isim,yazar,sayfa_sayi):
    cursor.execute('Insert into kitaplik Values(?,?,?)',(isim,yazar,sayfa_sayi))
    con.commit()
def verileri_al():
    cursor.execute('Select * From kitaplik')
    liste = cursor.fetchall()
    for i,j,k in liste:
        print(i,j,k,sep=',')
def verileri_al2():
    cursor.execute('Select isim,Yazar From kitaplik')
    liste = cursor.fetchall()
    for i in liste:
        print(i)
def verileri_al3(isim):
    cursor.execute('Select * From kitaplik where isim = ?',(isim,))
    liste=cursor.fetchall()                                               
    for i in liste:
        print(i)
def update_data(eski_isim,yeni_isim):
    cursor.execute("Update kitaplik set isim = ? Where isim = ?",(yeni_isim,eski_isim))
    con.commit()
def delete_data(isim):
    cursor.execute("Delete From kitaplik where isim = ?",(isim,))
    con.commit() # komutun gecerli olmasini saglar
#tablo_olustur()    
#delete_data('war art')
#verileri_al()
#verileri_al2()
#verileri_al3('ahmet')        
#isim = input('Isim gir')
#yazar = input('Yazar gir')
#sayfa_sayi = int(input('Sayfa sayisi gir'))
#veri_ekle(isim,yazar,sayfa_sayi)
#update_data('war art','savas sanati')
#delete_data()
con.close()