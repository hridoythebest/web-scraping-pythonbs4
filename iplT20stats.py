import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
url = "https://www.iplt20.com/auction"

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table", class_="ih-td-tab auction-tbl")
title = table.find_all("th")

header = []
for i in title:
    name = i.text
    header.append(name)

df = pd.DataFrame(columns=header)

rows = table.find_all("tr")
for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row = [tr.text for tr in data]
    row.insert(0, first_td)
    l = len(df)
    df.loc[l] = row

# Write the DataFrame to a CSV file
df.to_csv("ipl_auction.csv", index=False)
