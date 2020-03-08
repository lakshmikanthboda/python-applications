import requests
from bs4 import BeautifulSoup
data = requests.get("https://www.flipkart.com/search?q=mobiles&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_1_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_1_0_na_na_na&as-pos=1&as-type=TRENDING&suggestionId=mobiles&requestId=f833177f-b96a-4f81-b0ee-5fa4685d5d75")
soup = BeautifulSoup(data.content,'html.parser')
box = soup.find_all("div", {"class": "_1UoZlX"})
for data1 in box:
    name = data1.find("div", {"class": "_3wU53n"})
    price = data1.find("div", {"class": "_1vC4OE _2rQ-NK"})
    rating = data1.find("div", {"class": "hGSR34"})
    print (name.text,price.text[1:],rating.text)
