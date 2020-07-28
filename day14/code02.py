"""
异常
"""


def div_apple(count):
    person_count = int(input("人数："))
    apple = count / person_count
    print(apple)


try:
    div_apple(10)
except ValueError as e:
    print(e.args)
    print("ValueError")
except NameError:
    print("NameError")
except Exception:
    print("未知错误")
else:
    print("没有异常 执行")
finally:
    print("一定执行")





