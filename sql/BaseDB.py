# encoding=utf-8
import MySQLdb

from common import Encoding
from sql import DbProperties

Encoding.setEncoding()

class BaseDB:
    @staticmethod
    def getCursorAndDb():
        db = MySQLdb.connect(DbProperties.host, DbProperties.user, DbProperties.password, DbProperties.dbName,
                             charset='utf8', )
        cursor = db.cursor()
        return db, cursor

    @staticmethod
    def getDb():
        db = MySQLdb.connect(DbProperties.host, DbProperties.user, DbProperties.password, DbProperties.dbName,
                             charset='utf8')
        return db

    @staticmethod
    def getCursor():
        db = BaseDB.getDb()
        cursor = db.cursor()
        return cursor
    @staticmethod
    def test():
        print 'test static method'

if __name__ == '__main__':
    BaseDB.test()
    db, cursor = BaseDB.getCursorAndDb()
    sql = 'select * from follower'
    print type(db)
    print type(cursor)
    cursor = db.cursor()
    data = cursor.execute(sql)
    print data