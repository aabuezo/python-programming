from bs4 import BeautifulSoup

SIMPLE_HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Web Scraping</title>
</head>
<body>
    <h1>This is a title</h1>
    <p class="subtitle">Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem, quaerat!</p>
    <p>Here's another p without a class</p>
    <ul>
        <li>Rolf</li>
        <li>Charlie</li>
        <li>Jen</li>
        <li>Jose</li>
    </ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')
    return h1_tag.string


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_contents = [item.string for item in list_items]
    return list_contents


def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    return paragraph.string


def find_other_paragraph():
    paragraphs = simple_soup.find_all('p')
    other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]  # as in p.attr['class]
    return other_paragraph[0].string


print(find_title())
print(find_list_items())
print(find_subtitle())
print(find_other_paragraph())
