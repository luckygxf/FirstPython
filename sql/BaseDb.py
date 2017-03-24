#encoding=utf-8
import MySQLdb
import DbProperties
import common.Encoding

common.Encoding.setEncoding()

def getCursor():
    db = MySQLdb.connect(DbProperties.host,DbProperties.user,DbProperties.password,DbProperties.dbName,charset='utf8')
    sql = 'select * from follower'
    cursor = db.cursor()
    return db,cursor