"""

员工管理器

"""


class Employee:
    pass


class EmployeeManager:
    def __init__(self, all_employee):
        self.all_employee = all_employee

    def __iter__(self):
        return EmployeeIterator(self.all_employee)


class EmployeeIterator:

    def __init__(self, target):
        self.target = target
        self.index = 0

    def __next__(self):
        if self.index > len(self.target) - 1:
            raise StopIteration

        item = self.target[self.index]
        self.index += 1
        return item


manager = EmployeeManager([Employee(), Employee(), Employee()])
for item in manager:
    print(item)
