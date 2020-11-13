import requests
from pyquery import PyQuery as pq

response = requests.get("http://www.duanmeiwen.com/guanhougan/zhuanti/11104.html")
response.encoding = "gb2312"
doc = pq(response.text)
result = doc(".main")
print(result.text())
