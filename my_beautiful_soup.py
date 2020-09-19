'''
1.prettify格式化html并补全缺失部分
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title.string)
2.选择元素
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)
3.提取信息
print(soup.title.name) #获取title的名字
print(soup.title.string) #获取标签内内容
print(soup.p['name']) #获取参数信息
print(soup.p.attrs['name'])
4.获取节点
#获取孩子节点 contents（直接子节点） children（所有子节点）
#获取父节点 parent（直接父节点） parents（所有父节点）
#获取兄弟节点 next_sibling,previous_sibling(直接下、上兄弟节点），next_siblings,previous_siblings（所有下、上兄弟节点）
#所有获取到的节点都为生成器类型，需要遍历获取
for i, child in enumerate(soup.p.children):
    print(i, child)
5.find_All()方法
find_All(name, attrs, recursive, texxt, **kwargs)
name:根据节点名查询  find_All(name='ul')   find_All(name='li')
attrs:根据节点属性查询   find_All(attrs={'id': 'list-1'})  find_All(attrs={'name': 'elements'})  find_All(id='list_1') find_All(class='element')
text:根据文本查询（传入的可以是str，也可以是正则表达式  find_all(text='link')  find_All(re.compile('link'))
6.find()方法
与find_All()类似，查询到的是匹配到的第一个节点
7.find_parents() find_parent find_next_sibling() find_next_siblings() find_previous_sibling() find_previous_siblings()
find_all_next() find_next() find_all_previous() find_previous()
8.CSS选择器(.代表class   #代表id)
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-2 .element'))
'''
from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse's story</b></p>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''



