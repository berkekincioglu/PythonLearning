from library import *
print(""" 
*****************************************************************
islem numarasini giriniz.
1.Kitaplari goster
2.Kitap sorgulama
3.Kitap Ekle
4.Kitap Sil
5.Kitap sayfa sayisi ogren.
Cikmak icin 'q' ya basiniz.


*****************************************************************
""")
kutuphane = Kutuphane()
while True:
    a =input("islem seciniz")
    if (a =='q'):
        break
    elif(a=='1'):
        kutuphane.kitaplari_goster()
    elif(a=='2'):
        try:

            isim = input('Sorgulamak istediginiz kitabi girin.')
            kutuphane.kitap_sorgula(isim)
        except:
            print("Kitabi bulamadik.")
    elif(a=='3'):
        try:
            isim = input('Isim giriniz.')
            yazar = input('Yazar giriniz.')
            yayinevi= input('Yayinevi giriniz.')
            tur = input('Tur giriniz')
            baski= int(input('Baski sayisini giriniz.'))
            sayfa = int(input('sayfa sayisini giriniz'))
            yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski,sayfa)
            kutuphane.kitap_ekle(yeni_kitap)
        except:
            print('Hatali islem yaptiniz.')
    elif(a=='4'):
        try:
            isim = input('Kitap ismini giriniz.') 
            kutuphane.kitap_sil(isim)
        except:
            print('Kitap bulunamadi.')   
    elif(a=='5'):
        try:
            isim = input('kitabi giriniz.')
            kutuphane.kitap_sayfa(isim)
        except:
            print('hata')