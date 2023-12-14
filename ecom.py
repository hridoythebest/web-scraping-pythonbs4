import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone"

r = requests.get(url)
# print(r.status_code)
soup = BeautifulSoup(r.text, "lxml")
# print(soup)
# print(soup.header)
# print(soup.div)
# tag = soup.header.p
# print(tag.string)
# tag1 = soup.header.p.string
# print(tag1)

tag = soup.header
print(tag.attrs)
print(tag["role"])
print(tag['class'])
tag["add_attribute"]="this is my new attribute"
print(tag.attrs)
print(tag)