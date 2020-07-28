

# 方式一
import module01

module01.fun01()
cls = module01.Cls()
cls.fun02()

# 获取模块文档注释
print(module01.__doc__)

# 获取文件路径
print(module01.__file__)

print(__name__) # __main__

# 方式二
from module01 import Cls

Cls().fun02()

# 方式三
from module01 import *

fun01().__name__



