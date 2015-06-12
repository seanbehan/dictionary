from time import sleep
import requests as r
from lxml import html

# http://www.gutenberg.org/ebooks/661 - webster unabridged

# http://www.gutenberg.org/ebooks/37683 - p1
# http://www.gutenberg.org/ebooks/38538 - p2
# http://www.gutenberg.org/ebooks/38699 - p3
# http://www.gutenberg.org/ebooks/38700 - p4

urls = [
'http://www.gutenberg.org/files/37683/37683-h/37683-h.htm',
'http://www.gutenberg.org/files/38538/38538-h/38538-h.htm',
'http://www.gutenberg.org/files/38699/38699-h/38699-h.htm',
'http://www.gutenberg.org/files/38700/38700-h/38700-h.htm'
]

for url in urls:
    page = html.fromstring(r.get(url).text)
    words = [html.tostring(el) for el in page.xpath('//p/b/parent::*')]
    sleep(5)
