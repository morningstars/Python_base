list01 = [1, 2]
list02 = list01  # list02指向list01指向的内存地址
list01[0] = 100
print(list02)  # [100, 2]

list03 = [1, 2]
# list04 = list03[:]  # list04指向新list的内存地址
list04 = list03.copy()
list03[0] = 100
print(list04[0])  # 1

list01 = [1, [2, 3]]
list02 = list01.copy()  # 浅拷贝 只拷贝一层内存地址
list01[1][0] = 200
print(list02[1][0])  # 200

import copy

list02 = copy.deepcopy(list01)  # 深拷贝 拷贝全部内存地址
