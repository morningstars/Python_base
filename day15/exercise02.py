"""
参照一下代码 创建MyRange类

"""
for item in range(5):
    print(item)


class MyRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        return MyRangeIterator(self.stop)


class MyRangeIterator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 0

    def __next__(self):
        if self.start + 1 > self.stop:
            raise StopIteration

        temp = self.start
        self.start += 1
        return temp