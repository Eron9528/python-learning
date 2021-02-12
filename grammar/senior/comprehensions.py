
# 列表生成式既 List Comprehensions ， 是Python 内置的非常简单却强大的可以用来创建list的生成式

# 例如 要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
list(range(1, 11))

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L=[]
for x in range(1,11):
    L.append(x * x)
print(L)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list
Y=[x * x for x in range(1,11)]
print(Y)

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，
# 就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法

# for 后面还可以家伙是那个if 判断， 这样我们就可以筛选出仅偶数的平方：
X = [x * x for x in range(1, 11) if x % 2 == 0]
print(X)

# 还可以使用两层循环，可以生成全排列：
Z = [m+n for m in 'ABC' for n in 'XYZ']
print(Z)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B'}
for k,v in d.items():
    print(k , '=', v)

# 因此，列表生成式也可以使用两个变量来生成list：
# 最后把一个list中所有的字符串变成小写
T = ['Hello', 'World', 'IBM', 'Apple']
U = [s.lower() for s in T]
print(U)

# 在一个列表生成式中， for 前面的 if ... else 是表达式， 而 for 后面的 if 是过滤条件， 不能带else
















