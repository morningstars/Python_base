
#1.打印第一个字符
str01= input("输入字符串")
print(str01[0])
# print(str01[0:1])

#2.打印最后一个字符
print(str01[-1])
# print(str01[len(str01)-1])

#3.如果是奇数 打印中间的字符串
if len(str01) % 2 != 0:
    index = len(str01) // 2
    print(str01[index])

#4.打印倒数3个字符
print(str01[-3:])

#5.倒叙打印字符串
print(str01[::-1])



