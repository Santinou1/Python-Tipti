import requests
from bs4 import BeautifulSoup
import pandas as pd

class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch_page(self, url):
        """Fetches a page content."""
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f"Failed to fetch page: {url}")

    def parse_product(self, product):
        """Parses a single product's details."""
        title = product.find('a', class_='title').text.strip()
        description = product.find('p', class_='description').text.strip()
        price = product.find('h4', class_='price').text.strip()
        return {
            'title': title,
            'description': description,
            'price': price
        }

    def scrape(self):
        """Main scraping method."""
        page_content = self.fetch_page(self.base_url)
        soup = BeautifulSoup(page_content, 'html.parser')
        products = soup.find_all('div', class_='thumbnail')
        
        product_data = []
        for product in products:
            product_info = self.parse_product(product)
            product_data.append(product_info)

        return pd.DataFrame(product_data)

base_url = "https://webscraper.io/test-sites/e-commerce/allinone"
scraper = Scraper(base_url)
df = scraper.scrape()
print(df)
df.to_csv("../../data/raw/products.csv", index=False)
