import requests
from bs4 import BeautifulSoup

url = 'http://blog.jusun.org/'
source = requests.get(url)
plain_text = source.text

soup = BeautifulSoup(plain_text, 'html.parser')
for link in soup.select('h2 > a'):
    href = link.get('href')
    print(href)