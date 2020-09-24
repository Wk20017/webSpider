#未完成，需要后期加入滑动验证
import json
import time

import requests
import re


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/52.0.2743.116 Safari/537.6'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(response.text)
        return response.text
    return None


def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?board-img.*?src="(.*?)".*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>'
        '.*?releasetime.*?>(.*?)</p>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S
    )
    items = re.findall(pattern, html)
    print(items)


def write_to_file(item):
    with open('result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(i*10)
        time.sleep(1)

