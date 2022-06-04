import re
import requests
from bs4 import BeautifulSoup


ITEM_HTML = requests.get('http://books.toscrape.com/').text
soup = BeautifulSoup(ITEM_HTML, 'html.parser')


def find_item_attr(locator, attr):
    item_link = soup.select_one(locator)
    item_value = item_link.attrs[attr]
    return item_value


def find_item_price():
    locator = 'article.product_pod p.price_color'
    item_price = soup.select_one(locator).string
    matches = re.search('\£([0-9]*\.[0-9]*)', item_price)
    price = matches.group(1)
    return float(price)


product1_title = ('article.product_pod h3 a', 'title')
product1_link  = ('article.product_pod h3 a', 'href')
product1_price = find_item_price()
print(find_item_attr(*product1_title))
print(find_item_attr(*product1_link))
print(product1_price * 0.8)
