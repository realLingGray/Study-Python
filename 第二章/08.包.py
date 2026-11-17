import utils.my_fun
from utils.my_fun import log_seoa3

# 其实，就是你import后面跟了什么你就写什么就行
# import a.b，你就写a.b.函数()，就这么简单
utils.my_fun.log_seoa4()

from utils import my_fun
my_fun.log_seoa3()

from utils import *
# 此时会报错，因为如果要在包下import *，那么需要在__init__这个里面
# 写__all__这个变量的值
print(my_var.PI)
# 此时就不会报错了


# 这里的from utils中,其实是相对路径，要注意，此时的utils是跟当前文件是同一个目录下
# 才生效,如果 不在同一个目录下,可以用绝对路径
# 从项目下开始写:项目(不写)第二章.xxx
# 就是 from 第二章.utils .......