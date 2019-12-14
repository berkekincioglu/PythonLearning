import requests
from bs4 import BeautifulSoup
url='https://www.imdb.com/chart/top/?ref_=nv_mv_250'
response = requests.get(url)
print(response)
html=response.content
soup=BeautifulSoup(html,'html.parser')
basliklar=soup.find_all('td',{'class':'titleColumn'})
ratingler=soup.find_all('td',{'class':'ratingColumn imdbRating'})
rating_x=float(input('Rating girin'))
for baslik,rating in zip(basliklar,ratingler):
    baslik=baslik.text
    rating=rating.text
    if(float(rating)==rating_x):
        print('Baslik:',baslik)
        print('Rating',rating)
        print('-----------------------------------------')