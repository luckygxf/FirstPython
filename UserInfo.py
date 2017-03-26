# encoding=utf-8
# 爬取weibo m端数据

# 获取用户基本信息


import requests
import sys
import bs4
import Util
from sql import UserInfoDb
from Entities import UserInfoEntity

reload(sys)
sys.setdefaultencoding('utf-8')



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
    # div_class_c_list = soup.find_all('div', {'class' : 'c'})
    div_class_c_list = soup.find_all('div', {'class' : 'tip'})
    basicInfoNode =  div_class_c_list[0].next_sibling
    basicInfoContents = basicInfoNode.contents
    basicInfoContents = basicInfoContents[0::2]
    userInfo = {}
    for keyValue in basicInfoContents:
        try:
            key = keyValue.split(':')[0]
            value = keyValue.split(':')[1]
            userInfo[key] = value
        except Exception, e:
            # weibo使用中文冒号
            key = keyValue.split('：')[0]
            value = keyValue.split('：')[1]

    # index = 0
    # # 有些没有认证信息
    # nickName = basicInfoContents[index].split(':')[1]
    # index += 1
    # # 有认证信息的
    # if('认证' == basicInfoContents[index].split(':')[1]):
    #     auth = basicInfoContents[index].split(':')[1]
    #     index += 1
    # sex = basicInfoContents[index].split(':')[1]
    # index += 1
    # city = basicInfoContents[index].split(':')[1]
    # index += 1
    # birthday = basicInfoContents[index].split(':')[1]
    # index += 1
    # if ('认证信息' == basicInfoContents[index].split(':')[1]):
    #     authInfo = basicInfoContents[index].split('：')[1]
    #     index += 1
    # desc = basicInfoContents[index].split(':')[1].strip()
    # userInfo = UserInfoEntity.UserInfo(uid=uid, nickName=nickName, auth=auth, sex=sex, city=city, birthday=birthday, authInfo=authInfo, desc=desc)
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
    uid = '1669879400'
    userInfo = getUserInfo(uid)
    for key in userInfo.keys():
        print key, userInfo[key]
    # userInfoDb = UserInfoDb.UserInfoDb()
    # userInfoDb.insertUserInfo(userInfo)
    # # printUserInfo(userInfo)
    # homeUrl = 'http://weibo.cn/tangyan'
    # getUidFromHomePage(homeUrl)