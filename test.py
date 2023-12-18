import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set the URL of the website
url = "https://webscraper.io/test-sites/e-commerce/static"

# Make a GET request to the website
r = requests.get(url)

# Check for successful response
if r.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(r.content, "lxml")

    # Initialize empty lists for data
    product_names = []
    product_prices = []
    product_descriptions = []

    # Find all product containers using a CSS selector
    products = soup.find_all("div", class_="product-item")

    # Loop through each product container
    for product in products:
        # Extract product name
        name_element = product.find("h3", class_="product-title")
        if name_element:
            product_names.append(name_element.text.strip())
        else:
            product_names.append("N/A")

        # Extract product price
        price_element = product.find("span", class_="price")
        if price_element:
            product_prices.append(price_element.text.strip())
        else:
            product_prices.append("N/A")

        # Extract product description
        description_element = product.find("p", class_="description")
        if description_element:
            product_descriptions.append(description_element.text.strip())
        else:
            product_descriptions.append("N/A")

    # Create a Pandas DataFrame with extracted data
    df = pd.DataFrame({
        "Product Name": product_names,
        "Price": product_prices,
        "Description": product_descriptions,
    })

    # Print the DataFrame
    print(df.to_string())

    # Optionally, save the data to a CSV file
    df.to_csv("products.csv", index=False)

else:
    print(f"Error: Website returned status code {r.status_code}")
