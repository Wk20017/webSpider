from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germey'
}

data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, headers=headers, data=data, method='POST')

response = request.urlopen(req)
print(response.read().decode('utf-8'))
