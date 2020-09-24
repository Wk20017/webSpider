'''
1.使用request的get方法
r = requests.get('http://www.baidu.com')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
2.使用字典传入query参数，使用json()方法将json格式的返回值转为字典格式
data = {
    'age': 22,
    'name': 'germey'
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.json())
3.抓取网页
import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.6'
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
4.抓取二进制数据
import requests
r = requests.get('https://github.com/favicon.ico')
with open('favicon.ico', 'wb') as f: #打开‘favicon.ico’文件并以二进制格式写入('wb')
    f.write(r.content)
5.post请求
import requests
data = {
    'name': 'germey',
    'age': 22
}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)
print('----------')
print(r.content)
6.上传二进制文件
import requests
files = {
    'file': open('favicon.ico', 'rb')
}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)
7.cookies
import requests
r = requests.get('http://www.baidu.com')
print(r.cookies)
for key, values in r.cookies.items():
    print(key + ' ' + values)
8.session会话
import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456')
r = s.get('http://httpbin.org/cookies')
print(type(r.text), r.text)
import requests
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)
9.代理的使用
import requests
proxies = {
    'http': 'http://10.10.1.10:3128'
}
r = requests.get('http://www.baidu.com', proxies=proxies)
#proxies中可使用类似 http://user:password@host:port实现HTTP Basic Auth，例如http://user:password@10.10.1.10:3128
10.等待时间timeout
r = requests.get('http://www.baidu.com', timeout=1)，连接和读取时间共为1
r = requests.get('http://www.baidu.com', timeout=(5, 30))，传入元组分别指定连接和读取时间
不设置则默认为None，不设置等待时间
11.身份验证
import requests
r = requests.get('http://localhost:5000', auth=('username', 'password'), timeout=1)
print(r.status_code)
'''


