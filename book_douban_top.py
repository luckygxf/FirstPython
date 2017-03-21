#coding=utf-8
# 获取豆瓣top250
import requests
import bs4
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#定义Book类
class Book:
    def __init__(self, name, author, ratingNum):
        self.name = name
        self.author = author
        self.ratingNum = ratingNum

firstLineLength = 0

# 获取bookList
def getBookList(url):

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    bookInfoList = soup.find_all('td', {'valign':'top'})
    bookInfoList = bookInfoList[1::2]
    bookList = []
    for bookInfo in bookInfoList:
        name = ''
        author = ''
        ratingNum = ''
        try:
            name = bookInfo.div.a.attrs.get('title')
            authorList = bookInfo.p.string.split('/')[0: -3]
            author = authorList[0]
            # print type(bookInfo)
            divNode = bookInfo.find_all('div', class_ = 'clearfix')[0]
            ratingNum = divNode.find_all('span', class_='rating_nums')[0].string
            book = Book(name, author, ratingNum)
            bookList.append(book)
        except Exception, e:
            print repr(e)

    return bookList

# get top 250
def getTop250():
    bookListTop250 = []
    for index in range(0, 11):
        baseUrl =  'https://book.douban.com/top250?start=';
        baseUrl += str(index * 25)
        bookList = getBookList(baseUrl)
        bookListTop250.extend(bookList)
    saveBookList(bookListTop250)

# 保存书单信息到文本中
def saveBookList(bookList):
    bookListFile = open('bookList.txt', 'w')

    headLine = '序号'.ljust(30) + '评分'.ljust(30) +  '书名'.ljust(30) +  '作者\n'
    bookListFile.write(headLine)
    order = 1;
    global firstLineLength
    firstLineLength= len(bookList[0].name)
    for book in bookList:
        bookInfoLine = str(order).ljust(28) + getBookInfoLine(book).ljust(30)
        bookListFile.write(bookInfoLine)
        order += 1
    bookListFile.close()

# 拼接字符串
def getBookInfoLine(bookInfo):
    diff = (len(bookInfo.name) - firstLineLength)
    return bookInfo.ratingNum.ljust(28) + bookInfo.name.ljust(30 - diff) + bookInfo.author.ljust(30) + '\n'

if __name__ == '__main__':
    getTop250()