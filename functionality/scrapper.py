from bs4 import BeautifulSoup
from urllib import request


URL = "https://myfin.by/crypto-rates"
html = request.urlopen(URL).read()
soup = BeautifulSoup(html, "html.parser")


if __name__ == '__main__':
    btc = soup.findAll('tr', {'class': 'odd'})