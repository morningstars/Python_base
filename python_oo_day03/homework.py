"""
day11作业:
1. 定义父类:武器,数据:攻击力,行为:购买(所有子类都一样).攻击(不知道怎么攻击)
   定义子类:枪,数据:射速,行为:攻击
   定义子类:手雷,数据:爆炸范围,行为:攻击
   创建相应对象,调用相应方法.
   画出内存图

2. 一家公司,有如下几种岗位:
    普通员工:底薪
    程序员:底薪 + 项目分红
    销售员:底薪 + 销售额
   定义员工管理器,记录所有员工,提供计算总薪资方法.
   要求:增加新岗位,员工管理器代码不做修改.
   体会:依赖倒置

3. (扩展)学生管理系统,实现修改学生信息.


"""


# 2.

class Job:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary


# class Staff(Job):
#     def __init__(self, base_salary):
#         super().__init__(base_salary)
#
#     def get_salary(self):
#         return self.base_salary


class Programmer(Job):
    def __init__(self, base_salary, pro_salary):
        super().__init__(base_salary)
        self.pro_salary = pro_salary

    def get_salary(self):
        return super().get_salary() + self.pro_salary


class Sales(Job):
    def __init__(self, base_salary, sale_salary):
        super().__init__(base_salary)
        self.sale_salary = sale_salary

    def get_salary(self):
        return super().get_salary() + self.sale_salary


class StaffManager:
    def __init__(self):
        self.__staff_list = []

    def get_total_salary(self):
        total_salary = 0
        for staff in self.__staff_list:
            total_salary += staff.get_salary()
        print("工资", str(total_salary))

    def add_staff(self, staff):
        self.__staff_list.append(staff)


manager = StaffManager()
j2 = Programmer(1000, 2000)
j3 = Sales(1000, 500)
manager.add_staff(j2)
manager.add_staff(j3)
manager.get_total_salary()


# 1.
class Weapon:
    def __init__(self, atk):
        self.atk = atk

    def purchase(self):
        pass

    def attack(self):
        pass


class Gun(Weapon):
    def __init__(self, atk, speed):
        super().__init__(atk)
        self.speed = speed

    def attack(self):
        print("手枪攻击")


class Grenade(Weapon):
    def __init__(self, atk, area):
        super().__init__(atk)
        self.area = area

    def attack(self):
        print("手雷攻击")


g01 = Grenade(1000, 100)
g01.attack()

g02 = Gun(100, 1000)
g02.attack()
