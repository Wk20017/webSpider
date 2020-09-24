from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq
from urllib.parse import quote
import pymongo
from selenium.webdriver.chrome.options import Options


# cookies = {
#     'cna': 'Epy+F5a1YGkCAd9bV4EWXUfv',
#     't': '56e35ae44a86e439060afec658976ae2',
#     'sgcookie': 'Esy3IkuJYrvWM6n0gKJGd',
#     'uc3': 'F8dCufbE7i82z86qwbc%3D&nk2=pytyU4HMLxNxwA%3D%3D&id2=UU20t7KCQCR9OA%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D',
#     'vt3': 'F8dCufbE7i82z86qwbc%3D&nk2=pytyU4HMLxNxwA%3D%3D&id2=UU20t7KCQCR9OA%3D%3D&lg2=Vq8l%2BKCLz3%2F65A%3D%3D',
#     'lgc': '%5Cu4F60%5Cu771F%5Cu662F%5Cu7B28%5Cu5440',
#     'uc4': '0%40U2%2Fz8oIjgcKBsY%2BK7JrR2TcB97rB&nk4=0%40pR0ogTRaNJeBqR%2FkRWTTb%2F%2FzeDhG',
#     'id4': '0%40U2%2Fz8oIjgcKBsY%2BK7JrR2TcB97rB&nk4=0%40pR0ogTRaNJeBqR%2FkRWTTb%2F%2FzeDhG',
#     'tracknick': '%5Cu4F60%5Cu771F%5Cu662F%5Cu7B28%5Cu5440',
#     '_cc_': 'VFC%2FuZ9ajQ%3D%3D',
#     'thw': 'cn',
#     'enc': '7Gkuzok6gICjZSoUD%2F8YmU17QxtB5AUxDIIQlBzqOo%2FTJDUkb3BzAT8abes20qD25QWZQSNhaDWtEq0mbbxKwA%3D%3D',
#     'hng': 'CN%7Czh-CN%7CCNY%7C156',
#     'mt': '-1_0',
#     'ci': '-1_0',
#     'xlly_s': '1',
#     '_m_h5_tk': '7c1e31181b4572788f290b125487e432_1600872289447',
#     '_m_h5_tk_enc': '836e155091055799f1ca6c11cf41f7c4',
#     'miid': '925633832067289281',
#     'tk_trace': 'oTRxOWSBNwn9dPyorMJE%2FoPdY8zfvmw%2Fq5v3gzWJ8XDVwd0wAG5RSHsDBK%2FvbPvMZ18L8%2FMzwen3A55iTG8qJ%2B%2FjtYR%2FT6CdJKnSXRqjjw7PwzrFtETRophvJaA4aCNqmh3n3vmjFTqHsqaKgJLJJQ4GQ9RAXzWlFDe0Ze30tvK2GrEVDWYuKCpMWVvj0Zt%2BunYdVPSvsoopLprIvZyuZ9xdDo4srwRLWSZAvs0IwvYBwBRApOz%2FVza%2FPcQswe3ww9CPZjMCxP3%2B8TxTmNRcS2TBXUlK',
#     'lLtC1_': '1',
#     'samesite_flag_': 'true',
#     'cookie2': '19d9929845c8cf934c4e312eabe8ad4f',
#     '_tb_token_': '76e98f5bfe5e',
#     'uc1': 'Uoe0bUHy4prp8g%3D%3D',
#     'cookie14': 'Uoe0bUHy4prp8g%3D%3D',
#     'tfstk': 'cBCFBn0OlWFexcO7HBOrN-VYDfRdauAkMc8WKTcj_nAzX79H0sjj2F4s2dJXD5vh.',
#     'l': 'eBaFM3EIOhv8Z5lQBO5CPurza77OuIRb4FVzaNbMiInca6EP9FgbCNQ4vDwyWdtjgtCF_eKyNxVOSRLHR3AiVh9N3QeusLPr3xvO.',
#     'isg': 'BDc32_98JGKU26DVHRoNyxL2xiuB_AteXQaoSonkx4ZtOFd6kMw_rvcSGphm5ePW'
# }

'''
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(options=chrome_options)
'''


browser = webdriver.Chrome()
# browser.add_cookie(cookies)
wait = WebDriverWait(browser, 10)
KEYWORD = 'iPad'

Mongo_url = 'localhost'
Mongo_db = 'taobao'
Mongo_collection = 'products'
client = pymongo.MongoClient(Mongo_url)
db = client[Mongo_db]



def save_tomogo(product):
    try:
        if db[Mongo_collection].insert(product):
            print('success!')
    except Exception:
        print('failed!')



def get_products():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save_tomogo(product)


def index_page(page):
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
        )
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item'))
        )
        get_products()
    except TimeoutException:
        index_page(page)


def main():
    for i in range(1, 3):
        index_page(i)


if __name__ == '__main__':
    main()

