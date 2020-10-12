from bs4 import BeautifulSoup
import requests

def googleSearch(query):
    with requests.session() as c:
        url = 'https://en.wikipedia.org/wiki/'
        s = requests.get(url + query).text
        return s

def search(msg):

	