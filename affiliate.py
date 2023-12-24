import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.affpaying.com/affiliate-networks/dating"

r = requests.get(url, verify=False)
print(r.status_code)

soup = BeautifulSoup(r.text, "lxml")
title = soup.title

print(title.text)


network_name = soup.find_all("a", class_="text-blue-dark no-underline hover:text-orange")
network_list = []
for i in network_name:
    name = i.text
    network_list.append(name)
print(network_list)