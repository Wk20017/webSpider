'''
1.url初始化
doc = pq(url='https://cuiqingcai.com')
2.文件初始化
doc = pq(filename='demo.html')
3.节点查找：doc(#代表id；.代表class)
print(doc('.story #link1'))
print(doc('.story #next_test').text('change_test'))
4.查找节点：find()查找所有子孙节点；children()查找直接子节点；parents()查找所有祖先节点；parent()查找直接父节点
items = doc('.story')
a = items.find('a')
5.遍历节点，使用items()方法得到生成器，之后用for循环遍历
items = doc('.story').items()
for a in items:
    print(a)
6.获取参数的属性值：attr()方法。
items = doc('.story').items()
for p in items:
    for a in p.find('a').items():
        print(a.attr('href'))
7.获取信息：
text()方法： 获取文本信息
attr()方法： 获取参数信息
html()方法： 获取网页信息
8.节点操作：
addClass(' '),removeClass(' ')：增加或删除class属性
remove()：删除对应节点
append()：
empty()：
prepend()：
9.伪类选择器：
················不懂
'''

from pyquery import PyQuery as pq

