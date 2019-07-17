import requests
from lxml import etree
import time
from pypinyin import pinyin, lazy_pinyin, Style
import re
class QianTuSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0"}
        # self.baseurl = ""
        self.pageurl = "https://www.58pic.com/tupian/"
    # 获取所有搜索帖子url列表
    def getPageUrl(self,pageurl):
        res = requests.get(pageurl,headers = self.headers)
        res.encoding = "utf-8"
        html = res.text
        # 构建解析对象
        parseHtml = etree.HTML(html)
        t_list = parseHtml.xpath("/html/body/div[5]/div/div[6]/div/div[5]/div/div/div/a/@href")
        # print(t_list)
        for t_link in t_list:
            t_link = "https:"+t_link
            # print(t_link)
            self.getImgUrl(t_link)
    # 获取图片url列表
    def getImgUrl(self,t_link):
        # print("我是谁")
        res = requests.get(t_link,headers=self.headers)
        # print("我在哪")
        res.encoding = "utf-8"
        html = res.text
        # print(html)
        # 构建解析对象
        parseHtml = etree.HTML(html)
        img_list = parseHtml.xpath('//div[@id="show-area-height"]/img[1]/@src')
        for img_link in img_list:
            img_link = "https:"+img_link
            print(img_link)
            self.writeImge(img_link)
    # 保存到本地
    def writeImge(self,img_link):
        res = requests.get(img_link,headers=self.headers)
        res.encoding="utf-8"
        html= res.content
        filename = re.findall(r"\w+.jpg",img_link)
        filename = " ".join(filename)
        print(filename)
        with open(filename,"wb") as f:
            f.write(html)
            time.sleep(1)
            print("%s下载成功" % filename)
    # 主函数
    def workOn(self):
        name = input("请输入名字")
        start = int(input("请输入开始页"))
        end = int(input("请输入结束页"))
        name = lazy_pinyin(name)
        name = "".join(name)
        for i in range(start,end+1):
            i = str(i)
            pageurl = self.pageurl + name + "-0-0-"+ i +".html"
            self.getPageUrl(pageurl)

if __name__=="__main__":
    qiantu = QianTuSpider()
    qiantu.workOn()















