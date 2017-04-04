#encoding=utf-8

'''
获取微博用户信息
uid + nickname
使用DFS进行遍历
使用列表保存使用的种子UID
'''

import sys
import Follower
import UserInfo
from sql import FollowerDb
from sql import UserInfoDb

reload(sys)
sys.setdefaultencoding='utf-8'

# 已经使用的种子uidList
uidSeedUsedList = []

'''DFS'''
def startCrawlSimpleUserInfo(uid):
    followerList = Follower.getAllFollowersList(uid)
    FollowerDb.inserList(uid, followerList)
    getUserInfoSaveToRedis(followerList)
    while True:
        uid = getSeedUid(followerList)
        if uid == '':
            print 'find no uid seed stop program.'
            break
        uidSeedUsedList.append(uid)
        print 'uid = %s' %uid
        followerList = Follower.getAllFollowersList(uid)
        FollowerDb.inserList(uid, followerList)
        getUserInfoSaveToRedis(followerList)

# 查询用户信息插入到数据库
def getUserInfoAndSave(followerList):
    userInfoDb = UserInfoDb.UserInfoDb()
    print 'save  %d userinfo to database' %len(followerList)
    for follower in followerList:
        userInfo = UserInfo.getUserInfo(follower.uid)
        userInfoDb.insertUserInfo(userInfo)

# 查询用户信息保存到redis中
def getUserInfoSaveToRedis(followerList):
    for follower in followerList:
        userInfo = UserInfo.getUserInfo(follower.uid)
        if userInfo:
            UserInfo.saveUserinfoToRedis(userInfo)

# 获取一个种子uid
# 从uidList中选一个出来
def getSeedUid(followerList):
    foundSeed = False
    uidToReturn = ''
    # 遍历uidList
    for follower in followerList:
        # 找到了直接跳出
        if foundSeed:
            break
        # 遍历使用过的uid
        for uidSeedUsed in uidSeedUsedList:
            if follower.uid == uidSeedUsed:
                continue
            else:
                foundSeed = True
                uidToReturn = follower.uid
                # 找到了直接跳出
                break
    if foundSeed:
        print "find seeduid = %s " %uidToReturn
    else:
        print "not find seeduid"

    return uidToReturn

'''种子 uid = 1669879400'''
if __name__ == '__main__':
    uid = '2804085361'
    uidSeedUsedList.append(uid)
    startCrawlSimpleUserInfo(uid)