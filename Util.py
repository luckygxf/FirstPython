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