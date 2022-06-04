import requests
import logging

from pages.all_books_page import AllBooksPage


logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.INFO,
                    filename='logs.txt')
logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)
books_list = page.books


for page in range(1, page.page_count + 1):
    url = f'http://books.toscrape.com/catalogue/page-{page}.html'
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    books_list.extend(page.books)
