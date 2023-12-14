import requests
from bs4 import BeautifulSoup

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text,"lxml")
# print(soup)
# print(soup.find("header"))
# print(soup.find("H4"))
print(soup.find("h4",{"class":"pull-right price"}))
print (soup.find("p", {"class":"description"}))
print (soup.find("p", class_="description"))