#利用网页根目录下的robots.txt文件可获知该网站的某些网页是否可被爬取
from urllib.robotparser import RobotFileParser

rp = RobotFileParser('http://baike.baidu.com/tobots.txt')
# rp.set_url('http://baike.baidu.com/tobots.txt')
rp.read()
print(rp.can_fetch('*', 'https://baike.baidu.com/item/altavista'))
# from urllib import request
#
# re = request.urlopen('https://baike.baidu.com/item/altavista')
# print(re.read().decode('utf-8'))

