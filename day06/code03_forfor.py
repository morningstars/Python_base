"""

for for

"""

for c in range(2):
    for i in range(3):
        print("*****", end="")
    print()

"""
    函数
"""


def attack():
    print('----------')


attack()


def tr(count):
    for index in range(count):
        for j in range(index + 1):
            print("#", end="")
        print()


tr(5)


def add(num1, num2):
    # print(num1 + num2)
    return num1 + num2


a = add(10, 10)
print(a)


b = add((1,), [4,5,6])
print(b)




