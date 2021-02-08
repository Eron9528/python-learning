
# set 和dict 类似， 也是一组key 的集合，但不存储value. 由于key 不能重复，所以，在set 中，
# 没有重复的key。
# 要创建一个set, 需要提供一个list 作为输入集合：
s = set([1,2,3])
print(s)

# 通过add(key) 方法可以添加元素到set 中，可以重复添加，但不会有效果：
s.add(4)
print(s)

# 通过remove(key) 方法可以删除元素
s.remove(2)
print(s)