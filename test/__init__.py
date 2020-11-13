import json
import urllib.parse
import string

import xlrd
import requests
import re
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#
# headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
#         'Chrome/52.0.2743.116 Safari/537.6'
# }

import openpyxl as op

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


results = []

def write():
    bg = op.load_workbook(r"C:\Users\王凯\Desktop\test.xlsx")
    sheet = bg["Sheet1"]
    for i in range(1, len(results) + 1):
        sheet.cell(i, 1, results[i - 1])
    bg.save("test.xlsx")

def get_message(url):
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(url)
    html = browser.page_source
    doc = pq(html)
    a = doc('.body-wrapper .main-content .lemma-summary')
    print(a.text())
    results.append(a.text())
    print('------------------------------------------')
    browser.close()



data = xlrd.open_workbook(r'C:\Users\王凯\Desktop\新表.xlsx') #默认当前路径
# 获取所有的sheet
sheet_name = data.sheet_names()[0]
# 根据sheet索引或者名称获取sheet内容
sheet = data.sheet_by_index(0)  # sheet索引从0开始
# print(sheet.cell_value(1, 1))   #获取指定单元格里第2行，第3列的值
# # 获取整行和整列的值（数组）
# #rows = sheet.row_values(0)  # 获取第1行的内容
cols = sheet.col_values(1)  # 获取第2列的内容
# print(len(cols))
# # 第2列(cols对应列)，从第1行开始, 获取至第6行
value = []
# for i in range(1, len(cols)):
for i in range(1, 2):
    value.append(cols[i])



# url = "https://baike.so.com/doc/994131-1050943.html"
# browser = webdriver.Chrome()
# browser.get(url)

# html = browser.page_source
# doc = pq(html)
# a = doc('.main-content .lemmaWgt-lemmaTitle .lemmaWgt-lemmaTitle-title h1')
# print(a.text())
# browser.close()
# get_url = "https://baike.sogou.com/.*"


for i in value:
    #1
    # print(type(i))
    # wait1 = WebDriverWait(browser, 50)
    # wait1.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
    # my_input = browser.find_element_by_id('J-search-word')
    # my_input.clear()
    # my_input.send_keys(i)
    # my_input.send_keys(Keys.ENTER)
    # wait2 = WebDriverWait(browser, 50)
    # wait2.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
    # html = browser.page_source
    # print(html)
    # doc = pq(html)
    # a = doc('#main .entry-box wrap .uni-card .uni-card-bd')
    # print(a.text())
    # print('-------------------------------------------------------------------')

    # #2
    url = "https://baike.baidu.com/item/" + i
    new_url = urllib.parse.quote(url, safe=string.printable)
    get_message(new_url)

write()



