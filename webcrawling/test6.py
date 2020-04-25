from newspaper import Article

#url = 'https://news.v.daum.net/v/20170604205121164'
url = 'http://www.energy-news.co.kr/news/articleView.html?idxno=65091'

content = Article(url, language='ko')
content.download()
content.parse()
print('Title : \n', content.title)
print('Contents : \n', content.text)
#resource = content.get_resource_path()
#print(resource)
