import random
class Kumanda():
    def __init__(self,tvDurum="kapali",ses=0,kanalListesi=["Trt"],kanal="Trt"):
        self.tvDurum=tvDurum
        self.ses=ses
        self.kanalListesi=kanalListesi
        self.kanal=kanal
    def tvAc(self):
        if(self.tvDurum=="kapali"):
            print("tv aciliyor")
            self.tvDurum="acik"
        else:
            print("tv zaten acik")
    def tvKapa(self):
        if(self.tvDurum=="acik"):
            print("kapatiliyor")
            self.tvDurum="kapali"
        else:
            print("zaten kapali")
            
    def sesAyari(self):
       
        print("cikis icin 'q' giriniz")
        while True:
            x = input("Artirmak icin '>',Azaltmak icin '<' giriniz.")
            if (x=='q'):
                print('cikiliyor...')
                break
            elif(x=='>'):
                self.ses +=1
                print(self.ses)
            elif(x=='<'):
                self.ses-=1
                print(self.ses)
            else:
                print("Hatali giris tekrar dene")
                break
    def kanalEkle(self,yeniKanal):
        self.kanalListesi.append(yeniKanal)

    def randomKanal(self):
        y=random.randint(0,len(self.kanalListesi)-1)
        self.kanal=self.kanalListesi[y]
        print(self.kanal)
    def __len__(self):
        return len(self.kanalListesi)
    def __str__(self):
        return "Tv durumu:{}\nSes:{}\nKanal Listesi:{}\nBulundugun Kanal:{}".format(self.tvDurum,self.ses,self.kanalListesi,self.kanal)
kumanda = Kumanda()
print(''' 

Televiyon Uygulamasi.

1.Tv Ac

2.Tv Kapat

3.Ses Ayarlari

4.Kanal Ekle

5.Kanal Sayisini Ogrenme

6.Rastgele Kanal Cevirme

7.Televizyon Bilgileri

cikmak icin 'q' ya basiniz.1




''')

while True:
    a = input("Islem seciniz")
    if(a=='q'):
        print('Cikiliyor...')
        break
    elif(a=='1'):
        kumanda.tvAc()
        
        
    elif(a=='2'):
        kumanda.tvKapa()
        
    elif(a=='3'):
        kumanda.sesAyari()
    elif(a=='4'):
        x=input("kanal girin")
        y=x.split(",")
        for i in y:
            kumanda.kanalEkle(i)
    elif(a=='5'):
        print("Kanal sayisi:",len(kumanda))
    elif(a=='6'):
        kumanda.randomKanal()
    elif(a=='7'):
        print(kumanda)
    else:
        break
