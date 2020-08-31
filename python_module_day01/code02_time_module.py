"""

    标准库模块 -- time

"""

import time

# 返回时间戳
print(time.time())

# 时间戳 -->  时间元组（年 月 日 小时 分  周几 一年第几天 夏令时）
print(time.localtime(time.time()))

# 时间元组 --> 时间戳
print(time.mktime(time.localtime()))

# 时间元组 --> 字符串
print(time.strftime("%y-%m-%d %h:%m:%s", time.localtime()))  # 20-07-23 Jul:07:1595492369
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 2020-07-23 16:19:29

# 字符串 --> 时间元组
print(time.strptime("2020-07-23", "%Y-%m-%d"))


# 练习一 输入年月日 返回星期

def get_week(year, month, day):
    # 1.转时间元组
    time_tuple = time.strptime("%s-%s-%s" % (year, month, day), "%Y-%m-%d")

    # print(local_tuple)
    # print(local_tuple[6])

    dict_week = {0: "星期一",
                 1: "星期二",
                 2: "星期三",
                 3: "星期四",
                 4: "星期五",
                 5: "星期六",
                 6: "星期七"}

    # 取元组第6个元素为星期
    return dict_week[time_tuple[6]]


print(get_week(2020, 7, 23))


# 练习二 定义函数 根据生日返回活了多少天

def get_live_day(year, month, day):
    # 1. 转成时间戳
    time_tuple = time.strptime("%s-%s-%s" % (year, month, day), "%Y-%m-%d")

    # 2. 时间戳之差 计算天数
    time_dis = time.time() - time.mktime(time_tuple)

    days = time_dis / 60 / 60 // 24
    print("存活了%d天" % days)


get_live_day(1991, 12, 14)
