import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.mycyberbase.com"
r = requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.content, 'lxml')

Post_title = soup.find_all("h2", class_="post-title")
P_list = []
for i in Post_title:
    title = i.text 
    P_list.append(title)

for title in P_list:
    try:
        print(title.encode('utf-8', errors='replace').decode('utf-8'))
    except UnicodeEncodeError:
        pass 

Post_author = soup.find_all("a", class_="author-name tie-icon")
A_list = []
for j in Post_author:
    author = j.text 
    A_list.append(author)
print(A_list)

Post_time = soup.find_all("span", class_="date meta-item tie-icon")
Time_list = []
for k in Post_time:
    time = k.text 
    Time_list.append(time)
print(Time_list)

Post_desc = soup.find_all("p", class_="post-excerpt")
Desc_list = []
for l in Post_desc:
    desc = l.text 
    Desc_list.append(desc)
    
for desc in Desc_list:
    try:
        print(desc.encode('utf-8', errors='replace').decode('utf-8'))
    except UnicodeEncodeError:
        pass 


Post_viewbtn = soup.find_all("a", class_="more-link button")
view_link_list = []
for m in Post_viewbtn:
     link = m['href'] 
     view_link_list.append(link)

print(view_link_list)

# df = pd.DataFrame({"Post Title" : P_list, "Author" : A_list, "Post Time" : Time_list, "Description" : Desc_list, "Read More" : view_link_list })
# df.to_csv("articles.csv")
