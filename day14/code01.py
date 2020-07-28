"""
包
"""

from package01.module01 import *

fun01()

from package01 import module01

module01.fun01()

import package01.module01

fun01()


from package01.package02.module02 import *
fun02()
fun01()