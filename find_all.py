import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text,"lxml")
# print(soup)
priceList = (soup.find_all("h4",{"class":"float-end price card-title pull-right"}))

print (priceList[-2:])
# for x in priceList:
#     print("price : "+ x.string)
    
# descriptionList = (soup.find_all("p", {"class":"description card-text"}))

# for i in descriptionList:
#     print("description : " + i.string)