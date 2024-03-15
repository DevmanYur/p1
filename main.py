import os

import requests
from pathlib import Path
from requests import HTTPError
from pathvalidate import sanitize_filename
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.parse import unquote

def download_genre(url):
    url = 'https://tululu.org/b5'


    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'lxml')
    comm = soup.find('span', class_='d_book').find_all('a')
    for x in comm:
        print(x.text)


if __name__ == '__main__':
    url55 = 'https://tululu.org/b9'

    download_genre(url55)

