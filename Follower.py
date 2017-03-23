# encoding=utf-8
# 获取用户关注的用户列表
import UserInfo
import sys
import requests
import bs4
import Util
import traceback


reload(sys)
sys.setdefualtencoding='utf-8'

# 关注的用户
'''
这里设计了两个字段：关注用户的id和昵称
'''
class Follower:
    def __init__(self, uid, nickName):
        self.uid = uid
        self.nickName = nickName

#根据uid获取用户关注的用户列表,分页查询
def getFollowerListByPage(uid, pageNo):
    #url = 'http://weibo.cn/1669879400/follow?page=1'

    url = 'http://weibo.cn/%s/follow?page=%d' %(uid, pageNo)
    cookies = Util.getCookiesFromTxtFile()
    response = requests.get(url, cookies = cookies)
    #Util.saveFileContent('index.html', response.text)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    followerInfoList = soup.find_all('table')
    followerList = []
    for followerInfo in followerInfoList:
        try:
            uid = ''
            nickName = ''
            followerInfoNode = followerInfo.tr.find_all('td')[1]
            nickName = followerInfoNode.a.string
            # http://weibo.cn/attention/add?uid=1662068793&rl=1&st=273106
            href = followerInfoNode.find_all('a')[1].attrs.get('href')
            start = href.find('=')
            end = href.find('&')
            uid = href[start + 1: end]
            follower = Follower(uid, nickName)
            followerList.append(follower)
        except BaseException,e:
            print 'get getFollowerListByPage except'
            Util.saveFileContent(str(pageNo) + '.txt', response.text)
            errorMessage = traceback.format_exc()
            print  errorMessage

    return followerList

# 获取所有的关注用户的列表
def getAllFollowersList(uid):
    pageTotalNumStr = getFollowersPageNum(uid)
    pageTotalNum = int(pageTotalNumStr)
    allFollowersList = []
    pageNoList = range(1, pageTotalNum + 1)
    print pageNoList

    for pageNo in pageNoList:
        print 'pageNo = %d' %pageNo
        followListPerPage = getFollowerListByPage(uid, pageNo)
        allFollowersList.extend(followListPerPage)
    return allFollowersList

# 获取关注用户列表总页数
def getFollowersPageNum(uid):
    url = 'http://weibo.cn/%s/follow?page=1' % uid
    cookies = Util.getCookiesFromTxtFile()
    response = requests.get(url, cookies=cookies)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    pageNumNode = soup.find('input' , {'name' : 'mp'})
    return pageNumNode.attrs.get('value')

# test method
# if __name__ == '__main__':
#     uid = '1669879400'
#     # getFollowerList(uid)
#     followerList = getAllFollowersList(uid)
#     # Util.printFollowerList(followerList)
#     Util.saveFollowers(followerList)
#     # getFollowerListByPage(uid, 1)