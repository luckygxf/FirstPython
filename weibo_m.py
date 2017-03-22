# encoding = utf-8
# 获取用户关注的用户列表
import UserInfo
import sys
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

#根据uid获取用户关注的用户列表
def getFollowerList(uid):
    pass

# test method
if __name__ == '__main__':
    uid = '1669879400'
    userInfo = UserInfo.getUserInfo(uid)
    UserInfo.printUserInfo(userInfo)