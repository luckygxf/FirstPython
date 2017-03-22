#test sort

def testSort():
    students = [('john', 'A', 4), ('jane', 'B', 12), ('dave', 'B', 10),]
    sorted(students, cmp=lambda x,y:cmp(x[2], y[2]))
    print students

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __cmp__(self, other):
        return cmp(self.age, other.age)

def sortStudentList():
    studentList = []
    s1 = Student('zhangsan', 19)
    s2 = Student('lisi', 20)
    s3 = Student('wangwu', 14)
    studentList.append(s1)
    studentList.append(s2)
    studentList.append(s3)
    printStudentList(studentList)
    studentList = sorted(studentList)
    printStudentList(studentList)

def printStudentList(studentList):
    print '============================'
    for s in studentList:
        print s.name + '\t' + str(s.age)

if __name__ == '__main__':
    sortStudentList()