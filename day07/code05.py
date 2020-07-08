# 1.排序

count = 0


def order(list01):
    for i in range(len(list01)):
        for j in range(0, len(list01) - 1):
            global count
            count += 1
            if list01[j] > list01[j + 1]:
                list01[j], list01[j + 1] = list01[j + 1], list01[j]
    print(list01)


order([11, 21, 3, 4, 4, 8])
print(count)

count2 = 0


def order2(list01):
    for i in range(len(list01) - 1):
        for j in range(i + 1, len(list01)):
            global count2
            count2 += 1
            if list01[i] > list01[j]:
                list01[j], list01[i] = list01[i], list01[j]
    print(list01)


order2([11, 21, 3, 4, 4, 8])
print(count2)


# 2. 英文单词翻转  how are you -> you are how

def reverse(str):
    list01 = str.split(" ")
    list01 = list01[::-1]
    print(list01)
    # a = ""
    # for item in list01:
    #     a = a + item + " "

    re = " ".join(list01)
    return re


print(reverse("how are you"))
print(reverse("some body a a a v b"))

# sort([1,2,3,4,5,3,2,1])
sorted([1, 2, 3, 4, 5, 3, 2, 1])
