#encoding=utf-8
#保存用户基本信息到redis数据库
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import redis
from Entities import  UserInfoEntity
import UserInfo

r = redis.Redis(host='localhost', port=6379, db=0, charset='utf-8')

def getValue(key):
    return  r.get(key)

def setKeyAndValue(key, value):
    r.set(key, value)

# 保存用户信息，这里使用key value形式
def saveUserInfo(userInfo):
    # 遍历字典对象
    for key in userInfo.keys():
        # 这里的key是中文，需要转换一下
        keyEnglish = UserInfoEntity.getUserInfoKeyEnglish(key)
        print userInfo[key].encode('utf-8', userInfo[key])
        setKeyAndValue(keyEnglish, userInfo[key].encode('utf-8', userInfo[key]))


if __name__ == '__main__':
    # uid = '1669879400'
    # userInfo = UserInfo.getUserInfo(uid)
    # saveUserInfo(userInfo)
    setKeyAndValue('name', '官祥飞')