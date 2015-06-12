from time import sleep
import requests as r
from lxml import html
from glob import glob


for file in glob("data/*.htm"):
    raw = open(file).read()
    page = html.fromstring(raw)
    words = [html.tostring(el) for el in page.xpath('//p/b/parent::*')]
    print words
