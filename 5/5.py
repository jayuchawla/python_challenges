import pickle
import urllib.request
from bs4 import BeautifulSoup

address = pickle.load(urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p'))
for item in address:
    for i in item:
        print(i[0]*i[1], end='')
    print()