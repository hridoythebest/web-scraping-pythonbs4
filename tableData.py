import requests
from bs4 import BeautifulSoup
import pandas as pd

# url = "https://www.oneindia.com/covid-19-vaccine-tracker.html"
# with requests.Session() as session:
#     session.headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
#     }
#     r = session.get(url)
#     print(r)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
url = "https://www.oneindia.com/covid-19-vaccine-tracker.html"
r = requests.get(url, headers=headers)
print(r)

soup = BeautifulSoup(r.text, "lxml")
table = soup.find_all("table", class_="vaccine_dose_tbl")
# print(table)

titles = soup.find_all("th")
# print(titles)

table_header = []
for i in titles:
    name = i.text
    table_header.append(name)
# print(table_header)


df = pd.DataFrame(columns = table_header)
# print(df)

rows = soup.find_all("tr")

for i in rows[1:]:
    data = i.find_all("td")
    row = [tr.text for tr in data]
    l = len(df)
    df.loc[l] = row
    
print(df)

df.to_csv("covid_19_tracker.csv")

