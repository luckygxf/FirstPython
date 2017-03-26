#encoding=utf-8

'''
获取微博用户信息
uid + nickname
这里暂时不去重
'''

import sys
import Follower
import time
import UserInfo
from sql import FollowerDb
from sql import UserInfoDb
from redisOp import UserInfoRedis

reload(sys)
sys.setdefaultencoding='utf-8'

'''DFS'''
def startCrawlSimpleUserInfo(uid):
    followerList = Follower.getAllFollowersList(uid)
    FollowerDb.inserList(followerList)
    while True:
        time.sleep(2)
        uid = followerList[0].uid
        print 'uid = %s' %uid
        followerList = Follower.getAllFollowersList(uid)
        FollowerDb.inserList(followerList)
        getUserInfoAndSave(followerList)


# 查询用户信息插入到数据库
def getUserInfoAndSave(followerList):
    userInfoDb = UserInfoDb.UserInfoDb()
    print 'save  %d userinfo to database' %len(followerList)
    for follower in followerList:
        userInfo = UserInfo.getUserInfo(follower.uid)
        userInfoDb.insertUserInfo(userInfo)


'''种子 uid = 1669879400'''
if __name__ == '__main__':
    uid = '2804085361'
    userInfo = UserInfo.getUserInfo(uid)
    userInfoDb = UserInfoDb.UserInfoDb()
    userInfoDb.insertUserInfo(userInfo)
    startCrawlSimpleUserInfo(uid)