#Failed

import sys
import traceback

from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.parse import quote
import os

TARGET_URL_SEARCH = "https://www.google.com/search"
TARGET_URL_BEFORE_KEWORD = '?q='
TARGET_URL_BEFORE_START_NUM = "&start="
TARGET_URL_REST = '&newwindow=1&tbas=0&source=lnms&tbm=nws&sa=X'

HEADER = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

# 기사 검색 페이지에서 기사 제목에 링크된 기사 본문 주소 받아오기
def get_link_from_news_title(page_num, URL, output_file):
    for i in range(page_num):
        current_page_num = i * 10
        URL_with_page_num = URL + TARGET_URL_BEFORE_START_NUM + str(current_page_num)

        try:
           request_URL = urllib.request.Request(URL_with_page_num, headers = HEADER)
           codes_from_request_URL = urllib.request.urlopen(request_URL)
        except:
           traceback.print_exc()
        # print(source_code_from_URL.read())

        soup = BeautifulSoup(codes_from_request_URL, 'lxml', from_encoding='utf-8')
        for title in soup.find_all('h3', 'r'):
            title_link = title.select('a')
            article_URL = title_link[0]['href']
            get_text(article_URL, output_file)

# 기사 본문 내용 긁어오기 (위 함수 내부에서 기사 본문 주소 받아 사용되는 함수)
def get_text(URL, output_file):
    try:
        req_URL = urllib.request.Request(URL, headers=HEADER)
        codes_from_req_URL = urllib.request.urlopen(req_URL)
    except:
        traceback.print_exc()
    soup = BeautifulSoup(codes_from_req_URL, 'lxml', from_encoding='utf-8')
    content_of_article = soup.select('div.article_txt')
    for item in content_of_article:
        string_item = str(item.find_all(text=True))
        output_file.write(string_item)


# 메인함수
def main(argv):
    if len(argv) != 4:
        print("python [모듈이름] [키워드] [가져올 페이지 숫자] [결과 파일명]")
        return
    keyword = argv[1]
    page_num = int(argv[2])
    output_file_name = argv[3]
    target_URL = TARGET_URL_SEARCH \
                 + TARGET_URL_BEFORE_KEWORD + quote(keyword) \
                 + TARGET_URL_REST
    #print(target_URL)
    workingPath = os.getcwd()
    directory = 'WebCrawling'
    resultPath = workingPath + '/' + directory
    #print(resultPath)

    # create folder
    if os.path.exists(resultPath) == False:
        os.mkdir(resultPath)
    output_file = open(resultPath + '/' + output_file_name, 'w')
    # output_file = open(output_file_name, 'w')

    get_link_from_news_title(page_num, target_URL, output_file)

    output_file.close()

input_arg = ['test9.py', 'GSOMIA', 1, 'tt.txt']
main(input_arg)
#if __name__ == '__main__':
#    main(sys.argv)