#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + '\t' + str(self.age)

if __name__ == '__main__':
    s = u'\u5730\u533a'
    print s
    s = s.encode('utf-8')
    print s
