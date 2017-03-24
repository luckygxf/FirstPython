# encoding=utf-8
# 爬取weibo m端数据

# 获取用户基本信息


import requests
import sys
import bs4
import Util

reload(sys)
sys.setdefaultencoding('utf-8')

# 定义用户信息
class UserInfo:
    def __init__(self, uid = '', nickName = '', auth = '', sex = '', city = '', birthday = '', authInfo = '', desc = ''):
        self.uid = uid
        self.nickName = nickName
        self.auth = auth
        self.sex = sex
        self.city = city
        self.birthday = birthday
        self.authInfo = authInfo
        self.desc = desc

'''
1.先爬取好友列表
2。登录，获取cookie
3.使用cookie构造请求
4.解析返回的html
'''

# 获取url的网页文本
def getHmtl(url):
    cookies = getCookiesFromTxtFile()
    #url = 'http://weibo.cn/1669879400/follow'
    response = requests.get(url, cookies=cookies)
    #saveContent(response.text)
    #print response.text
    return response.text

# 获取个人信息
def getUserInfo(uid):
    url = 'http://weibo.cn/%s/info' %uid
    htmlText = getHmtl(url)
    # htmlText = open('index.html', 'r').read()
    nickName = ''
    auth = ''
    sex = ''
    city = ''
    birthday = ''
    authInfo = ''
    desc = ''
    soup = bs4.BeautifulSoup(htmlText, 'html.parser')
    div_class_c_list = soup.find_all('div', {'class' : 'c'})
    basicInfoNode =  div_class_c_list[2]
    basicInfoContents = basicInfoNode.contents
    basicInfoContents = basicInfoContents[0::2]
    nickName = basicInfoContents[0]
    auth = basicInfoContents[1]
    sex = basicInfoContents[2]
    city = basicInfoContents[3]
    birthday = basicInfoContents[4]
    authInfo = basicInfoContents[5]
    desc = basicInfoContents[6]
    userInfo = UserInfo(uid, nickName, auth, sex, city, birthday, authInfo, desc)

    return userInfo

# get Cookie
def getCookiesFromTxtFile():
    fileName = 'cookies.txt'
    file = open(fileName, 'r')
    cookies = {}
    for line in file.read().split('\n'):
        name,value = line.split('=', 1)
        cookies[name] = value
    # print cookies
    return cookies

# save html text to file
def saveContent(html):
    fileName = 'index.html'
    file = open(fileName, 'w')
    file.write(html)

# 打印用户信息
def printUserInfo(userInfo):
    print userInfo.nickName + '\t' + userInfo.auth + '\t' + userInfo.sex + '\t' + userInfo.city + '\t' \
          + userInfo.birthday + '\t' + userInfo.authInfo + '\t' + userInfo.desc + '\n'

# 从主页获取uid
def getUidFromHomePage(homeUrl):
    response = requests.get(homeUrl)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    #soup = bs4.BeautifulSoup(Util.readFileContent('homepage.html'), 'html.parser')
    #Util.saveFileContent('homepage.html', response.text)
    userInfoUrl = soup.find_all("div", {'class' : 'u'})[0].table.tr.find_all('td')[1].find_all('a')[1].attrs.get('href')

    return userInfoUrl.split('/')[1]


# test method
# uid = 1669879400
if __name__ == '__main__':
    #getHmtl()
    # getCookiesFromTxtFile()
    # uid = '1669879400'
    # userInfo = getUserInfo(uid)
    # printUserInfo(userInfo)
    homeUrl = 'http://weibo.cn/tangyan'
    getUidFromHomePage(homeUrl)