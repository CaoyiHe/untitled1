# print('c:\\some\\name')
# print(r'c:\some\name')  # 加r可以让有\字符的字符串连在一起

test = [1, 2, 3, 4, 5, 6]
print(test)
# print(test[1:2])  # X:X可以截断集合对应的区间或者[-2:]

# 列表的基本操作：append、insert、remove、pop、sort

# 堆栈用法:append(可在列表后面添加字符。使用方法：test.append（"a"）)、pop（可以把最后一个字符去除  test.pop（）)
print(test.append("a"))
# 队列用法(导入from collections import deque)：append、popleft(可以把第一个字符去除  test.popleft（）)

# 列表创建：list = [X*10 for] 使用方法：创建一个列表x = [1, 2, 3]   x =[x for x in range(10)] 输出的list为[0,1,2,xxx,10]
1