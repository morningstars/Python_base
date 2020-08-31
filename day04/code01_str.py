"""
字符串操作


"""

str01 = "悟空"
str02 = "八戒"
#创建新对象
str03 = str01 + str02
print(str03)

str01 += str02
print(str01)

print(str02 * 2)

print(str01 > str02)


str04 = "abcde"

#切片
print(str04[0:3]) #abc
print(str04[0:3:2]) #ac
print(str04[::]) #abcde

print(str04[::-1]) #edcba

print(str04[1:1]) #空
print(str04[1:100]) #bcde 切片即使越界也不会报错

print(str04[3:1]) #空
print(str04[3:1:-1]) #dc

print(str04[-2:]) #de






