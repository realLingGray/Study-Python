# 导入整个模块 调用：模块名.功能名
import random
# Python的内置模块-random

for i in range(100):
    print(random.randint(1, 100))
#     这个功能randint包含开始和结束，是闭区间


import random as rd
# as：别名
for i in range(100):
    print(rd.randint(1, 100))

# 导入模块功能  from 模块 import 功能 调用：功能名()
from random import randint
for i in range(100):
    print(randint(1, 100))
from random import randint as rint
# 给功能起一个别名

# 导入所有的功能
from random import *
# 此时导入的是random的所有功能