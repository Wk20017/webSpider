from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://www.baidu.com')
print(driver.current_url+'\n'+driver.title+'\n'+driver.page_source)
