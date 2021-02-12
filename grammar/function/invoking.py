from define import my_abs
# 调用函数需要函数名称和参数信息
# 调用abs 函数：
print(abs(100))
print(abs(-8))

# 调用函数的时候， 如果传入的参数数量不对，会报 TypeError 的错误
# 如果参数类型不能被函数所接受， 也会报 TypeError 的错误， 且给出错误信息

# max() 可以接受任意多个参数，并返回最大的那个：
print(max(1, 2))

# 数据类型转换
# Python 内置的常用函数还包括数据类型转换函数，比如int()
print(int('123'))
print(float())
print(str(12))
print(bool(''))

print(my_abs(-9))

