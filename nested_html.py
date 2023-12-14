import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
print(r)
soup = BeautifulSoup(r.text, "lxml")

# boxes = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
# print(len(boxes))
boxes = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")[3]
a = boxes.find("h4").text
print(a)

