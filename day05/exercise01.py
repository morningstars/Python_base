"""

输入月份 输出天数

"""

month = 10
t01 = (2,)
t02 = (4, 6, 9, 11)

if month < 0 or month > 12:
    print("error")
elif month in t01:
    print("28")
elif month in t02:
    print("30")
else:
    print("31")

"""
    输入月，日 输出第几天
"""
month = int(input("月:"))
day = int(input("日:"))
days = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
total = 0
# for i in range(month-1):
#     total += days[i]
total = sum(days[:month - 1])
total += day
print(total)
