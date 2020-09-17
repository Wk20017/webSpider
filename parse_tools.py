'''
1.urlparse 实现URL的识别和分段
from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result), result)
##ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
scheme为默认的协议(http或https等),netloc为域名，path为访问路径，params为参数，query为查询条件，fragment为锚点（用于定位页面内部的下拉位置。
2.urlunparsse 是urlparse的逆过程
from urllib.parse import urlunparse

data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
result = urlunparse(data)
print(type(result), result)
###<class 'str'> http://www.baidu.com/index.html;user?a=6#comment
3.urlsplit和urlunsplit类似于前两者
4.urljoin base链为第一个参数，新链为第二个参数
from urllib.parse import urljoin

print(urljoin('http://www.baidu.com', 'FAO.html'))
5.urlencode 将字典转换为url格式
from urllib.parse import urlencode
params = {
    'name': 'germey',
    'age': 22
}
base_url = 'http://www.baidu.com?'
url = base_url + urlencode(params)
print(url)
6.parse_qs 将str类型数据转换为字典类型

from urllib.parse import parse_qs
query = 'name=gerney&age=22'
print(parse_qs(query))
7.parse_qsl 与parse_qs类似，将str类型转换为列表
8.quote 可以将内容转换为URL编码格式

from urllib.parse import quote
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
###https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8
9.unquote 为quote的反过程
from urllib.parse import unquote
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))
###https://www.baidu.com/s?wd=壁纸
'''