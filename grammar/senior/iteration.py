from collections import Iterable

# 如果给定一个list 或者tuple , 我们可以通过for 循环来便利这个list 或 tuple,
# 这种遍历我们称为迭代

# Python 的for 循环抽象程度要高于 C 的 for 循环， 因为 Python 的for 循环不仅可以用在
# list 或 tuple 上， 还可以作用在其他可迭代对象上。

# list 这种数据类型虽然有下标， 但很多其他数据类型是没有下标的， 但是， 只要是可迭代对象，
# 无论有无下标， 都可以迭代， 比如dict 就可以迭代：
d={'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# 默认情况下， dict 迭代的是key. 如果要迭代value, 可以用 for value in d.values(),
# 如果同时迭代key 和 value, 可以用for k,v in d.items()

# 由于字符串也是可迭代对象，因此， 也可以作用于 for 循环：
for ch in 'ABC':
    print(ch)

# 如何判断一个对象是可迭代对象， 通过 collections 模块的 Iterable 类型判断：
a=isinstance('aba', Iterable)
print(a)


# 如果要对list 实现类似java 那样的下标循环怎么办。 Python 内置的 enumerate 函数
# 可以把一个list 变成索引-元素对， 这样就可以在for 循环中同时迭代索引和元素本身：
for i, value in enumerate(['a','b']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)



