"""

    函数
    def 函数名称(形参)：
        函数体


    函数名称(实参)

"""


# 判断字符串中中文字符的数量
# 0x4E00 ~ 0x9FA5  ord(字符)

def chinese_count(str):
    count = 0
    for c in str:
        if 0x4E00 <= ord(c) <= 0x9FA5:
            count += 1
    return count


count = chinese_count("abc阿萨德BCDhel你好ll")
print(count)
