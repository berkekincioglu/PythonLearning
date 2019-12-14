class Bilgisayar():
    def __init__(self,money=0,ram=None,cpu=None,ssd=None,gpu=None,hdd=None):
        self.money= money
        self.ram=ram
        self.ssd=ssd
        self.cpu=cpu
        self.gpu=gpu
        self.hdd=hdd
    def ramArttir(self,yeniRam):
        self.ram =+ yeniRam
        print(self.ram)
    def cpuDegistir(self,yeniCpu):
        self.cpu = yeniCpu
        print(yeniCpu)
    def ssdDegistir(self,yeniSSD):
        self.ssd = yeniSSD
        print(yeniSSD)
    def gpuDesgistir(self,yeniGPU):
        self.gpu=yeniGPU
        print(yeniGPU)
    def paraEkle(self,miktar):
        self.money +=miktar
        print(self.money)
    def hddArttir(self,HDD):
        self.hdd=HDD
        print(self.hdd)
    def moneyGoster(self):
        print(self.money)
    def __str__(self):
        return "Para:{}\nRam:{}\nCPU:{}\nGPU:{}\nHDD:{}\nSSD:{}".format(self.money,self.ram,self.cpu,self.gpu,self.hdd,self.ssd)
print(""" 
BILGISAYAR
Islem Seciniz
1.Ram Arttir
2.CPU Degistir
3.SSD Degistir
4.GPU Degistir
5.Para Ekle
6.HDD Arttir
7.Bilgisayar ozellikler
8.Bakiye Sorgulama
cikis icin '0' yaziniz.
""")

bilgisayar = Bilgisayar()
while True:
    
    try:
        a = int(input("Islem seciniz"))
    except:
        print("Lutfen sadece rakam giriniz")
    if(a==0):
        break
    elif(a==1):
        b=int(input("ram miktari"))
        bilgisayar.ramArttir(b)
        
    elif(a==2):
        b= input("yeni cpu")
        bilgisayar.cpuDegistir(b)
        
    elif(a==3):
        b=input("Yeni ssd")
        bilgisayar.ssdDegistir(b)
        
    elif(a==4):
        b= input("Yeni gpu girin")
        bilgisayar.gpuDesgistir(b)
        
    elif(a==5):
        b=int(input("eklenecek tutar"))
        bilgisayar.paraEkle(b)
    elif(a==6):
        b=int(input("arttirilacak gb"))
        bilgisayar.hddArttir(b)
    elif(a==7):
        print(bilgisayar)
    elif(a==8):
        print(bilgisayar.money)
    else:
        print("Lutfen dogru islem girin")
        break




class Adres_kayit():
    def __init__(self,sehir):
        self.sehir = sehir
        self.sozluk = {}
    def adres_ekle(self,sokak_adi,kapi_no):
        if sokak_adi in self.sozluk:
            self.sozluk[sokak_adi].add=kapi_no
        else:
            self.sozluk[sokak_adi]={kapi_no}
    def sokak_adlarini_getir(self,sokak_adi):
        return self.sozluk[sokak_adi]
    def kapi_nolarini_getir(self,sokak_adi):
        if sokak_adi in self.sozluk:
            return list(self.sozluk[sokak_adi])
        return []

