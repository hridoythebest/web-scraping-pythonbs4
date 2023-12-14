import requests
import re
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r= requests.get(url)
print(r)

soup = BeautifulSoup(r.text, "lxml")
# print(soup)

# print(soup.find_all(["p", "h4", "a"]))
# print(soup.find_all(id = True))
# print(soup.find_all(string=["Galaxy Note", "Lenovo IdeaTab"]))
# print(soup.find_all(string=re.compile("App")))
# print(soup.find_all(class_ = re.compile("desc")))
print(soup.find_all("h4", class_=re.compile("pull"), limit=2))