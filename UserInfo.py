# encoding=utf-8
# 爬取weibo m端数据

# 获取用户基本信息


import requests
import sys
import bs4
import Util
from sql import UserInfoDb
from Entities import UserInfoEntity
from util import CookiePool
from util import UserAgentPool
from redisOp import UserInfoRedis

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
    cookie = CookiePool.getRandomCookie()
    userAgent = UserAgentPool.getRandomUserAgent()
    headers = {"user-agent" : userAgent}
    response = requests.get(url, cookies=cookies, headers=headers)

    # 返回码不是200
    if response.status_code != 200:
        print 'url = %s response code = %d' %(url, response.status_code)
        return ''
    return response.text

# 获取个人信息
def getUserInfo(uid):
    url = 'http://weibo.cn/%s/info' %uid
    htmlText = getHmtl(url)
    # 没有获取到内容
    if htmlText == '':
        return
    soup = bs4.BeautifulSoup(htmlText, 'html.parser')
    div_class_c_list = soup.find_all('div', {'class' : 'tip'})
    try:
        basicInfoNode = div_class_c_list[0].next_sibling
    except BaseException, e:
        print e
        print 'getUserInfo() url = %s' %url

    basicInfoContents = basicInfoNode.contents
    basicInfoContents = basicInfoContents[0::2]
    userInfo = {}
    userInfo['uid'] = uid
    for keyValue in basicInfoContents:
        try:
            key = keyValue.split(':')[0]
            value = keyValue.split(':')[1]
            userInfo[key] = value
        except Exception, e:
            # weibo使用中文冒号
            try:
                key = keyValue.split('：')[0]
                value = keyValue.split('：')[1]
                userInfo[key] = value
            except BaseException,e:
                if key != '':
                    print 'key = %s' %key
                    print 'value = %s' %value
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

# 保存微博用户信息到redis
# userinfo 使用python 字典保存
def saveUserinfoToRedis(userInfo):
    uid = userInfo['uid']
    print 'save uid = %s to redis'%uid
    #遍历字典userInfo
    for (key, value) in userInfo.items():
        UserInfoRedis.hset(uid, key, value)


# test method
# uid = 1669879400
if __name__ == '__main__':
    userInfo = {}
    userInfo['uid'] = 4
    userInfo['nickname'] = 'zhangsan'
    userInfo['cigy'] = 'beijing'
    saveUserinfoToRedis(userInfo)