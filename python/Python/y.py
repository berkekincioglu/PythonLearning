#  evrim = "bilime olene kadar hizmet edecegim"
#  print("""**********************************************
#  Odev 4

#  1.Secim = Dortgen
#  2.Secim = Ucgen
#  ***********************************************
#  """)
#  secim = int(input("Seciminizi rakam olarak yazin"))
# if(secim==1):
#      a=int(input("1. kenari giriniz!:"))
#      b=int(input("2. kenari giriniz!:"))
#      c=int(input("3. kenari giriniz!:"))
#      d=int(input("4. kenari giriniz!:"))
#     if(a==b and a==c and b==c):
#          print("Kare")
#     else:#         print("Dortgen")    
# elif(secim==2):
#      a=int(input("1. kenari giriniz!:")) 
#      b=int(input("2. kenari giriniz!:")) 
#      c=int(input("3. kenari giriniz!:")) 
#      if (a==b and a!=c):
#          print("Ikizkenar ucgen")
#      elif(b==c and b!=a):
#          print("Ikizkenar ucgen")    
#      elif(a==b and a==c):
#          print("Eskaner ucgen")
#      else:
#          print("Ucgen belirlenemiyor")        
#  else:
# #     print("Seciminizi dogru yapin!")

# #WHILE LOOP
# # i=0
# # while(i<10):
# #     print(i)
# #     i+=1
# # a=0
# # while(a<40):
# #     print("40 kere while loop yazdiriyorum.")
# #     a+=1
# # liste = [0,1,2,3,4]
# # for i in liste:
# #     print(i) 
# # i=0
# # while(i<len(liste)):
# #     print("Index:",i,"Liste:",liste[i])
# #     i+=1 
# """ range(baslangic degeri,bitis degeri) Fonksiyonu:
# verilen degerlere gore range isimli yapi olusturur.
# bu yapi listelere oldukca benzer
# """
# #x=range(0,20)
# #print(*x) 
# # print(*range(15))
# # print(*range(0,102,2))
# # print(*range(20,0,-1)) #20 den 0 kadar -1 atlayarak git(tersten git)

# # for i in range(1,10): # 100 elemanli liste yapmak yerine range fonksiyonu kullanilabilir.
# #     print("*"*i)
# ## Break--Continue
# """
# """
# # while True:
# #     isim=input("Isim giriniz(cikmak icin q giriniz):")
# #     if(isim=="q"):
# #         print("programdan cikiliyor...")
# #         break
     
# #     else:
# #         print("Isminiz:",isim)

# # liste = list(range(0,11))          """
# #                                     i =3 veya i=5 olursa continue gelir kod satirinin basina donup devam eder. 
                                    
# #                                    """
# # for i in liste:
# #     if(i==3 or i==5):
# #         continue
# #     print("i:",i)
# '''
# a=0
# while(a<10):
#     if(a==2):
#         a+=1
#         continue
   
#     print(a)
#     a+=1
# '''
# #LIST COMPREHESION
# # liste1=[1,2,3,4,5]
# # liste2=[]
# # for i in liste1:
# #     liste2.append(i)
# # print(liste2)
# # liste2=[i for i in liste1] #list comprehesion
# # print(liste2)
# # liste=[1,2,3]
# # liste3=[]
# # liste3=[i*2 for i in liste]
# # print(*liste3)
# # liste5=[(1,2),(3,4),(5,6)]
# # liste4=[(i,j) for (i,j) in liste5]
# # print(liste4)
# # t=[[1,2,3],[5,4,7],[12,6,9,8,]]
# # m=[]
# # for i in t:
# #     print(i)
# #     for x in i:
# #         m.append(x)     
# #     print(m)
# # print(m)


# ###KULLANICI GIRISI
# # kullanici_adi="berk"
# # sifre = "1234"
# # giris_hakki=3
# # while True:
# #     x = input("Kullanici Adi:")
# #     y= input("Sifre")
# #     if(x!=kullanici_adi or y!=sifre):
# #         print("Kullanici adi veya sifre hatali")
# #         giris_hakki -=1
# #     else:
# #         print("Giris yapildi.")
# #         break
# #     if(giris_hakki==0):
# #         print("Giris hakkiniz bitti")
# #         break

# # ATM MAKINESI


#  print("""
# # ******************************************
# # ATM MAKINESINE HOSGELDINIZ
# # 1.Bakiye sorgulama
# # 2.Para yatirma
# # 3.Para cekme
# # Cikis icin 'q' ya basin.
# # ******************************************

