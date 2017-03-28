#encoding=utf-8
# 关注的用户
'''
这里设计了两个字段：关注用户的id和昵称
'''
class Follower:
    def __init__(self, uid, nickName):
        self.uid = uid
        self.nickName = nickName
    def __str__(self):
        return self.nickName + '\t' + self.uid