import urllib.parse
import string
import xlrd
from pyquery import PyQuery as pq
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import openpyxl as op

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

prefs = {
    'profile.default_content_setting_values': {
            'images': 2,
            'permissions.default.stylesheet': 2,
            'javascript': 2
        }
}
chrome_options.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome(options=chrome_options)

results = []

j = 0


def write():
    bg = op.load_workbook(r"D:\test.xlsx")
    sheet = bg["Sheet1"]
    for i in range(1, len(results) + 1):
        sheet.cell(i, 3, results[i - 1])
    bg.save("address.xlsx")


def get_message(url):
    browser.get(url)
    html = browser.page_source
    doc = pq(html)
    # a = doc('.lemma-summary')
    a = doc('.basic-info .name').items()
    # print(a)
    # print(a.text())
    flag = 0
    for k in a:
        if re.match('地.*', k.text()):
            address = k.next()
            print(address.text())
            results.append(address.text())
            flag = 1
    if flag == 0:
        results.append('')
    print(j, ":yes!")
    print('------------------------------------------')


data = xlrd.open_workbook(r'C:\Users\王凯\Desktop\新表.xlsx')
sheet_name = data.sheet_names()[0]
sheet = data.sheet_by_index(0)
cols = sheet.col_values(1)
value = []
for i in range(1, len(cols)):
    value.append(cols[i])
for i in value:
    url = "https://baike.baidu.com/item/" + i
    new_url = urllib.parse.quote(url, safe=string.printable)
    j += 1
    get_message(new_url)
browser.close()
write()
