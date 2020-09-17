'''
1.URLError
from urllib import error, request
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.URLError as e:
    print(e.reason)
2.HTTPError
from urllib import error, request
try:
    response = request.urlopen('https://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully!')
5.URLError有可能返回的是一个对象而不是字符串
from urllib import error, request
try:
    response = request.urlopen('https://www.baidu.com', timeout=0.01)
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')
except error.URLError as e:
    print(type(e.reason))
    print(e.reason)
else:
    print('Request Successfully!')
'''
