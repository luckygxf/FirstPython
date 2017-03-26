# encoding=utf-8
# 用户信息实体
'''
【个人信息】
昵称 简介
性别 头像
地区 生日
性取向 感情状况

【教育职业】
学校 公司

【其他信息】
个人标签
博客地址
个性域名
'''
class UserInfo:
    def __init__(self, uid = '', nickName = '', auth = '', sex = '', city = '', birthday = '', authInfo = '', desc = '', tag = ''):
        self.uid = uid
        self.nickName = nickName
        self.auth = auth
        self.sex = sex
        self.city = city
        self.birthday = birthday
        self.authInfo = authInfo
        self.desc = desc
        self.tag = tag

# 将中文key换成英文key
def getUserInfoKeyEnglish(key):
    keys = {'地区':'city', '简介':'desc', '昵称': 'nickName', '认证' : 'auth',
            '生日': 'birthday', '性别' : 'sex', '标签': 'tag', '达人' : 'expert' , '其他': 'other'}
    try:
        result =  keys[key.encode('utf-8', key)]
    except BaseException, e:
        print '基本信息需要添加标签: %s' %key
        result = 'other'
        print e
    return result;

if __name__ == '__main__':
    key = 'guanxiangfei'
    print getUserInfoKeyEnglish(key)