# encoding=utf-8
# 用户信息数据库操作

from common import Encoding
from sql import BaseDB
import traceback
from Entities import UserInfoEntity

Encoding.setEncoding()

# 使用继承(面向对象)
class UserInfoDb(BaseDB.BaseDB):
    # 查询所有的用户信息表
    def queryAllUserInfo(self):
        sql = 'select * from userinfo'
        db, cursor = UserInfoDb.getCursorAndDb()
        cursor.execute(sql)
        db.commit()
        print cursor.fetchone()

    # 向用户信息表中插入一条数据
    def insertUserInfo(self, userInfo):
        try:
            db, cursor = UserInfoDb.getCursorAndDb()
            sql = 'insert into userinfo(uid, nickname, auth, sex, city, birthday, descinfo) ' \
                  'values(\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')' % (userInfo.uid,
                                                                                 userInfo.nickName, userInfo.auth,
                                                                                 userInfo.sex, userInfo.city,
                                                                                 userInfo.birthday, userInfo.desc)
            cursor.execute(sql)
            db.commit()
        except Exception, e:
            print sql
            print e
            traceback.print_exc()
            db.rollback()
        db.close()

if __name__ == '__main__':
    userInfoDb = UserInfoDb()
    userInfo = UserInfoEntity.UserInfo(uid='1',nickName='guanxiangfei',auth='认证', sex='男', city='北京', birthday='天秤座', desc='帅的不行~')
    userInfoDb = UserInfoDb()
    userInfoDb.insertUserInfo(userInfo)