#  """)
# bakiye = 1000
# while True:
#     islem =input("Islemi seciniz")
#     if(islem=="q"):
#         print("Islem Sonlandirildi.")
#         break
#     elif(islem=="1"):
#         print("Bakiyeniz:{}".format(bakiye))
#         break
#     elif(islem=="2"):
#         miktar = int(input("Miktari giriniz."))
#         yeni_bakiye = miktar+bakiye
#         print("Islem tamamlandi.Guncel bakiyeniz:{}".format(yeni_bakiye))
#         break
#     elif(islem=="3"):
#         miktar=int(input("Cekilecek miktari girin."))
#         if(miktar<=bakiye):
#             yeni_bakiye = bakiye-miktar
#             print("Islem Tamamlandi.Guncel bakiye:{}".format(yeni_bakiye))
#             break
#         else:
#             print("Islemi tamamlayamiyoruz.Bakiye yetersiz.")
#             continue
#     else:
#         print("Gecersiz islem.")
#         break

#FAKTORIYEL BULMA
# print("""
# *****************************************
# Faktoriyel Bulma Programi

# cikmak icin 'q' ya basiniz.
# *****************************************
# """)
# number = input("Sayi girin.")
# while True:
#     if(number=='q'):
#         print("Programdan cikildi.")
#         break
#     else:
#         faktoriyel = 1
#         number = int(number)
#         for i in range(2,number+1):
#             faktoriyel*=i
#         print(faktoriyel)
#         break
#FIBONACCI SERISI
# a=1
# b=1
# fibonacci=[a,b]
# for i in range(20):
#     a,b=b,a+b
#     fibonacci.append(b)
# print(fibonacci)
#PROBLEM 1 MUKEMMEL SAYI BULMAK.
# sayi = int(input("Sayi girin."))
# i=1
# toplam=0
# while(i<sayi):
#     if(sayi%i==0):
#         toplam +=i
#         i+=1
#     else:
#         i+=1
# if(toplam==sayi):
#     print("{} Mukemmel sayi!".format(sayi))
# else:
#     print("{} Mukemmel sayi degil!".format(sayi))

#PROBLEM 2 ARMSTRONG SAYISI
#PROBLEM 3
# for i in range(1,11):
#      print("'''''''''''''''''''''''''''''''''''''")
#      for j in range(1,11):
#          print("{}x{}={}".format(i,j,i*j))
#PROBLEM 4
# toplam=0
# while True:
#     x=input("Sayi girin!")
#     if(x=='q'):
#         print(toplam)
#         break
#     else:
#         x=int(x)
#         toplam+=x
#PROBLEM 5
# for i in range(101):
#     if(i%3==0):
#         print(i)
#     else:
#         continue
# liste1=range(1,101)
# liste2=[]
# for i in liste1:
# #     if(i%2==0): """
#          liste2.append(i)
#      else:
#          continue
#  print(liste2)
# #ARMSTRONG SAYISI
#  sayi = input("Sayi giriniz.")
#  x = len(sayi)
#  toplam=0
#  for i in sayi:
#      toplam+=int(i)**x
#  if(toplam==int(sayi)):
#      print("done")
#  else:
#      print("none") """

# METHODLAR
#FAKTORIYEL FUNCTION
""" def faktoriyel(sayi):
    faktoriyel=1
    if(sayi==0 or sayi==1):
        print("Faktoriyel",faktoriyel)
    else:
        while(sayi>1):
            faktoriyel*=sayi
            sayi-=1
    print(faktoriyel)
faktoriyel(6) """
#RETURN PARAMETRESI
# def toplama(*a):
#     toplam=0
#     for i in a:
#         toplam+=i
#     print(toplam)
# toplama(1,2,3,4,5,6,7,8,9,10)
    
##GLOBAL YEREL DEGISKENLER
# d=5
# def function():
#     global d
#     d=3
#     print(d)
# function()
# print(d)
#LAMBDA IFADELERI
# def ikiylecarp(x):
#     return x*2
# ikiylecarp1 = lambda y:y*2
# print(ikiylecarp(3))
# print(ikiylecarp1(3))
##ASAL SAYI PROGRAMI

# def asal_sayi(sayi):
#     if(sayi==1):
#         return False
#     elif(sayi==2):
#         return True
#     for i in range(2,sayi):
#         if(sayi%i==0): 
#             return False
#     return True

