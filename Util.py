# encoding=utf-8
# 定义工具类
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# 保存文本到文件中
def saveFileContent(fileName, content):
    file = open(fileName, 'w')
    file.write(content)
    file.close()

# 获取cookies
def getCookiesFromTxtFile():
    fileName = 'cookies.txt'
    file = open(fileName, 'r')
    cookies = {}
    for line in file.read().split('\n'):
        name,value = line.split('=', 1)
        cookies[name] = value
    # print cookies
    return cookies

#读取文件内容
def readFileContent(fileName):
    file = open(fileName, 'r')
    return file.read()
    file.close()

# 显示关注用户信息
def printFollowerList(followerList):
    for follower in followerList:
        print follower.uid + '\t' + follower.nickName

# 保存关注的用户到文件中
def saveFollowers(followerList):
    file = open('followers.txt','w')
    index = 0
    for follower in followerList:
        try:
            line = follower.nickName + '\t' + follower.uid + '\n'
            if index % 10 == 0:
                file.write('========================= 第 ' + str(index / 10 + 1) + ' 页 =========================\n')
            file.write(line)
            index += 1
        except:
            file.close()
    file.close()
