import urllib.request
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.outputer = HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while (self.urls.has_new_url()):
            try:
                new_url = self.urls.get_new_url()
                print("craw %d : %s" %(count, new_url))
                count +=1
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 10:
                    break
            except:
                print("craw failed")
        self.outputer.output_html()


class UrlManager(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urs = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urs:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        else:
            for url in urls:
                self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0

    def get_new_url(self):
        new_url  = self.new_urls.pop()
        self.old_urs.add(new_url)
        return new_url


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()


class HtmlParser(object):
    def parse(self, page_url, html_content):
        if page_url == None or html_content == None:
            return
        soup = BeautifulSoup(
            html_content,
            "html.parser",
            from_encoding="utf-8"
        )
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all("a", href=re.compile("/item/*"))
        for link in links:
            new_url = link["href"]
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        title_node = soup.find("dd", class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data["title"] = title_node.get_text()
        summary_node = soup.find("div", class_="lemma-summary")
        res_data["summary"] = summary_node.get_text()
        # print(summary_node.get_text())
        res_data["url"] = page_url
        return res_data


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []


    def collect_data(self, data):
        if data == None:
            return
        self.datas.append(data)


    def output_html(self):
        fout = open("output.html","w")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            print(data["title"])
            fout.write("<tr>")

            fout.write("<td>%s</td>"%data["url"].encode("utf-8"))
            fout.write("<td>%s</td>"%data["title"].encode("utf-8"))
            fout.write("<td>%s</td>"%data["summary"].encode("utf-8"))

            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)