# while True:
#     sayi = input("Sayi giriniz.")
#     if(sayi=='q'):
#         break
#     else:
#         sayi=int(sayi)
#         if(asal_sayi(sayi)):
#             print("Asal sayidir.")
#         else:
#             print("Asal degildir.Bolenleri{}dir".format(liste))

# def tam_bolenler(sayi):
#     liste=[]
#     for i in range(2,sayi+1):
#         if(sayi%i==0):
#             liste.append(i)
#     return liste
# while True:
#     sayi=input("Sayi girin")
#     if(sayi=='q'):
#         break
#     else:
#         sayi = int(sayi)
#         print("Tam bolenler",tam_bolenler(sayi))
    
# PROBLEM 1
# def mukemmel_sayi(sayi):
#     toplam=0
#     for i in range(1,sayi):
#         if(sayi%i==0):
#             toplam +=i
#     if(toplam==sayi):
#         return True
# for i in range(1,1001):
#     if(mukemmel_sayi(i)):
#         print("Mukemmel",i)
'''2 basamakli sayilarin okunuslarini yazdirmak. '''
# liste1=['','bir','iki','uc','dort','bes','alti','yedi','sekiz','dokuz']
# liste2=['','on','yirmi','otuz','kirk','elli','altmis','yetmis','seksen','doksan']
# def problem(sayi):
#     birinci_sayi=sayi%10
#     ikinci_sayi=sayi//10
#     return liste2[ikinci_sayi]+" "+liste1[birinci_sayi]
# while True:
#     sayi = int(input("iki basamakli sayi girin"))
#     if(len(str(sayi))==2):
#         print(problem(sayi))
#     else:
#         print("Hatali")        
#         break
##1 den 100 e kadar pisagor degerleri bulmak
# def pisagor_bulma():
#     liste=[]
#     for i in range(1,101):
#         for j in range(1,101):
#             c=(i**2+j**2)**0.5
#             if(c==int(c)):
#                 liste.append((i,j,int(c)))
#     return liste
# for i in pisagor_bulma():
#     print(i)
##MODUL
#math modulunu programa dahil etmek icin --> import math
#modul icindeki fonksiyonlari gormek icin ==> dir(math)
#import math
#print(math.factorial(1000))
#import math as matematik ----> math modulunu matematik adi ile kullan demek.
''' from math import * ==> math modulu icindeki tum fonksiyonlari dahil etmek istiyorum. '''
# factoriel(5) ===> 120    math.factoriel yazmamiza gerek kalmaz.
# from math import floor,ceil ==> sadece 2 fonksiyonu aldik diger math fonksiyonlari calismaz.
#################################### SAYI TAHMIN OYUNU 1-10000 #####################################################
# import random
# import time
#  print('''
#  ***************************************************************

     #   ==============TAHMIN OYUNU=================
# 10 tahmin hakkiniz var.
# 
# ***************************************************************
# ''')
# rastgele_sayi=random.randint(1,10)
# tahmin_hakki=3
# print("Tahmin hakkiniz:",tahmin_hakki)
# while True:
#     x = int(input("Tahmininizi girin!."))
#     if(x<rastgele_sayi):
#         print("Sayi sorgulaniyor.")
#         time.sleep(1)
#         print("Daha buyuk tahmin yapin.")
#         tahmin_hakki-=1
#         print("Kalan tahmini hakkiniz:",tahmin_hakki)

#     elif(x>rastgele_sayi):
#         print("Sayi sorgulaniyor.")
#         time.sleep(1)
#         print("Daha dusuk bir tahmin yapin")
#         tahmin_hakki-=1
#         print("Kalan tahmin hakkiniz:",tahmin_hakki)
        
    
#     elif(x==rastgele_sayi):
#         print("Tebrikler dogru cevap=",rastgele_sayi)
#         break
#     if(tahmin_hakki==0):
#         print('Game over')
#         break
# NESNE TABANLI PROGRAMLAMA
#-1 CLASSES
# class Car():
#     def __init__(self,model,color,horse_power):
#         self.model=model
#         self.color=color
#         self.horse_power=horse_power
#         print("init cagirildi.")
# mustafa_car=Car("BMW","White",300)
# print(mustafa_car)
# print(mustafa_car.model)

class softwareEngineer():
    def __init__(self,name,languages,salary,age):
        self.name=name
        self.languages=languages
        self.salary=salary
        self.age=age
    def printInformation(self):
        print(""" 
        
        Engineer;
        Name = {}
        Languages={}        
        Age ={}
        Salary={}
        
        """.format(self.name,self.languages,self.age,self.salary))
    def payUp(self,newSalary):
        self.salary+=newSalary
    def addLanguage(self,*args):
        for i in args:
            self.languages.append(i)

