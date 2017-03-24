#encoding=utf-8

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return self.name + '\t' + str(self.age)

if __name__ == '__main__':
    p = Person('guanxiangfei', 27)
    print p