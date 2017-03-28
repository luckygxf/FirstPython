# -*- coding=utf-8 -*-
# define Person class
import requests
import codecs
import bs4
import urllib2

import sys
reload(sys)
sys.setdefaultencoding('utf8')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

#爬取豆瓣书单
def getBookList():
    url = 'https://book.douban.com/tag/推理'; #推理小说列表
    response = requests.get(url)                            #加载要解析的网页
    soup = bs4.BeautifulSoup(response.content, 'html.parser')                 #获取beautifulSoup对象

    # soup = bs4.BeautifulSoup(codecs.open('content.txt', 'r', 'utf-8'), 'html.parser')        #获取beautifulSoup对象
    links = soup.select('div.info a')                       #利用soup选择器获取书名连接
    print 'length of links = %d\n' %len(links)
    saveContentToTxtFile(response.content, 'content.txt')
    # saveContentToTxtFile(response.text, 'txt.txt')

    for a in links:
            if((a is not None)&(a.string is not None)):
                print a.string.strip()

#保存文本到文件中
def saveContentToTxtFile(content, filename):
    f = codecs.open(filename, 'w', 'utf-8')
    f.write(content)
    f.close()

# 使用urllib2获取网页内容
def getHtmlUseUrllib2():
    url = 'https://book.douban.com/tag/推理';  # 推理小说列表
    response = urllib2.urlopen(url)
    html = response.read()
    saveContentToTxtFile(html, 'content_urllib2.txt')

if __name__ == '__main__':
    #saveContentToTxtFile('welcome ', 'test.txt')
    getBookList()