murat = softwareEngineer("Murat",["Javascript,React,Python"],1200,21)
#del ---> bir objeyi silmemizi saglar
### INHERITANCE
#TRY,EXCEPT
# try:
#     a = int(input("Sayi girin"))
# except:
#     print("Hata olustu")
# finally:
#     print("Islemler sona erdi.")
#FINALLY ---> hata olsa bile mutalaka calisan kodlar
#RAISE
def terscevir(s):
    if(type(s)!=str):
        raise ValueError("Lutfen string girin.")
    else:
        return s[::-1]

print(terscevir("bam"))
try:
    print(terscevir("sinsa"))
except:
    print("HATALI ISLEM")

##PROBLEM 1
liste = ["345","sadas","324a","14","kemal"]
# for i in liste:
#     try:
#         i = int(i)
#         print(i)
#     except:
#         pass

# def cift(sayi):
#     if(sayi%2==0):
#         return sayi
#     else:
#         raise ValueError

# liste = range(101)
# for i in liste:
#     try:
#         print(cift(i))
#     except:
##          print("Hatali islem")


#DOSYA OKUMA

'''
# file= open("bilgiler.txt","a")
# file.write("berk baba\n")
# file = open("bilgiler.txt","r")
# #for i in file:
#  #   print(i,end="")   # end komutu i nin bosluk koymasini engeller.
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readline(),end='')
# print(file.readlines()) # liste olarak tim satirlari okumayi saglar.
# file.close
# 'w' parametresi islem sonu silmeyi saglar
# 'a' dosya acip yazmayi hazirda yazili olanlara eklemeyi saglar
# 'r'dosyalari okumak ve verileri almak icin kullaniriz.
# read() function
#a = file.read()
#print("Dosya icerigi:\n",a,sep='')
#readline() function
 
# with open("bilgiler.txt","r") as file:
#     for i in file:
#         print(i,end='')
# seek() - tell()
# with open("bilgiler.txt","+r") as file: # r+ hem okuma hem yazma islemi saglar.
#     file.seek(2)
#     file.write("zaq")
#     print(file.read())
    # print(file.tell())
    # file.seek(4)
    # print(file.tell())
    # file.seek(5)
    # a=file.read(10)
    # print(file.tell())
    # print(a)
'''
##MAP FONKSIYONU
'''
def double(x):
    return x*2
print(list(map(double,[1,2,3,4,5,6,7])))
a = list(map(lambda x:x**2,[1,2,3,4,5,6,7,8,9,]))
print(a)
liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10]
a = list(map(lambda x,y: x*y,liste1,liste2))
print(a)
'''
## REDUCE FONKSIYONU --> once ilk 2 islemi uygular 2. islemin sonucunu tek alarak diger islemlere uygular.
'''
from functools import reduce
def toplama(x,y):
    return x+y
print(reduce(toplama,[12,18,20,10,30]))
'''
##FILTER FONKSIYONU --> reduce dan farki gonderilen fonksiyonun true veya false dondurmesidir.
# filter ile asal mi fonksiyonu
'''
def asal_mi(x):
    i=2
    if(x==1):
        return False
    elif(x==2):
        return True
    else:
        while(i<x):
            if(x%i==0):
                return False
                i+=1
            else:
                return True
                i+=1
print(list(filter(asal_mi,range(1,101))))
'''
##ZIP FONKSIYONU
'''
liste1=[1,2,3,4,5]
liste2=[6,7,8,9,10,11]
sonuc=[]
i=0
while(i<len(liste1)and i<len(liste2)):
    sonuc.append((liste1[i],liste2[i]))
    i+=1
print(sonuc)

print(list(zip(liste1,liste2)))  ##== yukardaki islemlerin kisaltilmis fonksiyonudur

liste=['python','javascript','react']
liste2=[1,2,3]
for i,j in zip(liste2,liste):
    print(i,j)
sozluk1={'bir':1,'iki':2,'uc':3}
sozluk2={'dort':4,'bes':5,'alti':6}
print(list(zip(sozluk1,sozluk2)))
print(list(zip(sozluk1.values(),sozluk2.keys())))
'''
##ENUMERATE FONKSIYONU
'''
liste=['bir','iki','uc']
i=0
sonuc=[]
while(i<len(liste)):
    sonuc.append((i,liste[i])) ## LISTE ICINDEKI ELEMANLARI INDEXLERIYLE TUPLE'a cevirdik
    i+=1
print(sonuc)

print(list(enumerate(liste)))
'''
## ALL ve ANY FONKSIYONLARI
'''
def hepsi(liste):
    for i in liste:
        if not i:
            return False
        else:
            return True
liste=[False,False,False]
liste2=[False,False,True]
liste3  = [1,2,3,4,5,6]
print(hepsi(liste))
print(hepsi(liste2))
print(hepsi(liste3))

def herhangi(liste):
    for i in liste:
        if i:
            return True
    return False
print(herhangi(liste))   
print(herhangi(liste2))
print(herhangi(liste3))

print(all(liste))
print(all(liste2))
print(all(liste3))
print(any(liste))
print(any(liste2))
print(any(liste3))

'''
### PROBLEM -1
'''
def alan(liste):
    return liste[0]*liste[1]
liste = [(3,4),(10,3),(5,6),(1,9)]
print(list(map(alan,liste)))
'''
## PROBLEM-2
'''
liste = [(3,4,5),(6,8,10),(3,10,7)]
def ucgen(x):
    if(x[0]+x[1]>x[2]and abs(x[0]-x[1])<x[2]):
        return True
    return False
print(list(filter(ucgen,liste)))
'''
### PROBLEM -3
'''
from functools import reduce
liste= [1,2,3,4,5,6,7,8,9,10]
a = list(filter(lambda x:x%2==0,liste))
print(a)
print(reduce(lambda x,y:x+y,a))
'''
###PROBLEM -4
'''
import pprint
isimler = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
soyisimler= ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
a = zip(isimler,soyisimler)
for i in a:
    print(i)
'''
## ILERI SEVIYE SAYILAR
'''
# 10 luk tabandaki sayiyi 2 lik tabana cevirmek ====> bin()
# 10 luk tabandaki sayiyi 16 lik tabana cevirmek ====> hex()
# bir sayinin mutlak degerini almamizi saglar ====> abs()
# sayilari alta veya uste yuvarlamamizi saglar ====> round()
# en buyuk sayiyi dondurur ====> max()
# en kucuk sayiyi dondurur ====> min()
# tum sayilarin toplanmasini saglar ====> sum()
# bir sayinin ussunu almayi saglar ====> pow()
'''
# STRING METHODLARI

