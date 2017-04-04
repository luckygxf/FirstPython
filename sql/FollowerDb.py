#encoding=utf-8
# 关注用户表操作
import MySQLdb
import DbProperties
import common.Encoding
from sql import BaseDB
from Entities.FollowerEntity import Follower
import traceback

common.Encoding.setEncoding()

# DaseDB对象
dbHelper = BaseDB.BaseDB()

# 查询数据
def getData():
    sql = 'select * from follower'
    db, cursor = dbHelper.getCursorAndDb()
    cursor.execute(sql)
    data = cursor.fetchone()
    print data

# 插入数据
def insertData(uid, follower):
    sql = 'insert into follower(uid, followerid, nickname) values (\'%s\', \'%s\', \'%s\')' %(uid, follower.uid, follower.nickName)

    try:
        db, cursor = dbHelper.getCursorAndDb()
        cursor.execute(sql)
        db.commit()
    except BaseException,e:
        print e.message
        traceback.format_exc(e)
        db.rollback()
    db.close()

# 保存列表数据到数据库
def inserList(uid,listOfFollowers):
    print 'save %d follower to database' % len(listOfFollowers)
    for follower in listOfFollowers:
        insertData(uid, follower)


# 查询uid是否已经在数据库中了
def isUidExist(uid):
    result = False
    sql = 'select * from follower where uid=%s' %uid
    try:
        db, cursor = dbHelper.getCursorAndDb()
        data = cursor.execute(sql)
        db.commit()
        result = (cursor.rowcount == 1)
    except BaseException,e:
        print e.message
        traceback.format_exc(e)
        db.rollback()
    db.close()

    return result



if __name__ == '__main__':
    # getData()
    # follower = Follower('003', '官祥飞')
    # insertData(follower)
    result = isUidExist('004')
    print result