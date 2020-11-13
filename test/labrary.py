import json
import urllib.request

import xlrd
import requests
import re
from pyquery import PyQuery as pq


headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/52.0.2743.116 Safari/537.6'
}


data = xlrd.open_workbook(r'C:\Users\王凯\Desktop\新表.xlsx')
sheet_name = data.sheet_names()[0]
sheet = data.sheet_by_index(0)
cols = sheet.col_values(1)
value = []
for i in range(1, len(cols)):
    value.append(cols[i])

for i in value:
    url = "https://baike.baidu.com/item/" + json.dumps(i)
    response = urllib.request.urlopen(url)
    print(response.read().decode('utf-8'))