# upper()----lower()
x = 'python'
a='PYTHON'
print(x.upper())
print(a.lower())
# replace()
print(a.replace('Y','x'))
# startswith(x) -- string x ile basliyorsa true baslamiyorsa false dondurur 
# endswith(x) -- string x ile bitiyorsa true bitmiyorsa false dondurur
# split() ====> stringi parcalayarak her parcayi bir listeye atar
x = 'python-java'
print(list(x.split('-')))
#strip() ====> strip(x) - stringin basinda ve sonunda bulunan x degerlerini siler
#lstrip() ====> lstrip(x) - stringin sadece basinda bulunan x degerini siler
#rstrip() ====> rstrip(x) - stringin sadece sonunda bulunan x degelerini siler
a = 'abcddddd'
b='abcaaa'
print(a.rsplit('d'))
print(a.lstrip('a'))
print(b.strip('a'))
# join() ====> listenin her bir elemanina verdigimiz degerle birlestirerek string olusturur.
liste = ['21','12','49']
c=''.join(liste) 
print(c)
# count() ====> count(x) - string icindeki x degerlerinin sayisini soyler
# count* =====> count(x,index) - string icindeki x degerlerini verilen indexten baslayarak saymaya baslar
# find() ====> find(x) - x degerinin stringin basinda aramaya baslar buldugu ilk indexi bize dondurur. bulamazsa '-1' dondurur
# rfind() ====> rfind(x) - x degerini stringin sonundan itibaren arayip buldugu ilk indexi dondurur. bulamazsa '-1' dondurur

## SETS
x = set((1,4,5))
print(type(x))
a = set("python")
print(a)
# add() -- kumeye eleman ekleme methodu
# difference() == birinci kumenin ikinci kumeden farkini doner 
kume1= {1,3,4,5,6,7}
kume2={3,5,7,8,9,0,88,11,1}
print(kume1.difference(kume2))
print(kume2.difference(kume1))
# difference_update() == birinci kumenin ikinciden farkini donerek birinci kumeyi updateler
kume1.difference_update(kume2)
print(kume1)
# discard() == kumeden eleman cikarmak icin kullanilir
# intersection() == kumelerin ortak elemanlarini bulmamizi saglar
# intersection_update() == kumelerin kesisimlerinin update i
# isdisjoint() == kumeler ayrik kume ise True degeri ortak elemani varsa false dondurur
# issubset() == alt kumesi ise true degilse false dondurur.
# union() == iki kumenin birlesim kumesini doner
# update() ==  kumeyi gunceller


