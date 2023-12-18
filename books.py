import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://books.toscrape.com/"
r=requests.get(url)
print(r.status_code )

soup =BeautifulSoup(r.content, "lxml")

Product_title = soup.find_all("a")
B_list = []
for k in Product_title:
    book=k.text
    B_list.append(book)


Product_price = soup.find_all("p", class_="price_color")
P_list =[]
for i in Product_price:
    price = i.text
    P_list.append(price)
    
Product_status = soup.find_all("p", class_="instock availability")
S_list =[]
for j in Product_status:
    status = j.text
    S_list.append(status)
    
df = pd.DataFrame({"Product": B_list, "Price": P_list, "Status": S_list})
pd.to_csv("books.txt")



