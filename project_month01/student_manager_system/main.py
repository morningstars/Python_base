

"""

学生管理系统拆成4个模块

XXXModel
XXXView
XXXController
main

"""

from view import *

if __name__ == "__main__":
    view = StudentManagerView()
    view.main()