## LISTE METHODLARI
# append() = ekleme
# extend() = bir listeye baska bir listenin elemanlarini eklememizi saglar
# insert() = listenin belirli indexine eleman eklememizi saglar
# pop() = deger vermezsek listenin son elemanini silip ekrana basar , index verirsek verdigimiz index i silip ekrana basar
# remove() = verdigimiz degeri listeden cikarmamizi saglat(! index degil)
# index"() = verilen degerin bastan baslayarak buldugu ilk indexi soyler, baslamasini istedigimiz index degerinden baslatabiliriz

liste = [1,2,3,4,3,3,5,6,7,8,9]
liste.index(3) # 3 elemanı baştan başlayarak 2.indekste
liste.index(3,3) # 3 elemanı 3.indekten itibaren arandığından 4.indekste
# liste icinde olmayan degeri verdigimizde hata dondurur.
# count() = verilen bir degerin listede kac defa gectigini soyler
# sort() = listenin elemanlarını sayıysa küçükten büyüğe , string ise alfabetik olarak sıralar. 
# Eğer özellikle içine reverse = True değeri verilirse elemanları büyükten küçüğe sıralar.

liste.sort(reverse = True)

# ODEV -1 
# x = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
# kume = dict()
# for i in x:
#     if i in kume:
#         kume[i] +=1
#     else:
#         kume[i] = 1
# for i,j in kume.items():
#     print(i,j)
# ODEV -2
# a=''

# with open('siir.txt','r',encoding='utf-8') as file:
#     for i in file:
#         a+=i[0]   
# print(a)

#ODEV 3 
# with open('siir.txt','r',encoding='utf-8') as file:
#     for i in file:
#         i = i[:-1]
#         if(i.endswith('.com') and i.find('@') !=-1):
#             print(i)
# odev 4
# isim = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
# soyisim = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]
# liste = list(zip(isim,soyisim))
# liste.sort()
# for i,j in liste:
#     print(i,j)

## SQLITE VERITABANI

## FUNCTIONS --- DECORATORS
#*args
def func(*args): # func fonksiyonunun icine istedigimiz kadar deger gonderebiliriz
    for i in args:
        print(i)
def func2(isim,*args):    # isim degiskeni isim ile eslesti args devam etti
    print("isim",isim)
    print('======================')
    for i in args:
        print(i)
func2('berk',1,2,3,4,5,6,6,7)
#**kwargs ---- argumanlardan sozluk olusturur.
def func3(**kwargs):
    print(kwargs)
func3(isim='berk',soyisim='ekincioglu',yas=19)
# args ve kwargs beraber kullanimi
def func4(*args,**kwargs):
    for i in args:
        print(i)
    print('-------------')
    for i,j in kwargs.items():
        print(i,j)
func4('a','b','c','d',isim='berk',soyisim='ekincioglu',yas=19)
func4(1,2,3,4,5,6,7,8,9,0,isim='berk',soyisim='ekincioglu',yas=19)
# del x =================> x objesini silmek icin kullanilir.
# ic ice fonksiyonlar
def func5(*args):
    def func6(args):
        toplam =0
        for i in args:
            toplam+=i
        return toplam
    print(func6(args))
func5(1,2,3,4,5,6,7,8,9,0)
## FONKSIYONLARI DONMEK ve PARAMETRE OLARAK GONDERMEK

