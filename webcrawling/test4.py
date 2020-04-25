import os
import mechanize

factory = mechanize.OpenerFactory()

_browser = mechanize.Browser(factory)
_browser.set_handle_equiv(True)
_browser.set_handle_redirect(True)
_browser.set_handle_referer(True)
_browser.set_handle_robots(False)
_browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
_browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1')]

_browser.open('http://www.google.com/search?hl=en&q='+ 'Korea' +'&lr=lang_en')
response = _browser.response().read()

print(response)

#resultFile = open('WebCrawling/result' + '.txt', 'w')
#resultFile.write(response)
#resultFile.close()