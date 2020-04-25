from selenium import webdriver

dirverPath = '/home/kyungho/Public/chromedriver_linux64'
#print(_chromeDriverLocation + '/chromedriver')
driver = webdriver.Chrome(dirverPath + '/chromedriver')
driver.get('https://www.google.com')
assert "Google" in driver.title
#driver.get('https://www.naver.com')
elem = driver.find_element_by_name('q')
elem.clear()
elem.send_keys("대성에너지")
elem.submit()
assert "No results found" not in driver.page_source
driver.close()



