def fun01(a, b, c):
    a = 100
    b[0] = 200
    c = 300


num01 = 1
list01 = [2]
list02 = [3]
fun01(num01, list01, list02)
print(num01)  # 1
print(list01)  # [200]
print(list02)  # [3]
