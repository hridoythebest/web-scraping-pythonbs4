import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
r=requests.get(url)
print(r.status_code)

soup=BeautifulSoup(r.content, "lxml")


Quotes_list= soup.find_all("span", class_="text")

Q_list =[]
for i in Quotes_list:
    quote = i.text
    Q_list.append(quote)

Quotes_list= soup.find_all("span", class_="text")
Q_list =[]
for i in Quotes_list:
    quote = i.text
    Q_list.append(quote)

Author_list= soup.find_all("small", class_="author")
A_list =[]
for j in Quotes_list:
    author = j.text
    A_list.append(author)
Tag_list= soup.find_all("meta", class_="keywords")
T_list =[]
for k in Quotes_list:
    tag = k.text
    T_list.append(tag)

df=pd.DataFrame({"Quotes": Q_list, "Author":A_list, "Tags": T_list})
df.to_csv("quotes.txt")