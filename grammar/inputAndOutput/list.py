
# list 是一种有序集合，可以随时添加和删除其中的元素
children = ['1','2','3']
print(children[1])
print(len(children))

# 要取得组后一个的话，可以直接使用-1

print(children[-1])

# list 是一个可变的有序表， 所以往list 中追加元素到末尾
children.append('dddd')

children.insert(0,'ssss')

print(children)

children.pop()

print(children)

