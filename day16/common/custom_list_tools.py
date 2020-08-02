"""

列表相关的方法

"""


class ListHelper:

    @staticmethod
    def find_all(target, func_condition):
        for item in target:
            if func_condition(item):
                yield item

    @staticmethod
    def first(target, func_condition):
        for item in target:
            if func_condition(item):
                return item


    @staticmethod
    def select(target, func_condition):
        for item in target:
            yield func_condition(item)


    @staticmethod
    def sum(target, func_condition):
        sum_value = 0
        for item in target:
            sum_value += func_condition(item)
        return sum_value

