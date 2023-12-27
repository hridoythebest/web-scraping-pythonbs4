import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.airbnb.com/s/New-Delhi--India/homes?property_type_id%5B%5D=1&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&refinement_paths%5B%5D=%2Fhomes"

r=requests.get(url)
print(r)

while True:
    soup = BeautifulSoup(r.text, "lxml")
    np = soup.find("a", {"aria-label": "next"}).get("href")
    cnp="https://www.airbnb.com"+np
    print(cnp)

    url = cnp
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")