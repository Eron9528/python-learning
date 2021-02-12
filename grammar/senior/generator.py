
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢
# 这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，
# 称为生成器：generator。
g = (x * x for x in range(10))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# 当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，
# 因为generator也是可迭代对象：

# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，
# 还可以用函数来实现。

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n+1
    return 'done'

# 要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator：
# 回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。
# 当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。