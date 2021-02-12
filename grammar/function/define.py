# import math 语句表示导入math 包， 并允许后续代码引用math 包里的 sin\ cos 等函数
import math

# 定义函数
# 定义一个函数要使用def 语句， 依次写出函数名、括号、括号中的参数和冒号：
# 然后， 再缩进块中编写函数体，函数的返回值用return 语句返回。
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-99))


# 如果没有return 语句， 函数执行完毕后也会返回结果， 只是结果为None
# return None 可以简写成return

# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass 语句：
def nop():
    pass

# 参数检查
# 调用函数时， 如果参数个数不对，可以检查出来，如果参数类型不对，python 解释器就无法自动检查出来
# 需要再函数内部写对参数类型检查的语句，
# 数据类型检查可以用内置函数 isinstance() 实现

# import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
# 我们就可以同时获得返回值：

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny






