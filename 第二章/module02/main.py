# 要使用myfun的功能，先导入模块，导入自定义的模块
# 注：如果原py文件里面有执行函数，则导入的时候会执行
import my_fun

my_fun.log_seoa1()

print(my_fun.NAME)
print(my_fun.PI)

# 导入模块功能
from my_fun import log_seoa3 as log3
log3()

from my_fun import *
# 此时报错，因为my_fun中的__all__没有包括4这个函数
# log_seoa4()