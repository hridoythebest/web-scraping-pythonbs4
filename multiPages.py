import requests
from bs4 import BeautifulSoup
import pandas as pd
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
titles = []
price = []
description = []

for i in range(2, 10):
    url = f"https://www.flipkart.com/mobiles/smartphones~type/pr?sid=tyy%2C4io&page="+str(1)
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.text, "lxml")

    names = soup.find_all("div", {"class_":"_4rR01T"})
    print(names)
    for j in names:
        n = i.text
        titles.append(n)
    print(titles)
   
    price_list = soup.find_all("div", {"class":"_30jeq3 _1_WHN1"})
    for k in price_list:
       p=k.text
       price.append(p)
    print(price)
    
    description_list = soup.find_all("ul", {"class":"_1xgFaf"})
    for l in description_list:
       d=i.text
       description.append(d)
    print(description)
 
    df = pd.DataFrame({"Titles":titles, "Price":price, "Description": description})
    print(df)