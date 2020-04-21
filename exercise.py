# 1
class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def personlnfo(self):
        print(self.name + ' ' + str(self.age), self.sex)


class Student(Person):
    def __init__(self, name, age, sex, college, clas):
        super().__init__(name, age, sex, )
        self.college = college
        self.clas = clas

    def __str__(self):
        return self.name + str(self.age) + self.sex + self.college + self.clas

    def personlnfo(self):
        super().personlnfo()
        print(self.college, self.clas)

    def syudy(self, teacher):
        teacher.teachObj()
        print(teacher.name + "老师我学会了")


class Teacher(Person):
    def __init__(self, name, age, sex, college, professional):
        super().__init__(name, age, sex)
        self.college = college
        self.professional = professional

    def personlnfo(self):
        super().personlnfo()
        print(self.college, self.professional)

    def teachObj(self):
        print('今天学会了如何用面向对象设计程序')


CaoYi = Teacher("曹懿", 23, '男', '汽车电子技术', '电子')
# CaoYi.personlnfo()
GanLi = Student('淦丽', 22, '女', '数学与运用', '数学')
# GanLi.personlnfo()

GanLi.syudy(CaoYi)

print(GanLi)
GanLi1 = Student("曹懿", 23, '男', '汽车电子技术', '电子')
GanLi2 = Student("曹懿", 23, '男', '汽车电子技术', '电子')
GanLi3 = Student("曹懿", 23, '男', '汽车电子技术', '电子')

i = []
i.append(GanLi1)
i.append(GanLi2)
i.append(GanLi3)
for i in i:
    print(i)