def fonksiyon(işlem_adı):
    
    def toplama(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
        
    def çarpma(*args):
        çarpım = 1
        for i in args:
            çarpım *= i
        return çarpım
    
    if işlem_adı == "toplama":
        return toplama
    else:
        return çarpma
deneme = fonksiyon('toplama')
print(deneme(1,2,3,4,5))
## Fonksiyonu arguman olarak gondermek
def toplama(a,b):
    return a + b
def çıkarma(a,b):
    return a-b
def çarpma(a,b):
    return a * b
def bölme(a,b):
    return a / b

    
def anafonksiyon(func1,func2,func3,func4,işlem_adı): # Tanımladığımız 4 fonksiyonu da argüman olarak göndereceğiz.
    if (işlem_adı == "toplama"):
        print(func1(3,4))
    elif (işlem_adı == "çıkarma"):
        print(func2(10,3))
    elif (işlem_adı == "çarpma"):
        print(func3(10,3))
    elif (işlem_adı == "bölme"):
        print(func4(10,4))
    else:
        print("Geçersiz işlem adı...")
anafonksiyon(toplama,çıkarma,çarpma,bölme,'toplama')
## DECORATORS
import time
# def kare_al(sayilar):
#     sonuc = []
#     baslama = time.time()
#     for i in sayilar:
#         sonuc.append(i**2)
#     print(sonuc)
#     bitis = time.time()
#     print('Sure: ',bitis-baslama)
# kare_al(range(1000))
# def kup_al(sayilar):
#     sonuc =[]
#     baslama=time.time()
#     for i in sayilar:
#         sonuc.append(i**3)
#     bitis=time.time()
#     print(sonuc)
#     print('sure= ',bitis-baslama)    
# kup_al(range(10000))

##########DECORATOR ile yapimi

# import time
# def zaman_hesapla(fonksiyon):
#     def wrapper(sayılar):
        
        
#         baslama = time.time()
#         sonuç =  fonksiyon(sayılar)
#         bitis =  time.time()
#         print(fonksiyon.__name__ + " " + str(bitis-baslama) + " saniye sürdü.")
#         return sonuç
#     return wrapper
    
# @zaman_hesapla
# def kareleri_hesapla(sayılar):
#     sonuç = []
#     for i in sayılar:
#         sonuç.append(i ** 2)
#     return sonuç
# @zaman_hesapla
# def küpleri_hesapla(sayılar):
#     sonuç = []
#     for i in sayılar:
#         sonuç.append(i ** 3)
#     return sonuç
    

# kareleri_hesapla(range(100000))

# küpleri_hesapla(range(100000))
# ##################################################
# '''
# Decorator kodlama egzersizi 
# '''
# def ekstra(func):
#     def wrapper(sayilar):
#         ciftler_toplam=0
#         cift_sayi=0
#         tekler_toplami=0
#         tek_sayi=0
#         for i in sayilar:
#             if(i%2==0):
#                 ciftler_toplam+=i
#                 cift_sayi+=1
#             else:
#                 tekler_toplami+=i
#                 tek_sayi+=1
#         print('Tek sayilar ort: ',tekler_toplami )
#         print('Cift sayilar ort: ',ciftler_toplam)
#         func(sayilar)
#     return wrapper
# @ekstra
# def ortalama_al(sayilar):
#     toplam=0
#     for i in sayilar:
#         toplam+=i
#     print(toplam/len(sayilar))
# ortalama_al(range(1,100))
################################################################### ASAL MI DEGIL MI ##############################################################################
# def asal_mi(sayi):
#     i=2
#     if(sayi==0):
#         print('asal degildir')
#     elif(sayi==1):
#         print('asal degildir')
#     elif(sayi==2):
#         print('asal sayidir.')
#     else:
#         while(i<sayi):
#             if(sayi%i==0):
#                return True      
#             else:
#                 i+=1
#         return False
                
# print("cikmak icin 'q' ya bas")            
# while True:
#     try:
#         a = input('sayi giriniz.')
#         if(a=='q'):
#             break
#         elif(asal_mi(int(a))==True):
#             print('asal degildir.')
#         else:
#             print('asaldir')
#     except:
#         print('hatali islem')

#### ITERATORS
# liste = [1,2,3,4,5]
# iterator= iter(liste)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# for i in liste:          ######## FOR DONGUSU
#     print(i)

# iterator= iter(liste)
# while True:
#     try:                        ######## FOR DONGUSU
#         print(next(iterator))
#     except StopIteration:
#         break
# class Kumanda():
#     def __init__(self,kanal_listesi):
#         self.kanal_listesi=kanal_listesi
#         self.index=-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.index+=1
#         if (self.index < len(self.kanal_listesi)):
#             return self.kanal_listesi[self.index]
#         else:
#             self.index=-1
#             raise StopIteration

# kumanda = Kumanda(['x','y','z','d'])
# iterator = iter(kumanda)
# print(next(iterator))  
# for i in kumanda:
#     print(i)
###### GENERATOR ##########
## ram i isgal etmek yerine iterator kullanarak istedigimiz elemana ulasmamizi saglar.
# def kare_al():
#     sonuc=[]
#     for i in range(1,6):
#         sonuc.append(i**2)
#         print(sonuc)
# def generator_kare():
#     for i in range(1,5):
#         yield i**2
# generator = generator_kare()
# iterator= iter(generator)
# print(next(iterator))
# print(next(iterator))
# liste = [i*3 for i in range(5)]
# print(liste)
# # generator olusturmak icin () kullaniriz.
# generator_liste = (i*3 for i in range(5))    
# print(generator_liste)
# def carpim_tablosu():
#     for i in range(1,100):                 # Generatorlari listede saklamak yerine saklamadan ekrana bastirdik.
#         for j in range(1,100):
#             yield "{}x{}={}".format(i,j,i*j)
# for i in carpim_tablosu():
    #print(i)

## ITERABLE GENERATOR ILE FIBONACCI    
def fibonacci():
    a=1
    b=1
    yield a
    yield b
    while True:
        a,b=b,a+b
        yield b
for i in fibonacci():
    if ( i>1000000000000):
        break
    print(i)

class Kuvvet3():
    def __init__(self,max=0):
        self.max=max
        self.kuvvet=0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.kuvvet<=self.max):
            sonuc = 3**self.kuvvet
            self.kuvvet+=1
            return sonuc
        else:
            self.kuvvet=0
            raise StopIteration
