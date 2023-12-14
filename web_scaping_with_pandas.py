import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
print("<================================================================================>")
print(r)

soup = BeautifulSoup(r.text, 'lxml')
# print(soup)
Product_name = soup.find_all("a", class_ = "title")
# print(Product_name)

P_list = []

for i in Product_name:
    name = i.text
    P_list.append(name)
print(P_list)

Product_price = soup.find_all("h4", class_="float-end price card-title pull-right")

Price_list = []
for j in Product_price:
    price = j.text
    Price_list.append(price)
print(Price_list)

Description_list = soup.find_all("p", class_="description card-text")
# print(Description_list)
D_list = []
for m in Description_list:
    desc = m.text
    D_list.append(desc)
print(D_list)


Reviews_list = soup.find_all("p", class_="float-end review-count")

reviews = []
for l in Reviews_list:
    review = l.text
    reviews.append(review)
print(reviews)
    
df = pd.DataFrame({"Product Name" : P_list, "Price" : Price_list, "Description" : D_list, "Reviews": reviews})
df.to_csv("tablets.csv")