# print('c:\\some\\name')
# print(r'c:\some\name')  # 加r可以让有\字符的字符串连在一起
#
# test = [1, 2, 3, 4, 5, 6]
# print(test)
# print(test[1:2])  # X:X可以截断集合对应的区间或者[-2:]

# 列表的基本操作：append、insert、remove、pop、sort

# 堆栈用法:append(可在列表后面添加字符。使用方法：test.append（"a"）)、pop（可以把最后一个字符去除  test.pop（）)

# 队列用法(导入from collections import deque)：append、popleft(可以把第一个字符去除  test.popleft（）)

# 列表创建：list = [X*10 for] 使用方法：创建一个列表x = [1, 2, 3]   x =[x for x in range(10)] 输出的list为[0,1,2,xxx,10]

# mianshi = [26, 28, 30, 32, 26, 35, 40]
# for i in range(7):
#     x = i+1
#     if 30 < mianshi[i] < 35:
#         print(f"第{x}名面试者:{mianshi[i]}岁可能是一个高级工程师")
#     elif mianshi[i] >= 35:
#         print(f"第{x}名面试者:{mianshi[i]}岁可能是一个测试专家或者测试管理")
#     else:
#         print(f"第{x}名面试者:{mianshi[i]}岁可能是一个初中级工程师")


# 函数
# def fun(a, b=1, *c, **d): # 定义函数a为变量。b有默认值，c为列表，d为字典
#     print(f'a={a}\nb={b}\nc={c}\nd={d}')
# fun(1,2,3)

# 类
# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name+"坐下来了")
#
#     def roll_over(self):
#         print(self.name+"正在打滚")
#
#
# dog1 = Dog('ganli', 2)
#
# dog2 = Dog("caoyi", 1)
#
# dog1.sit()
# dog2.sit()
# dog1.roll_over()
# dog2.roll_over()

class Automobile:
    def __init__(self, 颜色, xinghao, jiage, jiasu):
        self.颜色 = 颜色
        self.xinghao = xinghao
        self.jiage = jiage
        self.jiasu = jiasu

    def baigonglijisu(self):
        print("一辆" + self.颜色 + "的" + self.xinghao + "加速时间为" + str(self.jiasu))


Automobile1 = Automobile('炭黑', '宝马新3系', '30万', 7.3)
Automobile2 = Automobile('白色', '奥迪A6', '35万', 8.5)
Automobile1.baigonglijisu()
Automobile2.baigonglijisu()
