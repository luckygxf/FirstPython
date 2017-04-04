#encoding=utf-8
#保存用户基本信息到redis数据库
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import redis
from Entities import  UserInfoEntity

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

# 使用hash类型保存用户信息
# ex: uid = 5905555624
# user:5905555624 uid = 5905555624 nickName = 小北帅三代
def hset(uid, key, value):
    hashkey = "user:%s"%uid
    r.hset(hashkey, key, value)

# 获取hash对象
def hgetAll(uid):
    hashkey = "user:%s"%uid
    result = r.hgetall(hashkey)
    return result

if __name__ == '__main__':
    # uid = '1669879400'
    hset('2', "name", "guanxiangfei")
    hset("2", "age", 27)
    info = hgetAll(2)
    print info