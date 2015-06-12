from lxml import html
from glob import glob

def definitions_from_html(text):
    page = html.fromstring(text)
    return [html.tostring(el) for el in page.xpath('//p/b/parent::*')]

def extract(str):
    el = html.fromstring(str)
    try:
        word = el.xpath('//b/text()')[0]
        return dict(word=word, html=str)
    except:
        print str

def open_html(file):
    return open(file).read()

def parse():
    for file in glob("data/*.htm"):
        print [extract(w) for w in definitions_from_html(open_html(file))]
