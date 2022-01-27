import requests
from bs4 import BeautifulSoup

response =requests.get("https://www.imdb.com/chart/top/")

html_icerigi = response.content

secim = float(input("Lutfen izlemek istediginiz minumum rating'i yaziniz: "))
soup = BeautifulSoup(html_icerigi,"html.parser")
baslıklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})
for baslık,rating in zip(baslıklar,ratingler):
    baslık = baslık.text
    rating = rating.text
    baslık = baslık.strip()
    baslık = baslık.replace("\n","")
    rating = rating.strip()
    rating = rating.replace("\n","")
    if(float(rating) >= secim):
        print("Film İsmi: ",baslık,"Rating: ",rating)


