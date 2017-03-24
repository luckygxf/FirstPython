#encoding=utf-8
# 关注用户表操作
import MySQLdb
import DbProperties
import common.Encoding
import BaseDb
from Entities.FollowerEntity import Follower
import traceback

common.Encoding.setEncoding()

# 查询数据
def getData():
    sql = 'select * from follower'
    db, cursor = BaseDb.getCursor()
    cursor.execute(sql)
    data = cursor.fetchone()
    print data

# 插入数据
def insertData(follower):
    sql = 'insert into follower(uid, nickname) values (\'%s\', \'%s\')' %(follower.uid, follower.nickName)

    try:
        db, cursor = BaseDb.getCursor()
        cursor.execute(sql)
        db.commit()
    except BaseException,e:
        print e.message
        traceback.format_exc(e)
        db.rollback()
    db.close()

# 保存列表数据到数据库
def inserList(listOfFollowers):
    for follower in listOfFollowers:
        insertData(follower)



if __name__ == '__main__':
#     # getData()
    follower = Follower('002', '官祥飞')
    insertData(follower)
