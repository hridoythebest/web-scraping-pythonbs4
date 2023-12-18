import requests
from bs4 import BeautifulSoup
import pandas as pd
import random

url="https://www.glassdoor.com/Job/south-africa-django-jobs-SRCH_IL.0,12_IN211_KO13,19.htm"

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    # Add more recent user agents here
]
user_agent = random.choice(user_agents)
headers={"User-Agent": user_agent}
r=requests.get(url, headers=headers)
print(r.status_code)