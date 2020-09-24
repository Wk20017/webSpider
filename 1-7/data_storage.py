import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/52.0.2743.116 Safari/537.6'
}

html = requests.get(url, headers).text
print(html)
