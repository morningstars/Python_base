"""


"""


class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def __init__(self, name, work):
        super().__init__(name)
        self.work = work


d01 = Dog("wc", "cs")
print(d01.work)
