import re
import logging
from ..locators.book_locators import BookLocators


logger = logging.getLogger('scraping.book_parser')


class BookParser:
    """
    A class to take in an HTML page (or part of it), and find properties of an item in it.
    """

    RATINGS = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created...')
        self.parent = parent

    def __repr__(self):
        return f'<Book {self.name}, £{self.price} ({self.rating} stars)>'

    def attr(self, locator, attr):
        item_link = self.parent.select_one(locator)
        item_value = item_link.attrs[attr]
        return item_value

    @property
    def name(self):
        return self.attr(BookLocators.NAME_LOCATOR, 'title')

    @property
    def link(self):
        return self.attr(BookLocators.LINK_LOCATOR, 'href')

    @property
    def price(self):
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string
        matches = re.search('\£([0-9]+\.[0-9]+)', item_price)
        price = float(matches.group(1))
        logger.debug(f'Found book price, `{price}`.')
        return price

    @property
    def rating(self):
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']    # ['star-rating', 'Three']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])   # None if not found
        return rating_number
