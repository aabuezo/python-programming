# https://regexr.com/
import re


email = 'ale.bue@mail.com'
expression = '[a-z\.]+@[a-z\.]+'

matches = re.findall(expression, email)
print(matches)


price = 'Price: $18,950.50'
expression = 'Price: \$([0-9,]*\.[0-9]*)'    # match and extract

matches = re.search(expression, price)
print(matches.group(0))
print(matches.group(1))

price_without_comma = matches.group(1).replace(',', '')
price = float(price_without_comma)
print(price)
