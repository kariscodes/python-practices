import requests
from bs4 import BeautifulSoup

def spider():
    #url = 'http://www.energy-news.co.kr/news/articleView.html?idxno=65091'
    #url = 'https://www.idaegu.co.kr/news/articleView.html?idxno=283960'
    url = 'http://creativeworks.tistory.com/' + str(1)
    #print('url : ' + url)
    source_code = requests.get(url)
    plain_text = source_code.text
    #print(plain_text)
    #soup = BeautifulSoup(plain_text, 'lxml')
    soup = BeautifulSoup(plain_text, 'html.parser')
    #print('soup : ')
    print(soup)
    link = soup.select('h2 > a')
    print(link.string)
    #title = link.
    #print(title)
    #for link in soup.select('h2 > a'):
    #    href = 'http://creativeworks.tistory.com/' + link.get('href')
    #    title = link.string
    #    print(href)
    #    print(title)


spider()
