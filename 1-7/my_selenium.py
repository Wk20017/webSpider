import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

'''
1.引入selenium
browser = webdriver.Chrome()
# try:
browser.get('https://www.baidu.com')
input = browser.find_element_by_id('kw')
input.send_keys('Python')
input.send_keys(Keys.ENTER)
wait = WebDriverWait(browser, 10)

print(browser.current_url)
print(browser.get_cookies())
print(browser.page_source)
# finally:
#     browser.close()
2.动作链
browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
source = browser.find_element_by_css_selector('#draggable')
target = browser.find_element_by_css_selector('#droppable')
actions = ActionChains(browser)
actions.drag_and_drop(source, target)
actions.perform()
3.执行JavaScript
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
browser.get('https://zhihu.com/explore')
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
wait = WebDriverWait(browser, 100)
browser.execute_script('alert("To bottom")')
4. 获取节点信息
browser = webdriver.Chrome()
url = 'https://zhihu.com/explore'
browser.get(url)
logo = browser.find_element_by_css_selector('.ZhihuLogoLink')
print(logo)
print(logo.get_attribute('class'))
print(logo.id)
print(logo.location)
print(logo.tag_name)
print(logo.size)
5. 切换frame
from selenium.common.exceptions import NoSuchElementException


browser = webdriver.Chrome()
url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
try:
    logo = browser.find_element_by_class_name('navbar-header logo')
except NoSuchElementException:
    print('No LOGO!')
browser.switch_to.parent_frame()
logo = browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)
6.等待
隐式等待：
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.zhihu.com/explore')
try:
    input = browser.find_element_by_class_name('zu-top-add-question')
    print(input)
except NoSuchElementException:
    print("not find!")
显式等待：
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
wait = WebDriverWait(browser, 10)
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
print(input, button)

7.前进和后退

browser = webdriver.Chrome()
browser.get('http://www.taobao.com')
browser.get('http://www.baidu.com')
browser.get('http://www.zhihu.com')
browser.back()
time.sleep(10)
browser.forward()
browser.close()

8.cookies
browser.get('http://www.zhihu.com')
print(browser.get_cookies())
browser.add_cookie({
    'name': 'Tom',
    'domain': 'www.zhihu.com',
    'value': 'gerney'
})
print('----------------------------')
print(browser.get_cookies())
browser.delete_all_cookies()
print('----------------------------')
print(browser.get_cookies())
browser.close()

9.选项卡管理
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to.window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(2)
browser.switch_to.window(browser.window_handles[0])
browser.get('https://lol.qq.com/main.shtml')
'''
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