kuvvet=Kuvvet3(90)
for i in kuvvet:
    print(i)
class Kareler():
    def __init__(self,maksimum=0):
        self.maksimum=maksimum
        self.sayi=1
    def __iter__(self):
        return self
    def __next__(self):
        if(self.sayi<=self.maksimum):
            sonuc=self.sayi**2
            self.sayi+=1
            return sonuc
        else:
            self.sayi=1
            raise StopIteration
kareler = Kareler(5)
for i in kareler:
    print(i)
######### ILERI SEVIYE MODULLER
##########DATE TIME MODUL###################
from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL,'') ####### KONUMA GORE BILGI VERIR
print(datetime.now())
x=datetime.now()
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(datetime.ctime(x)) ## ctime
# strftime()
print(datetime.strftime(x,'%Y'))  ## yil--'%Y' ,, ay--'%B' ,, gun_ismi--'%A' ,,saat--'%X' ,, gun--'%D'
print(datetime.strftime(x,'%A %B'))
## timestamp() --- fromtimestamp()
saniye = datetime.timestamp(x)
print(saniye)
x2=datetime.fromtimestamp(saniye)
print(x2)
print(datetime.fromtimestamp(0))
## BELLI IKI TARIH ARASI FARK BULMAK
tarih= datetime(2020,1,15)
x=datetime.now()
print(tarih-x)
## OS MODULU-- isletim sisteminde islemler gerceklestirebilmemizi saglar
import os
'''
#print(os.getcwd()) # getcwd konumu ogrenmemizi saglar
#os.chdir('C:/Users/user/Desktop') ---- chdir konumu degistirmemizi saglar.
#print(os.listdir()) # bulundugu klasordeki dosyalari listeler
#os.mkdir("Test/Test2") # mkdir bulundugumuz klasorde dosya olusturmamizi saglar.
#os.makedirs("Deneme/Deneme2") # makedirs dosya var olmasa bile olusturmamizi saglar
#os.rmdir("Deneme/Deneme2")   # dosyayi siler.
#os.removedirs("Deneme/Deneme2")   # dosyalarin hepsini siler 
#os.rename    # degistirilmek istenen dosya adi ve yeni adi verilir.
#os.stat()   # girilen dosyanin statulerini ogrenmemizi saglar.
'''
### sys modulu
import sys
print(dir(sys))
# sys.exit()
sys.stderr.write('hata') # cikti olusturur
sys.stderr.flush()  # aninda yazmayi saglar
sys.stdout.write('normal') # cikti olusturur
print('\n')
print(sys.argv) # dosyamizin konumunu yazdirir.

# def kok_bulma(a,b,c):
#     delta =b**2 - 4*a*c
#     if(delta<0):
#         return False
#     else:
#         x1=-b-delta**0.5
#         x2==b+delta**0.5
#         return(x1,x2)
# if (len(sys.argv)==4):
#     print('kok bulma',kok_bulma(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
# else:
#     sys.stderr.write('hata')
#     sys.stderr.flush()
''' NUMPY , PANDAS'''
import numpy as np
import pandas as pd
dictionary={'Name':['ali','veli','ayse','fatma'],
            'Yas':[10,20,30,40],
            'maas':[100,200,300,5000] }
dataFrame1=pd.DataFrame(dictionary)
print(dataFrame1)
