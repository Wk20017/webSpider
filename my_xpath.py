'''
1.引入xpath,使用lxml中的etree的tostring方法可以补全html中的缺失部分
from lxml import etree
text = \'''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
\'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))
2.etree也可以读取文本进行分析,这里的输出会比1多一个DOCTYPE声明
html = etree.parse('./test.html', etree.HTMLParser())
3.利用xpath获取子节点，//
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
#获取所有子节点
result = html.xpath('//*')
print(result)
#获取所有li节点
result = html.xpath('//li')
#获取第1个li
print(result[0])
#获取li的直接子节点a
result = html.xpath('//li/a')
#获取li的所有子节点a
result = html.xpath('//li//a')
4.利用xpath获取父节点，【@】可选择属性，..或者parent::都可获取父节点
result = html.xpath('//a[@href="link4.html"]/../@class')
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
5.属性获取，获取li下的a的href属性
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a/@href')
print(result)
6.属性多值匹配
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li/a[@href=“link4.html"]')
result1 = html.xpath('//li[contains(@class, "li) and @name="item"')
print(result)
7.按序选择
from lxml import etree
html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[1]/a/text()"]')
result1 = html.xpath('//li[last()]/a/text()')
result2 = html.xpath('//li[position()<3]/a/text()')
result3 = html.xpath('//li[last()-2]/a/text()')
print(result)
print(result1)
print(result2)
print(result3)

'''
