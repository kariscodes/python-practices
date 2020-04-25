import sys
from bs4 import BeautifulSoup
import requests
from urllib.parse import quote
import os

URL_with_page_num = 'https://www.google.com/search?q=GSOMIA&newwindow=1&tbas=0&source=lnms&tbm=nws&sa=X&start=0'
source_code_from_URL = requests.get(URL_with_page_num)
#source_code_from_URL = urllib.request.urlopen(URL_with_page_num)
plain_text = source_code_from_URL.text
print(plain_text)