import re
import requests
from bs4 import BeautifulSoup


ITEM_HTML = requests.get('https://books.toscrape.com/').text
# ITEM_HTML = requests.get('https://books.toscrape.com/').content   # b'...'
# print(ITEM_HTML)


class ParsedItemLocators:
    """
    Locators for an item in the HTML page

    This allows us to easily see what our code will be looking at
    as well as chang it quickly if we notice it is now different.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParsedItem:
    """
    A class to take in an HTML page (or part of it), and find properties of an item in it.
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def attr(self, locator, attr):
        item_link = self.soup.select_one(locator)
        item_value = item_link.attrs[attr]
        return item_value

    @property
    def name(self):
        return self.attr(ParsedItemLocators.NAME_LOCATOR, 'title')

    @property
    def link(self):
        return self.attr(ParsedItemLocators.LINK_LOCATOR, 'href')

    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string
        matches = re.search('\£([0-9]*\.[0-9]*)', item_price)
        price = matches.group(1)
        return float(price)

    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']    # ['star-rating', 'Three']
        rating_classes = [r for r in classes if r != 'star-rating']
        return rating_classes[0]


if __name__ == '__main__':
    item = ParsedItem(ITEM_HTML)
    print(item.name)
    print(item.link)
    print(item.price)
    print(item.rating)
