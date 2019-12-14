import numpy as np
import random
data_list = [1,2,3]
array1=np.array(data_list)
data_list2=[[10,20,30],[40,50,60],[70,80,90]]
array_2=np.array(data_list2)
print(array_2)
print(array_2[0,2])
x=np.arange(10,20)
print(x)
y=np.zeros(10)
print(y)
z=np.ones(10)
print(z)
#np.zeros((3,5))
print(np.linspace(0,100,5))
print(np.eye(6))
print(np.random.randint(0,10))
x= random.randint(0,10)
print(x)
print(np.random.rand(5)) #0 ile 5 arasi random 5 degeri depoladi
print(np.random.randn(5)) # negatif isler

arr=np.arange(25)
print(arr)
print(arr.reshape(5,5))
newArray=np.random.randint(1,100,10)
print(newArray)
print(newArray.max())
print(newArray.reshape(2,5))
print(newArray.mean()) ## ortalama
print(newArray.sum())
print(newArray.argmax()) # en buyuk degerin hangi indexte oldugunu soyler
detArray=np.random.randint(1,100,25)
print(detArray)
detArray=detArray.reshape(5,5)
print(detArray)
print(np.linalg.det(detArray)) # determinat bulmak

detArray2=np.array([[1,2],[3,4]])
print(np.linalg.det(detArray2))
print(round(np.linalg.det(detArray2)))
arr = np.arange(1,10)
#arr[:3]=25
print(arr)
print(arr>3)
booleanArray=arr>3
print(arr[booleanArray])
arr1=np.arange(0,100,10)
arr2=np.arange(0,10)
print(arr1)
print(arr2)
print(arr1+arr2)
print(np.sqrt(arr1)) # numpy da sqrt karekok almayi saglar
# ravel()   arrayi duz hale getirir(vektor haline)
arr1T=arr1.T # arr1.transpose()
print(arr1T)
#arr1.resize() ---> matrix i degistirir.
n=np.hstack((arr1,arr2))
t=np.vstack((arr1,arr2))
print(t)
print(n)
#### convert && copy
liste =[1,2,3,4]
array=np.array([5,6,7,8])
array=np.array(liste)
liste2=list(array)
'''
a=b
c=a
birini degistirince hepsinin degismemesi icin .copy() islemi kullanilir.
'''
import pandas as pd
dictionary={'Name':['ali','veli','ayse','fatma'],
            'Yas':[10,20,30,40],
            'maas':[100,200,300,5000] }
dataFrame1=pd.DataFrame(dictionary)
print(dataFrame1)
head=dataFrame1.head()#dataFrame1 icindeki bastan 5 satiri ver
print(head)
tail=dataFrame1.tail()#dataFrame1 icinde sondaki 5 satiri verir
print(tail)
print(dataFrame1.columns) # sutunlari gosterir
print(dataFrame1.info())
print(dataFrame1.dtypes)
print(dataFrame1.describe()) # numeric feature
#%%
## indexing slicing
print(dataFrame1['Name'])
print(dataFrame1['Yas'])
dataFrame1['yeni_feature']=[-1,-2,-3,-4]
print(dataFrame1.yeni_feature)
print(dataFrame1.loc[:,'Name'])
print(dataFrame1.loc[3:,'Name':'Yas'])
print(dataFrame1.loc[2:,'Name':'maas'])
print(dataFrame1.loc[1:,])
print(dataFrame1.loc[3:,])
print(dataFrame1.loc[::-1,:])
print(dataFrame1.iloc)
#%%
# filtering
filtre1=dataFrame1.maas > 100
filtre2=dataFrame1.Yas > 10
print(filtre1)
filtrelenmis_data=dataFrame1[filtre1]
filtrelenmis_data2=dataFrame1[filtre1 & filtre2]
print(filtrelenmis_data)
print(filtrelenmis_data2)
print(dataFrame1[dataFrame1.Yas>20])

#%% list compre
mean_value=dataFrame1.maas.mean()
print(round(mean_value))
print(dataFrame1.columns) 
dataFrame1.columns=[i.lower() for i in dataFrame1.columns]
print(dataFrame1.columns) 
dataFrame1.columns=[each.split()[0]+''+each.split[1] if len(each.split())>1 else each for each in dataFrame1.columns]
print(dataFrame1.columns) 
# %% drop and concatenating
print(dataFrame1)
#dataFrame1= dataFrame1.drop(['yeni_feature'],axis=1,inplace=True)
#print(dataFrame1)

#vertical
data1=dataFrame1.head()
data2=dataFrame1.tail()
data_concat=pd.concat([data1,data2],axis=0) # 0 verirsek vertical
print(data_concat)
#horizontal
maas=dataFrame1.maas
age=dataFrame1.yas
data_h_concat=pd.concat([maas,age],axis=1) # 1 verirse horizontal
print(data_h_concat)
#%% transforming Data
dataFrame1['list_comp']=  [i*2 for i in dataFrame1.yas]
print(dataFrame1['list_comp'])

def multiply(yas):
    return yas*2
dataFrame1['apply_metodu']=dataFrame1.yas.apply(multiply)
print(dataFrame1['apply_metodu'])
#%% matplotlib











