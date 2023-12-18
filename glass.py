import requests
from bs4 import BeautifulSoup

# Define URL and element selector
url = "https://books.toscrape.com/catalogue/category_books.html"
element_selector = "article.product_pod"

# Send request and get response
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all book listings
books = soup.findAll(element_selector)

# Extract and print book information
for book in books:
    title = book.find("h3", class_="product_name").a.text.strip()
    price = book.find("span", class_="price_color").text.strip()
    description = book.find("p", class_="product_description").text.strip()
    link = book.find("a", href=True)["href"]

    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Description: {description}")
    print(f"Link: {link}")
    print("---")

