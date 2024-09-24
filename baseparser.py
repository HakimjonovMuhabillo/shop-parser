from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
}


class Baseparser:
    def __init__(self):
        self.url = 'https://texnomart.uz/ru/promotions/'
        self.host = 'https://texnomart.uz'

    def get_html(self, url=None):
        if url:
            return requests.get(url, headers=headers).text
        else:
            return requests.get(self.url, headers=headers).text

    def get_soup(self, html):
        return BeautifulSoup(html, 'html.parser')
