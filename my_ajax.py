import requests
from urllib.parse import urlencode
import os
from hashlib import md5
from multiprocessing.pool import Pool
Group_start = 1
Group_end = 20


def get_page(offset):
    params = {
        'aid': 24,
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'en_qc': 1,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis'
    }
    url = 'https://www.toutiao.com/search/?' + urlencode(params)
    headers = {

    }
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            for items in images:
                yield {
                    'image': items.get('url'),
                    'title': title
                }


def save_images(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
    except requests.ConnectionError:
        print('Failed to Save image')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_images(item)


if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(Group_start, Group_end+1)])
    pool.map(main, groups)
    pool.close()
    pool.join()




















